# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationReader_Base as PgCfg_Reader_Base

from src.implementation.v00.configuration_base import PgCfgModel__OptionData

from ........TestServices import TestServices
from ........CfgFileReader import CfgFileReader
from ........ErrorMessageBuilder import ErrorMessageBuilder
# fmt: on

import pytest
import re
import typing
import logging
import datetime

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OptionNames: typing.List[str] = [
        "restart_after_crash",
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_OptionNames, ids=[x for x in sm_OptionNames])
    def optionName(self, request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) is str
        return request.param

    # --------------------------------------------------------------------
    class tagData001:
        set_value: any
        get_value: bool

        def __init__(self, set_value: any, get_value: bool):
            self.set_value = set_value
            self.get_value = get_value

    # --------------------------------------------------------------------
    sm_Data001: typing.List[tagData001] = [
        tagData001(True, True),
        tagData001(False, False),
        tagData001(1, True),
        tagData001(0, False),
        # LOWER
        tagData001("on", True),
        tagData001("t", True),
        tagData001("tr", True),
        tagData001("tru", True),
        tagData001("true", True),
        tagData001("y", True),
        tagData001("ye", True),
        tagData001("yes", True),
        tagData001("1", True),
        tagData001("of", False),
        tagData001("off", False),
        tagData001("f", False),
        tagData001("fa", False),
        tagData001("fal", False),
        tagData001("fals", False),
        tagData001("false", False),
        tagData001("n", False),
        tagData001("no", False),
        tagData001("0", False),
        # UPPER
        tagData001("ON", True),
        tagData001("T", True),
        tagData001("TR", True),
        tagData001("TRU", True),
        tagData001("TRUE", True),
        tagData001("Y", True),
        tagData001("YE", True),
        tagData001("YES", True),
        tagData001("1", True),
        tagData001("OF", False),
        tagData001("OFF", False),
        tagData001("F", False),
        tagData001("FA", False),
        tagData001("FAL", False),
        tagData001("FALS", False),
        tagData001("FALSE", False),
        tagData001("N", False),
        tagData001("NO", False),
        tagData001("0", False),
        # MIX
        tagData001("True", True),
        tagData001("falsE", False),
    ]

    # --------------------------------------------------------------------
    def test_001__ok(self, optionName: str):
        assert type(optionName) is str

        rootTmpDir = TestServices.GetRootTmpDir()

        for iData in range(len(__class__.sm_Data001)):
            logging.info("---------------------- data #{}".format(iData))

            cfg = PgCfg_Std(rootTmpDir)

            data = __class__.sm_Data001[iData]
            assert type(data) is __class__.tagData001

            try:
                logging.info(
                    "Set value [{}]: [{}]".format(
                        type(data.set_value).__name__, data.set_value
                    )
                )

                assert data.set_value is not None

                cfg.SetOptionValue(optionName, data.set_value)

                logging.info("Get value")

                actualValue = cfg.GetOptionValue(optionName)

                if actualValue is None:
                    raise Exception("Option is not found")

                logging.info(
                    "actualVaue is [{}]: [{}]".format(
                        type(actualValue).__name__, actualValue
                    )
                )

                assert type(actualValue) is bool
                assert type(data.get_value) is bool
                assert actualValue == data.get_value
            except Exception as e:
                logging.error(str(e))

    # --------------------------------------------------------------------
    class tagData002:
        set_value: any

        def __init__(self, set_value: any):
            self.set_value = set_value

    # --------------------------------------------------------------------
    sm_Data002: typing.List[tagData002] = [
        tagData002(""),
        tagData002(" False"),
        tagData002("False "),
        tagData002("Falsee"),
        tagData002(-2),
        tagData002(-1),
        tagData002(2),
        tagData002(3),
    ]

    # --------------------------------------------------------------------
    def test_002__cant_convert_value(self, optionName: str):
        assert type(optionName) is str

        rootTmpDir = TestServices.GetRootTmpDir()

        for iData in range(len(__class__.sm_Data002)):
            logging.info("---------------------- data #{}".format(iData))

            cfg = PgCfg_Std(rootTmpDir)

            data = __class__.sm_Data002[iData]
            assert type(data) is __class__.tagData002

            logging.info(
                "Set value [{}]: [{}]".format(
                    type(data.set_value).__name__, data.set_value
                )
            )

            assert data.set_value is not None

            try:
                errMsg = ErrorMessageBuilder.CantConvertOptionValue(
                    optionName, type(data.set_value), bool
                )

                with pytest.raises(Exception, match="^" + re.escape(errMsg) + "$"):
                    cfg.SetOptionValue(optionName, data.set_value)
            except Exception as e:
                logging.error(str(e))

    # --------------------------------------------------------------------
    class tagData003:
        set_value: any

        def __init__(self, set_value: any):
            self.set_value = set_value

    # --------------------------------------------------------------------
    sm_Data003: typing.List[tagData003] = [
        tagData003(1.2),
        tagData003(datetime.datetime.now()),
    ]

    # --------------------------------------------------------------------
    def test_003__bad_option_value_type(self, optionName: str):
        assert type(optionName) is str

        rootTmpDir = TestServices.GetRootTmpDir()

        for iData in range(len(__class__.sm_Data003)):
            logging.info("---------------------- data #{}".format(iData))

            cfg = PgCfg_Std(rootTmpDir)

            data = __class__.sm_Data003[iData]
            assert type(data) is __class__.tagData003

            logging.info(
                "Set value [{}]: [{}]".format(
                    type(data.set_value).__name__, data.set_value
                )
            )

            assert data.set_value is not None

            try:
                errMsg = ErrorMessageBuilder.BadOptionValueType(
                    optionName, type(data.set_value), bool
                )

                with pytest.raises(Exception, match="^" + re.escape(errMsg) + "$"):
                    cfg.SetOptionValue(optionName, data.set_value)
            except Exception as e:
                logging.error(str(e))

    # --------------------------------------------------------------------
    class tagData101_Assign:
        sign: str
        text: str

        def __init__(self, sign: str, text: str):
            assert type(sign) is str
            assert type(text) is str
            self.sign = sign
            self.text = text

    # --------------------------------------------------------------------
    sm_Data101_assigns: typing.List[tagData101_Assign] = [
        tagData101_Assign("assign", "="),
        tagData101_Assign("space", " "),
        tagData101_Assign("tab", "\t"),
        tagData101_Assign("space_assign", " ="),
        tagData101_Assign("assign_space", "= "),
        tagData101_Assign("space_assign_space", " = "),
        tagData101_Assign("tab_assign", "\t="),
        tagData101_Assign("assign_tab", "=\t"),
        tagData101_Assign("tab_assign_tab", "\t=\t"),
    ]

    # --------------------------------------------------------------------
    class tagData101_Quote:
        sign: str
        quote1: str
        quote2: str

        def __init__(self, sign: str, quote1: str, quote2: str):
            assert type(sign) is str
            assert type(quote1) is str
            assert type(quote2) is str
            self.sign = sign
            self.quote1 = quote1
            self.quote2 = quote2

    # --------------------------------------------------------------------
    sm_Data101_quotes: typing.List[tagData101_Quote] = [
        tagData101_Quote("none", "", ""),
        tagData101_Quote("single", "'", "'"),
        # tagData101_Quote("double", "\"", "\""),
    ]

    # --------------------------------------------------------------------
    class tagData101_Value:
        source: any
        result: bool

        def __init__(self, source: any, result: bool):
            self.source = source
            self.result = result

    # --------------------------------------------------------------------
    sm_Data101_values: typing.List[tagData101_Value] = [
        # LOWER
        tagData101_Value("on", True),
        tagData101_Value("t", True),
        tagData101_Value("tr", True),
        tagData101_Value("tru", True),
        tagData101_Value("true", True),
        tagData101_Value("y", True),
        tagData101_Value("ye", True),
        tagData101_Value("yes", True),
        tagData101_Value("1", True),
        tagData101_Value("of", False),
        tagData101_Value("off", False),
        tagData101_Value("f", False),
        tagData101_Value("fa", False),
        tagData101_Value("fal", False),
        tagData101_Value("fals", False),
        tagData101_Value("false", False),
        tagData101_Value("n", False),
        tagData101_Value("no", False),
        tagData101_Value("0", False),
        # UPPER
        tagData101_Value("ON", True),
        tagData101_Value("T", True),
        tagData101_Value("TR", True),
        tagData101_Value("TRU", True),
        tagData101_Value("TRUE", True),
        tagData101_Value("Y", True),
        tagData101_Value("YE", True),
        tagData101_Value("YES", True),
        tagData101_Value("1", True),
        tagData101_Value("OF", False),
        tagData101_Value("OFF", False),
        tagData101_Value("F", False),
        tagData101_Value("FA", False),
        tagData101_Value("FAL", False),
        tagData101_Value("FALS", False),
        tagData101_Value("FALSE", False),
        tagData101_Value("N", False),
        tagData101_Value("NO", False),
        tagData101_Value("0", False),
        # MIX
        tagData101_Value("True", True),
        tagData101_Value("falsE", False),
    ]

    # --------------------------------------------------------------------
    def test_101__parse_file_line(self, optionName: str):
        assert type(optionName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        for iAssign in range(len(__class__.sm_Data101_assigns)):
            for iQuote in range(len(__class__.sm_Data101_quotes)):
                for iValue in range(len(__class__.sm_Data101_values)):
                    logging.info(
                        "----------------------- [{}][{}][{}][{}]".format(
                            optionName,
                            __class__.sm_Data101_assigns[iAssign].sign,
                            __class__.sm_Data101_quotes[iQuote].sign,
                            __class__.sm_Data101_values[iValue].source,
                        )
                    )

                    cfg = PgCfg_Std(TestServices.GetRootTmpDir())
                    file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

                    line = optionName
                    line += __class__.sm_Data101_assigns[iAssign].text
                    line += __class__.sm_Data101_quotes[iQuote].quote1
                    line += __class__.sm_Data101_values[iValue].source
                    line += __class__.sm_Data101_quotes[iQuote].quote2

                    logging.info("source: {}".format(line))

                    src = CfgFileReader(line)

                    try:
                        PgCfg_Reader_Base.LoadFileContent(file1, src)

                        assert len(file1) == 1
                        assert len(file1.m_FileData.m_Lines) == 1

                        fileLineData0 = file1.m_FileData.m_Lines[0]
                        assert len(fileLineData0.m_Items) == 1
                        assert (
                            type(fileLineData0.m_Items[0].m_Element)
                            is PgCfgModel__OptionData
                        )
                        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
                        assert fileLineData0.m_Items[0].m_Element.m_Name == optionName
                        assert (
                            fileLineData0.m_Items[0].m_Element.m_Value
                            == __class__.sm_Data101_values[iValue].result
                        )
                    except Exception as e:
                        logging.error(str(e))


# //////////////////////////////////////////////////////////////////////////////
