# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData

# fmt: on

from .......TestServices import TestServices

import pytest
import os
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file is not None
        assert type(file) == PgCfg_TopLevelFile_Base  # noqa: E721
        assert file.get_Path() == os.path.join(rootTmpDir, cfg.C_POSTGRESQL_CONF)
        assert file.m_FileData is not None
        assert type(file.m_FileData) == PgCfgModel__FileData  # noqa: E721

        C_OPT_NAME = "port"

        option = file.AddOption(C_OPT_NAME, 123)

        assert file.m_FileData is not None
        assert type(file.m_FileData) == PgCfgModel__FileData  # noqa: E721

        assert option is not None
        assert option.get_Configuration() is cfg
        assert (
            option.get_Parent().get_Parent().Private__GetFileData() == file.m_FileData
        )
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == 123
        assert option.m_OptionData is not None
        assert type(option.m_OptionData) == PgCfgModel__OptionData  # noqa: E721

        assert C_OPT_NAME in file.m_FileData.m_OptionsByName.keys()
        assert file.m_FileData.m_OptionsByName[C_OPT_NAME] is option.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is option.m_OptionData

    # --------------------------------------------------------------------
    def test_002__already_in_this(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        option = file.AddOption(C_OPT_NAME, 123)

        with pytest.raises(
            Exception,
            match=re.escape(
                "Option [{0}] already exist in this file [{1}]".format(
                    C_OPT_NAME, file.get_Path()
                )
            ),
        ):
            file.AddOption(C_OPT_NAME, 321)

        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == 123

        assert C_OPT_NAME in file.m_FileData.m_OptionsByName.keys()
        assert file.m_FileData.m_OptionsByName[C_OPT_NAME] is option.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is option.m_OptionData

    # --------------------------------------------------------------------
    def test_003__already_in_another(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile("postgresql.proxima.conf")
        option = cfg.SetOptionValue(C_OPT_NAME, 123).Option
        assert type(option) is PgCfg_Option_Base
        assert len(file1) == 1

        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        with pytest.raises(
            Exception,
            match=re.escape(
                "Option [{0}] already exist in another file [{1}]".format(
                    C_OPT_NAME, file1.get_Path()
                )
            ),
        ):
            file2.AddOption(C_OPT_NAME, 321)

        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == 123

        assert C_OPT_NAME in file1.m_FileData.m_OptionsByName.keys()
        assert file1.m_FileData.m_OptionsByName[C_OPT_NAME] is option.m_OptionData

        assert C_OPT_NAME in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName[C_OPT_NAME] is option.m_OptionData

    # --------------------------------------------------------------------
    def test_004__bad_value_type(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(
            Exception,
            match=re.escape(
                "Bad option [{0}] value type [bool]. Expected type is [int].".format(
                    C_OPT_NAME,
                )
            ),
        ):
            file.AddOption(C_OPT_NAME, False)

    # --------------------------------------------------------------------
    def test_004__cant_convert_value(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(
            Exception,
            match=re.escape(
                "Can't convert option [{0}] value from type [str] to type [int].".format(
                    C_OPT_NAME,
                )
            ),
        ):
            file.AddOption(C_OPT_NAME, "blabla")

    # --------------------------------------------------------------------
    def test_005__None_value(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        C_OPT_NAME = "proxima.port"

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(
            Exception,
            match=re.escape("None value is not supported."),
        ):
            file.AddOption(C_OPT_NAME, None)

    # --------------------------------------------------------------------
    def test_006__None_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(
            Exception,
            match=re.escape("Option name is None."),
        ):
            file.AddOption(None, 123)

    # --------------------------------------------------------------------
    def test_007__empty_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str  # noqa: E721

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile("postgresql.proxima.conf")

        with pytest.raises(
            Exception,
            match=re.escape("Option name is empty."),
        ):
            file.AddOption("", 123)


# //////////////////////////////////////////////////////////////////////////////
