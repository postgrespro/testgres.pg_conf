# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from .model import OptionData
from .bugcheck_error import BugCheckError

from ..os.abstract.configuration_os_ops import ConfigurationOsOps

import typing

# //////////////////////////////////////////////////////////////////////////////


class Helpers:
    def ExtractOptionDataName(option: typing.Union[str, OptionData]) -> str:
        assert type(option) == str or type(option) == OptionData

        typeOption = type(option)

        if typeOption == str:
            return option

        if typeOption == OptionData:
            return option.m_Name

        BugCheckError.UnkObjectDataType(typeOption)

    # --------------------------------------------------------------------
    def ExtractFirstOptionFromIndexItem(
        optionName: str, indexItem: typing.Union[OptionData, list[OptionData]]
    ) -> OptionData:
        assert type(optionName) == str

        typeOfIndexItem = type(indexItem)

        if typeOfIndexItem == OptionData:
            assert indexItem.m_Name == optionName
            return indexItem

        if typeOfIndexItem == list:
            assert len(indexItem) > 1
            assert indexItem[0] is not None
            assert type(indexItem[0]) == OptionData
            assert indexItem[0].m_Name == optionName
            return indexItem[0]

        BugCheckError.UnkOptObjectDataType(optionName, typeOfIndexItem)

    # --------------------------------------------------------------------
    def DoesContainerContainsValue__NotNullAndExact(
        container: typing.Iterable, value: any
    ) -> bool:
        assert container is not None
        assert isinstance(container, typing.Iterable)
        assert value is not None

        for x in container:
            assert x is not None
            assert type(x) == type(value)

            if x == value:
                return True

        return False

    # --------------------------------------------------------------------
    def NormalizeFilePath(
        cfgOsOps: ConfigurationOsOps,
        baseFolder: str,
        filePath: str
    ) -> str:
        assert cfgOsOps is not None
        assert isinstance(cfgOsOps, ConfigurationOsOps)
        assert type(baseFolder) == str
        assert type(filePath) == str
        assert filePath != ""

        newFilePath = None

        if cfgOsOps.Path_IsAbs(filePath):
            newFilePath = cfgOsOps.Path_NormPath(filePath)
        else:
            newFilePath = cfgOsOps.Path_Join(baseFolder, filePath)
            newFilePath = cfgOsOps.Path_NormPath(newFilePath)

        assert type(newFilePath) == str
        assert newFilePath != ""

        newFilePath = cfgOsOps.Path_AbsPath(newFilePath)
        newFilePath = cfgOsOps.Path_NormCase(newFilePath)

        return newFilePath


# //////////////////////////////////////////////////////////////////////////////
