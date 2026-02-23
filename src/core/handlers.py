# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from .model import FileLineData
from .model import FileData
from .model import OptionData
from .raise_error import RaiseError

import typing

# //////////////////////////////////////////////////////////////////////////////
# ConfigurationDataHandler


class ConfigurationDataHandler:
    def __init__(self):
        pass

    # interface ----------------------------------------------------------
    def DataHandler__SetOptionValue__Simple(
        self,
        targetData: typing.Union[None, FileData, OptionData],
        optionName: str,
        optionValue: any,
    ) -> any:
        assert (
            targetData is None
            or type(targetData) is FileData
            or type(targetData) is FileLineData
        )
        assert type(optionName) is str
        assert optionValue is not None
        RaiseError.MethodIsNotImplemented(
            __class__, "DataHandler__SetOptionValue__Simple"
        )

    # --------------------------------------------------------------------
    def DataHandler__GetOptionValue__Simple(
        self,
        sourceData: typing.Union[None, FileData, OptionData],
        optionName: str,
    ) -> any:
        assert (
            sourceData is None
            or type(sourceData) is FileData
            or type(sourceData) is OptionData
        )
        assert type(optionName) is str or type(optionName) is OptionData
        RaiseError.MethodIsNotImplemented(
            __class__, "DataHandler__GetOptionValue__Simple"
        )

    # --------------------------------------------------------------------
    def DataHandler__GetOptionValue__UnionList(
        self,
        sourceData: typing.Union[None, FileLineData, OptionData],
        optionName: str,
    ) -> any:
        assert (
            sourceData is None
            or type(sourceData) is FileData
            or type(sourceData) is OptionData
        )
        assert type(optionName) is str
        RaiseError.MethodIsNotImplemented(
            __class__, "DataHandler__GetOptionValue__UnionList"
        )

    # --------------------------------------------------------------------
    def DataHandler__ResetOption(
        self,
        targetData: typing.Union[None, FileData, OptionData],
        optionName: str,
    ) -> any:
        assert (
            targetData is None
            or type(targetData) is FileData
            or type(targetData) is OptionData
        )
        assert type(optionName) is str
        RaiseError.MethodIsNotImplemented(__class__, "DataHandler__ResetOption")

    # --------------------------------------------------------------------
    def DataHandler__AddSimpleOption(
        self,
        target: typing.Union[None, FileData, FileLineData],
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: any,
    ) -> any:
        assert (
            target is None
            or type(target) is FileData
            or type(target) is FileLineData
        )
        assert optionOffset is None or type(optionOffset) is int
        assert type(optionName) is str
        assert optionValue is not None
        RaiseError.MethodIsNotImplemented(__class__, "DataHandler__AddSimpleOption")

    # --------------------------------------------------------------------
    def DataHandler__SetUniqueOptionValueItem(
        self,
        targetData: typing.Union[None, FileData, OptionData],
        optionName: str,
        optionValueItem: any,
    ) -> any:
        assert (
            targetData is None
            or type(targetData) is FileData
            or type(optionName) is OptionData
        )
        assert type(optionName) is str
        assert optionValueItem is not None
        RaiseError.MethodIsNotImplemented(
            __class__, "DataHandler__SetUniqueOptionValueItem"
        )


# //////////////////////////////////////////////////////////////////////////////
# OptionHandler


class OptionHandler:
    def __init__(self):
        pass


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToSetValue


class OptionHandlerCtxToSetValue:
    DataHandler: ConfigurationDataHandler
    TargetData: typing.Union[None, FileData, OptionData]
    OptionName: str
    OptionValue: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        targetData: typing.Union[None, FileData, OptionData],
        optionName: str,
        optionValue: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert (
            targetData is None
            or type(targetData) is FileData
            or type(targetData) is OptionData
        )
        assert type(optionName) is str

        self.DataHandler = dataHandler
        self.TargetData = targetData
        self.OptionName = optionName
        self.OptionValue = optionValue


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToSetValue


