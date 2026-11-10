# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from .model_s_multi_index import MultiIndex
from .raise_error import RaiseError

from ..os.abstract.configuration_os_ops import ConfigurationOsOps

import typing
import enum
import datetime

# //////////////////////////////////////////////////////////////////////////////
# ObjectData


class ObjectData:
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def get_Parent(self) -> typing.Optional[ObjectData]:
        RaiseError.MethodIsNotImplemented(__class__, "get_Parent")

    def IsAlive(self) -> bool:
        RaiseError.MethodIsNotImplemented(__class__, "IsAlive")


# //////////////////////////////////////////////////////////////////////////////
# FileLineElementData


class FileLineElementData(ObjectData):
    m_Parent: typing.Optional[FileLineData]
    m_Offset: typing.Optional[int]

    # --------------------------------------------------------------------
    def __init__(self, parent: FileLineData, offset: typing.Optional[int]):
        assert type(parent) is FileLineData
        assert offset is None or type(offset) is int

        super().__init__()

        self.m_Parent = parent
        self.m_Offset = offset
        return

    # own interface ------------------------------------------------------
    def MarkAsDeletedFrom(self, fileLineData: FileLineData) -> None:
        assert fileLineData is not None
        assert isinstance(fileLineData, FileLineData)
        assert self.m_Parent is fileLineData
        self.m_Parent = None
        return

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> FileLineData:
        assert type(self.m_Parent) is FileLineData
        return self.m_Parent

    # --------------------------------------------------------------------
    def IsAlive(self) -> bool:
        if self.m_Parent is None:
            return False

        return self.m_Parent.IsAlive()


# //////////////////////////////////////////////////////////////////////////////
# CommentData


class CommentData(FileLineElementData):
    m_Text: str

    # --------------------------------------------------------------------
    def __init__(self, parent: FileLineData, offset: typing.Optional[int], text: str):
        assert type(parent) is FileLineData
        assert offset is None or type(offset) is int
        assert type(text) is str

        super().__init__(parent, offset)

        self.m_Text = text
        return


# //////////////////////////////////////////////////////////////////////////////
# OptionData


class OptionData(FileLineElementData):
    m_Name: str
    m_Value: typing.Any

    # --------------------------------------------------------------------
    def __init__(
        self,
        parent: FileLineData,
        offset: typing.Optional[int],
        name: str,
        value: typing.Any,
    ):
        assert type(parent) is FileLineData
        assert offset is None or type(offset) is int
        assert type(name) is str
        assert value is not None
        assert name != ""

        super().__init__(parent, offset)

        self.m_Name = name
        self.m_Value = value
        return


# //////////////////////////////////////////////////////////////////////////////


T_OPTIONS_INDEX = MultiIndex[OptionData]


# //////////////////////////////////////////////////////////////////////////////
# IncludeData


class IncludeData(FileLineElementData):
    m_Path: str
    m_File: FileData

    # --------------------------------------------------------------------
    def __init__(
        self,
        parent: FileLineData,
        offset: typing.Optional[int],
        path: str,
        fileData: FileData,
    ):
        assert type(parent) is FileLineData
        assert type(path) is str
        assert type(fileData) is FileData
        assert offset is None or type(offset) is int

        assert parent.IsAlive()
        assert fileData.IsAlive()

        assert fileData.get_Parent() is parent.get_Parent().get_Parent()

        super().__init__(parent, offset)

        self.m_Path = path
        self.m_File = fileData
        return


# //////////////////////////////////////////////////////////////////////////////
# FileLineData


class FileLineData(ObjectData):
    class tagItem:
        m_Element: FileLineElementData

        # ----------------------------------------------------------------
        def __init__(self, element: FileLineElementData):
            assert isinstance(element, FileLineElementData)

            self.m_Element = element
            return

    # --------------------------------------------------------------------
    m_Parent: typing.Optional[FileData]
    m_Items: typing.List[tagItem]

    # --------------------------------------------------------------------
    def __init__(self, parent: FileData):
        assert type(parent) is FileData

        super().__init__()

        self.m_Parent = parent
        self.m_Items = list()
        return

    # own interface ------------------------------------------------------
    def MarkAsDeletedFrom(self, fileData: FileData) -> None:
        assert fileData is not None
        assert isinstance(fileData, FileData)
        assert self.m_Parent is fileData
        self.m_Parent = None

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> FileData:
        assert type(self.m_Parent) is FileData
        return self.m_Parent

    # --------------------------------------------------------------------
    def IsAlive(self) -> bool:
        if self.m_Parent is None:
            return False

        return self.m_Parent.IsAlive()


# //////////////////////////////////////////////////////////////////////////////
# FileStatus


class FileStatus(enum.Enum):
    IS_NEW = 0
    EXISTS = 1


# //////////////////////////////////////////////////////////////////////////////
# FileData


class FileData(ObjectData):
    m_Parent: ConfigurationData

    m_Status: FileStatus
    m_LastModifiedTimestamp: typing.Optional[datetime.datetime]

    m_Path: str
    m_Lines: typing.List[FileLineData]

    m_OptionsByName: T_OPTIONS_INDEX

    # --------------------------------------------------------------------
    def __init__(self, parent: ConfigurationData, path: str):
        assert type(parent) is ConfigurationData
        assert type(path) is str
        assert parent.OsOps.Path_IsAbs(path)
        assert parent.OsOps.Path_NormPath(path) == path
        assert parent.OsOps.Path_NormCase(path) == path

        super().__init__()

        self.m_Parent = parent

        self.m_Status = FileStatus.IS_NEW
        self.m_LastModifiedTimestamp = None

        self.m_Path = path
        self.m_Lines = list()

        self.m_OptionsByName = MultiIndex()
        assert type(self.m_OptionsByName) is MultiIndex

        assert type(self.m_Path) is str
        assert self.m_Path != ""
        return

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> ConfigurationData:
        assert type(self.m_Parent) is ConfigurationData
        return self.m_Parent

    # --------------------------------------------------------------------
    def IsAlive(self) -> bool:
        if self.m_Parent is None:
            return False

        return self.m_Parent.IsAlive()


# //////////////////////////////////////////////////////////////////////////////


T_FILES_INDEX = MultiIndex[FileData]


# //////////////////////////////////////////////////////////////////////////////
# ConfigurationData


class ConfigurationData(ObjectData):
    m_DataDir: str
    m_OsOps: ConfigurationOsOps

    m_Files: typing.List[FileData]

    m_AllOptionsByName: T_OPTIONS_INDEX
    m_AllFilesByName: T_FILES_INDEX

    # --------------------------------------------------------------------
    def __init__(self, data_dir: str, osOps: ConfigurationOsOps):
        assert type(data_dir) is str
        assert isinstance(osOps, ConfigurationOsOps)

        super().__init__()

        self.m_DataDir = data_dir
        self.m_OsOps = osOps

        self.m_Files = list()
        self.m_AllOptionsByName = MultiIndex()
        self.m_AllFilesByName = MultiIndex()

        assert type(self.m_Files) is list
        assert type(self.m_AllOptionsByName) is MultiIndex
        assert type(self.m_AllFilesByName) is MultiIndex
        return

    # Own interface ------------------------------------------------------
    @property
    def OsOps(self) -> ConfigurationOsOps:
        assert isinstance(self.m_OsOps, ConfigurationOsOps)
        return self.m_OsOps

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> typing.Optional[FileData]:
        return None

    # --------------------------------------------------------------------
    def IsAlive(self) -> bool:
        return True


# //////////////////////////////////////////////////////////////////////////////
