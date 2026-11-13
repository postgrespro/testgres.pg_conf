# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID

from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__ConfigurationData

from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None
        assert type(file) is PgCfg_TopLevelFile_Base
        assert file.get_Path() == os.path.join(rootTmpDir, cfg.C_POSTGRESQL_CONF)
        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        C_OPT_NAME = "port"

        option = file.AddOption(C_OPT_NAME, 123)

        assert file.m_FileData is not None
        assert type(file.m_FileData) is PgCfgModel__FileData

        assert option is not None
        assert option.get_Configuration() is cfg
        assert (
            option.get_Parent().get_Parent().Private__GetFileData() == file.m_FileData
        )
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == 123
        assert option.m_OptionData is not None
        assert type(option.m_OptionData) is PgCfgModel__OptionData

        assert C_OPT_NAME in file.m_FileData.m_OptionsByName.keys()
        assert file.m_FileData.m_OptionsByName[C_OPT_NAME] is option.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is option.m_OptionData
        return

    # --------------------------------------------------------------------
    def test_002__00A__already_in_this__Strict(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "port"

        if pg_conf_strategy == PgCfg_Std.Strategy.Standard:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        option = file.AddOption(C_OPT_NAME, 123)

        with pytest.raises(PostgresConfigException) as x:
            file.AddOption(C_OPT_NAME, 321)

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInThisFile(
            file.get_Path(),
            C_OPT_NAME,
        )
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == 123

        assert C_OPT_NAME in file.m_FileData.m_OptionsByName.keys()
        assert file.m_FileData.m_OptionsByName[C_OPT_NAME] is option.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is option.m_OptionData
        return

    # --------------------------------------------------------------------
    def test_002__00B__already_in_this__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "port"

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        option1 = file.AddOption(C_OPT_NAME, 123)
        option2 = file.AddOption(C_OPT_NAME, 321)

        assert option1.get_Name() == C_OPT_NAME
        assert option1.get_Value() == 123

        assert option2.get_Name() == C_OPT_NAME
        assert option2.get_Value() == 321

        assert option1.m_OptionData is not option2.m_OptionData

        assert C_OPT_NAME in file.m_FileData.m_OptionsByName.keys()
        s1 = file.m_FileData.m_OptionsByName[C_OPT_NAME]
        assert type(s1) is list
        assert len(s1) == 2

        assert option1.m_OptionData in s1
        assert option2.m_OptionData in s1

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        s2 = cfg.m_Data.m_AllOptionsByName[C_OPT_NAME]
        assert type(s2) is list
        assert len(s2) == 2

        assert option1.m_OptionData in s2
        assert option2.m_OptionData in s2
        return

    # --------------------------------------------------------------------
    def test_003__00A__already_in_another__Strict(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "proxima.port"

        if pg_conf_strategy == PgCfg_Std.Strategy.Standard:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile("postgresql.auto.conf")
        option = cfg.SetOptionValue(C_OPT_NAME, 123).Option
        assert type(option) is PgCfg_Option_Base
        assert len(file1) == 1

        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        with pytest.raises(PostgresConfigException) as x:
            file2.AddOption(C_OPT_NAME, 321)

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInAnotherFile(
            file1.get_Path(),
            C_OPT_NAME,
        )
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == 123

        assert C_OPT_NAME in file1.m_FileData.m_OptionsByName.keys()
        assert file1.m_FileData.m_OptionsByName[C_OPT_NAME] is option.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is option.m_OptionData
        return

    # --------------------------------------------------------------------
    def test_003__00B__already_in_another__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "proxima.port"

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile("postgresql.auto.conf")
        option1 = cfg.SetOptionValue(C_OPT_NAME, 123).Option
        assert type(option1) is PgCfg_Option_Base
        assert len(file1) == 1

        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        option2 = file2.AddOption(C_OPT_NAME, 321)

        assert option1.get_Name() == C_OPT_NAME
        assert option1.get_Value() == 123

        assert option2.get_Name() == C_OPT_NAME
        assert option2.get_Value() == 321

        assert C_OPT_NAME in file1.m_FileData.m_OptionsByName.keys()
        assert file1.m_FileData.m_OptionsByName[C_OPT_NAME] is option1.m_OptionData

        assert C_OPT_NAME in file2.m_FileData.m_OptionsByName.keys()
        assert file2.m_FileData.m_OptionsByName[C_OPT_NAME] is option2.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        s2 = cfg.m_Data.m_AllOptionsByName[C_OPT_NAME]
        assert type(s2) is list
        assert len(s2) == 2
        assert option1.m_OptionData in s2
        assert option2.m_OptionData in s2
        return

    # --------------------------------------------------------------------
    def test_004__bad_value_type(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(PostgresConfigException) as x:
            file.AddOption(C_OPT_NAME, False)

        assert str(x.value) == ErrorMessageBuilder.BadOptionValueType(
            C_OPT_NAME,
            bool,
            int,
        )
        return

    # --------------------------------------------------------------------
    def test_004__cant_convert_value(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(PostgresConfigException) as x:
            file.AddOption(C_OPT_NAME, "blabla")

        assert str(x.value) == ErrorMessageBuilder.CantConvertOptionValue(
            C_OPT_NAME,
            str,
            int,
        )
        return

    # --------------------------------------------------------------------
    def test_005__None_value(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(PostgresConfigException) as x:
            file.AddOption(C_OPT_NAME, None)

        assert str(x.value) == ErrorMessageBuilder.NoneValueIsNotSupported()
        return

    # --------------------------------------------------------------------
    def test_006__None_name(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(PostgresConfigException) as x:
            file.AddOption(None, 123)

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsNone()
        return

    # --------------------------------------------------------------------
    def test_007__empty_name(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(PostgresConfigException) as x:
            file.AddOption("", 123)

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsEmpty()
        return

    # --------------------------------------------------------------------
    def test_015__set_twice_around_include__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        C_OPT_NAME = "port"

        file1 = cfg.AddTopLevelFile("fil1.conf")
        assert file1 is not None

        r1 = file1.SetOptionValue(C_OPT_NAME, 1)
        assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option is not None
        assert r1.Option.get_Parent().get_Parent().m_FileData is file1.m_FileData
        assert r1.Option.get_Value() == 1
        file2 = r1.Option.get_Parent().get_Parent().AddInclude("a.conf")
        assert file2 is not None
        assert file1.GetOptionValue(C_OPT_NAME) == 1
        assert r1.Option.get_Value() == 1
        r2 = file1.SetOptionValue(C_OPT_NAME, 2)
        assert r2.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r2.Option is not None
        assert r2.Option.get_Parent().get_Parent().m_FileData is file1.m_FileData
        assert r2.Option.get_Value() == 2
        assert r2.Option.m_OptionData is not r1.Option.m_OptionData
        assert r1.Option.get_Value() == 1

        assert cfg.GetOptionValue(C_OPT_NAME) == 2
        return


# //////////////////////////////////////////////////////////////////////////////
