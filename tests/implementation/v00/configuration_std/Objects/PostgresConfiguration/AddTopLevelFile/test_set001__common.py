# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
# fmt: on

from .......TestServices import TestServices

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        C_FILE_NAME = "postgresql.auto.conf"

        file1 = cfg.AddTopLevelFile(C_FILE_NAME)
        assert file1 is not None
        assert type(file1) == PgCfg_TopLevelFile_Base  # noqa: E721

        assert len(cfg.get_AllFiles()) == 1
        assert (
            cfg.get_AllFiles().__iter__().__next__().Private__GetFileData()
            is file1.m_FileData
        )

        assert (
            cfg.get_AllFiles().GetFileByName(C_FILE_NAME).Private__GetFileData()
            == file1.m_FileData
        )

        assert len(file1.get_Lines()) == 0

        cfg.SetOptionValue("port", 123)

        assert len(file1.get_Lines()) == 1

        cfg.SetOptionValue("port", None)

        assert len(file1.get_Lines()) == 0


# //////////////////////////////////////////////////////////////////////////////
