# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.abstract.v00.configuration import PostgresConfigurationOption

from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult as PgCfg_SetOptionResult
from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import typing

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001__port(
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

        set_r = cfg.SetOptionValue(optName, 123)
        assert type(set_r) is PgCfg_SetOptionResult_Base
        assert isinstance(set_r, PgCfg_SetOptionResult)
        assert set_r.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        set_r_option = set_r.Option
        assert set_r_option is not None
        assert type(set_r_option) is PgCfg_Option_Base
        assert isinstance(set_r_option, PostgresConfigurationOption)
        assert set_r.Option is set_r_option  # check a cache

        assert set_r_option.get_Configuration() is cfg
        assert set_r_option.get_Name() == optName
        assert set_r_option.get_Value() == 123

        get_r = cfg.GetOptionValue(optName)
        assert type(get_r) is int
        assert get_r == 123
        return

    # --------------------------------------------------------------------
    def test_002__None_name(
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

        with pytest.raises(PostgresConfigException) as x:
            cfg.GetOptionValue(None)

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsNone()
        return

    # --------------------------------------------------------------------
    def test_003__empty_name(
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

        with pytest.raises(PostgresConfigException) as x:
            cfg.GetOptionValue("")

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsEmpty()
        return

    # --------------------------------------------------------------------
    def test_004__opt_with_list__get_None(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        v = cfg.GetOptionValue(C_OPT_NAME)

        assert v is None
        return

    # --------------------------------------------------------------------
    def test_005__mult_opts_in_auto__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        opt1 = cfg.AddOption(C_OPT_NAME, 1)
        assert opt1 is not None

        opt2 = cfg.AddOption(C_OPT_NAME, 2)
        assert opt2 is not None

        assert opt1.m_OptionData is not opt2.m_OptionData

        assert opt1.get_Name() == C_OPT_NAME
        assert opt1.get_Value() == 1

        assert opt2.get_Name() == C_OPT_NAME
        assert opt2.get_Value() == 2

        # ----------
        v = cfg.GetOptionValue(C_OPT_NAME)
        assert v is not None
        assert type(v) is int
        assert v == 2

        return

    # --------------------------------------------------------------------
    def test_006__mult_opts_in_pgconf__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        opt1 = file1.AddOption(C_OPT_NAME, 1)
        assert opt1 is not None

        opt2 = file1.AddOption(C_OPT_NAME, 2)
        assert opt2 is not None

        assert opt1.m_OptionData is not opt2.m_OptionData

        assert opt1.get_Name() == C_OPT_NAME
        assert opt1.get_Value() == 1

        assert opt2.get_Name() == C_OPT_NAME
        assert opt2.get_Value() == 2

        # ----------
        v = cfg.GetOptionValue(C_OPT_NAME)
        assert v is not None
        assert type(v) is int
        assert v == 2

        return

    # --------------------------------------------------------------------
    def test_007__mult_opts_and_includes__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        file2 = cfg.AddTopLevelFile("a.conf")
        assert file2 is not None
        file3 = cfg.AddTopLevelFile("b.conf")
        assert file3 is not None
        file4 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)
        assert file4 is not None

        opt1 = file2.AddOption(C_OPT_NAME, 1)
        assert opt1 is not None

        opt2 = file2.AddOption(C_OPT_NAME, 2)
        assert opt2 is not None

        file2.AddInclude("b.conf")
        file2.AddInclude("b.conf")

        file4.AddInclude("b.conf")
        file4.AddComment("O-LA-LA")
        file4.AddEmptyLine()
        file4.AddOption("blablabla", "123")

        assert opt1.m_OptionData is not opt2.m_OptionData

        assert opt1.get_Name() == C_OPT_NAME
        assert opt1.get_Value() == 1

        assert opt2.get_Name() == C_OPT_NAME
        assert opt2.get_Value() == 2

        # ----------
        v = cfg.GetOptionValue(C_OPT_NAME)
        assert v is not None
        assert type(v) is int
        assert v == 2

        return

    # --------------------------------------------------------------------
    def test_008__opt_in_include(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None
        file2 = file1.AddInclude("b.conf").get_File()
        assert file2 is not None
        file3 = file1.AddInclude("c.conf").get_File()
        assert file3 is not None

        option = file3.AddOption(C_OPT_NAME, 321)
        assert option is not None

        v = cfg.GetOptionValue(C_OPT_NAME)
        assert v is not None
        assert type(v) is int
        assert v == 321

    # --------------------------------------------------------------------
    def test_009__cycle_in_files(
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

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None
        file2 = file1.AddInclude("b.conf").get_File()
        assert file2 is not None
        file3 = file1.AddInclude("c.conf").get_File()
        assert file3 is not None

        file1a = file3.AddInclude("a.conf").get_File()
        assert file1a is not None
        assert file1.m_FileData is file1a.m_FileData

        v = cfg.GetOptionValue("a")
        assert v is None
        return

    # --------------------------------------------------------------------
    def test_010__subcycle_in_files(
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

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None
        file2 = file1.AddInclude("b.conf").get_File()
        assert file2 is not None
        file3 = file1.AddInclude("c.conf").get_File()
        assert file3 is not None

        file2a = file3.AddInclude("b.conf").get_File()
        assert file2a is not None
        assert file2.m_FileData is file2a.m_FileData

        v = cfg.GetOptionValue("c")
        assert v is None
        return


# //////////////////////////////////////////////////////////////////////////////
