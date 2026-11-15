# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationIncludeIfExists_Base as PgCfg_IncludeIfExists_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.implementation.v00.configuration_base import PostgresConfigurationIncludeIfExists as PgCfg_IncludeIfExists
from src.implementation.v00.configuration_base import PostgresConfigurationFile as PgCfg_File
from src.implementation.v00.configuration_base import AddIncludeIfExistsRule as PgCfg_AddIncludeIfExistsRule

from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__with_file(
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

        file1 = cfg.AddTopLevelFile(
            cfg.C_POSTGRESQL_CONF,
        )
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        C_BIHA_CONF_FILE_NAME = "postgresql.biha.conf"

        bihaConfFileInclude = file1.AddIncludeIfExists(
            C_BIHA_CONF_FILE_NAME,
            PgCfg_AddIncludeIfExistsRule.with_file,
        )

        assert bihaConfFileInclude is not None
        assert isinstance(bihaConfFileInclude, PgCfg_IncludeIfExists_Base)
        assert isinstance(bihaConfFileInclude, PgCfg_IncludeIfExists)

        assert len(file1.get_Lines()) == 1

        bihaConfFile = bihaConfFileInclude.get_File()
        assert bihaConfFile is not None
        assert isinstance(bihaConfFile, PgCfg_File_Base)
        assert isinstance(bihaConfFile, PgCfg_File)

        assert bihaConfFile.get_Path() == os.path.join(
            rootTmpDir,
            C_BIHA_CONF_FILE_NAME,
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

        assert file1.m_FileData in cfg.m_Data.m_TopLevelFiles
        assert bihaConfFile.m_FileData not in cfg.m_Data.m_TopLevelFiles

        assert len(cfg.m_Data.m_TopLevelFiles) == 1
        assert cfg.m_Data.m_TopLevelFiles[0] is file1.m_FileData

        assert len(list(cfg.m_Data.m_AllFilesByName.keys())) == 2

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

        with pytest.raises(PostgresConfigException) as x:
            len(bihaConfFile__Lines)

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            len(bihaConfFile)

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            bihaConfFileInclude.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            bihaConfFileInclude.get_File()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_002__without_file(
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

        file1 = cfg.AddTopLevelFile(
            cfg.C_POSTGRESQL_CONF,
        )
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        C_BIHA_CONF_FILE_NAME = "postgresql.biha.conf"

        bihaConfFileInclude = file1.AddIncludeIfExists(
            C_BIHA_CONF_FILE_NAME,
            PgCfg_AddIncludeIfExistsRule.without_file,
        )

        assert bihaConfFileInclude is not None
        assert isinstance(bihaConfFileInclude, PgCfg_IncludeIfExists_Base)
        assert isinstance(bihaConfFileInclude, PgCfg_IncludeIfExists)

        assert len(file1.get_Lines()) == 1

        bihaConfFile = bihaConfFileInclude.get_File()
        assert bihaConfFile is None

        # --------------
        bihaConfFileIncludeLine = file1.get_Lines().__iter__().__next__()

        assert (
            bihaConfFileIncludeLine.m_FileLineData
            is bihaConfFileInclude.m_FileLine.m_FileLineData
        )

        bihaConfFileIncludeLine.Clear()

        assert len(bihaConfFileIncludeLine) == 0

        with pytest.raises(PostgresConfigException) as x:
            bihaConfFileInclude.get_File()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_003__include_twice(
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

        bihaConfFile1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert bihaConfFile1 is not None
        assert type(bihaConfFile1) is PgCfg_TopLevelFile_Base

        C_BIHA_CONF_FILE_NAME = "postgresql.biha.conf"

        bihaConfFileInclude1 = bihaConfFile1.AddIncludeIfExists(
            C_BIHA_CONF_FILE_NAME,
            PgCfg_AddIncludeIfExistsRule.with_file,
        )
        bihaConfFileInclude2 = bihaConfFile1.AddIncludeIfExists(
            C_BIHA_CONF_FILE_NAME,
            PgCfg_AddIncludeIfExistsRule.with_file,
        )

        assert bihaConfFileInclude1 is not bihaConfFileInclude2
        # They use the one file
        bihaConfFile1 = bihaConfFileInclude1.get_File()
        bihaConfFile2 = bihaConfFileInclude2.get_File()
        assert bihaConfFile1 is not None
        assert bihaConfFile1.m_FileData is not None
        assert bihaConfFile2 is not None
        assert bihaConfFile2.m_FileData is not None
        assert bihaConfFile1.m_FileData is bihaConfFile2.m_FileData

        bihaConfFileInclude1.get_Parent().Clear()

        with pytest.raises(PostgresConfigException) as x:
            bihaConfFileInclude1.get_File()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        assert bihaConfFile2.get_Parent() is bihaConfFileInclude2
        assert bihaConfFile2.get_Path() == os.path.join(
            rootTmpDir,
            C_BIHA_CONF_FILE_NAME,
        )
        return

    # --------------------------------------------------------------------
    def test_004__empty_file_path(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        with pytest.raises(PostgresConfigException) as x:
            file1.AddIncludeIfExists(
                "",
                fx_add_include_if_exists_rule,
            )

        assert str(x.value) == ErrorMessageBuilder.FilePathIsEmpty()
        return


# //////////////////////////////////////////////////////////////////////////////
