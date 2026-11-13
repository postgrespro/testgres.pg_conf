# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from src.implementation.v00.configuration_base import PostgresConfigurationOption as PgCfg_Option

from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__ConfigurationData
from src.implementation.v00.configuration_base import PgCfgModel__MultiIndex

from src.exceptions import PostgresConfigException

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder
# fmt: on

import pytest
import typing
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001__int_opt(
        self,
        request: pytest.FixtureRequest,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        option = cfg.AddOption(optName, 123)
        assert type(option) is PgCfg_Option_Base
        assert isinstance(option, PgCfg_Option)

        __class__.Helper__CheckStateOfCfgWithOneIntOpt(
            cfg,
            option,
            optName,
            123,
        )

        # Amen
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CheckStateOfCfgWithOneIntOpt(
        cfg: PgCfg_Std,
        opt: PgCfg_Option_Base,
        optName: str,
        optValue: int,
    ):
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(opt) is PgCfg_Option_Base

        assert opt.get_Configuration() is cfg
        assert opt.get_Name() == optName
        assert opt.get_Value() == optValue

        assert type(opt) is PgCfg_Option_Base
        assert type(opt.m_OptionData) is PgCfgModel__OptionData
        assert opt.m_OptionData.m_Name == optName
        assert opt.m_OptionData.m_Value == optValue
        assert opt.m_OptionData.m_Parent is not None
        assert type(opt.m_OptionData.m_Parent) is PgCfgModel__FileLineData

        fileLine = opt.get_Parent()
        assert fileLine is opt.get_Parent()
        assert type(fileLine) is PgCfg_FileLine_Base
        assert len(fileLine) == 1

        fileLineData: PgCfgModel__FileLineData = opt.m_OptionData.m_Parent
        assert fileLineData is fileLine.m_FileLineData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) is list
        assert len(fileLineData.m_Items) == 1
        assert type(fileLineData.m_Items[0]) is PgCfgModel__FileLineData.tagItem
        assert fileLineData.m_Items[0].m_Element is opt.m_OptionData
        assert fileLineData.m_Items[0].m_Element.m_Offset is None
        assert type(fileLineData.m_Parent) is PgCfgModel__FileData
        assert type(fileLineData.get_Parent()) is PgCfgModel__FileData
        assert fileLineData.get_Parent() is fileLineData.m_Parent

        file = fileLine.get_Parent()
        assert type(file) is PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert len(file) == 1

        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert fileData is file.m_FileData
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.m_Path == os.path.join(
            cfg.m_Data.m_DataDir,
            cfg.C_POSTGRESQL_AUTO_CONF,
        )
        assert fileData.m_Parent is cfg.m_Data
        assert type(fileData.m_Lines) is list
        assert len(fileData.m_Lines) == 1
        assert fileData.m_Lines[0] is fileLineData

        assert type(cfg.m_Data.m_TopLevelFiles) is list
        assert len(cfg.m_Data.m_TopLevelFiles) == 1
        assert type(cfg.m_Data.m_TopLevelFiles[0]) is PgCfgModel__FileData
        assert cfg.m_Data.m_TopLevelFiles[0] is fileData
        assert type(cfg.m_Data.m_AllFilesByName) is PgCfgModel__MultiIndex
        assert cfg.m_Data.m_AllFilesByName.get_elements_count() == 1
        assert len(list(cfg.m_Data.m_AllFilesByName.keys())) == 1
        assert cfg.C_POSTGRESQL_AUTO_CONF in cfg.m_Data.m_AllFilesByName.keys()
        assert len(list(cfg.m_Data.m_AllFilesByName.elements())) == 1
        assert fileData in cfg.m_Data.m_AllFilesByName.elements()

        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex
        assert cfg.m_Data.m_AllOptionsByName.get_elements_count() == 1
        assert optName in cfg.m_Data.m_AllOptionsByName.keys()
        assert cfg.m_Data.m_AllOptionsByName.get_elements_count() == 1
        assert opt.m_OptionData in cfg.m_Data.m_AllOptionsByName.elements()
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_002__None_value(
        self,
        request: pytest.FixtureRequest,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        with pytest.raises(PostgresConfigException) as x:
            cfg.AddOption(optName, None)

        assert str(x.value) == ErrorMessageBuilder.NoneValueIsNotSupported()
        return

    # --------------------------------------------------------------------
    def test_003__empty_name(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        with pytest.raises(PostgresConfigException) as x:
            cfg.AddOption("", 123)

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsEmpty()
        return

    # --------------------------------------------------------------------
    def test_004__None_name(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        with pytest.raises(PostgresConfigException) as x:
            cfg.AddOption(None, 123)

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsNone()
        return

    # --------------------------------------------------------------------
    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_005__already_defined(
        self,
        request: pytest.FixtureRequest,
        optName: str,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        option = cfg.AddOption(optName, 123)

        with pytest.raises(PostgresConfigException) as x:
            cfg.AddOption(optName, 321)

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInFile(
            option.get_Parent().get_Parent().get_Path(),
            option.get_Name(),
        )

        assert option.get_Name() == optName
        assert option.get_Value() == 123
        return

    # --------------------------------------------------------------------
    def test_006__two_options(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_DataDir == rootTmpDir

        opt1 = cfg.AddOption("OPT1", 123)
        assert opt1 is not None
        assert opt1.m_FileLine is not None
        assert opt1.m_FileLine.m_FileLineData is not None
        assert opt1.m_FileLine.get_Parent() is not None
        assert opt1.m_FileLine.get_Parent().m_FileData is not None
        assert len(opt1.m_FileLine.get_Parent().m_FileData.m_Lines) == 1
        opt1_filelineData = opt1.m_FileLine.m_FileLineData
        assert opt1_filelineData is not None
        opt1_fileData = opt1_filelineData.m_Parent
        assert opt1_fileData is not None

        opt2 = cfg.AddOption("OPT2", 321)
        assert opt2 is not None
        assert opt2.m_FileLine is not None
        assert opt2.m_FileLine.m_FileLineData is not None
        assert opt2.m_FileLine.get_Parent() is not None
        assert opt2.m_FileLine.get_Parent().m_FileData is not None
        assert len(opt1.m_FileLine.get_Parent().m_FileData.m_Lines) == 2
        opt2_filelineData = opt2.m_FileLine.m_FileLineData
        assert opt2_filelineData is not None
        opt2_fileData = opt2_filelineData.m_Parent
        assert opt2_fileData is not None

        assert opt1 is not opt2
        assert opt1_filelineData is not opt2_filelineData
        assert opt1_fileData is opt2_fileData

        # --------
        assert opt1.get_Name() == "OPT1"
        assert opt1.get_Value() == 123

        assert opt2.get_Name() == "OPT2"
        assert opt2.get_Value() == 321

        # --------
        assert len(opt1_fileData.m_Lines) == 2
        assert opt1_fileData.m_Lines[0] is opt1_filelineData
        assert opt1_fileData.m_Lines[1] is opt2_filelineData

        assert opt1_fileData.m_Path == os.path.join(
            rootTmpDir,
            cfg.Internal__GetAutoConfFileName(),
        )
        return


# //////////////////////////////////////////////////////////////////////////////
