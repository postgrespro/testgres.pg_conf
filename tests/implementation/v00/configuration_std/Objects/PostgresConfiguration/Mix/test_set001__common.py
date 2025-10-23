# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PgCfgModel__ConfigurationData

from .......TestServices import TestServices
# fmt: on

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__get_Configuration(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        assert cfg.get_Configuration() is cfg

    # --------------------------------------------------------------------
    def test_002__get_Parent(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        assert cfg.get_Parent() is None


# //////////////////////////////////////////////////////////////////////////////
