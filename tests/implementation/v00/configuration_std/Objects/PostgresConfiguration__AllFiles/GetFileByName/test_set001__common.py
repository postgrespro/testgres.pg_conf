# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert type(file1) is PgCfg_TopLevelFile_Base

        assert (
            cfg.get_AllFiles()
            .GetFileByName(cfg.C_POSTGRESQL_CONF)
            .Private__GetFileData()
            == file1.m_FileData
        )
        return

    # --------------------------------------------------------------------
    def test_002__unk_file_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        C_FILE_NAME = "a.conf"

        with pytest.raises(PostgresConfigException) as x:
            cfg.get_AllFiles().GetFileByName(C_FILE_NAME)

        assert str(x.value) == ErrorMessageBuilder.UnknownFileName(
            C_FILE_NAME,
        )
        return


# //////////////////////////////////////////////////////////////////////////////
