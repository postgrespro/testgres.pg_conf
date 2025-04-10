# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ......src.implementation.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ......src.implementation.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ......src.implementation.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from ......src.implementation.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
# fmt: on

from .....TestServices import TestServices

import pytest
import logging
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        for nPass in range(3):
            logging.info("--------- pass: {0}".format(nPass))

            r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")

            assert r1 is not None
            assert type(r1) == PgCfg_SetOptionResult_Base
            assert type(r1.EventID) == PgCfg_SetOptionEventID

            if nPass == 0:
                assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
            else:
                assert (
                    r1.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ALREADY_DEFINED
                )

            assert r1.m_OptData is not None
            assert type(r1.m_OptData.m_Name) == str
            assert r1.m_OptData.m_Name == C_OPT_NAME
            assert type(r1.m_OptData.m_Value) == list
            assert len(r1.m_OptData.m_Value) == 1
            assert r1.m_OptData.m_Value[0] is not None
            assert type(r1.m_OptData.m_Value[0]) == str
            assert r1.m_OptData.m_Value[0] == "biha"
            assert r1.m_OptData.m_Value == ["biha"]

            assert type(r1.Option) == PgCfg_Option_Base
            assert r1.Option is r1.m_Opt  # check cache
            assert r1.Option.m_OptionData is r1.m_OptData
            assert r1.Option.get_Name() == C_OPT_NAME
            assert r1.Option.get_Value() == ["biha"]

            assert cfg.GetOptionValue(C_OPT_NAME) == ["biha"]

    # --------------------------------------------------------------------
    def test_002(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        optValues = ["biha", "proxima", "biha", "proxima"]

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        expectedValue = list[str]()

        index = set[str]()

        for iOptValue in range(len(optValues)):
            optValue = optValues[iOptValue]

            logging.info(
                "-------------- iOptValue: {0}, value: [{1}]".format(
                    iOptValue, optValue
                )
            )

            optValueWillBeAdded = not optValue in index

            if optValueWillBeAdded:
                expectedValue.append(optValue)
                index.add(optValue)

            r1 = cfg.SetOptionValueItem(C_OPT_NAME, optValue)

            assert r1 is not None
            assert type(r1) == PgCfg_SetOptionResult_Base
            assert type(r1.EventID) == PgCfg_SetOptionEventID

            if len(expectedValue) == 1:
                assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
            elif optValueWillBeAdded:
                assert r1.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ADDED
            else:
                assert (
                    r1.EventID == PgCfg_SetOptionEventID.VALUE_ITEM_WAS_ALREADY_DEFINED
                )

            assert r1.m_OptData is not None
            assert type(r1.m_OptData.m_Name) == str
            assert r1.m_OptData.m_Name == C_OPT_NAME
            assert type(r1.m_OptData.m_Value) == list
            assert len(r1.m_OptData.m_Value) == len(expectedValue)

            for i in range(len(expectedValue)):
                assert r1.m_OptData.m_Value[i] is not None
                assert type(r1.m_OptData.m_Value[i]) == str
                assert r1.m_OptData.m_Value[i] == expectedValue[i]

            assert r1.m_OptData.m_Value == expectedValue

            assert type(r1.Option) == PgCfg_Option_Base
            assert r1.Option is r1.m_Opt  # check cache
            assert r1.Option.m_OptionData is r1.m_OptData
            assert r1.Option.get_Name() == C_OPT_NAME
            assert r1.Option.get_Value() == expectedValue

            assert cfg.GetOptionValue(C_OPT_NAME) == expectedValue

    # --------------------------------------------------------------------
    def test_003(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")

        r2 = cfg.SetOptionValueItem(C_OPT_NAME, "proxima")

        assert r1.m_OptData is r2.m_OptData

        assert r1.Option.get_Value() == ["biha", "proxima"]

    # --------------------------------------------------------------------
    def test_004__check_get_prepare_filter__unique(
        self, request: pytest.FixtureRequest
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")

        assert r1.m_OptData.m_Value == ["biha"]
        assert r1.Option.get_Value() == ["biha"]

        r1.m_OptData.m_Value.append("biha")

        assert r1.m_OptData.m_Value == ["biha", "biha"]
        assert r1.Option.get_Value() == ["biha"]

    # --------------------------------------------------------------------
    def test_005__check_get_prepare_filter__to_str(
        self, request: pytest.FixtureRequest
    ):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")

        assert r1.m_OptData.m_Value == ["biha"]
        assert r1.Option.get_Value() == ["biha"]

        r1.m_OptData.m_Value.append(1)

        assert r1.m_OptData.m_Value == ["biha", 1]
        assert r1.m_OptData.m_Value != ["biha", "1"]
        assert r1.Option.get_Value() == ["biha", "1"]
        assert r1.Option.get_Value() != ["biha", 1]

    # --------------------------------------------------------------------
    def test_006__set_value_item_with_bad_type(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")

        assert r1.m_OptData.m_Value == ["biha"]
        assert r1.Option.get_Value() == ["biha"]

        errMsg = (
            "Bad option [{0}] value item type [{1}]. Expected type is [{2}].".format(
                C_OPT_NAME, "int", "str"
            )
        )

        with pytest.raises(Exception, match=re.escape(errMsg)):
            cfg.SetOptionValueItem(C_OPT_NAME, 1)

        assert r1.m_OptData.m_Value == ["biha"]
        assert r1.Option.get_Value() == ["biha"]

    # --------------------------------------------------------------------
    def test_007__set_None(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        r1 = cfg.SetOptionValueItem(C_OPT_NAME, "biha")

        assert r1.m_OptData.m_Value == ["biha"]
        assert r1.Option.get_Value() == ["biha"]

        errMsg = "None value is not supported."

        with pytest.raises(Exception, match=re.escape(errMsg)):
            cfg.SetOptionValueItem(C_OPT_NAME, None)

        assert r1.m_OptData.m_Value == ["biha"]
        assert r1.Option.get_Value() == ["biha"]


# //////////////////////////////////////////////////////////////////////////////
