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

from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import typing
import os
import logging

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001__Strict(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        if pg_conf_strategy == PgCfg_Std.Strategy.Standard:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

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
        assert type(set_r1.m_EventID) is PgCfg_SetOptionEventID
        assert type(set_r1.m_OptData) is PgCfgModel__OptionData
        assert type(set_r1.m_Cfg) is PgCfg_Std
        assert isinstance(set_r1.m_Cfg, PgCfg_Base)
        assert isinstance(set_r1.m_Cfg, PgCfg)
        assert set_r1.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert set_r1.m_Cfg is cfg
        assert set_r1.m_OptData.m_Name == optName
        assert set_r1.m_OptData.m_Value == 123
        assert set_r1.m_OptData.get_Parent().get_Parent() is file.m_FileData

        assert type(file.m_FileData.m_Lines) is list
        assert len(file.m_FileData.m_Lines) == 1
        assert type(file.m_FileData.m_Lines[0]) is PgCfgModel__FileLineData
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
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002__set_None(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        file.SetOptionValue(optName, 345)
        assert cfg.GetOptionValue(optName) == 345

        set_r2 = file.SetOptionValue(optName, None)

        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert set_r2 is not None
        assert type(set_r2) is PgCfg_SetOptionResult_Base
        assert type(set_r2.m_EventID) is PgCfg_SetOptionEventID
        assert set_r2.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_DELETED
        assert set_r2.m_Cfg is None
        assert set_r2.m_OptData is None

        assert cfg.GetOptionValue(optName) is None

        set_r3 = file.SetOptionValue(optName, None)

        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert set_r3 is not None
        assert type(set_r3) is PgCfg_SetOptionResult_Base
        assert type(set_r3.m_EventID) is PgCfg_SetOptionEventID
        assert set_r3.m_EventID == PgCfg_SetOptionEventID.NONE
        assert set_r3.m_Cfg is None
        assert set_r3.m_OptData is None

        assert cfg.GetOptionValue(optName) is None
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_003__already_exist__Strict(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        if pg_conf_strategy == PgCfg_Std.Strategy.Standard:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        option1 = file1.SetOptionValue(optName, 123).Option
        assert type(option1) is PgCfg_Option_Base

        assert option1.get_Name() == optName
        assert option1.get_Value() == 123

        assert len(file1.get_Lines()) == 1
        assert len(file2.get_Lines()) == 0

        with pytest.raises(PostgresConfigException) as x:
            file2.SetOptionValue(optName, 321)

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInAnotherFile(
            file1.get_Path(),
            optName,
        )

        assert option1.get_Name() == optName
        assert option1.get_Value() == 123

        assert len(file1.get_Lines()) == 1
        assert len(file2.get_Lines()) == 0
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_004__set_value_with_bad_type(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        badValues = [True, False]

        for badValue in badValues:
            logging.info("--------- badValue: {0}".format(badValue))

            with pytest.raises(PostgresConfigException) as x:
                file1.SetOptionValue(optName, badValue)

            assert str(x.value) == ErrorMessageBuilder.BadOptionValueType(
                optName,
                type(badValue),
                int,
            )

            assert cfg.m_Data.m_AllOptionsByName.get_elements_count() == 0
            assert file1.m_FileData.m_OptionsByName.get_elements_count() == 0
            continue
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_005__cant_convert_value(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        badValues = ["xyz", "abc", "123."]

        for badValue in badValues:
            logging.info("--------- badValue: {0}".format(badValue))

            with pytest.raises(PostgresConfigException) as x:
                file1.SetOptionValue(optName, badValue)

            assert str(x.value) == ErrorMessageBuilder.CantConvertOptionValue(
                optName,
                type(badValue),
                int,
            )

            assert cfg.m_Data.m_AllOptionsByName.get_elements_count() == 0
            assert file1.m_FileData.m_OptionsByName.get_elements_count() == 0
            continue
        return


# //////////////////////////////////////////////////////////////////////////////
