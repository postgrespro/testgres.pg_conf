# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ........src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ........src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationWriter_Base as PgCfg_Writer_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationWriterCtx_Base as PgCfg_WriterCtx_Base

from ........src.implementation.v00.configuration_base import PostgresConfigurationFile as PgCfg_File

from ........src.implementation.v00.configuration_base import PgCfgModel__FileData
from ........src.implementation.v00.configuration_base import PgCfgModel__FileStatus

from .......TestServices import TestServices
# fmt: on

import pytest
import logging
import os
import datetime
import re
import time

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_000__empty(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        logging.info("File object is building...")

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) == PgCfgModel__FileData

        assert file.m_FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
        assert file.m_FileData.m_LastModifiedTimestamp is None

        # ---------------
        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        nPass = 0
        while nPass < 3:
            nPass += 1

            logging.info("File object is being written [pass: {0}]...".format(nPass))

            PgCfg_Writer_Base.DoWork(cfgWriterCtx)

            # ---------------
            logging.info("File object is being checked...")

            assert file.m_FileData.m_Status == PgCfgModel__FileStatus.EXISTS
            assert file.m_FileData.m_LastModifiedTimestamp is not None

            assert os.path.exists(file.get_Path())

            curMDate = datetime.datetime.fromtimestamp(
                os.path.getmtime(file.get_Path())
            )
            assert curMDate == file.m_FileData.m_LastModifiedTimestamp

            with open(file.get_Path(), "r") as f:
                fileContent = f.read()
                assert fileContent is not None
                assert type(fileContent) == str

                fileContent_n = __class__.Helper__norm_content(fileContent)

                assert fileContent_n == ""

    # --------------------------------------------------------------------
    def test_001(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        logging.info("File object is building...")

        portNumber = 234

        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue("port", portNumber)

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_AUTO_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) == PgCfgModel__FileData

        assert file.m_FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
        assert file.m_FileData.m_LastModifiedTimestamp is None

        # ---------------
        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        nPass = 0
        while nPass < 3:
            nPass += 1

            logging.info("------------------- Pass: {0}".format(nPass))

            # ---------------
            if nPass == 1:
                logging.info("Port number is {0}".format(portNumber))
            else:
                portNumber += 1
                logging.info("Port is changed with number {0}".format(portNumber))
                file.SetOptionValue("port", portNumber)

            # ---------------
            logging.info("File object is being written [pass: {0}]...".format(nPass))

            PgCfg_Writer_Base.DoWork(cfgWriterCtx)

            # ---------------
            logging.info("File object is being checked...")

            assert file.m_FileData.m_Status == PgCfgModel__FileStatus.EXISTS
            assert file.m_FileData.m_LastModifiedTimestamp is not None

            assert os.path.exists(file.get_Path())

            curMDate = datetime.datetime.fromtimestamp(
                os.path.getmtime(file.get_Path())
            )
            assert curMDate == file.m_FileData.m_LastModifiedTimestamp

            with open(file.get_Path(), "r") as f:
                fileContent = f.read()
                assert fileContent is not None
                assert type(fileContent) == str

                fileContent_n = __class__.Helper__norm_content(fileContent)

                assert fileContent_n == "port = {0}\n".format(portNumber)

    # --------------------------------------------------------------------
    def test_003__two_files(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_FILE1_NAME = PgCfg_Std.C_POSTGRESQL_CONF
        C_FILE2_NAME = "postgresql.proxima.conf"

        C_OPT_NAME = "proxima.port"

        # ---------------
        logging.info("File object is building...")

        cfg = PgCfg_Std(rootTmpDir)

        file1 = cfg.AddTopLevelFile(C_FILE1_NAME)

        file2 = file1.AddInclude(C_FILE2_NAME).get_File()

        portNumber = 321

        cfg.AddOption(C_OPT_NAME, portNumber)

        assert file2.GetOptionValue(C_OPT_NAME) == portNumber

        assert file2.AddComment(" IT IS ALL!")

        # ---------------
        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        nPass = 0
        while nPass < 3:
            nPass += 1

            logging.info("------------------- Pass: {0}".format(nPass))

            # ---------------
            if nPass == 1:
                logging.info("Port number is {0}".format(portNumber))
            else:
                portNumber += 1
                logging.info("Port is changed with number {0}".format(portNumber))
                cfg.SetOptionValue(C_OPT_NAME, portNumber)
                assert file2.GetOptionValue(C_OPT_NAME) == portNumber

            # ---------------
            logging.info("File object is being written [pass: {0}]...".format(nPass))

            PgCfg_Writer_Base.DoWork(cfgWriterCtx)

            # ---------------
            logging.info("File objects are being checked...")

            fileDatas = [
                (file1, "include 'postgresql.proxima.conf'\n"),
                (file2, "{0} = {1}\n# IT IS ALL!\n".format(C_OPT_NAME, portNumber)),
            ]

            for fileData in fileDatas:
                file: PgCfg_File_Base = fileData[0]

                assert isinstance(file, PgCfg_File_Base)

                assert file.m_FileData.m_Status == PgCfgModel__FileStatus.EXISTS
                assert file.m_FileData.m_LastModifiedTimestamp is not None

                assert os.path.exists(file.get_Path())

                curMDate = datetime.datetime.fromtimestamp(
                    os.path.getmtime(file.get_Path())
                )
                assert curMDate == file.m_FileData.m_LastModifiedTimestamp

                with open(file.get_Path(), "r") as f:
                    fileContent = f.read()
                    assert fileContent is not None
                    assert type(fileContent) == str

                    fileContent_n = __class__.Helper__norm_content(fileContent)

                    assert fileContent_n == fileData[1]

    # --------------------------------------------------------------------
    def test_004__check_truncate(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue("port", 123)
        cfg.SetOptionValue("listen_addresses", "*")

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_AUTO_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) == PgCfgModel__FileData

        # ---------------
        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        PgCfg_Writer_Base.DoWork(cfgWriterCtx)

        with open(file.get_Path(), "r") as f:
            fileContent = f.read()
            assert fileContent is not None
            assert type(fileContent) == str
            fileContent_n = __class__.Helper__norm_content(fileContent)
            assert fileContent_n == "port = 123\nlisten_addresses = '*'\n"

        # ---------------
        cfg.SetOptionValue("port", None)

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_AUTO_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) == PgCfgModel__FileData

        # ---------------
        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        PgCfg_Writer_Base.DoWork(cfgWriterCtx)

        with open(file.get_Path(), "r") as f:
            fileContent = f.read()
            assert fileContent is not None
            assert type(fileContent) == str
            fileContent_n = __class__.Helper__norm_content(fileContent)
            assert fileContent_n == "listen_addresses = '*'\n"

    # --------------------------------------------------------------------
    def test_E01__file_is_exist(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        C_FILE1_NAME = PgCfg_Std.C_POSTGRESQL_CONF
        C_FILE2_NAME = "postgresql.proxima.conf"

        C_OPT_NAME = "proxima.port"

        # ---------------
        logging.info("File object is building...")

        cfg = PgCfg_Std(rootTmpDir)

        file1 = cfg.AddTopLevelFile(C_FILE1_NAME)

        file2 = file1.AddInclude(C_FILE2_NAME).get_File()

        cfg.AddOption(C_OPT_NAME, 123)

        # ---------------
        files: list[PgCfg_File_Base] = [file1, file2]

        for file in files:
            logging.info("Let's create our own [{0}]".format(file.get_Path()))

            with open(file.get_Path(), "x") as f:
                f.write(file.get_Path())
                f.close()

            cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

            # ---------------
            logging.info("Let's try to write our configuration!")

            while True:
                try:
                    PgCfg_Writer_Base.DoWork(cfgWriterCtx)
                except Exception as e:
                    logging.info(
                        "OK. We catch an exception ({0}): {1}".format(
                            type(e).__name__, e
                        )
                    )

                    errMsg = "File exists: '{0}'".format(file.get_Path())
                    assert errMsg in str(e)
                    break

                TestServices.ThrowWeWaitAnException()

            for fileX in files:
                assert fileX.m_FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
                assert fileX.m_FileData.m_LastModifiedTimestamp is None

            os.remove(file.get_Path())

    # --------------------------------------------------------------------
    def test_E02__external_modification(self, request: pytest.FixtureRequest):
        rootTmpDir = TestServices.GetCurTestTmpDir(request)

        os.makedirs(rootTmpDir, exist_ok=True)

        # ---------------
        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue("port", 123)
        cfg.SetOptionValue("listen_addresses", "*")

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_AUTO_CONF)
        assert type(file) == PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert type(file.m_FileData) == PgCfgModel__FileData

        # ---------------
        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        PgCfg_Writer_Base.DoWork(cfgWriterCtx)

        with open(file.get_Path(), "r") as f:
            fileContent = f.read()
            assert fileContent is not None
            assert type(fileContent) == str
            fileContent_n = __class__.Helper__norm_content(fileContent)
            assert fileContent_n == "port = 123\nlisten_addresses = '*'\n"

        mdate1 = file.m_FileData.m_LastModifiedTimestamp
        logging.info("Last1 modification date is [{0}]".format(mdate1))

        time.sleep(0.001)

        with open(file.get_Path(), "w") as f:
            f.write("BLA_BLA-BLA")
            f.flush()
            f.close()

        mdate2 = datetime.datetime.fromtimestamp(os.path.getmtime(file.get_Path()))
        logging.info("Last2 modification date is [{0}]".format(mdate2))
        assert mdate1 != mdate2

        cfg.SetOptionValue("port", 321)

        errMsg = "File [{0}] was modified externally. Our timestamp is [{1}]. The current file timestamp is [{2}].".format(
            file.get_Path(), mdate1, mdate2
        )

        with pytest.raises(Exception, match=re.escape(errMsg)):
            PgCfg_Writer_Base.DoWork(cfgWriterCtx)

        logging.info(
            "Last mofication date is [{0}]".format(
                file.m_FileData.m_LastModifiedTimestamp
            )
        )

    # --------------------------------------------------------------------
    def Helper__norm_content(text: str) -> str:
        assert text is not None
        assert type(text) == str

        r = text.replace("\r\n", "\r")

        assert r is not None
        assert type(r) == str
        return r
