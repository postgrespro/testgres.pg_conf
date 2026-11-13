# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

# fmt: off
from .configuration_base import PostgresConfiguration_Base
from .configuration_base import PostgresConfigurationSetOptionValueResult_Base
from .configuration_base import PostgresConfigurationSetOptionValueEventID
from .configuration_base import PostgresConfigurationSetOptionValueResult
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
from ...core.raise_error import RaiseError
from ...core.bugcheck_error import BugCheckError
# fmt: on

import typing

# //////////////////////////////////////////////////////////////////////////////
# PostgresConfiguration_Base__DataStrategy_Strict


class PostgresConfiguration_Base__DataStrategy_Strict:
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
            assert sourceData.IsAlive()

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

        return __class__.Helper__FindSimpleOption(
            cfg,
            cfg.m_Data.m_AllOptionsByName,
            optionName,
        )

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

        r = __class__.GetOptionValue__Simple(
            cfg,
            sourceData,
            optionName,
        )
        assert r is None or type(r) is list
        return r

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

        # -------------------------------- target is OptionData
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

        # -------------------------------- target is FileData
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

        # ------------------------------------------------
        optionData = __class__.Helper__FindSimpleOption(
            cfg,
            cfg.m_Data.m_AllOptionsByName,
            optionName,
        )

        if optionData is not None:
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName

            PgCfgModel__ModelUtils.Option__set_Value(
                optionData,
                optionValue,
            )

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
                cfg,
                optionData,
            )

        assert optionData is None

        result = __class__.Helper__FinalRegSimpleOptionValue__Common(
            cfg,
            optionName,
            optionValue,
        )

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        assert result.m_EventID in [
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
        ]
        assert result.m_OptData is not None
        assert type(result.m_OptData) is PgCfgModel__OptionData
        assert result.m_Cfg is cfg

        return result

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
        optionData = __class__.Helper__FindSimpleOption(
            cfg,
            fileData.m_OptionsByName,
            optionName,
        )

        if optionData is not None:
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName

            PgCfgModel__ModelUtils.Option__set_Value(
                optionData,
                optionValue,
            )

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
                cfg,
                optionData,
            )

        assert optionData is None

        # Let's append this new option
        if optionName in cfg.m_Data.m_AllOptionsByName.keys():
            optionData = Helpers.ExtractFirstOptionFromIndexItem(
                optionName,
                cfg.m_Data.m_AllOptionsByName[optionName],
            )

            assert optionData is not None
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert type(optionData.m_Parent) is PgCfgModel__FileLineData
            assert optionData.m_Parent.IsAlive()
            assert type(optionData.m_Parent.m_Parent) is PgCfgModel__FileData
            assert optionData.m_Parent.m_Parent.IsAlive()

            RaiseError.OptionIsAlreadyExistInAnotherFile(
                optionData.m_Parent.m_Parent.m_Path,
                optionName,
            )

        result = __class__.Helper__FinalRegSimpleOptionValue__File(
            cfg,
            fileData,
            optionName,
            optionValue,
        )

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

        if optionName in cfg.m_Data.m_AllOptionsByName.keys():
            assert cfg.m_Data.m_AllOptionsByName[optionName] is not None
            indexItem = cfg.m_Data.m_AllOptionsByName[optionName]
            optionData = Helpers.ExtractFirstOptionFromIndexItem(
                optionName,
                indexItem,
            )

            assert optionData is not None
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.get_Parent() is not None
            assert type(optionData.get_Parent()) is PgCfgModel__FileLineData

            anotherFileData = optionData.get_Parent().get_Parent()

            assert anotherFileData is not None
            assert type(anotherFileData) is PgCfgModel__FileData

            RaiseError.OptionIsAlreadyExistInFile(
                anotherFileData.m_Path,
                optionName,
            )

        # OK. Let's add this option
        assert optionValue is not None

        # Let's select the file to append this new option
        getFileData_r = __class__.Helper__GetFileForNewSimpleOption(
            cfg,
            optionName,
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

        if optionName in fileData.m_OptionsByName.keys():
            assert fileData.m_OptionsByName[optionName] is not None
            RaiseError.OptionIsAlreadyExistInThisFile(
                fileData.m_Path,
                optionName,
            )

        if optionName in cfg.m_Data.m_AllOptionsByName.keys():
            assert cfg.m_Data.m_AllOptionsByName[optionName] is not None
            indexItem = cfg.m_Data.m_AllOptionsByName[optionName]
            optionData = Helpers.ExtractFirstOptionFromIndexItem(
                optionName,
                indexItem,
            )

            assert optionData is not None
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert optionData.get_Parent() is not None
            assert type(optionData.get_Parent()) is PgCfgModel__FileLineData

            anotherFileData = optionData.get_Parent().get_Parent()

            assert anotherFileData is not None
            assert type(anotherFileData) is PgCfgModel__FileData
            assert anotherFileData is not fileData

            RaiseError.OptionIsAlreadyExistInAnotherFile(
                anotherFileData.m_Path,
                optionName,
            )

        assert optionName not in fileData.m_OptionsByName.keys()
        assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()

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

        if optionName in fileData.m_OptionsByName.keys():
            assert fileData.m_OptionsByName[optionName] is not None
            RaiseError.OptionIsAlreadyExistInThisFile(
                fileData.m_Path,
                optionName,
            )

        if optionName in cfg.m_Data.m_AllOptionsByName.keys():
            assert cfg.m_Data.m_AllOptionsByName[optionName] is not None
            indexItem = cfg.m_Data.m_AllOptionsByName[optionName]
            optionData = Helpers.ExtractFirstOptionFromIndexItem(
                optionName,
                indexItem,
            )

            assert optionData is not None
            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert optionData.get_Parent() is not None
            assert type(optionData.get_Parent()) is PgCfgModel__FileLineData

            anotherFileData = optionData.get_Parent().get_Parent()

            assert anotherFileData is not None
            assert type(anotherFileData) is PgCfgModel__FileData
            assert anotherFileData is not fileData

            RaiseError.OptionIsAlreadyExistInAnotherFile(
                anotherFileData.m_Path,
                optionName,
            )

        assert optionName not in fileData.m_OptionsByName.keys()
        assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()

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
    @staticmethod
    def Helper__FindSimpleOption(
        cfg: PostgresConfiguration_Base,
        allOptionsByName: PgCfgModel__T_OPTIONS_INDEX,
        optionName: str,
    ) -> typing.Optional[PgCfgModel__OptionData]:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(allOptionsByName) is PgCfgModel__MultiIndex
        assert type(optionName) is str

        if optionName not in allOptionsByName.keys():
            return None

        data = allOptionsByName[optionName]

        assert data is not None

        if type(data) is PgCfgModel__OptionData:
            assert data.IsAlive()
            assert data.m_Name == optionName
            cfg.Debug__CheckOurObjectData(data)
            return data

        if type(data) is list:
            assert len(data) > 1
            BugCheckError.MultipleDefOfOptionIsFound(
                optionName,
                len(data),
            )

        BugCheckError.UnkOptObjectDataType(
            optionName,
            type(data),
        )

    # --------------------------------------------------------------------
    # returns tuple[FileData, Bool_signal_about_creating_a_new_file]
    @staticmethod
    def Helper__GetFileForNewSimpleOption(
        cfg: PostgresConfiguration_Base,
        option_name: str,
    ) -> typing.Tuple[PgCfgModel__FileData, bool]:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(option_name) is str
        assert option_name != ""

        option_name_parts = option_name.split(".")

        assert type(option_name_parts) is list
        assert len(option_name_parts) > 0

        if len(option_name_parts) > 1:
            specFileName = "postgresql." + ".".join(option_name_parts[:-1]) + ".conf"
            assert type(specFileName) is str

            fileData = PgCfgModel__ModelUtils.Cfg__FindTopLevelFileByName(
                cfg.m_Data,
                specFileName,
            )

            if fileData is not None:
                assert type(fileData) is PgCfgModel__FileData
                return (fileData, False)

        # Let's use standard "postgresql.auto.conf"

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
            optionName,
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
# g_PgCfgBaseDataStrategy__Strict


g_PgCfgBaseDataStrategy__Strict = PostgresConfiguration_Base.tagDataStrategy(
    # fmt: off
    SetOptionValue__Simple=PostgresConfiguration_Base__DataStrategy_Strict.SetOptionValue__Simple,
    GetOptionValue__Simple=PostgresConfiguration_Base__DataStrategy_Strict.GetOptionValue__Simple,
    GetOptionValue__UnionList=PostgresConfiguration_Base__DataStrategy_Strict.GetOptionValue__UnionList,
    ResetOption=PostgresConfiguration_Base__DataStrategy_Strict.ResetOption,
    AddSimpleOption=PostgresConfiguration_Base__DataStrategy_Strict.AddSimpleOption,
    SetUniqueOptionValueItem=PostgresConfiguration_Base__DataStrategy_Strict.SetUniqueOptionValueItem,
    # fmt: on
)

# //////////////////////////////////////////////////////////////////////////////
