# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from src.implementation.v00.configuration_base import PgCfgModel__OptionData
# fmt: on

from .......TestServices import TestServices

import pytest
import re
import typing

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_data001__offsets: typing.List[typing.Optional[int]] = [None, 1, 2, 3, 10]

    # --------------------------------------------------------------------
    @pytest.fixture(
        params=sm_data001__offsets,
        ids=[
            ("offset_" + (str(x) if x is not None else "None"))
            for x in sm_data001__offsets
        ],
    )
    def offset001(self, request: pytest.FixtureRequest) -> typing.Optional[int]:
        assert isinstance(request, pytest.FixtureRequest)
        assert request.param is None or type(request.param) is int
        return request.param

    # --------------------------------------------------------------------
    def test_001(self, request: pytest.FixtureRequest, offset001: typing.Optional[int]):
        assert isinstance(request, pytest.FixtureRequest)
        assert offset001 is None or type(offset001) is int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        option = fileLine.AddOption("port", 123, offset001)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base  # noqa: E721
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721
        assert option.m_OptionData.m_Offset == offset001

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123

    # --------------------------------------------------------------------
    def test_002__shared_preload_libraries(
        self, request: pytest.FixtureRequest, offset001: typing.Optional[int]
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert offset001 is None or type(offset001) is int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_OPT_NAME = "shared_preload_libraries"

        optValue_set = ["a", "b", "c"]
        optValue_get = optValue_set.copy()

        option = fileLine.AddOption(C_OPT_NAME, optValue_set, offset001)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base  # noqa: E721
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721
        assert option.m_OptionData.m_Offset == offset001

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == C_OPT_NAME
        assert option.m_OptionData.m_Value == optValue_get
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == optValue_get

    # --------------------------------------------------------------------
    def test_003__shared_preload_libraries__as_str(
        self, request: pytest.FixtureRequest, offset001: typing.Optional[int]
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert offset001 is None or type(offset001) is int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_OPT_NAME = "shared_preload_libraries"

        optValue_set = '"a", "b", "c"'
        optValue_get = ["a", "b", "c"]

        option = fileLine.AddOption(C_OPT_NAME, optValue_set, offset001)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base  # noqa: E721
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721
        assert option.m_OptionData.m_Offset == offset001

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == C_OPT_NAME
        assert option.m_OptionData.m_Value == optValue_get
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == optValue_get

    # --------------------------------------------------------------------
    def test_004__shared_preload_libraries__with_None_item(
        self, request: pytest.FixtureRequest
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_OPT_NAME = "shared_preload_libraries"

        optValue_set = ["a", None, "c"]

        with pytest.raises(
            Exception,
            match=re.escape(
                "None value item of option [{0}] is not supported.".format(C_OPT_NAME)
            ),
        ):
            fileLine.AddOption(C_OPT_NAME, optValue_set, None)

        assert len(fileLine) == 0

    # --------------------------------------------------------------------
    def test_E01__after_option(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        option = fileLine.AddOption("port", 123, 2)

        with pytest.raises(
            Exception, match=re.escape("File line already has the option [port].")
        ):
            fileLine.AddOption("proxima.port", 321, 432)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base  # noqa: E721
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123

    # --------------------------------------------------------------------
    def test_E02__after_include(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        include = file.AddInclude(cfg.C_POSTGRESQL_AUTO_CONF)

        fileLine = include.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(
            Exception, match=re.escape("File line already has an include directive.")
        ):
            fileLine.AddOption("proxima.port", 321, 11)

        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is include.m_IncludeData

    # --------------------------------------------------------------------
    def test_E03__after_comment(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        comment = file.AddComment("comment")

        fileLine = comment.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(
            Exception, match=re.escape("File line already has a comment.")
        ):
            fileLine.AddOption("proxima.port", 321, 11)

        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is comment.m_CommentData

    # --------------------------------------------------------------------
    def test_E04__conflict_with_this_file(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()
        assert len(fileLine) == 0
        option = fileLine.AddOption("port", 123, 2)

        fileLine2 = file.AddEmptyLine()
        assert len(fileLine2) == 0

        with pytest.raises(
            Exception,
            match=re.escape(
                "Option [port] already exist in this file [{0}].".format(
                    file.get_Path()
                )
            ),
        ):
            fileLine2.AddOption("port", 321, 2)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base  # noqa: E721
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123

    # --------------------------------------------------------------------
    def test_E05__conflict_with_another_file(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        fileLine = file.AddEmptyLine()
        assert len(fileLine) == 0
        option = fileLine.AddOption("port", 123, 2)

        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)
        fileLine2 = file2.AddEmptyLine()
        assert len(fileLine2) == 0

        with pytest.raises(
            Exception,
            match=re.escape(
                "Option [port] already exist in another file [{0}].".format(
                    file.get_Path()
                )
            ),
        ):
            fileLine2.AddOption("port", 321, 2)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base  # noqa: E721
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123


# //////////////////////////////////////////////////////////////////////////////
