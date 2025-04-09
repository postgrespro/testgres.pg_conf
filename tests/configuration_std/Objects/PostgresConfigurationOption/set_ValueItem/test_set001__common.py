# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ......src.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ......src.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ......src.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from ......src.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ......src.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from ......src.configuration_base import PgCfgModel__ConfigurationData

from .....TestServices import TestServices
# fmt: on

import pytest
import re
import logging

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")
        assert type(r1) == PgCfg_SetOptionResult_Base
        assert r1.Option.get_Name() == C_OPT_NAME
        assert r1.Option.get_Value() == ["biha"]
        assert type(r1.Option.get_Parent()) == PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) == PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        assert r1.Option.get_Value() == ["biha"]

        for nPass in range(3):
            logging.info("------------------ pass: {0}".format(nPass))

            r2 = r1.Option.set_ValueItem("proxima")

            assert r2 is not None
            assert type(r2) == PgCfg_SetOptionResult_Base

            if nPass == 0:
                assert r2.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
            else:
                assert (
                    r2.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ALREADY_DEFINED
                )

            assert r2.m_OptData is not None
            assert r2.m_OptData is r1.m_OptData
            assert r2.m_OptData.m_Value is not None
            assert type(r2.m_OptData.m_Value) == list
            assert len(r2.m_OptData.m_Value) == 2
            assert r2.m_OptData.m_Value[0] == "biha"
            assert r2.m_OptData.m_Value[1] == "proxima"
            assert r2.m_OptData.m_Value == ["biha", "proxima"]
            assert r2.Option.get_Value() == ["biha", "proxima"]

    # --------------------------------------------------------------------
    def test_002__set_None(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")
        assert type(r1) == PgCfg_SetOptionResult_Base
        assert r1.Option.get_Name() == C_OPT_NAME
        assert r1.Option.get_Value() == ["biha"]
        assert type(r1.Option.get_Parent()) == PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) == PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        with pytest.raises(Exception, match=re.escape("None value is not supported.")):
            r1.Option.set_ValueItem(None)

        assert r1.Option.get_Value() == ["biha"]

    # --------------------------------------------------------------------
    def test_003__set_value_item_with_bad_type(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")
        assert type(r1) == PgCfg_SetOptionResult_Base
        assert r1.Option.get_Name() == C_OPT_NAME
        assert r1.Option.get_Value() == ["biha"]
        assert type(r1.Option.get_Parent()) == PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) == PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        errMsg = (
            "Bad option [{0}] value item type [{1}]. Expected type is [{2}].".format(
                C_OPT_NAME, "int", "str"
            )
        )
        with pytest.raises(Exception, match=re.escape(errMsg)):
            r1.Option.set_ValueItem(1)

        assert r1.Option.get_Value() == ["biha"]


# //////////////////////////////////////////////////////////////////////////////
