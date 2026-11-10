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
# class ModelUtils


class ModelUtils:
    @staticmethod
    def Option__set_Value(
        optionData: PgCfgModel__OptionData,
        value: typing.Any,
    ) -> None:
        assert type(optionData) is PgCfgModel__OptionData
        assert value is not None

        optionData.m_Value = value
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Option__add_ValueItem(
        optionData: PgCfgModel__OptionData,
        valueItem: typing.Any,
    ) -> None:
        assert type(optionData) is PgCfgModel__OptionData
        assert type(optionData.m_Value) is list
        assert valueItem is not None

        optionData.m_Value.append(valueItem)
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Option__delete(
        cfgData: PgCfgModel__ConfigurationData,
        optionData: PgCfgModel__OptionData,
        withLine: bool,
    ) -> None:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(optionData) is PgCfgModel__OptionData
        assert type(withLine) is bool

        fileLineData = optionData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData

        __class__.Helper__DeleteOption(
            cfgData,
            optionData,
        )

        if not withLine:
            return

        assert not __class__.Helper__FileLineHasWorkData(fileLineData)

        __class__.Helper__DeleteFileLine(
            cfgData,
            fileLineData,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Include__delete(
        cfgData: PgCfgModel__ConfigurationData,
        includeData: PgCfgModel__IncludeData,
        withLine: bool,
    ) -> None:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(includeData) is PgCfgModel__IncludeData
        assert type(withLine) is bool

        fileLineData = includeData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData

        __class__.Helper__DeleteInclude(includeData)

        if not withLine:
            return

        assert not __class__.Helper__FileLineHasWorkData(fileLineData)

        __class__.Helper__DeleteFileLine(cfgData, fileLineData)
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Comment__delete(
        cfgData: PgCfgModel__ConfigurationData,
        commentData: PgCfgModel__CommentData,
        withLineIfLast: bool,
    ) -> None:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(commentData) is PgCfgModel__CommentData
        assert type(withLineIfLast) is bool

        commentData.IsAlive()

        assert commentData.m_Parent is not None
        assert commentData.m_Parent.m_Parent is not None

        assert cfgData is commentData.m_Parent.m_Parent.m_Parent

        fileLineData = commentData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData

        __class__.Helper__DeleteComment(commentData)

        if not withLineIfLast:
            return

        if len(fileLineData.m_Items) != 0:
            return

        __class__.Helper__DeleteFileLine(
            cfgData,
            fileLineData,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def FileLine__add_Comment(
        fileLineData: PgCfgModel__FileLineData,
        offset: typing.Optional[int],
        text: str,
    ) -> PgCfgModel__CommentData:
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert (offset is None) or (type(offset) is int)
        assert type(text) is str
        assert type(fileLineData.m_Items) is list

        assert fileLineData.IsAlive()

        __class__.Helper__CheckThatWeCanAddCommentToFileLine(fileLineData)

        commentData = PgCfgModel__CommentData(fileLineData, offset, text)
        fileLineDataItem = PgCfgModel__FileLineData.tagItem(commentData)
        fileLineData.m_Items.append(fileLineDataItem)
        return commentData

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CheckThatWeCanAddCommentToFileLine(
        fileLineData: PgCfgModel__FileLineData,
    ) -> None:
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) is list

        assert fileLineData.IsAlive()

        if len(fileLineData.m_Items) == 0:
            return

        lastItem = fileLineData.m_Items[-1]

        assert lastItem is not None
        assert type(lastItem) is PgCfgModel__FileLineData.tagItem
        assert lastItem.m_Element is not None
        assert isinstance(lastItem.m_Element, PgCfgModel__FileLineElementData)

        if type(lastItem.m_Element) is PgCfgModel__OptionData:
            return

        if type(lastItem.m_Element) is PgCfgModel__IncludeData:
            return

        if type(lastItem.m_Element) is PgCfgModel__CommentData:
            RaiseError.FileLineAlreadyHasComment()

        BugCheckError.UnkObjectDataType(type(lastItem.m_Element))

    # --------------------------------------------------------------------
    @staticmethod
    def FileLine__add_Include(
        fileLineData: PgCfgModel__FileLineData,
        filePath: str,
        fileData: PgCfgModel__FileData,
        offset: typing.Optional[int],
    ) -> PgCfgModel__IncludeData:
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(filePath) is str
        assert type(fileData) is PgCfgModel__FileData
        assert filePath != ""
        assert offset is None or type(offset) is int

        assert fileLineData.IsAlive()
        assert fileData.IsAlive()

        __class__.Helper__CheckThatWeCanAddWorkDataToFileLine(fileLineData)

        includeData = PgCfgModel__IncludeData(
            fileLineData,
            offset,
            filePath,
            fileData,
        )
        fileLineDataItem = PgCfgModel__FileLineData.tagItem(
            includeData,
        )
        fileLineData.m_Items.append(
            fileLineDataItem,
        )

        # TODO: Reg include data in a global index?

        return includeData

    # --------------------------------------------------------------------
    @staticmethod
    def FileLine__add_Option(
        cfgData: PgCfgModel__ConfigurationData,
        fileLineData: PgCfgModel__FileLineData,
        optName: str,
        optValue: typing.Any,
        optOffset: typing.Optional[int],
    ) -> PgCfgModel__OptionData:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(optName) is str
        assert optValue is not None
        assert optName != ""
        assert type(fileLineData.m_Items) is list
        assert optOffset is None or type(optOffset) is int

        __class__.Helper__CheckThatWeCanAddWorkDataToFileLine(fileLineData)

        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) is dict

        optionData = PgCfgModel__OptionData(
            fileLineData,
            optOffset,
            optName,
            optValue,
        )
        fileLineDataItem = PgCfgModel__FileLineData.tagItem(
            optionData,
        )
        fileLineData.m_Items.append(
            fileLineDataItem,
        )

        try:
            __class__.Helper__InsertOptionIntoIndex(
                fileData.m_OptionsByName,
                optionData,
            )

            try:
                __class__.Helper__InsertOptionIntoIndex(
                    cfgData.m_AllOptionsByName,
                    optionData,
                )
            except:  # rollback
                __class__.Helper__DeleteOptionFromIndex(
                    fileData.m_OptionsByName,
                    optionData,
                )
                raise
        except:  # rollback
            assert type(fileLineData.m_Items) is list
            assert len(fileLineData.m_Items) > 0
            assert fileLineData.m_Items[-1] is fileLineDataItem
            assert fileLineData.m_Items[-1].m_Element is optionData
            fileLineData.m_Items.pop()
            raise

        return optionData

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CheckThatWeCanAddWorkDataToFileLine(
        fileLineData: PgCfgModel__FileLineData,
    ) -> None:
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) is list

        assert fileLineData.IsAlive()

        if len(fileLineData.m_Items) == 0:
            return

        lastItem = fileLineData.m_Items[-1]

        assert lastItem is not None
        assert type(lastItem) is PgCfgModel__FileLineData.tagItem
        assert lastItem.m_Element is not None
        assert isinstance(lastItem.m_Element, PgCfgModel__FileLineElementData)

        if type(lastItem.m_Element) is PgCfgModel__OptionData:
            RaiseError.FileLineAlreadyHasOption(lastItem.m_Element.m_Name)

        if type(lastItem.m_Element) is PgCfgModel__IncludeData:
            RaiseError.FileLineAlreadyHasIncludeDirective()

        if type(lastItem.m_Element) is PgCfgModel__CommentData:
            RaiseError.FileLineAlreadyHasComment()

        BugCheckError.UnkObjectDataType(type(lastItem.m_Element))

    # --------------------------------------------------------------------
    @staticmethod
    def FileLine__delete(
        cfgData: PgCfgModel__ConfigurationData,
        fileLineData: PgCfgModel__FileLineData,
    ) -> None:
        assert cfgData is not None
        assert fileLineData is not None
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        __class__.Helper__DeleteFileLine(
            cfgData,
            fileLineData,
        )

        assert not fileLineData.IsAlive()
        return

    # --------------------------------------------------------------------
    @staticmethod
    def FileLine__clear(
        cfgData: PgCfgModel__ConfigurationData,
        fileLineData: PgCfgModel__FileLineData,
    ) -> None:
        assert cfgData is not None
        assert fileLineData is not None
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) is list

        return __class__.Helper__ClearFileLine(cfgData, fileLineData)

    # --------------------------------------------------------------------
    @staticmethod
    def File__add_Option(
        cfgData: PgCfgModel__ConfigurationData,
        fileData: PgCfgModel__FileData,
        optName: str,
        optValue: typing.Any,
    ) -> PgCfgModel__OptionData:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(fileData) is PgCfgModel__FileData
        assert type(optName) is str
        assert optValue is not None

        newLineData = ModelUtils.File__add_Line(fileData)  # raise

        assert type(newLineData) is PgCfgModel__FileLineData

        try:
            optionData = __class__.FileLine__add_Option(
                cfgData,
                newLineData,
                optName,
                optValue,
                None,
            )  # raise

            assert type(optionData) is PgCfgModel__OptionData
            assert optionData.m_Name == optName
        except:
            ModelUtils.FileLine__delete(
                cfgData,
                newLineData,
            )
            raise

        assert optionData is not None
        assert type(optionData) is PgCfgModel__OptionData
        assert optionData.IsAlive()
        return optionData

    # --------------------------------------------------------------------
    @staticmethod
    def File__add_Line(
        fileData: PgCfgModel__FileData,
    ) -> PgCfgModel__FileLineData:
        assert type(fileData) is PgCfgModel__FileData
        assert type(fileData.m_Lines) is list

        lineData = PgCfgModel__FileLineData(fileData)
        fileData.m_Lines.append(lineData)
        return lineData

    # --------------------------------------------------------------------
    @staticmethod
    def Cfg__CreateAndAddTopLevelFile__AUTO(
        cfgData: PgCfgModel__ConfigurationData,
        file_name: str,
    ) -> PgCfgModel__FileData:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(cfgData.m_Files) is list
        assert type(cfgData.m_AllFilesByName) is dict
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(file_name) is str
        assert file_name != ""
        assert cfgData.OsOps.Path_BaseName(file_name) == file_name

        newFilePath = cfgData.OsOps.Path_Join(
            cfgData.m_DataDir,
            file_name,
        )
        newFilePath = cfgData.OsOps.Path_NormPath(
            newFilePath,
        )

        assert type(newFilePath) is str
        assert newFilePath != ""

        return __class__.Helper__FinishCreateTopLevelFile(
            cfgData,
            newFilePath,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Cfg__CreateAndAddTopLevelFile__USER(
        cfgData: PgCfgModel__ConfigurationData,
        path: str,
    ) -> PgCfgModel__FileData:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(cfgData.m_Files) is list
        assert type(cfgData.m_AllFilesByName) is dict
        assert type(path) is str
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert path != ""

        newFilePath = Helpers.NormalizeFilePath(
            cfgData.OsOps,
            cfgData.m_DataDir,
            path,
        )

        assert type(newFilePath) is str
        assert newFilePath != ""

        # TODO: use index
        for fileData in cfgData.m_AllFilesByName.values():
            assert fileData is not None
            assert type(fileData) is PgCfgModel__FileData
            assert fileData.IsAlive()

            if fileData.m_Path == newFilePath:
                RaiseError.FileIsAlreadyRegistered(newFilePath)

            continue

        return __class__.Helper__FinishCreateTopLevelFile(
            cfgData,
            newFilePath,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Cfg__GetOrCreateFile__USER(
        cfgData: PgCfgModel__ConfigurationData,
        baseFolder: str,
        path: str,
    ) -> PgCfgModel__FileData:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(cfgData.m_Files) is list
        assert type(cfgData.m_AllFilesByName) is dict
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(baseFolder) is str
        assert type(path) is str
        assert path != ""

        newFilePath = Helpers.NormalizeFilePath(
            cfgData.OsOps,
            baseFolder,
            path,
        )

        assert type(newFilePath) is str
        assert newFilePath != ""

        # TODO: use index
        for fileData in cfgData.m_AllFilesByName.values():
            assert fileData is not None
            assert type(fileData) is PgCfgModel__FileData
            assert fileData.IsAlive()

            if fileData.m_Path == newFilePath:
                return fileData

            continue

        newFileData = PgCfgModel__FileData(
            cfgData,
            newFilePath,
        )

        __class__.Helper__RegFileInCfgData(
            cfgData,
            newFileData,
        )  # raise

        return newFileData

    # Helper methods -----------------------------------------------------
    @staticmethod
    def Helper__FinishCreateTopLevelFile(
        cfgData: PgCfgModel__ConfigurationData,
        newFilePath: str,
    ) -> PgCfgModel__FileData:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(newFilePath) is str

        newFileData = PgCfgModel__FileData(
            cfgData,
            newFilePath,
        )

        __class__.Helper__RegFileInCfgData(
            cfgData,
            newFileData,
        )  # raise

        try:
            cfgData.m_Files.append(newFileData)  # raise
        except:
            __class__.Helper__UnRegFileFromCfgData(
                cfgData,
                newFileData,
            )
            raise

        return newFileData

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FindIndexOfFileLine(
        fileData: PgCfgModel__FileData,
        fileLineData: PgCfgModel__FileLineData,
    ) -> int:
        assert fileData is not None
        assert fileLineData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert type(fileData.m_Lines) is list
        assert type(fileLineData) is PgCfgModel__FileLineData

        cFileLines = len(fileData.m_Lines)

        iFileLine = 0

        while iFileLine != cFileLines:
            ptr = fileData.m_Lines[iFileLine]
            assert ptr is not None
            assert type(ptr) is PgCfgModel__FileLineData
            assert ptr.m_Parent is fileData

            if ptr is fileLineData:
                return iFileLine

            iFileLine += 1
            continue

        assert iFileLine == cFileLines
        return iFileLine

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FindIndexOfFileLineElement(
        fileLineData: PgCfgModel__FileLineData,
        elementData: PgCfgModel__FileLineElementData,
    ) -> int:
        assert fileLineData is not None
        assert elementData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert type(fileLineData.m_Items) is list
        assert isinstance(elementData, PgCfgModel__FileLineElementData)

        cItems = len(fileLineData.m_Items)

        iItem = 0

        while iItem != cItems:
            ptr = fileLineData.m_Items[iItem]
            assert ptr is not None
            assert type(ptr) is PgCfgModel__FileLineData.tagItem
            assert ptr.m_Element is not None

            if ptr.m_Element is elementData:
                return iItem

            iItem += 1
            continue

        assert iItem == cItems
        return iItem

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__RegFileInCfgData(
        cfgData: PgCfgModel__ConfigurationData,
        fileData: PgCfgModel__FileData,
    ) -> None:
        assert cfgData is not None
        assert fileData is not None
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(fileData) is PgCfgModel__FileData
        assert type(fileData.m_Path) is str
        assert fileData.m_Path != ""

        assert fileData.IsAlive()

        fileName = cfgData.OsOps.Path_BaseName(fileData.m_Path)
        assert type(fileName) is str
        assert fileName != ""

        __class__.Helper__InsertFileIntoIndex(
            cfgData.m_AllFilesByName,
            fileName,
            fileData,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__UnRegFileFromCfgData(
        cfgData: PgCfgModel__ConfigurationData,
        fileData: PgCfgModel__FileData,
    ) -> None:
        assert cfgData is not None
        assert fileData is not None
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert isinstance(cfgData.OsOps, ConfigurationOsOps)
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.m_Path != ""

        assert fileData.IsAlive()

        fileName = cfgData.OsOps.Path_BaseName(fileData.m_Path)
        assert type(fileName) is str
        assert fileName != ""

        __class__.Helper__DeleteFileIntoIndex(
            cfgData.m_AllFilesByName,
            fileName,
            fileData,
        )
        return

    # --------------------------------------------------------------------
    T_FILE_OR_FILES = typing.Union[
        PgCfgModel__FileData,
        typing.List[PgCfgModel__FileData],
    ]

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__InsertFileIntoIndex(
        filesByStrKeyDictionary: typing.Dict[str, T_FILE_OR_FILES],
        fileKey: str,
        fileData: PgCfgModel__FileData,
    ) -> None:
        assert type(filesByStrKeyDictionary) is dict
        assert type(fileKey) is str
        assert type(fileData) is PgCfgModel__FileData

        assert fileKey != ""
        assert fileData.IsAlive()

        if fileKey not in filesByStrKeyDictionary.keys():
            filesByStrKeyDictionary[fileKey] = fileData
            return

        # TODO: it is not tested
        indexItemData = filesByStrKeyDictionary[fileKey]

        if type(indexItemData) is PgCfgModel__FileData:
            assert indexItemData is not fileData
            filesByStrKeyDictionary[fileKey] = [
                indexItemData,
                fileData,
            ]
            return

        if type(indexItemData) is list:
            assert type(indexItemData) is list
            assert len(indexItemData) > 0
            indexItemData.append(fileData)  # throw
            return

        BugCheckError.UnkFileObjectDataType(
            fileKey,
            type(indexItemData),
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteFileIntoIndex(
        filesByStrKeyDictionary: typing.Dict[str, T_FILE_OR_FILES],
        fileKey: str,
        fileData: PgCfgModel__FileData,
    ) -> None:
        assert type(filesByStrKeyDictionary) is dict
        assert type(fileKey) is str
        assert type(fileData) is PgCfgModel__FileData

        assert fileKey != ""
        assert fileData.IsAlive()

        if fileKey not in filesByStrKeyDictionary.keys():
            BugCheckError.FileIsNotFoundInIndex(
                fileKey,
                fileData.m_Path,
            )

        indexItemData = filesByStrKeyDictionary[fileKey]

        assert indexItemData is not None

        if type(indexItemData) is PgCfgModel__FileData:
            assert indexItemData is fileData

            if indexItemData is not fileData:
                BugCheckError.FileIsNotFoundInIndex(
                    fileKey,
                    fileData.m_Path,
                )

            filesByStrKeyDictionary.pop(fileKey)
            assert fileKey not in filesByStrKeyDictionary.keys()
            return

        if type(indexItemData) is list:
            assert type(indexItemData) is list
            assert len(indexItemData) > 1

            i = 0

            while i != len(indexItemData):
                ptr = indexItemData[i]
                assert ptr is not None
                assert type(ptr) is PgCfgModel__FileData

                if ptr is fileData:
                    break

                i += 1
                continue

            assert i >= 0
            assert i <= len(indexItemData)

            if i == len(indexItemData):
                BugCheckError.FileIsNotFoundInIndex(
                    fileKey,
                    fileData.m_Path,
                )

            assert type(indexItemData) is list
            assert i < len(indexItemData)
            indexItemData.pop(i)
            assert len(indexItemData) > 0

            if len(indexItemData) == 0:  # it is an abnormal situation
                filesByStrKeyDictionary.pop(fileKey)
            elif len(indexItemData) == 1:
                filesByStrKeyDictionary[fileKey] = indexItemData[0]

            return

        BugCheckError.UnkFileObjectDataType(
            fileKey,
            type(indexItemData),
        )

    # --------------------------------------------------------------------
    T_OPTION_OR_OPTIONS = typing.Union[
        PgCfgModel__OptionData,
        typing.List[PgCfgModel__OptionData],
    ]

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__InsertOptionIntoIndex(
        optionsByNameDictionary: typing.Dict[str, T_OPTION_OR_OPTIONS],
        optionData: PgCfgModel__OptionData,
    ) -> None:
        assert optionsByNameDictionary is not None
        assert optionData is not None
        assert type(optionsByNameDictionary) is dict
        assert type(optionData) is PgCfgModel__OptionData

        if optionData.m_Name not in optionsByNameDictionary.keys():
            optionsByNameDictionary[optionData.m_Name] = optionData
            return

        # TODO: it is not tested

        indexItemData = optionsByNameDictionary[optionData.m_Name]

        if type(indexItemData) is PgCfgModel__OptionData:
            assert indexItemData is not optionData
            optionsByNameDictionary[optionData.m_Name] = [
                indexItemData,
                optionData,
            ]
            return

        if type(indexItemData) is list:
            assert type(indexItemData) is list
            assert len(indexItemData) > 1
            indexItemData.append(optionData)
            return

        BugCheckError.UnkOptObjectDataType(
            optionData.m_Name,
            type(indexItemData),
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteOptionFromIndex(
        optionsByNameDictionary: typing.Dict[str, T_OPTION_OR_OPTIONS],
        optionData: PgCfgModel__OptionData,
    ) -> None:
        assert optionsByNameDictionary is not None
        assert optionData is not None
        assert type(optionsByNameDictionary) is dict
        assert type(optionData) is PgCfgModel__OptionData

        if optionData.m_Name not in optionsByNameDictionary.keys():
            BugCheckError.OptionIsNotFoundInIndex(optionData.m_Name)

        indexItemData = optionsByNameDictionary[optionData.m_Name]

        assert indexItemData is not None

        if type(indexItemData) is PgCfgModel__OptionData:
            assert indexItemData is optionData

            if indexItemData is not optionData:
                BugCheckError.OptionIsNotFoundInIndex(optionData.m_Name)

            optionsByNameDictionary.pop(optionData.m_Name)
            assert optionData.m_Name not in optionsByNameDictionary.keys()
            return

        if type(indexItemData) is list:
            assert len(indexItemData) > 1

            i = 0
            while i != len(indexItemData):
                ptr = indexItemData[i]
                assert ptr is not None
                assert type(ptr) is PgCfgModel__OptionData
                assert type(ptr.m_Name) is str
                assert ptr.m_Name == optionData.m_Name

                if ptr is optionData:
                    break

                i += 1
                continue

            assert i >= 0
            assert i <= len(indexItemData)

            if i == len(indexItemData):
                BugCheckError.OptionIsNotFoundInIndex(optionData.m_Name)

            indexItemData.pop(i)
            assert len(indexItemData) > 0

            if len(indexItemData) == 0:  # an abnormal situation
                optionsByNameDictionary.pop(optionData.m_Name)
            elif len(indexItemData) == 1:
                optionsByNameDictionary[optionData.m_Name] = indexItemData[0]

            return

        BugCheckError.UnkOptObjectDataType(
            optionData.m_Name,
            type(indexItemData),
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ClearFileLine(
        cfgData: PgCfgModel__ConfigurationData,
        fileLineData: PgCfgModel__FileLineData,
    ) -> None:
        assert cfgData is not None
        assert fileLineData is not None
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) is list

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
            assert type(fileLineData.m_Items) is list

            cItems__new = len(fileLineData.m_Items)

            assert cItems__new == cItems - 1
            cItems = cItems__new
            continue

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FileLineHasWorkData(
        fileLineData: PgCfgModel__FileLineData,
    ) -> bool:
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) is list

        for item in fileLineData.m_Items:
            assert item is not None
            assert type(item) is PgCfgModel__FileLineData.tagItem
            assert item.m_Element is not None
            assert isinstance(item.m_Element, PgCfgModel__FileLineElementData)

            if type(item.m_Element) is PgCfgModel__OptionData:
                return True

            if type(item.m_Element) is PgCfgModel__CommentData:
                continue

            if type(item.m_Element) is PgCfgModel__IncludeData:
                return True

            BugCheckError.UnkObjectDataType(type(item.m_Element))

        return False

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteElement(
        cfgData: PgCfgModel__ConfigurationData,
        objectData: PgCfgModel__ObjectData,
    ) -> None:
        assert cfgData is not None
        assert objectData is not None
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert isinstance(objectData, PgCfgModel__ObjectData)

        if type(objectData) is PgCfgModel__CommentData:
            return __class__.Helper__DeleteComment(objectData)

        if type(objectData) is PgCfgModel__OptionData:
            return __class__.Helper__DeleteOption(cfgData, objectData)

        if type(objectData) is PgCfgModel__IncludeData:
            return __class__.Helper__DeleteInclude(objectData)

        BugCheckError.UnkObjectDataType(type(objectData))

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteComment(
        commentData: PgCfgModel__CommentData,
    ) -> None:
        assert type(commentData) is PgCfgModel__CommentData
        assert commentData.IsAlive()

        # 0.
        fileLineData = None
        iFileLineItem = None

        # 1.1 Set fileLineData
        fileLineData = commentData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 1.2 Set iFileLineItem
        iFileLineItem = __class__.Helper__FindIndexOfFileLineElement(
            fileLineData,
            commentData,
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
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteOption(
        cfgData: PgCfgModel__ConfigurationData,
        optionData: PgCfgModel__OptionData,
    ) -> None:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(optionData) is PgCfgModel__OptionData
        assert type(optionData.m_Name) is str
        assert optionData.IsAlive()

        # 0.
        fileLineData = None
        iFileLineItem = None
        fileData = None

        # 1.1 Set fileLineData
        fileLineData = optionData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 1.2 Set iFileLineItem
        iFileLineItem = __class__.Helper__FindIndexOfFileLineElement(
            fileLineData,
            optionData,
        )

        assert iFileLineItem >= 0
        assert iFileLineItem <= len(fileLineData.m_Items)

        if iFileLineItem == len(fileLineData.m_Items):
            BugCheckError.OptionIsNotFoundInFileLine(
                optionData.m_Name,
            )

        assert iFileLineItem >= 0
        assert iFileLineItem < len(fileLineData.m_Items)

        # 1.3 Set fileData
        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.IsAlive()

        # 1.3
        assert type(fileData.m_OptionsByName) is dict
        assert optionData.m_Name in fileData.m_OptionsByName.keys()

        # 1.4
        assert type(cfgData.m_AllOptionsByName) is dict
        assert optionData.m_Name in cfgData.m_AllOptionsByName.keys()

        # 2. Perform delete operations

        # delete option from global index
        __class__.Helper__DeleteOptionFromIndex(
            cfgData.m_AllOptionsByName,
            optionData,
        )

        # delete option from file index
        __class__.Helper__DeleteOptionFromIndex(
            fileData.m_OptionsByName,
            optionData,
        )

        # delete from fileLine
        optionData.MarkAsDeletedFrom(fileLineData)
        assert not optionData.IsAlive()
        fileLineData.m_Items.pop(iFileLineItem)
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteInclude(
        includeData: PgCfgModel__IncludeData,
    ) -> None:
        assert type(includeData) is PgCfgModel__IncludeData
        assert includeData.IsAlive()

        # 0.
        fileLineData = None
        iFileLineItem = None

        # 1.1 Set fileLineData
        fileLineData = includeData.m_Parent
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 1.2 Set iFileLineItem
        iFileLineItem = __class__.Helper__FindIndexOfFileLineElement(
            fileLineData,
            includeData,
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
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DeleteFileLine(
        cfgData: PgCfgModel__ConfigurationData,
        fileLineData: PgCfgModel__FileLineData,
    ) -> None:
        assert type(cfgData) is PgCfgModel__ConfigurationData
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()

        # 0.
        fileData = None
        iFileLine = None

        # 1.1 Set fileData
        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.IsAlive()

        # 1.2 Set iFileLine
        iFileLine = __class__.Helper__FindIndexOfFileLine(
            fileData,
            fileLineData,
        )

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
        assert type(fileLineData.m_Items) is list
        assert len(fileLineData.m_Items) == 0

        # delete from file
        fileLineData.MarkAsDeletedFrom(fileData)
        assert not fileLineData.IsAlive()
        fileData.m_Lines.pop(iFileLine)
        return


# //////////////////////////////////////////////////////////////////////////////
