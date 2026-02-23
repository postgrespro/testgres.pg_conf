# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
# fmt: on

from .......TestServices import TestServices

import pytest
import typing
import logging

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001__no_opt(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        assert file.GetOptionValue(optName) is None

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        option = file.AddOption(optName, 123)

        assert option.get_Name() == optName
        assert option.get_Value() == 123

        assert file.GetOptionValue(optName) == 123

        option.set_Value(321)

        assert file.GetOptionValue(optName) == 321

    # --------------------------------------------------------------------
    def test_003__opt_with_list__get_None(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        v = file.GetOptionValue(C_OPT_NAME)

        assert v is None

    # --------------------------------------------------------------------
    def test_004__opt_with_list__with_data(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        file.SetOptionValueItem(C_OPT_NAME, "xxx")

        for nPass in range(3):
            logging.info("----------- nPass: {0}".format(nPass))
            v = file.GetOptionValue(C_OPT_NAME)

            assert type(v) is list
            assert v == ["xxx"]

            v.append("yyy")


# //////////////////////////////////////////////////////////////////////////////
