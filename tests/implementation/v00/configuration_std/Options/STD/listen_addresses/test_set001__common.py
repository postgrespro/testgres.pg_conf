# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_std import PostgresConfigurationWriter_Base as PgCfg_Writer_Base
from src.implementation.v00.configuration_std import PostgresConfigurationWriterCtx_Base as PgCfg_WriterCtx_Base
from src.exceptions import PostgresConfigException

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder
# fmt: on

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    C_OPTION_NAME = "listen_addresses"

    # --------------------------------------------------------------------
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)

        set_r = cfg.SetOptionValue(__class__.C_OPTION_NAME, "*")

        assert set_r.Option is not None
        assert set_r.Option.get_Name() == __class__.C_OPTION_NAME
        assert set_r.Option.get_Value() == "*"

        assert cfg.GetOptionValue(__class__.C_OPTION_NAME) == "*"

        set_r.Option.set_Value("localhost")

        assert set_r.Option.get_Value() == "localhost"

        assert cfg.GetOptionValue(__class__.C_OPTION_NAME) == "localhost"

        set_r.Option.set_Value(None)

        assert cfg.GetOptionValue(__class__.C_OPTION_NAME) is None

        add_r = cfg.AddOption(__class__.C_OPTION_NAME, "*")

        assert add_r.m_OptionData is not set_r.m_OptData
        assert add_r.get_Name() == __class__.C_OPTION_NAME
        assert add_r.get_Value() == "*"

        # WRITE INTO FILE
        writeCtx = PgCfg_WriterCtx_Base(cfg)

        file = cfg.get_AllFiles().GetFileByName(cfg.C_POSTGRESQL_AUTO_CONF)

        writeResult = PgCfg_Writer_Base.MakeFileDataContent(writeCtx, file.m_FileData)

        assert writeResult == "listen_addresses = '*'\n"
        return

    # --------------------------------------------------------------------
    def test_E01__bad_value(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)

        with pytest.raises(PostgresConfigException) as x:
            cfg.SetOptionValue(__class__.C_OPTION_NAME, 123)

        assert str(x.value) == ErrorMessageBuilder.BadOptionValueType(
            "listen_addresses",
            int,
            str,
        )
        return


# //////////////////////////////////////////////////////////////////////////////
