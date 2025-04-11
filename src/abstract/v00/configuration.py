# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ...core.raise_error import RaiseError

import typing
import enum

# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationObject


class PostgresConfigurationObject:
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration:
        RaiseError.MethodIsNotImplemented(__class__, "get_Configuration")

    # --------------------------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationObject:
        RaiseError.MethodIsNotImplemented(__class__, "get_Parent")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationSetOptionValueEventID


class PostgresConfigurationSetOptionValueEventID(enum.Enum):
    NONE = 0
    OPTION_WAS_UPDATED = 1
    OPTION_WAS_ADDED = 2
    OPTION_WAS_DELETED = 3

    VALUE_ITEM_WAS_ALREADY_DEFINED = 4
    VALUE_ITEM_WAS_ADDED = 5


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationSetOptionValueResult


class PostgresConfigurationSetOptionValueResult:
    def __init__(self):
        pass

    # interface -----------------------------------------------------------
    @property
    def Option(self) -> PostgresConfigurationOption:
        RaiseError.GetPropertyIsNotImplemented(__class__, "Option")

    # ---------------------------------------------------------------------
    @property
    def EventID(self) -> PostgresConfigurationSetOptionValueEventID:
        RaiseError.GetPropertyIsNotImplemented(__class__, "EventID")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationElement


class PostgresConfigurationElement(PostgresConfigurationObject):
    def __init__(self):
        super().__init__()


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationComment


class PostgresConfigurationComment(PostgresConfigurationElement):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def get_Text(self) -> str:
        RaiseError.MethodIsNotImplemented(__class__, "get_Text")

    # --------------------------------------------------------------------
    def Delete(self, withLineIfLast: bool):
        assert type(withLineIfLast) == bool
        RaiseError.MethodIsNotImplemented(__class__, "Delete")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationOption


class PostgresConfigurationOption(PostgresConfigurationElement):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def get_Name(self) -> str:
        RaiseError.MethodIsNotImplemented(__class__, "get_Name")

    # --------------------------------------------------------------------
    def get_Value(self) -> any:
        RaiseError.MethodIsNotImplemented(__class__, "get_Value")

    # --------------------------------------------------------------------
    def set_Value(self, value: any) -> PostgresConfigurationSetOptionValueResult:
        RaiseError.MethodIsNotImplemented(__class__, "set_Value")

    # --------------------------------------------------------------------
    def set_ValueItem(
        self, value_item: any
    ) -> PostgresConfigurationSetOptionValueResult:
        assert value_item is not None
        RaiseError.MethodIsNotImplemented(__class__, "set_ValueItem")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationOptionsIterator


class PostgresConfigurationOptionsIterator(
    typing.Iterator[PostgresConfigurationOption]
):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationOptionsIterator:
        RaiseError.MethodIsNotImplemented(__class__, "__iter__")

    def __next__(self) -> PostgresConfigurationOption:
        RaiseError.MethodIsNotImplemented(__class__, "__next__")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationOptions


class PostgresConfigurationOptions(typing.Iterable[PostgresConfigurationOption]):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        RaiseError.MethodIsNotImplemented(__class__, "__len__")

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFileLinesIterator:
        RaiseError.MethodIsNotImplemented(__class__, "__iter__")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationInclude


class PostgresConfigurationInclude(PostgresConfigurationElement):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def get_File(self) -> PostgresConfigurationFile:
        RaiseError.MethodIsNotImplemented(__class__, "get_File")

    # --------------------------------------------------------------------
    def Delete(self, withLine: bool):
        assert type(withLine) == bool
        RaiseError.MethodIsNotImplemented(__class__, "Delete")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLine


class PostgresConfigurationFileLine(PostgresConfigurationObject):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        RaiseError.MethodIsNotImplemented(__class__, "__len__")

    # --------------------------------------------------------------------
    def AddComment(
        self, text: str, offset: typing.Optional[int]
    ) -> PostgresConfigurationComment:
        assert type(text) == str
        assert (offset is None) or (type(offset) == int)
        RaiseError.MethodIsNotImplemented(__class__, "AddComment")

    # --------------------------------------------------------------------
    def AddOption(
        self, name: str, value: any, offset: typing.Optional[int]
    ) -> PostgresConfigurationOption:
        assert type(name) == str
        assert name != ""
        assert value is not None
        assert (offset is None) or (type(offset) == int)
        RaiseError.MethodIsNotImplemented(__class__, "AddOption")

    # --------------------------------------------------------------------
    def AddInclude(
        self, path: str, offset: typing.Optional[int]
    ) -> PostgresConfigurationInclude:
        assert type(path) == str
        assert path != ""
        assert (offset is None) or (type(offset) == int)
        RaiseError.MethodIsNotImplemented(__class__, "AddInclude")

    # --------------------------------------------------------------------
    def Clear(self) -> None:
        RaiseError.MethodIsNotImplemented(__class__, "Clear")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLinesIterator


class PostgresConfigurationFileLinesIterator(
    typing.Iterator[PostgresConfigurationFileLine]
):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFileLinesIterator:
        RaiseError.MethodIsNotImplemented(__class__, "__iter__")

    def __next__(self) -> PostgresConfigurationFileLine:
        RaiseError.MethodIsNotImplemented(__class__, "__next__")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLines


