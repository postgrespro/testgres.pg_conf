# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_std import PostgresConfigurationReader_Base as PgCfg_Reader_Base

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID

from src.exceptions import PostgresConfigException

from .....TestServices import TestServices
# fmt: on

import pytest
import logging
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet002__EdgeCases


class TestSet003__EdgeCases:
    def test_001__diamond_include__Standard(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        # Author: Mark G. <mark@google.com>

        rootTmpDir = TestServices.GetCurTestTmpDir(request)
        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_PG_CONF = PgCfg_Std.C_POSTGRESQL_CONF
        C_COMMON_CONF = "common.conf"
        C_OVERRIDE_CONF = "override.conf"

        # 1. Create common.conf with base port value
        commonConfPath = os.path.join(rootTmpDir, C_COMMON_CONF)
        logging.info("Creating {0}...".format(commonConfPath))
        with open(commonConfPath, "x") as f:
            # fmt: off
            f.write("# Common base configuration\n")
            f.write("port = 5432\n")
            f.flush()
            # fmt: on

        # 2. Create override.conf which changes the port
        overrideConfPath = os.path.join(rootTmpDir, C_OVERRIDE_CONF)
        logging.info("Creating {0}...".format(overrideConfPath))
        with open(overrideConfPath, "x") as f:
            # fmt: off
            f.write("# Override configuration\n")
            f.write("port = 5433\n")
            f.flush()
            # fmt: on

        # 3. Create postgresql.conf with diamond/repeated include:
        # common.conf (5432) -> override.conf (5433) -> common.conf (5432)
        pgConfPath = os.path.join(rootTmpDir, C_PG_CONF)
        logging.info("Creating {0}...".format(pgConfPath))
        with open(pgConfPath, "x") as f:
            # fmt: off
            f.write("include '{0}'\n".format(C_COMMON_CONF))
            f.write("include '{0}'\n".format(C_OVERRIDE_CONF))
            f.write("include '{0}'\n".format(C_COMMON_CONF))
            f.flush()
            # fmt: on

        # ---------------
        # Initialize in Standard mode
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )

        # ---------------
        # Load configuration
        PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_PG_CONF)

        # Should load 3 unique files despite repeated includes
        assert len(cfg.get_AllFiles()) == 3

        # Reverse DFS must hit the last include ('common.conf') first
        # and return 5432, ignoring the earlier 'override.conf' (5433)
        assert cfg.GetOptionValue("port") == 5432

        # Total option instances across unique loaded files must be 2
        # (one in common.conf, one in override.conf)
        assert len(cfg.get_AllOptions()) == 2
        return

    # --------------------------------------------------------------------
    def test_002__fallback_after_delete__Standard(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        # Author: Mark G. <mark@google.com>

        rootTmpDir = TestServices.GetCurTestTmpDir(request)
        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_PG_CONF = PgCfg_Std.C_POSTGRESQL_CONF
        C_AUTO_CONF = PgCfg_Std.C_POSTGRESQL_AUTO_CONF

        # 1. Create postgresql.conf with two inline definitions of max_connections
        pgConfPath = os.path.join(rootTmpDir, C_PG_CONF)
        with open(pgConfPath, "x") as f:
            # fmt: off
            f.write("max_connections = 100\n")
            f.write("max_connections = 200\n")
            f.flush()
            # fmt: on

        # 2. Initialize in Standard mode and load postgresql.conf
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )
        pgFile = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_PG_CONF)

        assert cfg.GetOptionValue("max_connections") == 200
        assert len(cfg.get_AllOptions()) == 2

        # 3. Override globally -> creates postgresql.auto.conf with max_connections = 500
        r_auto = cfg.SetOptionValue("max_connections", 500)
        assert r_auto.Option is not None
        autoOpt = r_auto.Option

        autoLine = autoOpt.get_Parent()
        assert autoLine.get_Parent().get_Path().endswith(C_AUTO_CONF)
        assert cfg.GetOptionValue("max_connections") == 500
        assert len(cfg.get_AllOptions()) == 3

        # 4. Clear the line containing the top-level override in postgresql.auto.conf
        autoLine.Clear()

        # The line itself stays alive (now empty), but the option object must be dead
        assert len(autoLine) == 0

        with pytest.raises(PostgresConfigException):
            autoOpt.get_Value()

        # Global value must fall back to the latest duplicate in postgresql.conf (200)
        assert cfg.GetOptionValue("max_connections") == 200
        assert len(cfg.get_AllOptions()) == 2

        # 5. Clear the second line in postgresql.conf (which holds max_connections = 200)
        pgLines = list(pgFile.get_Lines())
        assert len(pgLines) == 2

        pgLines[1].Clear()

        # Find the option object located on line 1 (comparing underlying m_FileLineData)
        secondOpt = None
        for opt in cfg.get_AllOptions():
            if opt.get_Parent().m_FileLineData.m_Parent is pgFile.m_FileData:
                secondOpt = opt
                break

        assert secondOpt is not None
        assert secondOpt.get_Value() == 100

        # Global value must now fall back to the very first definition (100)
        assert cfg.GetOptionValue("max_connections") == 100
        assert len(cfg.get_AllOptions()) == 1
        return

    # --------------------------------------------------------------------
    def test_003__insert_include_after_option_and_update__Standard(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        # Author: Mark G. <mark@google.com>

        rootTmpDir = TestServices.GetCurTestTmpDir(request)
        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_PG_CONF = PgCfg_Std.C_POSTGRESQL_CONF
        C_OVERRIDE_CONF = "override.conf"

        # 1. Create override.conf on disk with port = 5433
        overrideConfPath = os.path.join(rootTmpDir, C_OVERRIDE_CONF)
        with open(overrideConfPath, "x") as f:
            # fmt: off
            f.write("port = 5433\n")
            f.flush()
            # fmt: on

        # 2. Initialize in Standard mode and create top-level postgresql.conf
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )
        pgFile = cfg.AddTopLevelFile(C_PG_CONF)

        # Add initial option: port = 5432
        r_init = pgFile.SetOptionValue("port", 5432)
        assert r_init.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r_init.Option is not None
        firstOpt = r_init.Option

        assert pgFile.GetOptionValue("port") == 5432
        assert cfg.GetOptionValue("port") == 5432

        # 3. Append include directive AFTER the existing option
        inc = pgFile.AddInclude(C_OVERRIDE_CONF)
        incFile = inc.get_File()

        with cfg.m_Data.OsOps.OpenFileToRead(incFile.get_Path()) as f:
            PgCfg_Reader_Base.LoadFileContent(incFile, f)

        # Now override.conf takes precedence (5433)
        assert pgFile.GetOptionValue("port") == 5433
        assert cfg.GetOptionValue("port") == 5433

        # 4. Update 'port' via pgFile.SetOptionValue
        # Because an include exists below the initial option, enterIntoIncludes=False
        # must prevent updating line 0 in-place and must append a new option at the tail.
        r_upd = pgFile.SetOptionValue("port", 5434)
        assert r_upd.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r_upd.Option is not None
        lastOpt = r_upd.Option

        # Verify that a new distinct OptionData was created at the end of postgresql.conf
        assert lastOpt.m_OptionData is not firstOpt.m_OptionData
        assert firstOpt.get_Value() == 5432
        assert lastOpt.get_Value() == 5434

        # Verify effective values across file and global config
        assert pgFile.GetOptionValue("port") == 5434
        assert cfg.GetOptionValue("port") == 5434

        # Total lines in postgresql.conf:
        # 0: port = 5432
        # 1: include 'override.conf'
        # 2: port = 5434
        assert len(pgFile.get_Lines()) == 3
        assert len(cfg.get_AllOptions()) == 3
        return

    # --------------------------------------------------------------------
    def test_004__global_reset_with_multiple_duplicates__Standard(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        # Author: Mark G. <mark@google.com>

        rootTmpDir = TestServices.GetCurTestTmpDir(request)
        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_PG_CONF = PgCfg_Std.C_POSTGRESQL_CONF
        C_BIHA_CONF = "postgresql.biha.conf"

        # 1. Create postgresql.conf with two definitions of 'port' (one with inline comment)
        # and an unrelated option 'max_connections'
        pgConfPath = os.path.join(rootTmpDir, C_PG_CONF)
        with open(pgConfPath, "x") as f:
            # fmt: off
            f.write("port = 5432 # first def\n")
            f.write("max_connections = 100\n")
            f.write("port = 5433\n")
            f.write("include '{0}'\n".format(C_BIHA_CONF))
            f.flush()
            # fmt: on

        # 2. Create postgresql.biha.conf with a third definition of 'port'
        bihaConfPath = os.path.join(rootTmpDir, C_BIHA_CONF)
        with open(bihaConfPath, "x") as f:
            # fmt: off
            f.write("port = 5434\n")
            f.flush()
            # fmt: on

        # 3. Initialize in Standard mode and load files
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )
        pgFile = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_PG_CONF)
        bihaFile = cfg.get_AllFiles().GetFileByName(C_BIHA_CONF)

        assert cfg.GetOptionValue("port") == 5434
        # 3 instances of 'port' + 1 instance of 'max_connections' = 4 total
        assert len(cfg.get_AllOptions()) == 4

        # Collect references to all 3 'port' option objects before deletion
        portOptions = [opt for opt in cfg.get_AllOptions() if opt.get_Name() == "port"]
        assert len(portOptions) == 3

        # 4. Perform global reset of 'port' (SetOptionValue with None)
        res = cfg.SetOptionValue("port", None)
        assert res.EventID == PgCfg_SetOptionEventID.OPTION_WAS_DELETED
        assert res.Option is None

        # Verify 'port' is completely gone globally and from each file
        assert cfg.GetOptionValue("port") is None
        assert pgFile.GetOptionValue("port") is None
        assert bihaFile.GetOptionValue("port") is None

        # Verify unrelated option 'max_connections' is untouched
        assert cfg.GetOptionValue("max_connections") == 100
        assert len(cfg.get_AllOptions()) == 1

        # Verify all 3 previously acquired Option objects are now dead
        for opt in portOptions:
            with pytest.raises(PostgresConfigException):
                opt.get_Value()

        # Verify file lines structure is preserved:
        # Line 0 in postgresql.conf still holds its inline comment '# first def'
        pgLines = list(pgFile.get_Lines())
        assert len(pgLines) == 2
        assert len(pgLines[0]) == 1
        assert len(pgLines[1]) == 1

        assert pgFile.GetOptionValue("max_connections") == 100

        bihaLines = list(bihaFile.get_Lines())
        assert len(bihaLines) == 0

        # 5. Repeated reset on already deleted option must return NONE event
        res_again = cfg.SetOptionValue("port", None)
        assert res_again.EventID == PgCfg_SetOptionEventID.NONE
        return

    # --------------------------------------------------------------------
    def test_005__repeated_set_option_item_around_include__Standard(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        # Author: Mark G. <mark@google.com>

        rootTmpDir = TestServices.GetCurTestTmpDir(request)
        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_PG_CONF = PgCfg_Std.C_POSTGRESQL_CONF
        C_INC_CONF = "a.conf"
        C_AUTO_CONF = PgCfg_Std.C_POSTGRESQL_AUTO_CONF
        C_OPT_NAME = "shared_preload_libraries"

        # 1. Create empty a.conf and postgresql.conf with initial library + include
        with open(os.path.join(rootTmpDir, C_INC_CONF), "x") as f:
            f.flush()

        with open(os.path.join(rootTmpDir, C_PG_CONF), "x") as f:
            # fmt: off
            f.write("{0} = 'biha'\n".format(C_OPT_NAME))
            f.write("include '{0}'\n".format(C_INC_CONF))
            f.flush()
            # fmt: on

        # 2. Load configuration in Standard mode
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )
        pgFile = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_PG_CONF)

        assert cfg.GetOptionValue(C_OPT_NAME) == ["biha"]
        assert len(cfg.get_AllOptions()) == 1

        # 3. First global SetOptionValueItem -> creates entry in postgresql.auto.conf
        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "proxima")
        assert r1.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
        assert r1.Option is not None
        assert r1.Option.get_Value() == ["biha", "proxima"]
        assert r1.Option.get_Parent().get_Parent().get_Path().endswith(C_AUTO_CONF)
        assert len(cfg.get_AllOptions()) == 2

        # 4. Second global SetOptionValueItem -> must update the same entry in auto.conf
        # without creating a third duplicate
        r2 = cfg.SetOptionValueItem(C_OPT_NAME, "pg_stat_statements")
        assert r2.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
        assert r2.Option is not None
        assert r2.Option.m_OptionData is r1.Option.m_OptionData
        assert r2.Option.get_Value() == ["biha", "proxima", "pg_stat_statements"]

        # Verify total count and original file isolation
        assert len(cfg.get_AllOptions()) == 2
        assert cfg.GetOptionValue(C_OPT_NAME) == [
            "biha",
            "proxima",
            "pg_stat_statements",
        ]
        assert pgFile.GetOptionValue(C_OPT_NAME) == ["biha"]
        return


# //////////////////////////////////////////////////////////////////////////////
