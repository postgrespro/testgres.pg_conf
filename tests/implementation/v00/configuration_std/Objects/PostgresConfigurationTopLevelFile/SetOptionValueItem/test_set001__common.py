# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID

from src.implementation.v00.configuration_base import PgCfgModel__OptionData

from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import logging

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__set_None(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        with pytest.raises(PostgresConfigException) as x:
            file.SetOptionValueItem(C_OPT_NAME, None)

        assert str(x.value) == ErrorMessageBuilder.NoneValueIsNotSupported()
        return

    # --------------------------------------------------------------------
    def test_002__set_value_item_with_bad_type(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        with pytest.raises(PostgresConfigException) as x:
            file.SetOptionValueItem(C_OPT_NAME, 123)

        assert str(x.value) == ErrorMessageBuilder.BadOptionValueItemType(
            C_OPT_NAME,
            int,
            str,
        )
        return

    # --------------------------------------------------------------------
    def test_003(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        for nPass in range(3):
            logging.info("------------- pass: {0}".format(nPass))

            r1 = file.SetOptionValueItem(C_OPT_NAME, "biha")
            assert r1 is not None
            assert type(r1) is PgCfg_SetOptionResult_Base

            if nPass == 0:
                assert r1.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
            else:
                assert (
                    r1.m_EventID
                    == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ALREADY_DEFINED
                )

            assert r1.m_OptData is not None
            assert type(r1.m_OptData) is PgCfgModel__OptionData
            assert type(r1.m_OptData.m_Name) is str
            assert r1.m_OptData.m_Name == C_OPT_NAME
            assert r1.m_OptData.m_Value is not None
            assert type(r1.m_OptData.m_Value) is list
            assert len(r1.m_OptData.m_Value) == 1
            assert type(r1.m_OptData.m_Value[0]) is str
            assert r1.m_OptData.m_Value[0] == "biha"
            assert r1.m_OptData.m_Value == ["biha"]

            assert r1.Option is r1.m_Opt  # check cache
            assert r1.Option is not None
            assert r1.Option.get_Value() == ["biha"]
            assert r1.Option.get_Name() == C_OPT_NAME

            assert (
                r1.Option.get_Parent().get_Parent().Private__GetFileData()
                is file.m_FileData
            )
            assert r1.Option.get_Configuration() is cfg

            assert cfg.m_Data.m_AllOptionsByName.get_elements_count() == 1
            assert file.m_FileData.m_OptionsByName.get_elements_count() == 1

            assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
            assert C_OPT_NAME in file.m_FileData.m_OptionsByName.keys()
            continue
        return

    # --------------------------------------------------------------------
    def test_004__already_defined_in_another_file(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None

        file2 = cfg.AddTopLevelFile("b.conf")
        assert file2 is not None

        r1 = file1.SetOptionValueItem(C_OPT_NAME, "biha")
        assert r1.Option is not None
        assert (
            r1.Option.get_Parent().get_Parent().Private__GetFileData()
            is file1.m_FileData
        )
        assert r1.Option.get_Value() == ["biha"]

        with pytest.raises(PostgresConfigException) as x:
            file2.SetOptionValueItem(C_OPT_NAME, "biha")

        assert str(
            x.value,
        ) == ErrorMessageBuilder.OptionIsAlreadyExistInAnotherFile(
            file1.get_Path(),
            C_OPT_NAME,
        )
        return

    # --------------------------------------------------------------------
    def test_005__opt_is_defined_in_another_file(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file1 = cfg.AddTopLevelFile("a.conf")
        assert file1 is not None

        file2 = cfg.AddTopLevelFile("b.conf")
        assert file2 is not None

        r1 = file1.SetOptionValueItem(C_OPT_NAME, "biha")
        assert r1.Option is not None
        assert (
            r1.Option.get_Parent().get_Parent().Private__GetFileData()
            is file1.m_FileData
        )
        assert r1.Option.get_Value() == ["biha"]

        with pytest.raises(PostgresConfigException) as x:
            file2.SetOptionValueItem(C_OPT_NAME, "proxima")

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInAnotherFile(
            file1.get_Path(),
            C_OPT_NAME,
        )
        return

    # --------------------------------------------------------------------
    def test_006__two_items(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None

        r1 = file.SetOptionValueItem(C_OPT_NAME, "biha")
        assert r1 is not None
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.Option is not None
        assert r1.Option.get_Value() == ["biha"]

        r2 = file.SetOptionValueItem(C_OPT_NAME, "proxima")
        assert r2 is not None
        assert type(r2) is PgCfg_SetOptionResult_Base
        assert r2.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
        assert r2.Option is not None
        assert r2.Option.get_Value() == ["biha", "proxima"]

        assert r1.Option.get_Value() == ["biha", "proxima"]
        return


# //////////////////////////////////////////////////////////////////////////////
