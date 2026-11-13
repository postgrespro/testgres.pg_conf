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
    def test_001__no_opt(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        assert file.GetOptionValue(optName) is None
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        option = file.AddOption(optName, 123)

        assert option.get_Name() == optName
        assert option.get_Value() == 123

        assert file.GetOptionValue(optName) == 123

        option.set_Value(321)

        assert file.GetOptionValue(optName) == 321
        return

    # --------------------------------------------------------------------
    def test_003__opt_with_list__get_None(
        self,
        pg_conf_strategy: PgCfg_Std.Strategy,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        v = file.GetOptionValue(C_OPT_NAME)

        assert v is None
        return

    # --------------------------------------------------------------------
    def test_004__opt_with_list__with_data(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "shared_preload_libraries"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        file.SetOptionValueItem(C_OPT_NAME, "xxx")

        for nPass in range(3):
            logging.info("----------- nPass: {0}".format(nPass))
            v = file.GetOptionValue(C_OPT_NAME)

            assert type(v) is list
            assert v == ["xxx"]

            v.append("yyy")
            continue
        return

    # --------------------------------------------------------------------
    def test_005__mult_opts__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile("a.conf")
        file2 = cfg.AddTopLevelFile("b.conf")

        assert file1 is not None
        assert file2 is not None
        assert file1.m_FileData is not file2.m_FileData

        file1.AddOption(C_OPT_NAME, 10)
        file1.AddOption(C_OPT_NAME, 11)
        file2.AddOption(C_OPT_NAME, 20)
        file2.AddOption(C_OPT_NAME, 21)

        v1 = file1.GetOptionValue(C_OPT_NAME)
        assert type(v1) is int
        assert v1 == 11

        v2 = file2.GetOptionValue(C_OPT_NAME)
        assert type(v2) is int
        assert v2 == 21

        return

    # --------------------------------------------------------------------
    def test_006__include(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile("a.conf")

        file2 = file1.AddInclude("b.conf").get_File()
        file3 = file2.AddInclude("c.conf").get_File()

        file3.AddOption(C_OPT_NAME, 123)
        file3.AddOption("blablabla", True)
        file3.AddComment("ohoho")
        file1a = file3.AddInclude("a.conf").get_File()

        assert file1.m_FileData is not None
        assert file1a.m_FileData is not None
        assert file1.m_FileData is file1a.m_FileData

        v = file1.GetOptionValue(C_OPT_NAME)
        assert type(v) is int
        assert v == 123

    # --------------------------------------------------------------------
    def test_007__include_and_comment(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile("a.conf")
        file1_L1 = file1.AddEmptyLine()

        file2 = file1_L1.AddInclude("b.conf", 0).get_File()
        file2_L1 = file2.AddEmptyLine()
        file1_L1.AddComment("it is a comment in  a file 1")

        file3 = file2_L1.AddInclude("c.conf", 0).get_File()
        file2_L1.AddComment("it is a comment in a file 2")

        file3_L1 = file3.AddEmptyLine()
        file3_L2 = file3.AddEmptyLine()
        file3_L1.AddOption(C_OPT_NAME, 123, 0)
        file3_L1.AddComment("line1")
        file3_L2.AddOption("blablabla", True, 0)
        file3_L2.AddComment("line2")
        file3.AddComment("ohoho")
        file1a = file3.AddInclude("a.conf").get_File()

        assert file1.m_FileData is not None
        assert file1a.m_FileData is not None
        assert file1.m_FileData is file1a.m_FileData

        v = file1.GetOptionValue(C_OPT_NAME)
        assert type(v) is int
        assert v == 123


# //////////////////////////////////////////////////////////////////////////////
