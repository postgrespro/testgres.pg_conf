# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_std import PostgresConfigurationReader_Base as PgCfg_Reader_Base
from src.implementation.v00.configuration_std import PostgresConfigurationWriterCtx_Base as PgCfg_WriterCtx_Base
from src.implementation.v00.configuration_std import PostgresConfigurationWriter_Base as PgCfg_Writer_Base

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID


from .....TestServices import TestServices
# fmt: on

import pytest
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet002__RealWork


class TestSet002__RealWork:
    def test_001__modify_and_save_realistic_config__Standard(
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
        C_PROXIMA_CONF = "postgresql.proxima.conf"
        C_AUTO_CONF = PgCfg_Std.C_POSTGRESQL_AUTO_CONF

        # 1. Prepare initial files on disk with comments and duplicates
        pgConfPath = os.path.join(rootTmpDir, C_PG_CONF)
        with open(pgConfPath, "x") as f:
            # fmt: off
            f.write("# Main PostgreSQL config\n")
            f.write("port = 5432 # default port\n")
            f.write("max_connections = 100\n")
            f.write("max_connections = 200 # inline override\n")
            f.write("shared_preload_libraries = 'pg_stat_statements'\n")
            f.write("include '{0}'\n".format(C_BIHA_CONF))
            f.write("include '{0}'\n".format(C_PROXIMA_CONF))
            f.write("listen_addresses = 'localhost'\n")
            f.flush()
            # fmt: on
            f.close()

        bihaConfPath = os.path.join(rootTmpDir, C_BIHA_CONF)
        with open(bihaConfPath, "x") as f:
            # fmt: off
            f.write("# BiHA settings\n")
            f.write("shared_preload_libraries = 'pg_stat_statements, biha'\n")
            f.write("biha.node_id = 1\n")
            f.flush()
            # fmt: on
            f.close()

        proximaConfPath = os.path.join(rootTmpDir, C_PROXIMA_CONF)
        with open(proximaConfPath, "x") as f:
            # fmt: off
            f.write("# Proxima settings\n")
            f.write("proxima.port = 6432\n")
            f.write("proxima.pool_size = 32\n")
            f.flush()
            # fmt: on
            f.close()

        # Note: postgresql.auto.conf does NOT exist yet on disk

        # 2. Load configuration in Standard mode
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )

        pgFile = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_PG_CONF)
        assert pgFile is not None
        assert len(cfg.get_AllFiles()) == 3

        bihaFile = cfg.get_AllFiles().GetFileByName(C_BIHA_CONF)
        proximaFile = cfg.get_AllFiles().GetFileByName(C_PROXIMA_CONF)

        # 3. Perform modifications via object interfaces

        # 3.1. Global override -> must create postgresql.auto.conf and write there
        r_port = cfg.SetOptionValue("port", 5433)
        assert r_port.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r_port.Option is not None
        assert r_port.Option.get_Parent().get_Parent().get_Path().endswith(C_AUTO_CONF)

        # 3.2. Global list item addition -> inherits active list from biha.conf
        # and writes ['pg_stat_statements', 'biha', 'proxima'] into postgresql.auto.conf
        r_libs = cfg.SetOptionValueItem("shared_preload_libraries", "proxima")
        assert r_libs.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
        assert r_libs.Option is not None
        assert r_libs.Option.get_Value() == [
            "pg_stat_statements",
            "biha",
            "proxima",
        ]

        # 3.3. File-scoped update -> updates existing option in-place inside biha.conf
        r_biha = bihaFile.SetOptionValue("biha.node_id", 2)
        assert r_biha.EventID == PgCfg_SetOptionEventID.OPTION_WAS_UPDATED

        # 3.4. File-scoped addition -> appends new option and comment to proxima.conf
        proximaFile.AddComment("Added via API")
        proximaFile.SetOptionValue("proxima.pool_size", 64)

        # 4. Save all changes to disk via Writer
        # (Replace with your actual Writer call, e.g., PgCfg_Writer_Base.SaveConfiguration(cfg))
        writeCtx = PgCfg_WriterCtx_Base(cfg)

        PgCfg_Writer_Base.DoWork(writeCtx)

        # 5. Verify disk state by reloading into a fresh configuration instance
        cfg_reloaded = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )
        PgCfg_Reader_Base.LoadConfigurationFile(cfg_reloaded, C_PG_CONF)
        PgCfg_Reader_Base.LoadConfigurationFile(cfg_reloaded, C_AUTO_CONF)

        assert len(cfg_reloaded.get_AllFiles()) == 4

        # Check effective values after reload
        assert cfg_reloaded.GetOptionValue("port") == 5433
        assert cfg_reloaded.GetOptionValue("max_connections") == 200
        assert cfg_reloaded.GetOptionValue("listen_addresses") == "localhost"
        assert cfg_reloaded.GetOptionValue("biha.node_id") == 2
        assert cfg_reloaded.GetOptionValue("proxima.port") == 6432
        assert cfg_reloaded.GetOptionValue("proxima.pool_size") == 64
        assert cfg_reloaded.GetOptionValue("shared_preload_libraries") == [
            "pg_stat_statements",
            "biha",
            "proxima",
        ]

        # Verify that original postgresql.conf preserved its comments and duplicates intact
        pgFile_reloaded = cfg_reloaded.get_AllFiles().GetFileByName(C_PG_CONF)
        assert pgFile_reloaded.GetOptionValue("port") == 5432
        assert pgFile_reloaded.GetOptionValue("max_connections") == 200
        assert len(pgFile_reloaded.get_Lines()) == 8

        return


# //////////////////////////////////////////////////////////////////////////////
