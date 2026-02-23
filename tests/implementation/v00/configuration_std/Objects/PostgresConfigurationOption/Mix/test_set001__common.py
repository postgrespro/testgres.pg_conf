# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.implementation.v00.configuration_base import PgCfgModel__ConfigurationData

from .......TestServices import TestServices
# fmt: on

import pytest
import typing
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 234)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 234
        assert type(r1.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002__set_Value__int(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 234)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 234
        assert type(r1.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        r2 = r1.Option.set_Value(432)
        assert type(r2) is PgCfg_SetOptionResult_Base
        assert r2.EventID == PgCfg_SetOptionEventID.OPTION_WAS_UPDATED
        assert r2.Option.get_Name() == optName
        assert r2.Option.get_Value() == 432
        assert type(r2.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r2.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r2.Option.get_Parent().get_Parent().get_Parent() is cfg

        assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 432
        assert type(r1.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_003__set_Value__None(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 234)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 234
        assert type(r1.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        r2 = r1.Option.set_Value(None)
        assert type(r2) is PgCfg_SetOptionResult_Base
        assert r2.EventID == PgCfg_SetOptionEventID.OPTION_WAS_DELETED
        assert r2.Option is None

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Name()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Value()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.set_Value(123)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.set_Value(None)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            r1.Option.get_Parent()

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_004__set_Value__invalid(
        self, request: pytest.FixtureRequest, optName: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 234)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 234
        assert type(r1.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        invalidValues = [True, False]

        for invalidValue in invalidValues:
            with pytest.raises(
                Exception,
                match=re.escape(
                    "Bad option [{0}] value type [bool]. Expected type is [int].".format(
                        optName,
                    )
                ),
            ):
                r1.Option.set_Value(invalidValue)

            assert r1.Option.get_Name() == optName
            assert r1.Option.get_Value() == 234

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_005__set_Value__cant_convert_value(
        self, request: pytest.FixtureRequest, optName: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        r1 = cfg.SetOptionValue(optName, 234)
        assert type(r1) is PgCfg_SetOptionResult_Base
        assert r1.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert r1.Option.get_Name() == optName
        assert r1.Option.get_Value() == 234
        assert type(r1.Option.get_Parent()) is PgCfg_FileLine_Base
        assert type(r1.Option.get_Parent().get_Parent()) is PgCfg_TopLevelFile_Base
        assert r1.Option.get_Parent().get_Parent().get_Parent() is cfg

        invalidValues = ["qwe", "123."]

        for invalidValue in invalidValues:
            with pytest.raises(
                Exception,
                match=re.escape(
                    "Can't convert option [{0}] value from type [str] to type [int].".format(
                        optName,
                    )
                ),
            ):
                r1.Option.set_Value(invalidValue)

            assert r1.Option.get_Name() == optName
            assert r1.Option.get_Value() == 234


# //////////////////////////////////////////////////////////////////////////////
