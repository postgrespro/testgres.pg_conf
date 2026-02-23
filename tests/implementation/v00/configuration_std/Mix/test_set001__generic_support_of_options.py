# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_std import PostgresConfigurationWriter_Base as PgCfg_Writer_Base
from src.implementation.v00.configuration_std import PostgresConfigurationWriterCtx_Base as PgCfg_WriterCtx_Base
from src.implementation.v00.configuration_std import PostgresConfigurationReader_Base as PgCfg_Reader_Base

from .....TestServices import TestServices
# fmt: on

import pytest
import typing
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__GenericSupportOfOptions


class TestSet001__GenericSupportOfOptions:
    sm_data001: typing.List[typing.Tuple[str, any, any]] = [
        ("int", 0, 0),
        ("str__empty", "", ""),
        ("bool_prop_true", True, True),
        ("bool_prop_false", False, False),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data001, ids=[x[0] for x in sm_data001])
    def data001(self, request: pytest.FixtureRequest) -> typing.Tuple[any, any]:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple  # noqa: E721
        assert len(request.param) == 3
        return request.param[1:]

    # --------------------------------------------------------------------
    def test_001__set_get(
        self, request: pytest.FixtureRequest, data001: typing.Tuple[any, any]
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        cfg.SetOptionValue("a", data001[0])

        assert cfg.GetOptionValue("a") == data001[1]

    # --------------------------------------------------------------------
    sm_data002: typing.List[typing.Tuple[str, any, any]] = [
        ("int", 0, "0"),
        ("str__empty", "", ""),
        ("bool_prop_true", True, "on"),
        ("bool_prop_false", False, "off"),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data002, ids=[x[0] for x in sm_data002])
    def data002(self, request: pytest.FixtureRequest) -> typing.Tuple[any, any]:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple  # noqa: E721
        assert len(request.param) == 3
        return request.param[1:]

    # --------------------------------------------------------------------
    def test_002__write_and_read(
        self, request: pytest.FixtureRequest, data002: typing.Tuple[any, any]
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data002) == tuple  # noqa: E721
        assert len(data002) == 2

        rootTmpDir = TestServices.GetCurTestTmpDir(request)
        assert type(rootTmpDir) is str

        os.makedirs(rootTmpDir, exist_ok=True)

        cfg = PgCfg_Std(rootTmpDir)

        cfg.SetOptionValue("a", data002[0])

        writeCtx = PgCfg_WriterCtx_Base(cfg)
        PgCfg_Writer_Base.DoWork(writeCtx)

        cfg2 = PgCfg_Std(rootTmpDir)

        PgCfg_Reader_Base.LoadConfigurationFile(cfg2, cfg.C_POSTGRESQL_AUTO_CONF)

        assert cfg2.GetOptionValue("a") == data002[1]


# //////////////////////////////////////////////////////////////////////////////
