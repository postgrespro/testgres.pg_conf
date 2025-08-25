# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

# fmt: off
from .model import ConfigurationData as PgCfgModel__ConfigurationData
from .model import ObjectData as PgCfgModel__ObjectData
from .model import FileLineElementData as PgCfgModel__FileLineElementData
from .model import CommentData as PgCfgModel__CommentData
from .model import OptionData as PgCfgModel__OptionData
from .model import IncludeData as PgCfgModel__IncludeData
from .model import FileLineData as PgCfgModel__FileLineData
from .model import FileData as PgCfgModel__FileData
# fmt: on

from ..os.abstract.configuration_os_ops import ConfigurationOsOps

from .raise_error import RaiseError
from .bugcheck_error import BugCheckError
from .helpers import Helpers

import typing

# //////////////////////////////////////////////////////////////////////////////
# class DataControllerUtils


class DataControllerUtils:
    def Option__set_Value(optionData: PgCfgModel__OptionData, value: any):
        assert type(optionData) == PgCfgModel__OptionData
        assert value is not None

        optionData.m_Value = value

    # --------------------------------------------------------------------
    def Option__add_ValueItem(optionData: PgCfgModel__OptionData, valueItem: any):
        assert type(optionData) == PgCfgModel__OptionData
        assert type(optionData.m_Value) == list
        assert valueItem is not None

        optionData.m_Value.append(valueItem)

    # --------------------------------------------------------------------
    def Option__delete(
        cfgData: PgCfgModel__ConfigurationData,
        optionData: PgCfgModel__OptionData,
        withLine: bool,
    ):
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(optionData) == PgCfgModel__OptionData
        assert type(withLine) == bool

        fileLineData = optionData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData

        __class__.Helper__DeleteOption(cfgData, optionData)

        if not withLine:
            return

        assert not __class__.Helper__FileLineHasWorkData(fileLineData)

        __class__.Helper__DeleteFileLine(cfgData, fileLineData)

    # --------------------------------------------------------------------
    def Include__delete(
        cfgData: PgCfgModel__ConfigurationData,
        includeData: PgCfgModel__IncludeData,
        withLine: bool,
    ):
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(includeData) == PgCfgModel__IncludeData
        assert type(withLine) == bool

        fileLineData = includeData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData

        __class__.Helper__DeleteInclude(includeData)

        if not withLine:
            return

        assert not __class__.Helper__FileLineHasWorkData(fileLineData)

        __class__.Helper__DeleteFileLine(cfgData, fileLineData)

    # --------------------------------------------------------------------
    def Comment__delete(
        cfgData: PgCfgModel__ConfigurationData,
        commentData: PgCfgModel__CommentData,
        withLineIfLast: bool,
    ):
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(commentData) == PgCfgModel__CommentData
        assert type(withLineIfLast) == bool

        commentData.IsAlive()

        assert cfgData is commentData.m_Parent.m_Parent.m_Parent

        fileLineData = commentData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData

        __class__.Helper__DeleteComment(commentData)

        if not withLineIfLast:
            return

        if len(fileLineData.m_Items) != 0:
            return

        __class__.Helper__DeleteFileLine(cfgData, fileLineData)

    # --------------------------------------------------------------------
    def FileLine__add_Comment(
        fileLineData: PgCfgModel__FileLineData, offset: typing.Optional[int], text: str
    ) -> PgCfgModel__CommentData:
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert (offset is None) or (type(offset) == int)
        assert type(text) == str
        assert type(fileLineData.m_Items) == list

        assert fileLineData.IsAlive()

        __class__.Helper__CheckThatWeCanAddCommentToFileLine(fileLineData)

        commentData = PgCfgModel__CommentData(fileLineData, offset, text)
        fileLineDataItem = PgCfgModel__FileLineData.tagItem(commentData)
        fileLineData.m_Items.append(fileLineDataItem)
        return commentData

    # --------------------------------------------------------------------
    def Helper__CheckThatWeCanAddCommentToFileLine(
        fileLineData: PgCfgModel__FileLineData,
    ):
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) == list

        assert fileLineData.IsAlive()

        if len(fileLineData.m_Items) == 0:
            return

        lastItem = fileLineData.m_Items[-1]

        assert lastItem is not None
        assert type(lastItem) == PgCfgModel__FileLineData.tagItem
        assert lastItem.m_Element is not None
        assert isinstance(lastItem.m_Element, PgCfgModel__FileLineElementData)

        typeOfLastElement = type(lastItem.m_Element)

        if typeOfLastElement == PgCfgModel__OptionData:
            return

        if typeOfLastElement == PgCfgModel__IncludeData:
            return

        if typeOfLastElement == PgCfgModel__CommentData:
            RaiseError.FileLineAlreadyHasComment()

        BugCheckError.UnkObjectDataType(typeOfLastElement)

    # --------------------------------------------------------------------
    def FileLine__add_Include(
        fileLineData: PgCfgModel__FileLineData,
        filePath: str,
        fileData: PgCfgModel__FileData,
        offset: typing.Optional[int],
    ) -> PgCfgModel__IncludeData:
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert type(filePath) == str
        assert type(fileData) == PgCfgModel__FileData
        assert filePath != ""
        assert offset is None or type(offset) == int

        assert fileLineData.IsAlive()
        assert fileData.IsAlive()

        __class__.Helper__CheckThatWeCanAddWorkDataToFileLine(fileLineData)

        includeData = PgCfgModel__IncludeData(fileLineData, offset, filePath, fileData)
        fileLineDataItem = PgCfgModel__FileLineData.tagItem(includeData)
        fileLineData.m_Items.append(fileLineDataItem)

        # TODO: Reg include data in a global index?

        return includeData

    # --------------------------------------------------------------------
    def FileLine__add_Option(
        cfgData: PgCfgModel__ConfigurationData,
        fileLineData: PgCfgModel__FileLineData,
        optName: str,
        optValue: any,
        optOffset: typing.Optional[int],
    ) -> PgCfgModel__OptionData:
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert type(optName) == str
        assert optValue is not None
        assert optName != ""
        assert type(fileLineData.m_Items) == list
        assert optOffset is None or type(optOffset) == int

        __class__.Helper__CheckThatWeCanAddWorkDataToFileLine(fileLineData)

        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) == dict

        optionData = PgCfgModel__OptionData(fileLineData, optOffset, optName, optValue)
        fileLineDataItem = PgCfgModel__FileLineData.tagItem(optionData)
        fileLineData.m_Items.append(fileLineDataItem)

        try:
            __class__.Helper__InsertOptionIntoIndex(
                fileData.m_OptionsByName, optionData
            )

            try:
                __class__.Helper__InsertOptionIntoIndex(
                    cfgData.m_AllOptionsByName, optionData
                )
            except:  # rollback
                __class__.Helper__DeleteOptionFromIndex(
                    fileData.m_OptionsByName, optionData
                )
                raise
        except:  # rollback
            assert type(fileLineData.m_Items) == list
            assert len(fileLineData.m_Items) > 0
            assert fileLineData.m_Items[-1] is fileLineDataItem
            assert fileLineData.m_Items[-1].m_Element is optionData
            fileLineData.m_Items.pop()
            raise

        return optionData

    # --------------------------------------------------------------------
    def Helper__CheckThatWeCanAddWorkDataToFileLine(
        fileLineData: PgCfgModel__FileLineData,
    ):
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) == list

        assert fileLineData.IsAlive()

        if len(fileLineData.m_Items) == 0:
            return

        lastItem = fileLineData.m_Items[-1]

        assert lastItem is not None
        assert type(lastItem) == PgCfgModel__FileLineData.tagItem
        assert lastItem.m_Element is not None
        assert isinstance(lastItem.m_Element, PgCfgModel__FileLineElementData)

        typeOfLastElement = type(lastItem.m_Element)

        if typeOfLastElement == PgCfgModel__OptionData:
            RaiseError.FileLineAlreadyHasOption(lastItem.m_Element.m_Name)

        if typeOfLastElement == PgCfgModel__IncludeData:
            RaiseError.FileLineAlreadyHasIncludeDirective()

        if typeOfLastElement == PgCfgModel__CommentData:
            RaiseError.FileLineAlreadyHasComment()

        BugCheckError.UnkObjectDataType(typeOfLastElement)

    # --------------------------------------------------------------------
    def FileLine__delete(
        cfgData: PgCfgModel__ConfigurationData, fileLineData: PgCfgModel__FileLineData
    ):
        assert cfgData is not None
        assert fileLineData is not None
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        __class__.Helper__DeleteFileLine(cfgData, fileLineData)

        assert not fileLineData.IsAlive()

    # --------------------------------------------------------------------
    def FileLine__clear(
        cfgData: PgCfgModel__ConfigurationData, fileLineData: PgCfgModel__FileLineData
    ):
        assert cfgData is not None
        assert fileLineData is not None
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) == list

        return __class__.Helper__ClearFileLine(cfgData, fileLineData)

    # --------------------------------------------------------------------
    def File__add_Option(
        cfgData: PgCfgModel__ConfigurationData,
        fileData: PgCfgModel__FileData,
        optName: str,
        optValue: any,
    ) -> PgCfgModel__OptionData:
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(fileData) == PgCfgModel__FileData
        assert type(optName) == str
        assert optValue is not None

        newLineData = DataControllerUtils.File__add_Line(fileData)  # raise

        assert type(newLineData) == PgCfgModel__FileLineData

        try:
            optionData = __class__.FileLine__add_Option(
                cfgData, newLineData, optName, optValue, None
            )  # raise

            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.m_Name == optName
        except:
            DataControllerUtils.FileLine__delete(cfgData, newLineData)
            raise

        assert optionData is not None
        assert type(optionData) == PgCfgModel__OptionData
        assert optionData.IsAlive()
        return optionData

    # --------------------------------------------------------------------
    def File__add_Line(fileData: PgCfgModel__FileData) -> PgCfgModel__FileLineData:
        assert type(fileData) == PgCfgModel__FileData
        assert type(fileData.m_Lines) == list

        lineData = PgCfgModel__FileLineData(fileData)
        fileData.m_Lines.append(lineData)
        return lineData

    # --------------------------------------------------------------------
    def Cfg__CreateAndAddTopLevelFile__AUTO(
        cfgData: PgCfgModel__ConfigurationData, file_name: str
    ) -> PgCfgModel__FileData:
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(cfgData.m_Files) == list
        assert type(cfgData.m_AllFilesByName) == dict
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(file_name) == str
        assert file_name != ""
        assert cfgData.OsOps.Path_BaseName(file_name) == file_name

        newFilePath = cfgData.OsOps.Path_Join(cfgData.m_DataDir, file_name)
        newFilePath = cfgData.OsOps.Path_NormPath(newFilePath)

        assert type(newFilePath) == str
        assert newFilePath != ""

        return __class__.Helper__FinishCreateTopLevelFile(cfgData, newFilePath)

    # --------------------------------------------------------------------
    def Cfg__CreateAndAddTopLevelFile__USER(
        cfgData: PgCfgModel__ConfigurationData, path: str
    ) -> PgCfgModel__FileData:
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(cfgData.m_Files) == list
        assert type(cfgData.m_AllFilesByName) == dict
        assert type(path) == str
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert path != ""

        newFilePath = Helpers.NormalizeFilePath(cfgData.OsOps, cfgData.m_DataDir, path)

        assert type(newFilePath) == str
        assert newFilePath != ""

        # TODO: use index
        for fileData in cfgData.m_AllFilesByName.values():
            assert fileData is not None
            assert type(fileData) == PgCfgModel__FileData
            assert fileData.IsAlive()

            if fileData.m_Path == newFilePath:
                RaiseError.FileIsAlreadyRegistered(newFilePath)

        return __class__.Helper__FinishCreateTopLevelFile(cfgData, newFilePath)

    # --------------------------------------------------------------------
    def Cfg__GetOrCreateFile__USER(
        cfgData: PgCfgModel__ConfigurationData, baseFolder: str, path: str
    ) -> PgCfgModel__FileData:
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(cfgData.m_Files) == list
        assert type(cfgData.m_AllFilesByName) == dict
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(baseFolder) == str
        assert type(path) == str
        assert path != ""

        newFilePath = Helpers.NormalizeFilePath(cfgData.OsOps, baseFolder, path)

        assert type(newFilePath) == str
        assert newFilePath != ""

        # TODO: use index
        for fileData in cfgData.m_AllFilesByName.values():
            assert fileData is not None
            assert type(fileData) == PgCfgModel__FileData
            assert fileData.IsAlive()

            if fileData.m_Path == newFilePath:
                return fileData

        newFileData = PgCfgModel__FileData(cfgData, newFilePath)

        __class__.Helper__RegFileInCfgData(cfgData, newFileData)  # raise

        return newFileData

    # Helper methods -----------------------------------------------------
    def Helper__FinishCreateTopLevelFile(
        cfgData: PgCfgModel__ConfigurationData, newFilePath: str
    ) -> PgCfgModel__FileData:

        newFileData = PgCfgModel__FileData(cfgData, newFilePath)

        __class__.Helper__RegFileInCfgData(cfgData, newFileData)  # raise

        try:
            cfgData.m_Files.append(newFileData)  # raise
        except:
            __class__.Helper__UnRegFileFromCfgData(cfgData, newFileData)
            raise

        return newFileData

    # --------------------------------------------------------------------
    def Helper__FindIndexOfFileLine(
        fileData: PgCfgModel__FileData, fileLineData: PgCfgModel__FileLineData
    ) -> int:
        assert fileData is not None
        assert fileLineData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert type(fileData.m_Lines) == list
        assert type(fileLineData) == PgCfgModel__FileLineData

        cFileLines = len(fileData.m_Lines)

        for iFileLine in range(cFileLines):
            ptr = fileData.m_Lines[iFileLine]
            assert ptr is not None
            assert type(ptr) == PgCfgModel__FileLineData
            assert ptr.m_Parent is fileData

            if ptr is fileLineData:
                return iFileLine

        assert iFileLine == cFileLines
        return iFileLine

    # --------------------------------------------------------------------
    def Helper__FindIndexOfFileLineElement(
        fileLineData: PgCfgModel__FileLineData,
        elementData: PgCfgModel__FileLineElementData,
    ) -> int:
        assert fileLineData is not None
        assert elementData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) == list
        assert isinstance(elementData, PgCfgModel__FileLineElementData)

        cItems = len(fileLineData.m_Items)

        for iItem in range(cItems):
            ptr = fileLineData.m_Items[iItem]
            assert ptr is not None
            assert type(ptr) == PgCfgModel__FileLineData.tagItem
            assert ptr.m_Element is not None

            if ptr.m_Element is elementData:
                return iItem

        assert iItem == cItems
        return iItem

    # --------------------------------------------------------------------
    def Helper__RegFileInCfgData(
        cfgData: PgCfgModel__ConfigurationData, fileData: PgCfgModel__FileData
    ):
        assert cfgData is not None
        assert fileData is not None
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(fileData) == PgCfgModel__FileData
        assert type(fileData.m_Path) == str
        assert fileData.m_Path != ""

        assert fileData.IsAlive()

        fileName = cfgData.OsOps.Path_BaseName(fileData.m_Path)
        assert type(fileName) == str
        assert fileName != ""

        __class__.Helper__InsertFileIntoIndex(
            cfgData.m_AllFilesByName, fileName, fileData
        )

    # --------------------------------------------------------------------
    def Helper__UnRegFileFromCfgData(
        cfgData: PgCfgModel__ConfigurationData, fileData: PgCfgModel__FileData
    ):
        assert cfgData is not None
        assert fileData is not None
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(fileData) == PgCfgModel__FileData
        assert fileData.m_Path != ""

        assert fileData.IsAlive()

        fileName = cfgData.OsOps.Path_BaseName(fileData.m_Path)
        assert type(fileName) == str
        assert fileName != ""

        __class__.Helper__DeleteFileIntoIndex(
            cfgData.m_AllFilesByName, fileName, fileData
        )

    # --------------------------------------------------------------------
    def Helper__InsertFileIntoIndex(
        filesByStrKeyDictionary: dict[str, PgCfgModel__FileData],
        fileKey: str,
        fileData: PgCfgModel__FileData,
    ):
        assert type(filesByStrKeyDictionary) == dict
        assert type(fileKey) == str
        assert type(fileData) == PgCfgModel__FileData

        assert fileKey != ""
        assert fileData.IsAlive()

        if not (fileKey in filesByStrKeyDictionary.keys()):
            filesByStrKeyDictionary[fileKey] = fileData
        else:
            indexItemData = filesByStrKeyDictionary[fileKey]

            if indexItemData is PgCfgModel__FileData:
                filesByStrKeyDictionary[fileKey] = [indexItemData, fileData]  # throw
            else:
                assert type(indexItemData) == list
                assert len(indexItemData) > 0
                indexItemData.append(fileData)  # throw

            assert type(filesByStrKeyDictionary[fileKey]) == list
            assert len(filesByStrKeyDictionary[fileKey]) > 1
            assert filesByStrKeyDictionary[fileKey][-1] is fileData

    # --------------------------------------------------------------------
    def Helper__DeleteFileIntoIndex(
        filesByStrKeyDictionary: dict[str, PgCfgModel__FileData],
        fileKey: str,
        fileData: PgCfgModel__FileData,
    ):
        assert type(filesByStrKeyDictionary) == dict
        assert type(fileKey) == str
        assert type(fileData) == PgCfgModel__FileData

        assert fileKey != ""
        assert fileData.IsAlive()

        if not (fileKey in filesByStrKeyDictionary.keys()):
            BugCheckError.FileIsNotFoundInIndex(fileKey, fileData.m_Path)

        indexItemData = filesByStrKeyDictionary[fileKey]

        assert indexItemData is not None

        typeOfIndexItemData = type(indexItemData)

        if typeOfIndexItemData == fileData:
            assert indexItemData is fileData

            if not (indexItemData is fileData):
                BugCheckError.FileIsNotFoundInIndex(fileKey, fileData.m_Path)

            filesByStrKeyDictionary.pop(fileKey)
            assert not (fileKey in filesByStrKeyDictionary.keys())
            return

        if typeOfIndexItemData == list:
            assert type(indexItemData) == list
            assert len(indexItemData) > 1

            for i in range(len(indexItemData)):
                ptr = indexItemData[i]
                assert ptr is not None
                assert type(ptr) == PgCfgModel__FileData

                if ptr is fileData:
                    break

            assert i >= 0
            assert i <= len(indexItemData)

            if i == len(indexItemData):
                BugCheckError.FileIsNotFoundInIndex(fileKey, fileData.m_Path)

            assert type(indexItemData) == list
            assert i < len(indexItemData)
            indexItemData.pop(i)
            assert len(indexItemData) > 0

            if len(indexItemData) == 0:  # it is an abnormal situation
                filesByStrKeyDictionary.pop(fileKey)
            elif len(indexItemData) == 1:
                filesByStrKeyDictionary[fileKey] == indexItemData[0]

            return

        BugCheckError.UnkFileObjectDataType(fileKey, typeOfIndexItemData)

    # --------------------------------------------------------------------
    def Helper__InsertOptionIntoIndex(
        optionsByNameDictionary: dict[str, PgCfgModel__OptionData],
        optionData: PgCfgModel__OptionData,
    ):
        assert optionsByNameDictionary is not None
        assert optionData is not None
        assert type(optionsByNameDictionary) == dict
        assert type(optionData) == PgCfgModel__OptionData

        if not (optionData.m_Name in optionsByNameDictionary.keys()):
            optionsByNameDictionary[optionData.m_Name] = optionData
            return

        data = optionsByNameDictionary[optionData.m_Name]

        typeOfData = type(data)

        if typeOfData == PgCfgModel__OptionData:
            assert data is not optionData
            optionsByNameDictionary[optionData.m_Name] = [data, optionData]
            return

        if typeOfData == list:
            assert type(data) == list
            assert len(data) > 1
            data.append(optionData)
            return

        BugCheckError.UnkOptObjectDataType(optionData.m_Name, typeOfData)

    # --------------------------------------------------------------------
    def Helper__DeleteOptionFromIndex(
        optionsByNameDictionary: dict[str, PgCfgModel__OptionData],
        optionData: PgCfgModel__OptionData,
    ):
        assert optionsByNameDictionary is not None
        assert optionData is not None
        assert type(optionsByNameDictionary) == dict
        assert type(optionData) == PgCfgModel__OptionData

        if not (optionData.m_Name in optionsByNameDictionary.keys()):
            BugCheckError.OptionIsNotFoundInIndex(optionData.m_Name)

        data = optionsByNameDictionary[optionData.m_Name]

        assert data is not None

        typeOfData = type(data)

        if typeOfData == PgCfgModel__OptionData:
            assert data is optionData

            if not (data is optionData):
                BugCheckError.OptionIsNotFoundInIndex(optionData.m_Name)

            optionsByNameDictionary.pop(optionData.m_Name)
            assert not (optionData.m_Name in optionsByNameDictionary.keys())
            return

        if typeOfData == list:
            assert type(data) == list
            assert len(data) > 1

            for i in range(len(data)):
                ptr = data[i]
                assert ptr is not None
                assert type(ptr) == PgCfgModel__OptionData
                assert type(ptr.m_Name) == str
                assert ptr.m_Name == optionData.m_Name

                if ptr is optionData:
                    break

            assert i >= 0
            assert i <= len(data)

            if i == len(data):
                BugCheckError.OptionIsNotFoundInIndex(optionData.m_Name)

            assert type(data) == list
            data.pop(i)
            assert len(data) > 0

            if len(data) == 0:  # an abnormal situation
                optionsByNameDictionary.pop(optionData.m_Name)
            elif len(data) == 1:
                optionsByNameDictionary[optionData.m_Name] = data[0]

            return

        BugCheckError.UnkOptObjectDataType(optionData.m_Name, typeOfData)

    # --------------------------------------------------------------------
    def Helper__ClearFileLine(
        cfgData: PgCfgModel__ConfigurationData, fileLineData: PgCfgModel__FileLineData
    ):
        assert cfgData is not None
        assert fileLineData is not None
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) == list

        cItems = len(fileLineData.m_Items)

        while True:
            if cItems == 0:
                return

            assert cItems > 0
            lastItem = fileLineData.m_Items[-1]
            assert lastItem is not None
            assert isinstance(lastItem.m_Element, PgCfgModel__FileLineElementData)

            __class__.Helper__DeleteElement(cfgData, lastItem.m_Element)

            assert fileLineData.m_Items is not None
            assert type(fileLineData.m_Items) == list

            cItems__new = len(fileLineData.m_Items)

            assert cItems__new == cItems - 1
            cItems = cItems__new

    # --------------------------------------------------------------------
    def Helper__FileLineHasWorkData(fileLineData: PgCfgModel__FileLineData):
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) == list

        for item in fileLineData.m_Items:
            assert item is not None
            assert type(item) == PgCfgModel__FileLineData.tagItem
            assert item.m_Element is not None
            assert isinstance(item.m_Element, PgCfgModel__FileLineElementData)

            typeOfElementData = type(item.m_Element)

            if typeOfElementData == PgCfgModel__OptionData:
                return True

            if typeOfElementData == PgCfgModel__CommentData:
                continue

            if typeOfElementData == PgCfgModel__IncludeData:
                return True

            BugCheckError.UnkObjectDataType(typeOfElementData)

        return False

    # --------------------------------------------------------------------
    def Helper__DeleteElement(
        cfgData: PgCfgModel__ConfigurationData, objectData: PgCfgModel__ObjectData
    ):
        assert cfgData is not None
        assert objectData is not None
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert isinstance(objectData, PgCfgModel__ObjectData)

        typeOfObjectData = type(objectData)

        if typeOfObjectData == PgCfgModel__CommentData:
            return __class__.Helper__DeleteComment(objectData)

        if typeOfObjectData == PgCfgModel__OptionData:
            return __class__.Helper__DeleteOption(cfgData, objectData)

        if typeOfObjectData == PgCfgModel__IncludeData:
            return __class__.Helper__DeleteInclude(objectData)

        BugCheckError.UnkObjectDataType(typeOfObjectData)

    # --------------------------------------------------------------------
    def Helper__DeleteComment(commentData: PgCfgModel__CommentData):
        assert type(commentData) == PgCfgModel__CommentData
        assert commentData.IsAlive()

        # 0.
        fileLineData = None
        iFileLineItem = None

        # 1.1 Set fileLineData
        fileLineData = commentData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 1.2 Set iFileLineItem
        iFileLineItem = __class__.Helper__FindIndexOfFileLineElement(
            fileLineData, commentData
        )

        assert iFileLineItem >= 0
        assert iFileLineItem <= len(fileLineData.m_Items)

        if iFileLineItem == len(fileLineData.m_Items):
            BugCheckError.CommentIsNotFoundInFileLine()

        assert iFileLineItem >= 0
        assert iFileLineItem < len(fileLineData.m_Items)

        # 2. Perform delete operations

        # delete from fileLine
        commentData.MarkAsDeletedFrom(fileLineData)
        assert not commentData.IsAlive()
        fileLineData.m_Items.pop(iFileLineItem)

    # --------------------------------------------------------------------
    def Helper__DeleteOption(
        cfgData: PgCfgModel__ConfigurationData, optionData: PgCfgModel__OptionData
    ):
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(optionData) == PgCfgModel__OptionData
        assert type(optionData.m_Name) == str
        assert optionData.IsAlive()

        # 0.
        fileLineData = None
        iFileLineItem = None
        fileData = None

        # 1.1 Set fileLineData
        fileLineData = optionData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 1.2 Set iFileLineItem
        iFileLineItem = __class__.Helper__FindIndexOfFileLineElement(
            fileLineData, optionData
        )

        assert iFileLineItem >= 0
        assert iFileLineItem <= len(fileLineData.m_Items)

        if iFileLineItem == len(fileLineData.m_Items):
            BugCheckError.OptionIsNotFoundInFileLine(optionData.m_Name)

        assert iFileLineItem >= 0
        assert iFileLineItem < len(fileLineData.m_Items)

        # 1.3 Set fileData
        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert fileData.IsAlive()

        # 1.3
        assert type(fileData.m_OptionsByName) == dict
        assert optionData.m_Name in fileData.m_OptionsByName.keys()

        # 1.4
        assert type(cfgData.m_AllOptionsByName) == dict
        assert optionData.m_Name in cfgData.m_AllOptionsByName.keys()

        # 2. Perform delete operations

        # delete option from global index
        __class__.Helper__DeleteOptionFromIndex(cfgData.m_AllOptionsByName, optionData)

        # delete option from file index
        __class__.Helper__DeleteOptionFromIndex(fileData.m_OptionsByName, optionData)

        # delete from fileLine
        optionData.MarkAsDeletedFrom(fileLineData)
        assert not optionData.IsAlive()
        fileLineData.m_Items.pop(iFileLineItem)

    # --------------------------------------------------------------------
    def Helper__DeleteInclude(includeData: PgCfgModel__IncludeData):
        assert type(includeData) == PgCfgModel__IncludeData
        assert includeData.IsAlive()

        # 0.
        fileLineData = None
        iFileLineItem = None

        # 1.1 Set fileLineData
        fileLineData = includeData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 1.2 Set iFileLineItem
        iFileLineItem = __class__.Helper__FindIndexOfFileLineElement(
            fileLineData, includeData
        )

        assert iFileLineItem >= 0
        assert iFileLineItem <= len(fileLineData.m_Items)

        if iFileLineItem == len(fileLineData.m_Items):
            BugCheckError.IncludeIsNotFoundInFileLine()

        assert iFileLineItem >= 0
        assert iFileLineItem < len(fileLineData.m_Items)

        # 2. Perform delete operations

        # delete from fileLine
        includeData.MarkAsDeletedFrom(fileLineData)
        assert not includeData.IsAlive()
        fileLineData.m_Items.pop(iFileLineItem)

    # --------------------------------------------------------------------
    def Helper__DeleteFileLine(
        cfgData: PgCfgModel__ConfigurationData, fileLineData: PgCfgModel__FileLineData
    ):
        assert type(cfgData) == PgCfgModel__ConfigurationData
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 0.
        fileData = None
        iFileLine = None

        # 1.1 Set fileData
        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert fileData.IsAlive()

        # 1.2 Set iFileLine
        iFileLine = __class__.Helper__FindIndexOfFileLine(fileData, fileLineData)

        assert iFileLine >= 0
        assert iFileLine <= len(fileData.m_Lines)

        if iFileLine == len(fileData.m_Lines):
            BugCheckError.FileLineIsNotFoundInFile()

        assert iFileLine >= 0
        assert iFileLine < len(fileData.m_Lines)

        # 2. Perform cleanup operations
        __class__.Helper__ClearFileLine(cfgData, fileLineData)

        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) == list
        assert len(fileLineData.m_Items) == 0

        # delete from file
        fileLineData.MarkAsDeletedFrom(fileData)
        assert not fileLineData.IsAlive()
        fileData.m_Lines.pop(iFileLine)


# //////////////////////////////////////////////////////////////////////////////
