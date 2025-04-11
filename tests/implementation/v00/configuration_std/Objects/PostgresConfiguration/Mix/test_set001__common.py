# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ........src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from ........src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from ........src.implementation.v00.configuration_base import PostgresConfigurationOption as PgCfg_Option
from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult as PgCfg_SetOptionResult

from ........src.implementation.v00.configuration_base import PgCfgModel__ConfigurationData

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
