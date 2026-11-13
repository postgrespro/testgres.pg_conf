# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_std import PostgresConfigurationReader_Base as PgCfg_Reader_Base

from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.implementation.v00.configuration_base import PostgresConfigurationFile as PgCfg_File

from src.implementation.v00.configuration_base import PgCfgModel__CommentData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__FileData

from src.implementation.v00.configuration_base_r import PgCfgModel__FileStatus

from .......TestServices import TestServices
# fmt: on

import pytest
import logging
import os
import datetime

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_000__empty(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        logging.info("File object is creating...")

        filePath = os.path.join(rootTmpDir, PgCfg_Std.C_POSTGRESQL_CONF)

        with open(filePath, "x") as f:
            fd = f.fileno()
            assert type(fd) is int
            lastMDate = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate) is datetime.datetime
            f.close()

        # ---------------
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        # ---------------
        logging.info("File object is loading...")

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_CONF)
        assert type(file) is PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) is PgCfgModel__FileData
        assert file.m_FileData.m_Status == PgCfgModel__FileStatus.EXISTS
        assert file.m_FileData.m_LastModifiedTimestamp == lastMDate
        assert len(file.m_FileData.m_Lines) == 0
        return

    # --------------------------------------------------------------------
    def test_001__comment_and_options(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        logging.info("File object is creating...")

        filePath = os.path.join(rootTmpDir, PgCfg_Std.C_POSTGRESQL_CONF)

        with open(filePath, "x") as f:
            # fmt: off
            f.write("#It is a test configuration file\n")  # 0
            f.write("port=123 #It is a port\n")            # 1
            f.write("\n")                                  # 2
            f.write("listen_addresses='*' #addresses\n")   # 3
            f.write("\n")                                  # 4
            f.flush()
            # fmt: on

            fd = f.fileno()
            assert type(fd) is int
            lastMDate = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate) is datetime.datetime
            f.close()

        # ---------------
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        # ---------------
        logging.info("File object is loading...")

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_CONF)
        assert type(file) is PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) is PgCfgModel__FileData
        assert file.m_FileData.m_Status == PgCfgModel__FileStatus.EXISTS
        assert file.m_FileData.m_LastModifiedTimestamp == lastMDate

        assert cfg.GetOptionValue("port") == 123
        assert cfg.GetOptionValue("listen_addresses") == "*"

        # exact check
        fileDataLines = file.m_FileData.m_Lines
        assert len(fileDataLines) == 5
        assert len(fileDataLines[0].m_Items) == 1
        assert len(fileDataLines[1].m_Items) == 2
        assert len(fileDataLines[2].m_Items) == 0
        assert len(fileDataLines[3].m_Items) == 2
        assert len(fileDataLines[4].m_Items) == 0

        # LINE 0
        assert type(fileDataLines[0].m_Items[0].m_Element) is PgCfgModel__CommentData
        assert (
            fileDataLines[0].m_Items[0].m_Element.m_Text
            == "It is a test configuration file"
        )
        assert fileDataLines[0].m_Items[0].m_Element.m_Offset == 0

        # LINE 1
        assert type(fileDataLines[1].m_Items[0].m_Element) is PgCfgModel__OptionData
        assert fileDataLines[1].m_Items[0].m_Element.m_Name == "port"
        assert fileDataLines[1].m_Items[0].m_Element.m_Value == 123
        assert fileDataLines[1].m_Items[0].m_Element.m_Offset == 0

        assert type(fileDataLines[1].m_Items[1].m_Element) is PgCfgModel__CommentData
        assert fileDataLines[1].m_Items[1].m_Element.m_Text == "It is a port"
        assert fileDataLines[1].m_Items[1].m_Element.m_Offset == 9

        # LINE 3
        assert type(fileDataLines[3].m_Items[0].m_Element) is PgCfgModel__OptionData
        assert fileDataLines[3].m_Items[0].m_Element.m_Name == "listen_addresses"
        assert fileDataLines[3].m_Items[0].m_Element.m_Value == "*"
        assert fileDataLines[3].m_Items[0].m_Element.m_Offset == 0

        assert type(fileDataLines[3].m_Items[1].m_Element) is PgCfgModel__CommentData
        assert fileDataLines[3].m_Items[1].m_Element.m_Text == "addresses"
        assert fileDataLines[3].m_Items[1].m_Element.m_Offset == 21
        return

    # --------------------------------------------------------------------
    def test_002__two_files(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_FILE_NAME1 = PgCfg_Std.C_POSTGRESQL_CONF
        C_FILE_NAME2 = "postgresql.biha.conf"

        # ---------------
        filePath1 = os.path.join(rootTmpDir, C_FILE_NAME1)

        logging.info("File {0} is creating...".format(filePath1))

        with open(filePath1, "x") as f:
            # fmt: off
            f.write("include 'postgresql.biha.conf'\n")
            f.flush()
            # fmt: on

            fd = f.fileno()
            assert type(fd) is int
            lastMDate1 = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate1) is datetime.datetime
            f.close()

        # ---------------
        filePath2 = os.path.join(rootTmpDir, C_FILE_NAME2)

        logging.info("File {0} is creating...".format(filePath2))

        with open(filePath2, "x") as f:
            # fmt: off
            f.write("port 123\n")
            f.flush()
            # fmt: on

            fd = f.fileno()
            assert type(fd) is int
            lastMDate2 = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate2) is datetime.datetime
            f.close()

        # ---------------
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        # ---------------
        logging.info("File {0} is loading...".format(C_FILE_NAME1))

        load_r1 = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_FILE_NAME1)
        assert isinstance(load_r1, PgCfg_File)

        load_r2 = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_FILE_NAME2)
        assert isinstance(load_r2, PgCfg_File)

        assert len(cfg.get_AllFiles()) == 2

        assert (cfg.GetOptionValue("port")) == 123

        file1 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME1)
        file2 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME2)

        assert file1.m_FileData is load_r1.m_FileData
        assert file2.m_FileData is load_r2.m_FileData

        assert file1.GetOptionValue("port") == 123
        assert file2.GetOptionValue("port") == 123
        return

    # --------------------------------------------------------------------
    def test_003__two_files__duplication_and_cycles(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_FILE_NAME1 = PgCfg_Std.C_POSTGRESQL_CONF
        C_FILE_NAME2 = "postgresql.biha.conf"

        # ---------------
        filePath1 = os.path.join(rootTmpDir, C_FILE_NAME1)

        logging.info("File {0} is creating...".format(filePath1))

        with open(filePath1, "x") as f:
            # fmt: off
            f.write("include '{0}'\n".format(C_FILE_NAME2))
            f.write("include '{0}'\n".format(C_FILE_NAME2))
            f.flush()
            # fmt: on

            fd = f.fileno()
            assert type(fd) is int
            lastMDate1 = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate1) is datetime.datetime
            f.close()

        # ---------------
        filePath2 = os.path.join(rootTmpDir, C_FILE_NAME2)

        logging.info("File {0} is creating...".format(filePath2))

        with open(filePath2, "x") as f:
            # fmt: off
            f.write("include '{0}'\n".format(C_FILE_NAME1))
            f.write("include '{0}'\n".format(C_FILE_NAME2))
            f.write("port 123\n")
            f.flush()
            # fmt: on

            fd = f.fileno()
            assert type(fd) is int
            lastMDate2 = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate2) is datetime.datetime
            f.close()

        # ---------------
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        # ---------------
        logging.info("File {0} is loading...".format(C_FILE_NAME1))

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 2

        assert (cfg.GetOptionValue("port")) == 123

        file1 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME1)
        file2 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME2)

        assert file1.GetOptionValue("port") == 123
        assert file2.GetOptionValue("port") == 123
        return

    # --------------------------------------------------------------------
    def test_004__realistic_config_overrides__Standard(
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

        # 1. Create main postgresql.conf
        # Contains base settings, an inline duplicate, and includes for extensions.
        pgConfPath = os.path.join(rootTmpDir, C_PG_CONF)
        logging.info("Creating {0}...".format(pgConfPath))

        with open(pgConfPath, "x") as f:
            # fmt: off
            f.write("# Base PostgreSQL configuration\n")
            f.write("listen_addresses = 'localhost'\n")
            f.write("port = 5432\n")
            f.write("max_connections = 100\n")
            f.write("shared_buffers = '128MB'\n")
            f.write("shared_preload_libraries = 'pg_stat_statements'\n")
            f.write("\n")
            f.write("# Inline override within the same file\n")
            f.write("max_connections = 200\n")
            f.write("\n")
            f.write("# Include extension configurations in specific order\n")
            f.write("include '{0}'\n".format(C_BIHA_CONF))
            f.write("include '{0}'\n".format(C_PROXIMA_CONF))
            f.write("\n")
            f.write("# Final override at the tail of main config\n")
            f.write("listen_addresses = '*'\n")
            f.flush()
            # fmt: on
            f.close()

        # 2. Create postgresql.biha.conf
        # Overrides shared_preload_libraries and sets BiHA-specific options.
        bihaConfPath = os.path.join(rootTmpDir, C_BIHA_CONF)
        logging.info("Creating {0}...".format(bihaConfPath))

        with open(bihaConfPath, "x") as f:
            # fmt: off
            f.write("# BiHA extension configuration\n")
            f.write("shared_preload_libraries = 'pg_stat_statements, biha'\n")
            f.write("wal_level = 'logical'\n")
            f.write("biha.node_id = 1\n")
            f.flush()
            # fmt: on
            f.close()

        # 3. Create postgresql.proxima.conf
        # Included after BiHA; overrides shared_preload_libraries again and tunes memory.
        proximaConfPath = os.path.join(rootTmpDir, C_PROXIMA_CONF)
        logging.info("Creating {0}...".format(proximaConfPath))

        with open(proximaConfPath, "x") as f:
            # fmt: off
            f.write("# Proxima extension configuration\n")
            f.write("shared_preload_libraries = 'pg_stat_statements, biha, proxima'\n")
            f.write("shared_buffers = '1GB'\n")
            f.write("proxima.pool_size = 64\n")
            f.flush()
            # fmt: on
            f.close()

        # 4. Create postgresql.auto.conf (simulating ALTER SYSTEM overrides)
        # Takes highest precedence over postgresql.conf and all its includes.
        autoConfPath = os.path.join(rootTmpDir, C_AUTO_CONF)
        logging.info("Creating {0}...".format(autoConfPath))

        with open(autoConfPath, "x") as f:
            # fmt: off
            f.write("# Do not edit this file manually!\n")
            f.write("# It will be overwritten by the ALTER SYSTEM command.\n")
            f.write("max_connections = 500\n")
            f.write("port = 5433\n")
            f.flush()
            # fmt: on
            f.close()

        # ---------------
        # Initialize configuration manager in Standard mode (duplicates allowed)
        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=PgCfg_Std.Strategy.Standard,
        )

        # ---------------
        # Load top-level configuration files
        logging.info("Loading configuration files...")

        pgFile = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_PG_CONF)
        autoFile = PgCfg_Reader_Base.LoadConfigurationFile(cfg, C_AUTO_CONF)

        assert len(cfg.get_AllFiles()) == 4

        bihaFile = cfg.get_AllFiles().GetFileByName(C_BIHA_CONF)
        proximaFile = cfg.get_AllFiles().GetFileByName(C_PROXIMA_CONF)

        # ---------------
        # Verify effective global configuration values (last definition wins)

        # Overridden in postgresql.auto.conf
        assert cfg.GetOptionValue("port") == 5433
        assert cfg.GetOptionValue("max_connections") == 500

        # Overridden at the tail of postgresql.conf (after includes)
        assert cfg.GetOptionValue("listen_addresses") == "*"

        # Overridden in postgresql.proxima.conf (the last include defining these)
        assert cfg.GetOptionValue("shared_buffers") == "1GB"
        assert cfg.GetOptionValue("shared_preload_libraries") == [
            "pg_stat_statements",
            "biha",
            "proxima",
        ]

        # Defined only in specific extension files
        assert cfg.GetOptionValue("wal_level") == "logical"
        assert cfg.GetOptionValue("biha.node_id") == 1
        assert cfg.GetOptionValue("proxima.pool_size") == 64

        # ---------------
        # Verify file-scoped effective values (subtree lookup)

        # In context of postgresql.conf (ignoring postgresql.auto.conf):
        # max_connections is 200 (inline override), port is 5432
        assert pgFile.GetOptionValue("max_connections") == 200
        assert pgFile.GetOptionValue("port") == 5432
        assert pgFile.GetOptionValue("shared_preload_libraries") == [
            "pg_stat_statements",
            "biha",
            "proxima",
        ]

        # In context of postgresql.biha.conf (ignoring proxima.conf):
        assert bihaFile.GetOptionValue("shared_preload_libraries") == [
            "pg_stat_statements",
            "biha",
        ]
        assert bihaFile.GetOptionValue("proxima.pool_size") is None

        # In context of postgresql.proxima.conf:
        assert proximaFile.GetOptionValue("shared_preload_libraries") == [
            "pg_stat_statements",
            "biha",
            "proxima",
        ]
        assert proximaFile.GetOptionValue("biha.node_id") is None

        # In context of postgresql.auto.conf:
        assert autoFile.GetOptionValue("port") == 5433
        assert autoFile.GetOptionValue("max_connections") == 500
        assert autoFile.GetOptionValue("shared_buffers") is None

        # ---------------
        # Verify total count of all option instances (including duplicates)
        # postgresql.conf: 6 options (listen_addresses x2, port, max_connections x2, shared_buffers, shared_preload_libraries -> 7 total)
        # biha.conf: 3 options
        # proxima.conf: 3 options
        # auto.conf: 2 options
        # Total = 15 option instances across 4 files
        allOptions = list(cfg.get_AllOptions())
        assert len(allOptions) == 15
        assert len(cfg.get_AllOptions()) == 15

        return


# //////////////////////////////////////////////////////////////////////////////
