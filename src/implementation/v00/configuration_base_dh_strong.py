# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

# fmt: off
from .configuration_base import PostgresConfiguration_Base
from .configuration_base import PostgresConfigurationSetOptionValueResult_Base
from .configuration_base import PostgresConfigurationSetOptionValueEventID
from .configuration_base import PostgresConfigurationSetOptionValueResult
from .configuration_base import PostgresConfigurationOption_Base
from .configuration_base import PostgresConfigurationFactory_Base

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

from ...os.abstract.configuration_os_ops import ConfigurationOsOps
# fmt: on

import typing

# //////////////////////////////////////////////////////////////////////////////
# PostgresConfiguration_Base__DataHandler_Strong


class PostgresConfiguration_Base__DataHandler_Strong:
    @staticmethod
    def SetOptionValue__Simple(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
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
        sourceData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
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
            optionData = __class__.Helper__FindSimpleOption(
                cfg,
                cfg.m_Data.m_AllOptionsByName,
                optionName,
            )

            if optionData is not None:
                assert type(optionData) is PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                return __class__.Helper__PrepareGetValue(
                    cfg,
                    optionData.m_Name,
                    optionData.m_Value,
                )

            return None

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
            fileData = sourceData

            assert fileData.IsAlive()
            assert fileData.m_OptionsByName is not None
            assert type(fileData.m_OptionsByName) is PgCfgModel__MultiIndex

            optionData = __class__.Helper__FindSimpleOption(
                cfg,
                fileData.m_OptionsByName,
                optionName,
            )

            if optionData is not None:
                assert type(optionData) is PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                return __class__.Helper__PrepareGetValue(
                    cfg,
                    optionData.m_Name,
                    optionData.m_Value,
                )

            return None

        BugCheckError.UnkObjectDataType(type(sourceData))

    # --------------------------------------------------------------------
    @staticmethod
    def GetOptionValue__UnionList(
        cfg: PostgresConfiguration_Base,
        sourceData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
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
            unionList = __class__.Helper__AggregateAllOptionValues(
                cfg.m_Data.m_AllOptionsByName,
                optionName,
            )

            if unionList is None:
                return None

            assert type(unionList) is list
            return __class__.Helper__PrepareGetValue(
                cfg,
                optionName,
                unionList,
            )

        # -------------------------------------- OPTION DATA
        if type(sourceData) is PgCfgModel__OptionData:
            optionData = sourceData

            assert optionData.IsAlive()
            assert optionData.m_Value is not None
            cfg.Debug__CheckOurObjectData(
                optionData,
            )
            assert optionData.m_Name == optionName
            return __class__.Helper__PrepareGetValue(
                cfg,
                optionData.m_Name,
                optionData.m_Value,
            )

        # -------------------------------------- FILE DATA
        if type(sourceData) is PgCfgModel__FileData:
            sourceFileData = sourceData

            assert type(sourceFileData) is PgCfgModel__FileData
            assert sourceFileData.IsAlive()
            assert sourceFileData.m_OptionsByName is not None
            assert type(sourceFileData.m_OptionsByName) is PgCfgModel__MultiIndex

            typeOfOption = type(optionName)

            if typeOfOption is str:
                unionList = __class__.Helper__AggregateAllOptionValues(
                    sourceFileData.m_OptionsByName,
                    optionName,
                )

                if unionList is None:
                    return None

                assert type(unionList) is list
                return __class__.Helper__PrepareGetValue(
                    cfg,
                    optionName,
                    unionList,
                )

            BugCheckError.UnkObjectDataType(typeOfOption)

        BugCheckError.UnkObjectDataType(type(sourceData))

    # --------------------------------------------------------------------
    @staticmethod
    def ResetOption(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
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
        target: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__FileLineData,
        ],
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationOption_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            target is None
            or type(target) is PgCfgModel__FileData
            or type(target) is PgCfgModel__FileLineData
        )
        assert optionOffset is None or type(optionOffset) is int
        assert type(optionName) is str
        assert optionValue is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert cfg.m_Data.m_AllOptionsByName is not None
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        if type(target) is PgCfgModel__FileLineData:
            return __class__.Helper__AddSimpleOption__FileLine(
                cfg,
                target,
                optionOffset,
                optionName,
                optionValue,
            )

        assert optionOffset is None

        if type(target) is PgCfgModel__FileData:
            return __class__.Helper__AddSimpleOption__File(
                cfg,
                target,
                optionName,
                optionValue,
            )

        if target is None:
            return __class__.Helper__AddSimpleOption__Common(
                cfg,
                optionName,
                optionValue,
            )

        BugCheckError.UnkObjectDataType(type(target))

    # --------------------------------------------------------------------
    @staticmethod
    def SetUniqueOptionValueItem(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
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

        # -------------------------------- target is NONE
        if targetData is None:
            return __class__.Helper__SetUniqueOptionValueItem__Common(
                cfg,
                optionName,
                optionValueItem,
            )

        # -------------------------------- target is OPTION DATA
        if type(targetData) is PgCfgModel__OptionData:
            assert targetData.m_Name == optionName

            return __class__.Helper__SetUniqueOptionValueItem__Exact(
                cfg,
                targetData,
                optionValueItem,
            )

        # -------------------------------- target is FILE DATA
        if type(targetData) is PgCfgModel__FileData:
            return __class__.Helper__SetUniqueOptionValueItem__File(
                cfg,
                targetData,
                optionName,
                optionValueItem,
            )

        BugCheckError.UnkObjectDataType(type(targetData))

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
    def Helper__AggregateAllOptionValues(
        allOptionsByName: PgCfgModel__T_OPTIONS_INDEX,
        optionName: str,
    ) -> typing.Optional[list]:
        assert type(allOptionsByName) is PgCfgModel__MultiIndex
        assert type(optionName) is str

        if optionName not in allOptionsByName.keys():
            return None

        data = allOptionsByName[optionName]
        assert data is not None

        if type(data) is PgCfgModel__OptionData:
            assert data.IsAlive()
            assert data.m_Name == optionName
            assert data.m_Value is not None
            assert type(data.m_Value) is list
            return data.m_Value

        if type(data) is list:
            data = data.copy()
            assert type(data) is list

            result = []

            for optionData in data:
                assert optionData is not None
                assert type(optionData) is PgCfgModel__OptionData
                assert optionData.m_Name == optionName
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                assert type(optionData.m_Value) is list
                result.extend(optionData.m_Value)
                continue

            assert result is not None
            assert type(result) is list

            return result

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
    def Helper__SetUniqueOptionValueItem__Common(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        optionValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str
        assert optionValueItem is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        # ------------------------------------------------
        while True:
            if optionName not in cfg.m_Data.m_AllOptionsByName.keys():
                break

            data = cfg.m_Data.m_AllOptionsByName[optionName]

            typeOfData = type(data)

            if typeOfData == PgCfgModel__OptionData:
                assert type(data) is PgCfgModel__OptionData
                assert data.m_Name == optionName
                assert data.m_Value is not None
                assert type(data.m_Value) is list

                if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                    data,
                    optionValueItem,
                ):
                    return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                        cfg,
                        data,
                    )

                PgCfgModel__ModelUtils.Option__add_ValueItem(
                    data,
                    optionValueItem,
                )

                return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAdded(
                    cfg,
                    data,
                )

            if typeOfData is list:
                assert type(data) is list
                assert len(data) > 1

                for optionData in data:
                    assert optionData is not None
                    assert type(optionData) is PgCfgModel__OptionData
                    assert optionData.m_Name == optionName
                    assert optionData.m_Value is not None
                    assert type(optionData.m_Value) is list

                    if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                        optionData,
                        optionValueItem,
                    ):
                        # Create__OptWithThisValueItemAlreadyExist
                        return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                            cfg,
                            optionData,
                        )
                    continue

                # [2025-01-07] Postgres does not able to join multiple list
                # TODO: We have to take into account overriding the values of postgresql.conf
                BugCheckError.MultipleDefOfOptionIsFound(
                    optionName,
                    len(data),
                )

            BugCheckError.UnkOptObjectDataType(
                optionName,
                typeOfData,
            )

        # ------------------------------------------------
        assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()

        # OK. Let's add a new option with list that contains our optionValueItem

        result = __class__.Helper__FinalRegSimpleOptionValue__Common(
            cfg,
            optionName,
            [optionValueItem],
        )

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        assert result.m_EventID in [
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
        ]
        assert result.m_OptData is not None
        assert type(result.m_OptData) is PgCfgModel__OptionData
        assert result.m_OptData.m_Name == optionName
        assert result.m_Cfg is cfg

        return result

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__SetUniqueOptionValueItem__Exact(
        cfg: PostgresConfiguration_Base,
        optionData: PgCfgModel__OptionData,
        optionValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionData) is PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionValueItem is not None

        return __class__.Helper__SetUniqueOptionPreparedValueItem__Exact(
            cfg,
            optionData,
            optionValueItem,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__SetUniqueOptionPreparedValueItem__Exact(
        cfg: PostgresConfiguration_Base,
        optionData: PgCfgModel__OptionData,
        optionPreparedValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionData) is PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionData.m_Value is not None
        assert type(optionData.m_Value) is list
        assert optionPreparedValueItem is not None

        # ------------------------------------------------
        if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
            optionData,
            optionPreparedValueItem,
        ):
            return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                cfg,
                optionData,
            )

        # ------------------------------------------------
        cfg.Debug__CheckOurObjectData(optionData)

        assert optionData.m_Name in cfg.m_Data.m_AllOptionsByName.keys()

        data = cfg.m_Data.m_AllOptionsByName[optionData.m_Name]

        typeOfData = type(data)

        if typeOfData is PgCfgModel__OptionData:
            assert type(data) is PgCfgModel__OptionData
            # It is the single property!
            assert data is optionData
            assert type(data.m_Value) is list

            PgCfgModel__ModelUtils.Option__add_ValueItem(
                data,
                optionPreparedValueItem,
            )

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAdded(
                cfg,
                data,
            )

        if typeOfData is list:
            assert type(data) is list
            assert len(data) > 1

            for optionData2 in data:
                if optionData2 is optionData:
                    continue

                assert optionData2 is not None
                assert type(optionData2) is PgCfgModel__OptionData
                assert optionData2.IsAlive()
                assert optionData2.m_Name == optionData.m_Name
                assert optionData2.m_Value is not None
                assert type(optionData2.m_Value) is list
                assert optionData2.m_Parent is not None
                assert optionData2.m_Parent.IsAlive()

                fileData2 = optionData2.m_Parent.m_Parent
                assert type(fileData2) is PgCfgModel__FileData
                assert fileData2.IsAlive()

                if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                    optionData2,
                    optionPreparedValueItem,
                ):
                    RaiseError.OptionValueItemIsAlreadyDefined(
                        fileData2.m_Path,
                        optionData2.m_Name,
                        optionPreparedValueItem,
                    )
                continue

            # [2025-01-07] Postgres does not able to join multiple list
            # TODO: We have to take into account overriding the values of postgresql.conf
            BugCheckError.MultipleDefOfOptionIsFound(
                optionData.m_Name,
                len(data),
            )

        assert typeOfData is not PgCfgModel__OptionData
        assert typeOfData is not list

        BugCheckError.UnkOptObjectDataType(
            optionData.m_Name,
            typeOfData,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__SetUniqueOptionValueItem__File(
        cfg: PostgresConfiguration_Base,
        fileData: PgCfgModel__FileData,
        optionName: str,
        optionValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) is PgCfgModel__FileData
        assert type(optionName) is str
        assert fileData.IsAlive()
        assert optionValueItem is not None

        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) is PgCfgModel__MultiIndex

        # ------------------------------------------------
        C_BUGCHECK_SRC = __class__.__name__ + "::Helper__SetUniqueOptionValueItem__File"

        # ------------------------------------------------
        while True:
            if optionName not in cfg.m_Data.m_AllOptionsByName.keys():
                # It is an absolutely new option
                assert optionName not in fileData.m_OptionsByName.keys()
                break

            if optionName in fileData.m_OptionsByName.keys():
                data = fileData.m_OptionsByName[optionName]
                assert data is not None

                if type(data) is PgCfgModel__OptionData:
                    assert data.IsAlive()
                    assert data.m_Name == optionName
                    assert data.m_Value is not None
                    assert type(data.m_Value) is list

                    if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                        data,
                        optionValueItem,
                    ):
                        return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                            cfg,
                            data,
                        )

                    # this option value does not have this item

                    return __class__.Helper__SetUniqueOptionPreparedValueItem__Exact(
                        cfg,
                        data,
                        optionValueItem,
                    )

                assert type(data) is not PgCfgModel__OptionData
                assert type(data) is not list

                BugCheckError.UnkOptObjectDataType(
                    optionName,
                    type(data),
                )

            assert optionName not in fileData.m_OptionsByName.keys()

            assert optionName in cfg.m_Data.m_AllOptionsByName.keys()

            data = cfg.m_Data.m_AllOptionsByName[optionName]
            assert data is not None

            if type(data) is PgCfgModel__OptionData:
                assert data.IsAlive()
                assert data.m_Name == optionName
                assert data.m_Value is not None
                assert type(data.m_Value) is list
                assert data.get_Parent().IsAlive()

                fileData2 = data.get_Parent().get_Parent()
                assert fileData2 is not None
                assert type(fileData2) is PgCfgModel__FileData
                assert fileData2.IsAlive()
                assert fileData2 is not fileData

                if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                    data,
                    optionValueItem,
                ):
                    RaiseError.OptionValueItemIsAlreadyDefinedInAnotherFile(
                        fileData2.m_Path,
                        optionName,
                        optionValueItem,
                    )

                RaiseError.OptionIsAlreadyExistInAnotherFile(
                    fileData2.m_Path,
                    optionName,
                )

            if type(data) is list:
                assert len(data) > 1

                for optionData2 in data:
                    assert optionData2 is not None
                    assert type(optionData2) is PgCfgModel__OptionData
                    assert optionData2.IsAlive()
                    assert optionData2.m_Name == optionName
                    assert optionData2.m_Value is not None
                    assert type(optionData2.m_Value) is list

                    fileData2 = optionData2.get_Parent().get_Parent()
                    assert fileData2 is not None
                    assert type(fileData2) is PgCfgModel__FileData
                    assert fileData2.IsAlive()
                    assert fileData2 is not fileData

                    if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                        optionData2,
                        optionValueItem,
                    ):
                        RaiseError.OptionValueItemIsAlreadyDefinedInAnotherFile(
                            fileData2.m_Path,
                            optionName,
                            optionValueItem,
                        )

                    RaiseError.OptionIsAlreadyExistInAnotherFile(
                        fileData2.m_Path,
                        optionName,
                    )
                    continue

                BugCheckError.UnexpectedSituation(
                    C_BUGCHECK_SRC,
                    "#001",
                    "optionName=[{0}].".format(optionName),
                )

            BugCheckError.UnkOptObjectDataType(
                optionName,
                type(data),
            )

        assert optionName not in fileData.m_OptionsByName.keys()
        assert optionName not in cfg.m_Data.m_AllOptionsByName.keys()

        result = __class__.Helper__FinalRegSimpleOptionValue__File(
            cfg,
            fileData,
            optionName,
            [optionValueItem],
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
        getFileData_r = __class__.Helper__GetFileForSimpleOption(
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
    def Helper__GetFileForSimpleOption(
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

            fileData = __class__.Helper__FindFile(
                cfg,
                specFileName,
            )

            if fileData is not None:
                assert type(fileData) is PgCfgModel__FileData
                return (fileData, False)

        # Let's use standard "postgresql.auto.conf"

        fileData = __class__.Helper__FindFile(
            cfg,
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
    def Helper__FindFile(
        cfg: PostgresConfiguration_Base,
        file_name: str,
    ) -> typing.Optional[PgCfgModel__FileData]:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(file_name) is str
        assert file_name != ""
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert isinstance(cfg.m_Data.OsOps, ConfigurationOsOps)
        assert cfg.m_Data.OsOps.Path_BaseName(file_name) == file_name

        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(cfg.m_Data.m_AllFilesByName) is PgCfgModel__MultiIndex

        file_name_n = cfg.m_Data.OsOps.Path_NormCase(file_name)

        if file_name_n not in cfg.m_Data.m_AllFilesByName.keys():
            return None

        data = cfg.m_Data.m_AllFilesByName[file_name_n]

        assert data is not None

        if type(data) is PgCfgModel__FileData:
            return data

        if type(data) is list:
            assert len(data) > 1
            BugCheckError.MultipleDefOfFileIsFound(
                file_name_n,
                len(data),
            )

        BugCheckError.UnkFileObjectDataType(
            file_name_n,
            type(data),
        )

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
        getFileData_r = __class__.Helper__GetFileForSimpleOption(
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
# g_PgCfgBaseHandlers__Strong


g_PgCfgBaseHandlers__Strong = PostgresConfiguration_Base.tagDataHandlers(
    # fmt: off
    SetOptionValue__Simple=PostgresConfiguration_Base__DataHandler_Strong.SetOptionValue__Simple,
    GetOptionValue__Simple=PostgresConfiguration_Base__DataHandler_Strong.GetOptionValue__Simple,
    GetOptionValue__UnionList=PostgresConfiguration_Base__DataHandler_Strong.GetOptionValue__UnionList,
    ResetOption=PostgresConfiguration_Base__DataHandler_Strong.ResetOption,
    AddSimpleOption=PostgresConfiguration_Base__DataHandler_Strong.AddSimpleOption,
    SetUniqueOptionValueItem=PostgresConfiguration_Base__DataHandler_Strong.SetUniqueOptionValueItem,
    # fmt: on
)

# //////////////////////////////////////////////////////////////////////////////
