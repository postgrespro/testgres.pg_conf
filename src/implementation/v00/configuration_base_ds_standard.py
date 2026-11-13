# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

# fmt: off
from .configuration_base import PostgresConfiguration_Base
from .configuration_base import PostgresConfigurationSetOptionValueResult_Base
from .configuration_base import PostgresConfigurationSetOptionValueEventID
from .configuration_base import PostgresConfigurationOption_Base
from .configuration_base import PostgresConfigurationFactory_Base
from .configuration_base import PgCfgModel__DataHandler

from ...core.model import ConfigurationData as PgCfgModel__ConfigurationData
from ...core.model import OptionData as PgCfgModel__OptionData
from ...core.model import FileLineData as PgCfgModel__FileLineData
from ...core.model import FileData as PgCfgModel__FileData
from ...core.model import MultiIndex as PgCfgModel__MultiIndex
from ...core.model import T_OPTIONS_INDEX as PgCfgModel__T_OPTIONS_INDEX

from ...core.model_utils import ModelUtils as PgCfgModel__ModelUtils

from ...core.handlers import OptionHandlerCtxToPrepareGetValue as PgCfgModel__OptionHandlerCtxPrepareToGetValue
from ...core.handlers import OptionHandlerToPrepareGetValue as PgCfgModel__OptionHandlerToPrepareGetValue

from ...core.helpers import Helpers
from ...core.bugcheck_error import BugCheckError
# fmt: on

import typing

# //////////////////////////////////////////////////////////////////////////////
# PostgresConfiguration_Base__DataStrategy_Standard


