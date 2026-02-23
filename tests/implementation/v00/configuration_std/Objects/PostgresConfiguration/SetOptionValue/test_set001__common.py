# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.abstract.v00.configuration import PostgresConfigurationOption

from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.implementation.v00.configuration_base import PostgresConfigurationOption as PgCfg_Option
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult as PgCfg_SetOptionResult

from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__ConfigurationData

from .......TestServices import TestServices
# fmt: on

import pytest
import typing
import os
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001__int_opt(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r = cfg.SetOptionValue(optName, 123)
        assert type(r) is PgCfg_SetOptionResult_Base
        assert isinstance(r, PgCfg_SetOptionResult)
        assert r.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        r_option: PgCfg_Option_Base = r.Option
        assert r_option is not None
        assert type(r_option) is PgCfg_Option_Base
        assert isinstance(r_option, PostgresConfigurationOption)
        assert r.Option is r_option  # check a cache

        __class__.Helper__CheckStateOfCfgWithOneOpt(cfg, r_option, optName, 123)

        # Amen

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002__port___reasign(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r = cfg.SetOptionValue(optName, 123)
        r = cfg.SetOptionValue(optName, 321)
        assert type(r) is PgCfg_SetOptionResult_Base
        assert r.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_UPDATED
        r_option: PgCfg_Option_Base = r.Option
        assert r_option is not None
        assert type(r_option) is PgCfg_Option_Base
        assert isinstance(r_option, PostgresConfigurationOption)
        assert r.Option is r_option  # check a cache

        __class__.Helper__CheckStateOfCfgWithOneOpt(cfg, r_option, optName, 321)

    # --------------------------------------------------------------------
    def Helper__CheckStateOfCfgWithOneOpt(
        cfg: PgCfg_Std, opt: PgCfg_Option_Base, optName: str, optValue: any
    ):
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(opt) is PgCfg_Option_Base

        assert opt.get_Configuration() is cfg
        assert opt.get_Name() == optName
        assert opt.get_Value() == optValue

        assert type(opt) is PgCfg_Option_Base
        assert type(opt.m_OptionData) is PgCfgModel__OptionData
        assert opt.m_OptionData.m_Name == optName
        assert opt.m_OptionData.m_Value == optValue
        assert opt.m_OptionData.m_Parent is not None
        assert type(opt.m_OptionData.m_Parent) is PgCfgModel__FileLineData

        fileLine = opt.get_Parent()
        assert fileLine is opt.get_Parent()
        assert type(fileLine) == PgCfg_FileLine_Base  # noqa: E721
        assert len(fileLine) == 1

        fileLineData: PgCfgModel__FileLineData = opt.m_OptionData.m_Parent
        assert fileLineData is fileLine.m_FileLineData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) is list
        assert len(fileLineData.m_Items) == 1
        assert (  # noqa: E721
            type(fileLineData.m_Items[0]) == PgCfgModel__FileLineData.tagItem
        )
        assert fileLineData.m_Items[0].m_Element is opt.m_OptionData
        assert fileLineData.m_Items[0].m_Element.m_Offset is None
        assert type(fileLineData.m_Parent) is PgCfgModel__FileData
        assert type(fileLineData.get_Parent()) is PgCfgModel__FileData
        assert fileLineData.get_Parent() is fileLineData.m_Parent

        file = fileLine.get_Parent()
        assert type(file) is PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert len(file) == 1

        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert fileData is file.m_FileData
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.m_Path == os.path.join(
            cfg.m_Data.m_DataDir, "postgresql.auto.conf"
        )
        assert fileData.m_Parent is cfg.m_Data
        assert type(fileData.m_Lines) is list
        assert len(fileData.m_Lines) == 1
        assert fileData.m_Lines[0] is fileLineData

        assert type(cfg.m_Data.m_Files) is list
        assert len(cfg.m_Data.m_Files) == 1
        assert type(cfg.m_Data.m_Files[0]) is PgCfgModel__FileData
        assert cfg.m_Data.m_Files[0] is fileData
        assert type(cfg.m_Data.m_AllFilesByName) is dict
        assert len(cfg.m_Data.m_AllFilesByName) == 1
        assert len(cfg.m_Data.m_AllFilesByName.keys()) == 1
        assert "postgresql.auto.conf" in cfg.m_Data.m_AllFilesByName.keys()
        assert len(cfg.m_Data.m_AllFilesByName.values()) == 1
        assert fileData in cfg.m_Data.m_AllFilesByName.values()

        assert type(cfg.m_Data.m_AllOptionsByName) is dict
        assert len(cfg.m_Data.m_AllOptionsByName) == 1
        assert optName in cfg.m_Data.m_AllOptionsByName.keys()
        assert len(cfg.m_Data.m_AllOptionsByName.values()) == 1
        assert opt.m_OptionData in cfg.m_Data.m_AllOptionsByName.values()

    # --------------------------------------------------------------------
    def test_003__port___bad_type(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        with pytest.raises(
            Exception,
            match=re.escape(
                "Bad option [port] value type [bool]. Expected type is [int]."
            ),
        ):
            cfg.SetOptionValue("port", True)

    # --------------------------------------------------------------------
    def test_004__port___cont_convert_value(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        with pytest.raises(
            Exception,
            match=re.escape(
                "Can't convert option [port] value from type [str] to type [int]."
            ),
        ):
            cfg.SetOptionValue("port", "123.")

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_006(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 123)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 123

        r2 = cfg.SetOptionValue(optName, 321)
        assert type(r2) is PgCfg_SetOptionResult_Base
        assert r2.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_UPDATED
        assert r2.Option.get_Name() == optName
        assert r2.Option.get_Value() == 321

        assert r1.Option.get_Value() == 321

        # -------------- DIRECT ASSIGN
        r3 = r1.Option.set_Value(555)
        assert type(r3) is PgCfg_SetOptionResult_Base
        assert r3.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_UPDATED
        assert r3.Option is r1.Option
        assert r3.Option.get_Name() == optName
        assert r3.Option.get_Value() == 555

        assert r1.Option.get_Value() == 555
        assert r2.Option.get_Value() == 555

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_007__set_None(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r = cfg.SetOptionValue(optName, None)
        assert type(r) is PgCfg_SetOptionResult_Base
        assert r.m_EventID == PgCfg_SetOptionEventID.NONE
        assert r.m_Cfg is None
        assert r.m_Opt is None
        assert r.m_OptData is None
        assert r.Option is None

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_008__set_Int_set_None(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 123)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.m_Cfg is cfg
        assert r1.m_OptData is not None
        assert r1.m_Opt is None
        assert r1.Option is not None
        assert r1.Option is r1.m_Opt

        assert len(cfg.m_Data.m_Files) == 1
        assert type(cfg.m_Data.m_Files[0]) is PgCfgModel__FileData
        assert len(cfg.m_Data.m_Files[0].m_Lines) == 1
        assert len(cfg.m_Data.m_AllOptionsByName) == 1

        r2 = cfg.SetOptionValue(optName, None)
        assert type(r2) is PgCfg_SetOptionResult_Base
        assert r2.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_DELETED
        assert r2.m_Cfg is None
        assert r2.m_Opt is None
        assert r2.m_OptData is None
        assert r2.Option is None

        assert len(cfg.m_Data.m_Files) == 1
        assert type(cfg.m_Data.m_Files[0]) is PgCfgModel__FileData
        assert len(cfg.m_Data.m_Files[0].m_Lines) == 0
        assert len(cfg.m_Data.m_AllOptionsByName) == 0

        assert type(r1.Option) is PgCfg_Option_Base
        assert isinstance(r1.Option, PgCfg_Option)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Name()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Value()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.set_Value(123)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.set_Value(None)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Parent()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Configuration()

        r3 = cfg.SetOptionValue(optName, None)
        assert type(r3) is PgCfg_SetOptionResult_Base
        assert r3.m_EventID == PgCfg_SetOptionEventID.NONE
        assert r3.m_Cfg is None
        assert r3.m_Opt is None
        assert r3.m_OptData is None
        assert r3.Option is None

    # --------------------------------------------------------------------
    def test_009__spec_file(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile("postgresql.proxima.conf")
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base
        assert type(file1.m_FileData) is PgCfgModel__FileData
        assert type(file1.m_FileData.m_OptionsByName) is dict
        assert len(file1.m_FileData.m_OptionsByName) == 0

        assert len(cfg.get_AllFiles()) == 1
        assert (
            cfg.get_AllFiles().__iter__().__next__().Private__GetFileData()
            is file1.m_FileData
        )

        optValues = [1, 2, 3, 4]

        C_OPT_NAME = "proxima.port"

        for optValue in optValues:
            assert len(file1.get_Lines()) == 0
            assert len(file1.m_FileData.m_OptionsByName) == 0

            rs1 = cfg.SetOptionValue(C_OPT_NAME, optValue)
            assert type(rs1) is PgCfg_SetOptionResult_Base
            assert type(rs1.m_OptData) is PgCfgModel__OptionData
            assert rs1.m_OptData.m_Value == optValue
            assert rs1.m_OptData.m_Name == C_OPT_NAME
            assert rs1.Option.get_Name() == C_OPT_NAME
            assert rs1.Option.get_Value() == optValue
            assert rs1.Option.get_Configuration() is cfg

            assert len(file1.get_Lines()) == 1
            assert len(file1.m_FileData.m_OptionsByName) == 1
            assert C_OPT_NAME in file1.m_FileData.m_OptionsByName.keys()
            assert (  # noqa: E721
                type(file1.m_FileData.m_OptionsByName[C_OPT_NAME])
                == PgCfgModel__OptionData
            )
            assert file1.m_FileData.m_OptionsByName[C_OPT_NAME] is rs1.m_OptData

            assert cfg.m_Data is not None
            assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
            assert type(cfg.m_Data.m_AllOptionsByName) is dict
            assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
            assert (  # noqa: E721
                type(cfg.m_Data.m_AllOptionsByName[C_OPT_NAME])
                == PgCfgModel__OptionData
            )
            assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is rs1.m_OptData

            cfg.SetOptionValue(C_OPT_NAME, None)

            assert len(file1.get_Lines()) == 0

    # --------------------------------------------------------------------
    def test_010__None_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        with pytest.raises(Exception, match=re.escape("Option name is None.")):
            cfg.SetOptionValue(None, 123)

    # --------------------------------------------------------------------
    def test_011__empty_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        with pytest.raises(Exception, match=re.escape("Option name is empty.")):
            cfg.SetOptionValue("", 123)

    # --------------------------------------------------------------------
    sm_data012__values: typing.List[typing.Tuple[str, str, any, any]] = [
        ("port-int_int", "port", 123, 123),
        ("port-str_int", "port", "321", 321),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data012__values, ids=[x[0] for x in sm_data012__values])
    def data012(self, request: pytest.FixtureRequest) -> typing.Tuple[str, any, any]:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) is tuple
        assert len(request.param) == 4
        assert type(request.param[0]) is str
        return request.param[1:]

    # --------------------------------------------------------------------
    def test_012__one_opt(
        self, request: pytest.FixtureRequest, data012: typing.Tuple[str, any, any]
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data012) is tuple
        assert len(data012) == 3

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r = cfg.SetOptionValue(data012[0], data012[1])
        assert type(r) is PgCfg_SetOptionResult_Base
        assert isinstance(r, PgCfg_SetOptionResult)
        assert r.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        r_option: PgCfg_Option_Base = r.Option
        assert r_option is not None
        assert type(r_option) is PgCfg_Option_Base
        assert isinstance(r_option, PostgresConfigurationOption)
        assert r.Option is r_option  # check a cache

        __class__.Helper__CheckStateOfCfgWithOneOpt(
            cfg, r_option, data012[0], data012[2]
        )


# //////////////////////////////////////////////////////////////////////////////
