# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ........src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ........src.implementation.v00.configuration_base import PostgresConfiguration_Base as PgCfg_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from ........src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base

from ........src.implementation.v00.configuration_base import PgCfgModel__FileData
from ........src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from ........src.implementation.v00.configuration_base import PgCfgModel__OptionData

from ........src.abstract.v00.configuration import PostgresConfiguration as PgCfg
from ........src.abstract.v00.configuration import PostgresConfigurationFile as PgCfg_File
# fmt: on

from .......TestServices import TestServices

import pytest
import re
import logging

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__set_None(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        with pytest.raises(Exception, match=re.escape("None value is not supported.")):
            file.SetOptionValueItem(C_OPT_NAME, None)

    # --------------------------------------------------------------------
    def test_002__set_value_item_with_bad_type(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        errMsg = (
            "Bad option [{0}] value item type [{1}]. Expected type is [{2}].".format(
                C_OPT_NAME, "int", "str"
            )
        )
        with pytest.raises(Exception, match=re.escape(errMsg)):
            file.SetOptionValueItem(C_OPT_NAME, 123)

    # --------------------------------------------------------------------
    def test_003(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        for nPass in range(3):
            logging.info("------------- pass: {0}".format(nPass))

            r1 = file.SetOptionValueItem(C_OPT_NAME, "biha")
            assert r1 is not None
            assert type(r1) == PgCfg_SetOptionResult_Base

            if nPass == 0:
                assert r1.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
            else:
                assert (
                    r1.m_EventID
                    == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ALREADY_DEFINED
                )

            assert r1.m_OptData is not None
            assert type(r1.m_OptData) == PgCfgModel__OptionData
            assert type(r1.m_OptData.m_Name) == str
            assert r1.m_OptData.m_Name == C_OPT_NAME
            assert r1.m_OptData.m_Value is not None
            assert type(r1.m_OptData.m_Value) == list
            assert len(r1.m_OptData.m_Value) == 1
            assert type(r1.m_OptData.m_Value[0]) == str
            assert r1.m_OptData.m_Value[0] == "biha"
            assert r1.m_OptData.m_Value == ["biha"]

            assert r1.Option is r1.m_Opt  # check cache
            assert r1.Option.get_Value() == ["biha"]
            assert r1.Option.get_Name() == C_OPT_NAME

            assert (
                r1.Option.get_Parent().get_Parent().Private__GetFileData()
                is file.m_FileData
            )
            assert r1.Option.get_Configuration() is cfg

            assert len(cfg.m_Data.m_AllOptionsByName) == 1
            assert len(file.m_FileData.m_OptionsByName) == 1

            assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName
            assert C_OPT_NAME in file.m_FileData.m_OptionsByName

    # --------------------------------------------------------------------
    def test_004__already_defined_in_another_file(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None

        file2 = cfg.AddTopLevelFile("b.conf")
        assert file2 is not None

        r1 = file1.SetOptionValueItem(C_OPT_NAME, "biha")
        assert (
            r1.Option.get_Parent().get_Parent().Private__GetFileData()
            is file1.m_FileData
        )
        assert r1.Option.get_Value() == ["biha"]

        errMsg = "Definition of option [{1}] value item [{2}] is found in another file [{0}].".format(
            file1.get_Path(), C_OPT_NAME, "biha"
        )

        with pytest.raises(Exception, match=re.escape(errMsg)):
            file2.SetOptionValueItem(C_OPT_NAME, "biha")

    # --------------------------------------------------------------------
    def test_005__opt_is_defined_in_another_file(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None

        file2 = cfg.AddTopLevelFile("b.conf")
        assert file2 is not None

        r1 = file1.SetOptionValueItem(C_OPT_NAME, "biha")
        assert (
            r1.Option.get_Parent().get_Parent().Private__GetFileData()
            is file1.m_FileData
        )
        assert r1.Option.get_Value() == ["biha"]

        errMsg = "Option [{0}] already exist in another file [{1}].".format(
            C_OPT_NAME, file1.get_Path()
        )

        with pytest.raises(Exception, match=re.escape(errMsg)):
            file2.SetOptionValueItem(C_OPT_NAME, "proxima")

    # --------------------------------------------------------------------
    def test_006__two_items(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        r1 = file.SetOptionValueItem(C_OPT_NAME, "biha")
        assert r1 is not None
        assert type(r1) == PgCfg_SetOptionResult_Base
        assert r1.Option.get_Value() == ["biha"]

        r2 = file.SetOptionValueItem(C_OPT_NAME, "proxima")
        assert r2 is not None
        assert type(r2) == PgCfg_SetOptionResult_Base
        assert r2.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
        assert r2.Option.get_Value() == ["biha", "proxima"]

        assert r1.Option.get_Value() == ["biha", "proxima"]


# //////////////////////////////////////////////////////////////////////////////
