# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValueItem
from ....handlers import OptionHandlerCtxToPrepareSetValueItem
from ....handlers import ConfigurationDataHandler

import typing

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValueItem__Std__Str


class OptionHandlerToPrepareSetValueItem__Std__Str(OptionHandlerToPrepareSetValueItem):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValueItem(
        self, ctx: OptionHandlerCtxToPrepareSetValueItem
    ) -> typing.Any:
        assert type(ctx) is OptionHandlerCtxToPrepareSetValueItem
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) is str
        assert ctx.OptionValueItem is not None

        typeOfOptionValue = type(ctx.OptionValueItem)

        if typeOfOptionValue is not str:
            optionName = ctx.OptionName
            assert type(optionName) is str
            RaiseError.BadOptionValueItemType(optionName, typeOfOptionValue, str)

        return ctx.OptionValueItem


# //////////////////////////////////////////////////////////////////////////////