class PostgresConfigurationFileLines(typing.Iterable[PostgresConfigurationFileLine]):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        RaiseError.MethodIsNotImplemented(__class__, "__len__")

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFileLinesIterator:
        RaiseError.MethodIsNotImplemented(__class__, "__iter__")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFile


class PostgresConfigurationFile(PostgresConfigurationObject):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        RaiseError.MethodIsNotImplemented(__class__, "__len__")

    # --------------------------------------------------------------------
    def get_Path(self) -> str:
        RaiseError.MethodIsNotImplemented(__class__, "get_Path")

    # --------------------------------------------------------------------
    def get_Lines(self) -> PostgresConfigurationFileLines:
        RaiseError.MethodIsNotImplemented(__class__, "get_Lines")

    # --------------------------------------------------------------------
    def AddEmptyLine(self) -> PostgresConfigurationFileLine:
        RaiseError.MethodIsNotImplemented(__class__, "AddEmptyLine")

    # --------------------------------------------------------------------
    def AddComment(self, text: str) -> PostgresConfigurationComment:
        assert type(text) == str
        RaiseError.MethodIsNotImplemented(__class__, "AddComment")

    # --------------------------------------------------------------------
    def AddOption(self, name: str, value: any) -> PostgresConfigurationOption:
        assert type(name) == str
        assert name != ""
        assert value is not None
        RaiseError.MethodIsNotImplemented(__class__, "AddOption")

    # --------------------------------------------------------------------
    def AddInclude(self, path: str) -> PostgresConfigurationInclude:
        assert type(path) == str
        assert path != ""
        RaiseError.MethodIsNotImplemented(__class__, "AddInclude")

    # --------------------------------------------------------------------
    #
    # Method for inserting, updating and deleting of an option.
    #
    # It finds a suitable file or uses/creates default file (auto.conf).
    #
    # Set of None will delete an option from all files.
    #
    # Return:
    #  PostgresConfigurationSetOptionValueResult object.
    #
    def SetOptionValue(
        self, name: str, value: any
    ) -> PostgresConfigurationSetOptionValueResult:
        assert type(name) == str
        assert name != ""
        RaiseError.MethodIsNotImplemented(__class__, "SetOptionValue")

    # --------------------------------------------------------------------
    #
    # Method for getting a value of option.
    #
    # Return:
    #  - Value of option.
    #  - None if option is not found in this file.
    #
    def GetOptionValue(self, name: str) -> any:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(__class__, "GetOptionValue")

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        self, name: str, value_item: any
    ) -> PostgresConfigurationSetOptionValueResult:
        assert type(name) == str
        assert name != ""
        assert value_item is not None
        RaiseError.MethodIsNotImplemented(__class__, "SetOptionValueItem")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFilesIterator


class PostgresConfigurationFilesIterator(typing.Iterator[PostgresConfigurationFile]):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFilesIterator:
        RaiseError.MethodIsNotImplemented(__class__, "__iter__")

    def __next__(self) -> PostgresConfigurationFile:
        RaiseError.MethodIsNotImplemented(__class__, "__next__")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFiles


class PostgresConfigurationFiles(typing.Iterable[PostgresConfigurationFile]):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        RaiseError.MethodIsNotImplemented(__class__, "__len__")

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFilesIterator:
        RaiseError.MethodIsNotImplemented(__class__, "__iter__")

    # --------------------------------------------------------------------
    def GetFileByName(self, file_name: str) -> PostgresConfigurationFile:
        assert file_name is not None
        RaiseError.MethodIsNotImplemented(__class__, "GetFileByName")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration


class PostgresConfiguration(PostgresConfigurationObject):
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def AddTopLevelFile(self, path: str) -> PostgresConfigurationFile:
        assert type(path) == str
        assert path != ""
        RaiseError.MethodIsNotImplemented(__class__, "AddTopLevelFile")

    # --------------------------------------------------------------------
    def AddOption(self, name: str, value: any) -> PostgresConfigurationOption:
        assert type(name) == str
        assert name != ""
        assert value is not None
        RaiseError.MethodIsNotImplemented(__class__, "AddOption")

    # --------------------------------------------------------------------
    #
    # Method for inserting, updating and deleting of an option.
    #
    # It finds a suitable file or uses/creates default file (auto.conf).
    #
    # Set of None will delete an option from all files.
    #
    # Return:
    #  PostgresConfigurationSetOptionValueResult object.
    #
    def SetOptionValue(
        self, name: str, value: any
    ) -> PostgresConfigurationSetOptionValueResult:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(__class__, "SetOptionValue")

    # --------------------------------------------------------------------
    #
    # Method for getting a value of option.
    #
    # Return:
    #  - Value of option.
    #  - None if option is not found.
    #
    def GetOptionValue(self, name: str) -> any:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(__class__, "GetOptionValue")

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        self, name: str, value_item: any
    ) -> PostgresConfigurationSetOptionValueResult:
        assert type(name) == str
        assert value_item is not None
        RaiseError.MethodIsNotImplemented(__class__, "SetOptionValueItem")

    # --------------------------------------------------------------------
    def get_AllFiles(self) -> PostgresConfigurationFiles:
        RaiseError.MethodIsNotImplemented(__class__, "get_AllFiles")

    # --------------------------------------------------------------------
    def get_AllOptions(self) -> PostgresConfigurationOptions:
        RaiseError.GetPropertyIsNotImplemented(__class__, "get_AllOptions")


# //////////////////////////////////////////////////////////////////////////////
