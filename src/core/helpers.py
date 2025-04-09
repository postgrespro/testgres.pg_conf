# //////////////////////////////////////////////////////////////////////////////
# Postgres Configuration. Implementation.

from .model import OptionData
from .bugcheck_error import BugCheckError

import typing
import os

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
    def NormalizeFilePath(baseFolder: str, filePath: str) -> str:
        assert type(baseFolder) == str
        assert type(filePath) == str
        assert filePath != ""

        newFilePath = None

        if os.path.isabs(filePath):
            newFilePath = os.path.normpath(filePath)
        else:
            newFilePath = os.path.join(baseFolder, filePath)
            newFilePath = os.path.normpath(newFilePath)

        assert type(newFilePath) == str
        assert newFilePath != ""

        newFilePath = os.path.abspath(newFilePath)
        newFilePath = os.path.normcase(newFilePath)

        return newFilePath


# //////////////////////////////////////////////////////////////////////////////
