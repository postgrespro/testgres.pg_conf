# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfiguration_Base as PgCfg_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base

from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData

from src.abstract.v00.configuration import PostgresConfiguration as PgCfg
from src.abstract.v00.configuration import PostgresConfigurationFile as PgCfg_File
# fmt: on

from .......TestServices import TestServices

import pytest
import typing
import os
import re
import logging

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None
        assert type(file) is PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert file.get_Path() == os.path.join(rootTmpDir, cfg.C_POSTGRESQL_CONF)
        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert len(file.get_Lines()) == 0
        assert len(list(file.get_Lines())) == 0

        set_r1 = file.SetOptionValue(optName, 123)

        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert set_r1 is not None
        assert type(set_r1) is PgCfg_SetOptionResult_Base
        assert type(set_r1.m_EventID) == PgCfg_SetOptionEventID  # noqa: E721
        assert type(set_r1.m_OptData) is PgCfgModel__OptionData
        assert type(set_r1.m_Cfg) == PgCfg_Std  # noqa: E721
        assert isinstance(set_r1.m_Cfg, PgCfg_Base)
        assert isinstance(set_r1.m_Cfg, PgCfg)
        assert set_r1.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert set_r1.m_Cfg is cfg
        assert set_r1.m_OptData.m_Name == optName
        assert set_r1.m_OptData.m_Value == 123
        assert set_r1.m_OptData.get_Parent().get_Parent() is file.m_FileData

        assert type(file.m_FileData.m_Lines) is list
        assert len(file.m_FileData.m_Lines) == 1
        assert (
            type(file.m_FileData.m_Lines[0]) is PgCfgModel__FileLineData
        )
        assert type(file.m_FileData.m_Lines[0].m_Items) is list
        assert len(file.m_FileData.m_Lines[0].m_Items) == 1
        assert file.m_FileData.m_Lines[0].m_Items[0].m_Element is not None
        assert (
            type(file.m_FileData.m_Lines[0].m_Items[0].m_Element)
            is PgCfgModel__OptionData
        )
        assert file.m_FileData.m_Lines[0].m_Items[0].m_Element is set_r1.m_OptData

        option = set_r1.Option
        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.get_Configuration() is cfg
        assert set_r1.Option is option  # check cache

        assert option is not None
        assert option.m_OptionData is set_r1.m_OptData
        assert option.get_Name() == optName
        assert option.get_Value() == 123
        assert option.get_Configuration() is cfg

        optionFileLine = option.get_Parent()
        assert optionFileLine is not None
        assert type(optionFileLine) is PgCfg_FileLine_Base
        assert optionFileLine.m_FileLineData.m_Items[0].m_Element is set_r1.m_OptData

        optionFile = optionFileLine.get_Parent()
        assert type(optionFile) is PgCfg_TopLevelFile_Base
        assert isinstance(optionFile, PgCfg_File_Base)
        assert isinstance(optionFile, PgCfg_File)
        assert optionFile.m_FileData == optionFile.m_FileData

        assert option.m_OptionData is not None
        assert type(option.m_OptionData) is PgCfgModel__OptionData

        assert optName in optionFile.m_FileData.m_OptionsByName.keys()
        assert optionFile.m_FileData.m_OptionsByName[optName] is option.m_OptionData

        assert optName in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[optName] is option.m_OptionData

        assert cfg.GetOptionValue(optName) == 123

        set_r2 = cfg.SetOptionValue(optName, 321)
        assert type(set_r2) is PgCfg_SetOptionResult_Base

        assert set_r2.m_OptData is option.m_OptionData
        assert set_r2.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_UPDATED

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == optName
        assert option.m_OptionData.m_Value == 321
        assert option.get_Name() == optName
        assert option.get_Value() == 321

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002__set_None(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        file.SetOptionValue(optName, 345)
        assert cfg.GetOptionValue(optName) == 345

        set_r2 = file.SetOptionValue(optName, None)

        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert set_r2 is not None
        assert type(set_r2) is PgCfg_SetOptionResult_Base
        assert type(set_r2.m_EventID) == PgCfg_SetOptionEventID  # noqa: E721
        assert set_r2.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_DELETED
        assert set_r2.m_Cfg is None
        assert set_r2.m_OptData is None

        assert cfg.GetOptionValue(optName) is None

        set_r3 = file.SetOptionValue(optName, None)

        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert set_r3 is not None
        assert type(set_r3) is PgCfg_SetOptionResult_Base
        assert type(set_r3.m_EventID) == PgCfg_SetOptionEventID  # noqa: E721
        assert set_r3.m_EventID == PgCfg_SetOptionEventID.NONE
        assert set_r3.m_Cfg is None
        assert set_r3.m_OptData is None

        assert cfg.GetOptionValue(optName) is None

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_003__already_exist(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        option1 = file1.SetOptionValue(optName, 123).Option
        assert type(option1) is PgCfg_Option_Base

        assert option1.get_Name() == optName
        assert option1.get_Value() == 123

        assert len(file1.get_Lines()) == 1
        assert len(file2.get_Lines()) == 0

        with pytest.raises(
            Exception,
            match=re.escape(
                "Option [{0}] already exist in another file [{1}].".format(
                    optName, file1.get_Path()
                )
            ),
        ):
            file2.SetOptionValue(optName, 321)

        assert option1.get_Name() == optName
        assert option1.get_Value() == 123

        assert len(file1.get_Lines()) == 1
        assert len(file2.get_Lines()) == 0

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_004__set_value_with_bad_type(
        self, request: pytest.FixtureRequest, optName: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        badValues = [True, False]

        for badValue in badValues:
            logging.info("--------- badValue: {0}".format(badValue))

            errMsg = (
                "Bad option [{0}] value type [{1}]. Expected type is [{2}].".format(
                    optName, type(badValue).__name__, "int"
                )
            )

            with pytest.raises(Exception, match=re.escape(errMsg)):
                file1.SetOptionValue(optName, badValue)

            assert len(cfg.m_Data.m_AllOptionsByName) == 0
            assert len(file1.m_FileData.m_OptionsByName) == 0

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_005__cant_convert_value(
        self, request: pytest.FixtureRequest, optName: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        badValues = ["xyz", "abc", "123."]

        for badValue in badValues:
            logging.info("--------- badValue: {0}".format(badValue))

            errMsg = "Can't convert option [{0}] value from type [{1}] to type [{2}].".format(
                optName, type(badValue).__name__, "int"
            )

            with pytest.raises(Exception, match=re.escape(errMsg)):
                file1.SetOptionValue(optName, badValue)

            assert len(cfg.m_Data.m_AllOptionsByName) == 0
            assert len(file1.m_FileData.m_OptionsByName) == 0


# //////////////////////////////////////////////////////////////////////////////
