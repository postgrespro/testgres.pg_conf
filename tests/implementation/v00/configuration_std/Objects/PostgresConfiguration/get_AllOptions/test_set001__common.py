# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfiguration_Base__AllOptions as PgCfg_Base__AllOptions
from src.implementation.v00.configuration_base import PostgresConfiguration_Base__AllOptionsIterator as PgCfg_Base__AllOptionsIterator
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from src.abstract.v00.configuration import PostgresConfigurationOption as PgCfg_Option
from src.abstract.v00.configuration import PostgresConfigurationOptions as PgCfg_Options
from src.abstract.v00.configuration import PostgresConfigurationOptionsIterator as PgCfg_OptionsIterator
# fmt: on

from .......TestServices import TestServices

import pytest
import typing

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_000(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        allOptions1 = cfg.get_AllOptions()
        assert allOptions1 is not None
        assert type(allOptions1) is PgCfg_Base__AllOptions
        assert isinstance(allOptions1, PgCfg_Options)
        assert len(allOptions1) == 0

        allOptions2 = cfg.get_AllOptions()
        assert allOptions2 is allOptions1  # check cache

    # --------------------------------------------------------------------
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        cfg.SetOptionValue(optName, 123)

        allOptions1 = cfg.get_AllOptions()
        assert allOptions1 is not None
        assert type(allOptions1) is PgCfg_Base__AllOptions
        assert isinstance(allOptions1, PgCfg_Options)
        assert len(allOptions1) == 1

        allOptions1_list: list[PgCfg_Option_Base] = []
        for option in allOptions1:
            assert option is not None
            assert type(option) is PgCfg_Option_Base
            assert isinstance(option, PgCfg_Option)
            allOptions1_list.append(option)

        assert allOptions1_list is not None
        assert len(allOptions1_list) == 1

        assert allOptions1_list[0].get_Name() == optName
        assert allOptions1_list[0].get_Value() == 123

        assert allOptions1_list[0].get_Parent().get_Parent().get_Parent() == cfg

    # --------------------------------------------------------------------
    def test_002__iter(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        allOptions1 = cfg.get_AllOptions()
        assert type(allOptions1) is PgCfg_Base__AllOptions

        it1 = allOptions1.__iter__()
        assert it1 is not None
        assert type(it1) == PgCfg_Base__AllOptionsIterator  # noqa: E721
        assert isinstance(it1, PgCfg_OptionsIterator)
        assert it1.m_Cfg is cfg
        assert it1.m_OptionDataIterator is not None

        it1a = it1.__iter__()
        assert it1a is not None
        assert type(it1a) == PgCfg_Base__AllOptionsIterator  # noqa: E721
        assert isinstance(it1a, PgCfg_OptionsIterator)
        assert it1a.m_Cfg is cfg

        # NOTE: it may change in the future
        assert it1a.m_OptionDataIterator is it1.m_OptionDataIterator
        assert it1a is it1

    # --------------------------------------------------------------------
    def test_003__transform_to_list(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        allOptions1 = cfg.get_AllOptions()
        v = list(allOptions1)
        assert len(v) == 0

        cfg.SetOptionValue("port", 333)
        v = list(allOptions1)
        assert len(v) == 1

    # --------------------------------------------------------------------
    def test_004__two_options(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        cfg.SetOptionValue("port", 123)
        cfg.SetOptionValue("proxima.port", 321)

        assert len(cfg.get_AllOptions()) == 2

        names: typing.Set[str] = set()

        for opt in cfg.get_AllOptions():
            assert opt is not None
            assert type(opt) is PgCfg_Option_Base
            assert isinstance(opt, PgCfg_Option)
            assert type(opt) is PgCfg_Option_Base

            assert not opt.get_Name() in names

            names.add(opt.get_Name())


# //////////////////////////////////////////////////////////////////////////////
