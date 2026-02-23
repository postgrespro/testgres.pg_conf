# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationReader_Base as PgCfg_Reader_Base

from src.implementation.v00.configuration_base import PostgresConfigurationFile as PgCfg_File

from src.implementation.v00.configuration_base import PgCfgModel__CommentData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__FileStatus

from .......TestServices import TestServices
# fmt: on

import pytest
import logging
import os
import datetime

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_000__empty(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        logging.info("File object is creating...")

        filePath = os.path.join(rootTmpDir, PgCfg_Std.C_POSTGRESQL_CONF)

        with open(filePath, "x") as f:
            fd = f.fileno()
            assert type(fd) is int
            lastMDate = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
            assert type(lastMDate) == datetime.datetime  # noqa: E721
            f.close()

        # ---------------
        cfg = PgCfg_Std(rootTmpDir)

        # ---------------
        logging.info("File object is loading...")

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base  # noqa: E721
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) is PgCfgModel__FileData
        assert file.m_FileData.m_Status == PgCfgModel__FileStatus.EXISTS
        assert file.m_FileData.m_LastModifiedTimestamp == lastMDate
        assert len(file.m_FileData.m_Lines) == 0

    # --------------------------------------------------------------------
    def test_001__comment_and_options(self, request: pytest.FixtureRequest):
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
            assert type(lastMDate) == datetime.datetime  # noqa: E721
            f.close()

        # ---------------
        cfg = PgCfg_Std(rootTmpDir)

        # ---------------
        logging.info("File object is loading...")

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base  # noqa: E721
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
        assert (  # noqa: E721
            type(fileDataLines[0].m_Items[0].m_Element) == PgCfgModel__CommentData
        )
        assert (
            fileDataLines[0].m_Items[0].m_Element.m_Text
            == "It is a test configuration file"
        )
        assert fileDataLines[0].m_Items[0].m_Element.m_Offset == 0

        # LINE 1
        assert (  # noqa: E721
            type(fileDataLines[1].m_Items[0].m_Element) == PgCfgModel__OptionData
        )
        assert fileDataLines[1].m_Items[0].m_Element.m_Name == "port"
        assert fileDataLines[1].m_Items[0].m_Element.m_Value == 123
        assert fileDataLines[1].m_Items[0].m_Element.m_Offset == 0

        assert (  # noqa: E721
            type(fileDataLines[1].m_Items[1].m_Element) == PgCfgModel__CommentData
        )
        assert fileDataLines[1].m_Items[1].m_Element.m_Text == "It is a port"
        assert fileDataLines[1].m_Items[1].m_Element.m_Offset == 9

        # LINE 3
        assert (  # noqa: E721
            type(fileDataLines[3].m_Items[0].m_Element) == PgCfgModel__OptionData
        )
        assert fileDataLines[3].m_Items[0].m_Element.m_Name == "listen_addresses"
        assert fileDataLines[3].m_Items[0].m_Element.m_Value == "*"
        assert fileDataLines[3].m_Items[0].m_Element.m_Offset == 0

        assert (  # noqa: E721
            type(fileDataLines[3].m_Items[1].m_Element) == PgCfgModel__CommentData
        )
        assert fileDataLines[3].m_Items[1].m_Element.m_Text == "addresses"
        assert fileDataLines[3].m_Items[1].m_Element.m_Offset == 21

    # --------------------------------------------------------------------
    def test_002__two_files(self, request: pytest.FixtureRequest):
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
            assert type(lastMDate1) == datetime.datetime  # noqa: E721
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
            assert type(lastMDate2) == datetime.datetime  # noqa: E721
            f.close()

        # ---------------
        cfg = PgCfg_Std(rootTmpDir)

        # ---------------
        logging.info("File {0} is loading...".format(C_FILE_NAME1))

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 2

        assert (cfg.GetOptionValue("port")) == 123

        file1 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME1)
        file2 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME2)

        assert file1.GetOptionValue("port") is None
        assert file2.GetOptionValue("port") == 123

    # --------------------------------------------------------------------
    def test_003__two_files__duplication_and_cycles(
        self, request: pytest.FixtureRequest
    ):
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
            assert type(lastMDate1) == datetime.datetime  # noqa: E721
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
            assert type(lastMDate2) == datetime.datetime  # noqa: E721
            f.close()

        # ---------------
        cfg = PgCfg_Std(rootTmpDir)

        # ---------------
        logging.info("File {0} is loading...".format(C_FILE_NAME1))

        PgCfg_Reader_Base.LoadConfigurationFile(cfg, cfg.C_POSTGRESQL_CONF)

        assert len(cfg.get_AllFiles()) == 2

        assert (cfg.GetOptionValue("port")) == 123

        file1 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME1)
        file2 = cfg.get_AllFiles().GetFileByName(C_FILE_NAME2)

        assert file1.GetOptionValue("port") is None
        assert file2.GetOptionValue("port") == 123


# //////////////////////////////////////////////////////////////////////////////