class OptionHandlerToSetValue(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def SetOptionValue(self, ctx: OptionHandlerCtxToSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToSetValue  # noqa: E721
        assert ctx.OptionName is not None
        assert ctx.OptionValue is not None
        RaiseError.MethodIsNotImplemented(__class__, "SetOptionValue")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToGetValue


class OptionHandlerCtxToGetValue:
    DataHandler: ConfigurationDataHandler
    SourceData: typing.Union[None, FileData, OptionData]
    OptionName: str

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        sourceData: typing.Union[None, FileData, OptionData],
        optionName: str,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert (
            sourceData is None
            or type(sourceData) is FileData
            or type(sourceData) is OptionData
        )
        assert type(optionName) is str

        self.DataHandler = dataHandler
        self.SourceData = sourceData
        self.OptionName = optionName


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToGetValue


class OptionHandlerToGetValue(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def GetOptionValue(self, ctx: OptionHandlerCtxToGetValue) -> any:
        assert type(ctx) is OptionHandlerCtxToGetValue
        assert (
            ctx.SourceData is None
            or type(ctx.SourceData) is FileData
            or type(ctx.SourceData) is OptionData
        )
        assert type(ctx.OptionName) is str
        RaiseError.MethodIsNotImplemented(__class__, "GetOptionValue")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToAddOption


class OptionHandlerCtxToAddOption:
    DataHandler: ConfigurationDataHandler
    Target: typing.Union[None, FileData, FileLineData]
    OptionOffset: typing.Optional[int]
    OptionName: str
    OptionValue: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        target: typing.Union[None, FileData, FileLineData],
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert (
            target is None
            or type(target) is FileData
            or type(target) is FileLineData
        )
        assert type(optionName) is str
        assert optionValue is not None

        self.DataHandler = dataHandler
        self.Target = target
        self.OptionOffset = optionOffset
        self.OptionName = optionName
        self.OptionValue = optionValue


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToAddOption


class OptionHandlerToAddOption(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def AddOption(self, ctx: OptionHandlerCtxToSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToSetValue  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "AddOption")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToSetValueItem


class OptionHandlerCtxToSetValueItem:
    DataHandler: ConfigurationDataHandler
    TargetData: typing.Union[None, FileData, OptionData]
    OptionName: str
    OptionValueItem: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        targetData: typing.Union[None, FileData, OptionData],
        optionName: str,
        optionValueItem: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert (
            targetData is None
            or type(targetData) is FileData
            or type(targetData) is OptionData
        )
        assert type(optionName) is str

        self.DataHandler = dataHandler
        self.TargetData = targetData
        self.OptionName = optionName
        self.OptionValueItem = optionValueItem


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToSetValueItem


class OptionHandlerToSetValueItem(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def SetOptionValueItem(self, ctx: OptionHandlerCtxToSetValueItem) -> any:
        assert type(ctx) == OptionHandlerCtxToSetValueItem  # noqa: E721
        assert (
            ctx.TargetData is None
            or type(ctx.TargetData) is FileData
            or type(ctx.TargetData) is OptionData
        )
        assert type(ctx.OptionName) is str
        assert ctx.OptionValueItem is not None
        RaiseError.MethodIsNotImplemented(__class__, "SetOptionValueItem")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToPrepareSetValue


class OptionHandlerCtxToPrepareSetValue:
    DataHandler: ConfigurationDataHandler
    OptionName: str
    OptionValue: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        optionName: str,
        optionValue: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert type(optionName) is str
        assert optionValue is not None

        self.DataHandler = dataHandler
        self.OptionName = optionName
        self.OptionValue = optionValue


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue


class OptionHandlerToPrepareSetValue(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValue(self, ctx: OptionHandlerCtxToPrepareSetValue) -> str:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValue  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "PrepareSetValue")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToPrepareSetValueItem


class OptionHandlerCtxToPrepareSetValueItem:
    DataHandler: ConfigurationDataHandler
    OptionName: str
    OptionValueItem: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        optionName: str,
        optionValueItem: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert type(optionName) is str
        assert optionValueItem is not None

        self.DataHandler = dataHandler
        self.OptionName = optionName
        self.OptionValueItem = optionValueItem


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValueItem


class OptionHandlerToPrepareSetValueItem(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValueItem(self, ctx: OptionHandlerCtxToPrepareSetValueItem) -> str:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValueItem  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "PrepareSetValueItem")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToPrepareGetValue


class OptionHandlerCtxToPrepareGetValue:
    DataHandler: ConfigurationDataHandler
    OptionName: str
    OptionValue: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        optionName: str,
        optionValue: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert type(optionName) is str
        assert optionValue is not None

        self.DataHandler = dataHandler
        self.OptionName = optionName
        self.OptionValue = optionValue


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareGetValue


class OptionHandlerToPrepareGetValue(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareGetValue(self, ctx: OptionHandlerCtxToPrepareGetValue) -> str:
        assert type(ctx) == OptionHandlerCtxToPrepareGetValue  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "PrepareGetValue")


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerCtxToWrite


class OptionHandlerCtxToWrite:
    DataHandler: ConfigurationDataHandler
    OptionName: str
    OptionValue: any

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataHandler: ConfigurationDataHandler,
        optionName: str,
        optionValue: any,
    ):
        assert isinstance(dataHandler, ConfigurationDataHandler)
        assert type(optionName) is str
        assert optionValue is not None

        self.DataHandler = dataHandler
        self.OptionName = optionName
        self.OptionValue = optionValue


# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToWrite


class OptionHandlerToWrite(OptionHandler):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def OptionValueToString(self, ctx: OptionHandlerCtxToWrite) -> str:
        assert type(ctx) == OptionHandlerCtxToWrite  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "OptionValueToString")


# //////////////////////////////////////////////////////////////////////////////
