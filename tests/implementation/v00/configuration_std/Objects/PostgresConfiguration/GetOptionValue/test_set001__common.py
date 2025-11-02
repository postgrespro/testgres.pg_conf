# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.abstract.v00.configuration import PostgresConfigurationOption

from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult as PgCfg_SetOptionResult
# fmt: on

from .......TestServices import TestServices

import pytest
import typing
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001__port(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        set_r = cfg.SetOptionValue(optName, 123)
        assert type(set_r) == PgCfg_SetOptionResult_Base
        assert isinstance(set_r, PgCfg_SetOptionResult)
        assert set_r.m_EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        set_r_option: PgCfg_Option_Base = set_r.Option
        assert set_r_option is not None
        assert type(set_r_option) == PgCfg_Option_Base
        assert isinstance(set_r_option, PostgresConfigurationOption)
        assert set_r.Option is set_r_option  # check a cache

        assert set_r_option.get_Configuration() is cfg
        assert set_r_option.get_Name() == optName
        assert set_r_option.get_Value() == 123

        get_r = cfg.GetOptionValue(optName)
        assert type(get_r) == int
        assert get_r == 123

    # --------------------------------------------------------------------
    def test_002__None_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        with pytest.raises(Exception, match=re.escape("Option name is None.")):
            cfg.GetOptionValue(None)

    # --------------------------------------------------------------------
    def test_003__empty_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        with pytest.raises(Exception, match=re.escape("Option name is empty.")):
            cfg.GetOptionValue("")

    # --------------------------------------------------------------------
    def test_004__opt_with_list__get_None(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        v = cfg.GetOptionValue(C_OPT_NAME)

        assert v is None


# //////////////////////////////////////////////////////////////////////////////