class PostgresConfiguration_Base__DataStrategy_Standard:
    @staticmethod
    def SetOptionValue__Simple(
        cfg: PostgresConfiguration_Base,
        targetData: PgCfgModel__DataHandler.T_TARGET_OF_SET_OPTION_VALUE,
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str
        assert optionValue is not None

        # ------------------------------------------------
        if targetData is None:
            return __class__.Helper__SetSimpleOptionValue__Common(
                cfg,
                optionName,
                optionValue,
            )

        # ------------------------------------------------
        assert targetData is not None

        if type(targetData) is PgCfgModel__OptionData:
            return __class__.Helper__SetSimpleOptionValue__Exact(
                cfg,
                targetData,
                optionValue,
            )

        if type(targetData) is PgCfgModel__FileData:
            return __class__.Helper__SetSimpleOptionValue__File(
                cfg,
                targetData,
                optionName,
                optionValue,
            )

        # ------------------------------------------------
        BugCheckError.UnkObjectDataType(type(targetData))

    # --------------------------------------------------------------------
    @staticmethod
    def GetOptionValue__Simple(
        cfg: PostgresConfiguration_Base,
        sourceData: PgCfgModel__DataHandler.T_TARGET_OF_GET_OPTION_VALUE,
        optionName: str,
    ) -> typing.Any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            sourceData is None
            or type(sourceData) is PgCfgModel__FileData
            or type(sourceData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        # -------------------------------------- ROOT
        if sourceData is None:
            if optionName not in cfg.m_Data.m_AllOptionsByName.keys():
                return None

            optionData = __class__.Helper__FindActiveSimpleOption__Common(
                cfg,
                optionName,
            )

            if optionData is None:
                return None

            assert optionData is not None
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert optionData.m_Value is not None

            return __class__.Helper__PrepareGetValue(
                cfg,
                optionName,
                optionData.m_Value,
            )

        # -------------------------------------- OPTION DATA
        if type(sourceData) is PgCfgModel__OptionData:
            optionData = sourceData

            assert optionData.IsAlive()
            assert optionData.m_Value is not None
            assert optionData.m_Name == optionName
            return __class__.Helper__PrepareGetValue(
                cfg,
                optionData.m_Name,
                optionData.m_Value,
            )

        # -------------------------------------- FILE DATA
        if type(sourceData) is PgCfgModel__FileData:
            if optionName not in cfg.m_Data.m_AllOptionsByName.keys():
                return None

            findCtx = PgCfgModel__ModelUtils.tagFindCtx()

            optionData = PgCfgModel__ModelUtils.File__FindSimpleOption(
                findCtx,
                sourceData,
                optionName,
                enterIntoIncludes=True,
            )

            if optionData is not None:
                assert type(optionData) is PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                assert optionData.m_Name == optionName
                return __class__.Helper__PrepareGetValue(
                    cfg,
                    optionData.m_Name,
                    optionData.m_Value,
                )

            return None

        BugCheckError.UnkObjectDataType(type(sourceData))

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FindActiveSimpleOption__Common(
        cfg: PostgresConfiguration_Base,
        optionName: str,
    ) -> typing.Optional[PgCfgModel__OptionData]:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str

        findCtx: typing.Optional[PgCfgModel__ModelUtils.tagFindCtx] = None

        autoConfFileData = PgCfgModel__ModelUtils.Cfg__FindTopLevelFileByName(
            cfg.m_Data,
            cfg.Internal__GetAutoConfFileName(),
        )

        if autoConfFileData is not None:
            findCtx = PgCfgModel__ModelUtils.tagFindCtx()

            optionData = PgCfgModel__ModelUtils.File__FindSimpleOption(
                findCtx,
                autoConfFileData,
                optionName,
                enterIntoIncludes=True,
            )

            if optionData is not None:
                assert type(optionData) is PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                assert optionData.m_Name == optionName
                return optionData

        iFile = len(cfg.m_Data.m_TopLevelFiles)

        while iFile > 0:
            iFile -= 1
            fileData = cfg.m_Data.m_TopLevelFiles[iFile]

            if autoConfFileData is None:
                pass
            elif autoConfFileData.m_Path == fileData.m_Path:
                continue

            if findCtx is None:
                findCtx = PgCfgModel__ModelUtils.tagFindCtx()

            optionData = PgCfgModel__ModelUtils.File__FindSimpleOption(
                findCtx,
                fileData,
                optionName,
                enterIntoIncludes=True,
            )

            if optionData is None:
                continue

            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Value is not None
            assert optionData.m_Name == optionName
            return optionData

        return None

    # --------------------------------------------------------------------
    @staticmethod
    def GetOptionValue__UnionList(
        cfg: PostgresConfiguration_Base,
        sourceData: PgCfgModel__DataHandler.T_TARGET_OF_GET_OPTION_VALUE,
        optionName: str,
    ) -> typing.Any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            sourceData is None
            or type(sourceData) is PgCfgModel__FileData
            or type(sourceData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        return __class__.GetOptionValue__Simple(
            cfg,
            sourceData,
            optionName,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def ResetOption(
        cfg: PostgresConfiguration_Base,
        targetData: PgCfgModel__DataHandler.T_TARGET_OF_RESET_OPTION,
        optionName: str,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        # -------------------------------- target is NONE
        if targetData is None:
            eventID = __class__.Helper__FindAndDeleteOption(
                cfg,
                cfg.m_Data.m_AllOptionsByName,
                optionName,
            )

            assert eventID in [
                PostgresConfigurationSetOptionValueEventID.NONE,
                PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED,
            ]

            return PostgresConfigurationSetOptionValueResult_Base(
                None,
                None,
                eventID,
            )

        # -------------------------------- target is FileData or OptionData
        if type(targetData) is PgCfgModel__OptionData:
            cfg.Debug__CheckOurObjectData(
                targetData,
            )

            PgCfgModel__ModelUtils.Option__delete(
                cfg.m_Data,
                targetData,
                True,
            )

            return (
                PostgresConfigurationSetOptionValueResult_Base.Create__OptWasDeleted()
            )

        if type(targetData) is PgCfgModel__FileData:
            assert type(targetData) is PgCfgModel__FileData

            eventID = __class__.Helper__FindAndDeleteOption(
                cfg,
                targetData.m_OptionsByName,
                optionName,
            )

            assert eventID in [
                PostgresConfigurationSetOptionValueEventID.NONE,
                PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED,
            ]

            return PostgresConfigurationSetOptionValueResult_Base(
                None,
                None,
                eventID,
            )

        BugCheckError.UnkObjectDataType(type(targetData))

    # --------------------------------------------------------------------
    @staticmethod
    def AddSimpleOption(
        cfg: PostgresConfiguration_Base,
        targetData: PgCfgModel__DataHandler.T_TARGET_OF_ADD_OPTION,
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationOption_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__FileLineData
        )
        assert optionOffset is None or type(optionOffset) is int
        assert type(optionName) is str
        assert optionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_AllOptionsByName is not None
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        if type(targetData) is PgCfgModel__FileLineData:
            return __class__.Helper__AddSimpleOption__FileLine(
                cfg,
                targetData,
                optionOffset,
                optionName,
                optionValue,
            )

        assert optionOffset is None

        if type(targetData) is PgCfgModel__FileData:
            return __class__.Helper__AddSimpleOption__File(
                cfg,
                targetData,
                optionName,
                optionValue,
            )

        if targetData is None:
            return __class__.Helper__AddSimpleOption__Common(
                cfg,
                optionName,
                optionValue,
            )

        BugCheckError.UnkObjectDataType(type(targetData))

    # --------------------------------------------------------------------
    @staticmethod
    def SetUniqueOptionValueItem(
        cfg: PostgresConfiguration_Base,
        targetData: PgCfgModel__DataHandler.T_TARGET_OF_SET_OPTION_VALUE,
        optionName: str,
        optionValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str
        assert optionValueItem is not None

        currentOptData: typing.Optional[PgCfgModel__OptionData] = None

        if targetData is None:
            currentOptData = __class__.Helper__FindActiveSimpleOption__Common(
                cfg,
                optionName,
            )
        elif type(targetData) is PgCfgModel__OptionData:
            assert targetData.IsAlive()
            assert targetData.m_Name == optionName
            cfg.Debug__CheckOurObjectData(targetData)
            currentOptData = targetData
        elif type(targetData) is PgCfgModel__FileData:
            assert targetData.IsAlive()
            findCtx = PgCfgModel__ModelUtils.tagFindCtx()
            currentOptData = PgCfgModel__ModelUtils.File__FindSimpleOption(
                findCtx,
                targetData,
                optionName,
                enterIntoIncludes=True,
            )
        else:
            BugCheckError.UnkObjectDataType(type(targetData))

        if currentOptData is None:
            return __class__.SetOptionValue__Simple(
                cfg,
                targetData,
                optionName,
                [optionValueItem],
            )

        assert currentOptData.IsAlive()
        assert type(currentOptData.m_Value) is list

        if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
            currentOptData,
            optionValueItem,
        ):
            return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                cfg,
                currentOptData,
            )

        newList = currentOptData.m_Value.copy()
        newList.append(optionValueItem)

        res = __class__.SetOptionValue__Simple(
            cfg,
            targetData,
            optionName,
            newList,
        )

        assert res.m_OptData is not None
        return (
            PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAdded(
                cfg,
                res.m_OptData,
            )
        )

    # Helper methods -----------------------------------------------------
    @staticmethod
    def Helper__FindAndDeleteOption(
        cfg: PostgresConfiguration_Base,
        allOptionsByName: PgCfgModel__T_OPTIONS_INDEX,
        optionName: str,
    ) -> PostgresConfigurationSetOptionValueEventID:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(allOptionsByName) is PgCfgModel__MultiIndex
        assert type(optionName) is str

        if optionName not in allOptionsByName.keys():
            return PostgresConfigurationSetOptionValueEventID.NONE

        data = allOptionsByName[optionName]
        assert data is not None

        if type(data) is PgCfgModel__OptionData:
            assert data.IsAlive()
            assert data.m_Name == optionName

            PgCfgModel__ModelUtils.Option__delete(
                cfg.m_Data,
                data,
                True,
            )

            return PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED

        if type(data) is list:
            data = data.copy()
            assert type(data) is list

            for optionData in data:
                assert optionData is not None
                assert type(optionData) is PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Name == optionName

                PgCfgModel__ModelUtils.Option__delete(
                    cfg.m_Data,
                    optionData,
                    True,
                )
                continue

            # [2025-01-02] It is expected
            assert optionName not in allOptionsByName.keys()

            return PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED

        # Unknown type of option data in dictionary

        assert type(optionName) is str
        BugCheckError.UnkOptObjectDataType(
            optionName,
            type(data),
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__SetSimpleOptionValue__Common(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str
        assert optionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        autoConfFileData = PgCfgModel__ModelUtils.Cfg__FindTopLevelFileByName(
            cfg.m_Data,
            cfg.Internal__GetAutoConfFileName(),
        )

        if autoConfFileData is not None:
            return __class__.Helper__SetSimpleOptionValue__File(
                cfg,
                autoConfFileData,
                optionName,
                optionValue,
            )

        assert autoConfFileData is None

        autoConfFileData = PgCfgModel__ModelUtils.Cfg__CreateAndAddTopLevelFile__AUTO(
            cfg.m_Data,
            cfg.Internal__GetAutoConfFileName(),
        )

        assert autoConfFileData is not None

        try:
            # Append new property into auto conf
            optionData = PgCfgModel__ModelUtils.File__add_Option(
                cfg.m_Data,
                autoConfFileData,
                optionName,
                optionValue,
            )
        except BaseException:
            # TODO: delete autoConfFileData
            raise

        assert optionData is not None
        assert optionData.IsAlive()
        assert optionData.get_Parent().get_Parent() is autoConfFileData

        return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasAdded(
            cfg,
            optionData,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__SetSimpleOptionValue__File(
        cfg: PostgresConfiguration_Base,
        fileData: PgCfgModel__FileData,
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) is PgCfgModel__FileData
        assert type(fileData.m_OptionsByName) is PgCfgModel__MultiIndex
        assert type(optionName) is str
        assert optionValue is not None

        # ------------------------------------------------
        optionData = PgCfgModel__ModelUtils.File__FindSimpleOption(
            None,
            fileData,
            optionName,
            enterIntoIncludes=False,
        )

        if optionData is not None:
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Value is not None
            assert optionData.m_Name == optionName

            PgCfgModel__ModelUtils.Option__set_Value(
                optionData,
                optionValue,
            )

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
                cfg,
                optionData,
            )

        # Append new property into auto conf
        optionData = PgCfgModel__ModelUtils.File__add_Option(
            cfg.m_Data,
            fileData,
            optionName,
            optionValue,
        )

        assert optionData is not None
        assert optionData.IsAlive()
        assert optionData.get_Parent().get_Parent() is fileData

        return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasAdded(
            cfg,
            optionData,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__SetSimpleOptionValue__Exact(
        cfg: PostgresConfiguration_Base,
        optionData: PgCfgModel__OptionData,
        optionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionData) is PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionValue is not None

        # ------------------------------------------------
        cfg.Debug__CheckOurObjectData(optionData)

        # ------------------------------------------------
        PgCfgModel__ModelUtils.Option__set_Value(
            optionData,
            optionValue,
        )

        return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
            cfg,
            optionData,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
        optionData: PgCfgModel__OptionData,
        optionValueItem: typing.Any,
    ) -> bool:
        assert optionData is not None
        assert optionValueItem is not None
        assert type(optionData) is PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionData.m_Value is not None
        assert type(optionData.m_Value) is list

        return Helpers.DoesContainerContainsValue__NotNullAndExact(
            optionData.m_Value,
            optionValueItem,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__AddSimpleOption__Common(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationOption_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str
        assert optionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_AllOptionsByName is not None
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        # OK. Let's add this option
        assert optionValue is not None

        # Let's select the file to append this new option
        getFileData_r = __class__.Helper__GetFileForNewSimpleOption(
            cfg,
        )

        assert type(getFileData_r) is tuple
        assert len(getFileData_r) == 2

        assert type(getFileData_r[0]) is PgCfgModel__FileData
        assert type(getFileData_r[1]) is bool

        fileData = getFileData_r[0]
        assert type(fileData) is PgCfgModel__FileData

        try:
            # may raise
            optionData = PgCfgModel__ModelUtils.File__add_Option(
                cfg.m_Data,
                fileData,
                optionName,
                optionValue,
            )

            assert optionData is not None
            assert type(optionData) is PgCfgModel__OptionData

            assert optionName in cfg.m_Data.m_AllOptionsByName.keys()
            assert optionName in fileData.m_OptionsByName.keys()

            try:
                # may raise
                option = PostgresConfigurationFactory_Base.GetObject(
                    cfg,
                    optionData,
                )

                assert option is not None
                assert type(option) is PostgresConfigurationOption_Base
                assert option.m_OptionData is optionData
            except:  # rollback line with option
                assert optionData.IsAlive()

                PgCfgModel__ModelUtils.FileLine__delete(
                    cfg.m_Data,
                    optionData.get_Parent(),
                )

                assert not optionData.IsAlive()

                assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()
                assert optionName not in fileData.m_OptionsByName.keys()
                raise
        except:  # rollback file
            assert type(getFileData_r) is tuple
            assert len(getFileData_r) == 2

            assert type(getFileData_r[0]) is PgCfgModel__FileData
            assert type(getFileData_r[1]) is bool

            if getFileData_r[1]:
                pass  # TODO: delete file

            raise

        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        assert option.m_OptionData is optionData
        assert option.m_OptionData.IsAlive()
        return option

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__AddSimpleOption__FileLine(
        cfg: PostgresConfiguration_Base,
        fileLineData: PgCfgModel__FileLineData,
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: typing.Any,
    ):
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert optionOffset is None or type(optionOffset) is int
        assert type(optionName) is str
        assert optionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_AllOptionsByName is not None
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData

        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) is PgCfgModel__MultiIndex

        # OK. Let's add this option
        assert optionValue is not None

        optionData = PgCfgModel__ModelUtils.FileLine__add_Option(
            cfg.m_Data,
            fileLineData,
            optionName,
            optionValue,
            optionOffset,
        )

        assert optionData is not None
        assert type(optionData) is PgCfgModel__OptionData

        assert optionName in fileData.m_OptionsByName.keys()
        assert optionName in cfg.m_Data.m_AllOptionsByName.keys()

        try:
            option = PostgresConfigurationFactory_Base.GetObject(
                cfg,
                optionData,
            )

            assert option is not None
            assert type(option) is PostgresConfigurationOption_Base
            assert option.m_OptionData is optionData
        except:
            PgCfgModel__ModelUtils.Option__delete(
                cfg.m_Data,
                optionData,
                withLine=False,
            )

            assert not optionData.IsAlive()
            assert optionName not in fileData.m_OptionsByName.keys()
            assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()
            raise

        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        assert option.m_OptionData is optionData
        assert option.m_OptionData.IsAlive()
        return option

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__AddSimpleOption__File(
        cfg: PostgresConfiguration_Base,
        fileData: PgCfgModel__FileData,
        optionName: str,
        optionValue: typing.Any,
    ):
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert type(optionName) is str
        assert optionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_AllOptionsByName is not None
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) is PgCfgModel__MultiIndex

        # OK. Let's add this option
        assert optionValue is not None

        optionData = PgCfgModel__ModelUtils.File__add_Option(
            cfg.m_Data,
            fileData,
            optionName,
            optionValue,
        )

        assert optionData is not None
        assert type(optionData) is PgCfgModel__OptionData

        assert optionName in fileData.m_OptionsByName.keys()
        assert optionName in cfg.m_Data.m_AllOptionsByName.keys()

        try:
            option = PostgresConfigurationFactory_Base.GetObject(
                cfg,
                optionData,
            )

            assert option is not None
            assert type(option) is PostgresConfigurationOption_Base
            assert option.m_OptionData is optionData
        except:
            PgCfgModel__ModelUtils.FileLine__delete(
                cfg.m_Data,
                optionData.get_Parent(),
            )

            assert not optionData.IsAlive()
            assert optionName not in fileData.m_OptionsByName.keys()
            assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()
            raise

        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        assert option.m_OptionData is optionData
        assert option.m_OptionData.IsAlive()
        return option

    # --------------------------------------------------------------------
    # returns tuple[FileData, Bool_signal_about_creating_a_new_file]
    @staticmethod
    def Helper__GetFileForNewSimpleOption(
        cfg: PostgresConfiguration_Base,
    ) -> typing.Tuple[PgCfgModel__FileData, bool]:
        assert isinstance(cfg, PostgresConfiguration_Base)

        # We always append into standard "postgresql.auto.conf"

        fileData = PgCfgModel__ModelUtils.Cfg__FindTopLevelFileByName(
            cfg.m_Data,
            cfg.Internal__GetAutoConfFileName(),
        )

        if fileData is not None:
            assert type(fileData) is PgCfgModel__FileData
            return (fileData, False)

        assert fileData is None

        fileData = PgCfgModel__ModelUtils.Cfg__CreateAndAddTopLevelFile__AUTO(
            cfg.m_Data,
            cfg.Internal__GetAutoConfFileName(),
        )

        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData

        return (fileData, True)

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FinalRegSimpleOptionValue__Common(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        preparedOptionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str
        assert preparedOptionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()

        # Select the file to append this new option
        getFileData_r = __class__.Helper__GetFileForNewSimpleOption(
            cfg,
        )

        assert getFileData_r is not None
        assert type(getFileData_r) is tuple
        assert len(getFileData_r) == 2
        assert type(getFileData_r[0]) is PgCfgModel__FileData
        assert type(getFileData_r[1]) is bool

        fileData = getFileData_r[0]
        assert type(fileData) is PgCfgModel__FileData

        try:
            result = __class__.Helper__FinalRegSimpleOptionValue__File(
                cfg,
                fileData,
                optionName,
                preparedOptionValue,
            )
        except:  # rollback file
            assert type(getFileData_r) is tuple
            assert len(getFileData_r) == 2

            assert type(getFileData_r[0]) is PgCfgModel__FileData
            assert type(getFileData_r[1]) is bool

            if getFileData_r[1]:
                pass  # TODO: delete file

            raise

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert result.m_EventID in [
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
        ]
        assert result.m_OptData is not None
        assert type(result.m_OptData) is PgCfgModel__OptionData
        assert result.m_OptData.IsAlive()
        assert result.m_OptData.m_Name == optionName
        return result

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FinalRegSimpleOptionValue__File(
        cfg: PostgresConfiguration_Base,
        fileData: PgCfgModel__FileData,
        optionName: str,
        preparedOptionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) is PgCfgModel__FileData
        assert type(optionName) is str
        assert preparedOptionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        assert optionName not in fileData.m_OptionsByName.keys()
        assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()

        optionData = PgCfgModel__ModelUtils.File__add_Option(
            cfg.m_Data,
            fileData,
            optionName,
            preparedOptionValue,
        )

        assert optionData is not None
        assert type(optionData) is PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionData.m_Name == optionName
        assert type(optionData.m_Parent) is PgCfgModel__FileLineData
        assert optionData.m_Parent.m_Parent is fileData
        assert optionName in fileData.m_OptionsByName.keys()
        assert optionName in cfg.m_Data.m_AllOptionsByName.keys()

        try:
            result = PostgresConfigurationSetOptionValueResult_Base.Create__OptWasAdded(
                cfg,
                optionData,
            )
            assert result is not None
            assert type(result) is PostgresConfigurationSetOptionValueResult_Base
            assert result.m_EventID in [
                PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
            ]
            assert result.m_OptData is optionData
        except:  # rollback line with option
            assert optionData.IsAlive()

            PgCfgModel__ModelUtils.FileLine__delete(
                cfg.m_Data,
                optionData.get_Parent(),
            )

            assert not optionData.IsAlive()

            assert optionName not in fileData.m_OptionsByName.keys()
            assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()
            raise

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert result.m_EventID in [
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
        ]
        assert result.m_OptData is optionData

        return result

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__PrepareGetValue(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        optionValue: typing.Any,
    ) -> typing.Any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert optionName is not None
        assert optionValue is not None
        assert type(optionName) is str

        prepareHandler = cfg.Internal__GetOptionHandlerToPrepareGetValue(
            optionName,
        )
        assert prepareHandler is not None
        assert isinstance(
            prepareHandler,
            PgCfgModel__OptionHandlerToPrepareGetValue,
        )

        prepareCtx = PgCfgModel__OptionHandlerCtxPrepareToGetValue(
            cfg,
            optionName,
            optionValue,
        )

        return prepareHandler.PrepareGetValue(prepareCtx)


# //////////////////////////////////////////////////////////////////////////////
# g_PgCfgBaseDataStrategy__Standard


g_PgCfgBaseDataStrategy__Standard = PostgresConfiguration_Base.tagDataStrategy(
    # fmt: off
    SetOptionValue__Simple=PostgresConfiguration_Base__DataStrategy_Standard.SetOptionValue__Simple,
    GetOptionValue__Simple=PostgresConfiguration_Base__DataStrategy_Standard.GetOptionValue__Simple,
    GetOptionValue__UnionList=PostgresConfiguration_Base__DataStrategy_Standard.GetOptionValue__UnionList,
    ResetOption=PostgresConfiguration_Base__DataStrategy_Standard.ResetOption,
    AddSimpleOption=PostgresConfiguration_Base__DataStrategy_Standard.AddSimpleOption,
    SetUniqueOptionValueItem=PostgresConfiguration_Base__DataStrategy_Standard.SetUniqueOptionValueItem,
    # fmt: on
)

# //////////////////////////////////////////////////////////////////////////////
