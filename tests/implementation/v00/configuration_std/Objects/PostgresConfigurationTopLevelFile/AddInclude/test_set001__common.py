# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationInclude_Base as PgCfg_Include_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.implementation.v00.configuration_base import PostgresConfigurationInclude as PgCfg_Include
from src.implementation.v00.configuration_base import PostgresConfigurationFile as PgCfg_File
# fmt: on

from .......TestServices import TestServices

import pytest
import re
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        C_BIHA_CONF_FILE_NAME = "postgresql.biha.conf"

        bihaConfFileInclude = file1.AddInclude(C_BIHA_CONF_FILE_NAME)

        assert bihaConfFileInclude is not None
        assert isinstance(bihaConfFileInclude, PgCfg_Include_Base)
        assert isinstance(bihaConfFileInclude, PgCfg_Include)

        assert len(file1.get_Lines()) == 1

        bihaConfFile = bihaConfFileInclude.get_File()
        assert bihaConfFile is not None
        assert isinstance(bihaConfFile, PgCfg_File_Base)
        assert isinstance(bihaConfFile, PgCfg_File)

        assert bihaConfFile.get_Path() == os.path.join(
            rootTmpDir, C_BIHA_CONF_FILE_NAME
        )

        assert bihaConfFile.get_Configuration() is cfg
        assert bihaConfFile.get_Parent() is bihaConfFileInclude

        bihaConfFile__Lines = bihaConfFile.get_Lines()

        assert bihaConfFile.get_Lines() is bihaConfFile__Lines  # check a cache
        assert len(bihaConfFile__Lines) == 0

        # --------------
        assert (
            cfg.get_AllFiles().GetFileByName(C_BIHA_CONF_FILE_NAME).m_FileData
            is bihaConfFile.m_FileData
        )

        assert file1.m_FileData in cfg.m_Data.m_Files
        assert not (bihaConfFile.m_FileData in cfg.m_Data.m_Files)

        assert len(cfg.m_Data.m_Files) == 1
        assert cfg.m_Data.m_Files[0] is file1.m_FileData

        assert len(cfg.m_Data.m_AllFilesByName.keys()) == 2

        assert cfg.C_POSTGRESQL_CONF in cfg.m_Data.m_AllFilesByName.keys()
        assert cfg.m_Data.m_AllFilesByName[cfg.C_POSTGRESQL_CONF] is file1.m_FileData

        assert C_BIHA_CONF_FILE_NAME in cfg.m_Data.m_AllFilesByName.keys()
        assert (
            cfg.m_Data.m_AllFilesByName[C_BIHA_CONF_FILE_NAME]
            is bihaConfFile.m_FileData
        )

        # --------------
        bihaConfFileIncludeLine = file1.get_Lines().__iter__().__next__()

        assert (
            bihaConfFileIncludeLine.m_FileLineData
            is bihaConfFileInclude.m_FileLine.m_FileLineData
        )

        bihaConfFileIncludeLine.Clear()

        assert len(bihaConfFileIncludeLine) == 0

        with pytest.raises(Exception, match="Include object was deleted."):
            len(bihaConfFile__Lines)

        with pytest.raises(Exception, match="Include object was deleted."):
            len(bihaConfFile)

        with pytest.raises(Exception, match="Include object was deleted."):
            bihaConfFileInclude.get_Configuration()

        with pytest.raises(Exception, match="Include object was deleted."):
            bihaConfFileInclude.get_File()

    # --------------------------------------------------------------------
    def test_002__include_twice(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        C_BIHA_CONF_FILE_NAME = "postgresql.biha.conf"

        bihaConfFileInclude1 = file1.AddInclude(C_BIHA_CONF_FILE_NAME)
        bihaConfFileInclude2 = file1.AddInclude(C_BIHA_CONF_FILE_NAME)

        assert bihaConfFileInclude1 is not bihaConfFileInclude2
        # They use the one file
        assert (
            bihaConfFileInclude1.get_File().m_FileData
            is bihaConfFileInclude2.get_File().m_FileData
        )

        bihaConfFileInclude1.get_Parent().Clear()

        with pytest.raises(Exception, match="Include object was deleted."):
            bihaConfFileInclude1.get_File()

        bihaConfFile2 = bihaConfFileInclude2.get_File()

        assert bihaConfFile2.get_Parent() is bihaConfFileInclude2
        assert bihaConfFile2.get_Path() == os.path.join(
            rootTmpDir, C_BIHA_CONF_FILE_NAME
        )

    # --------------------------------------------------------------------
    def test_003__empty_file_path(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        with pytest.raises(Exception, match=re.escape("File path is empty.")):
            file1.AddInclude("")


# //////////////////////////////////////////////////////////////////////////////
