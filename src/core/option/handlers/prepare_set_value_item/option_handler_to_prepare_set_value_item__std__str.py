# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValueItem
from ....handlers import OptionHandlerCtxToPrepareSetValueItem
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValueItem__Std__Str


class OptionHandlerToPrepareSetValueItem__Std__Str(OptionHandlerToPrepareSetValueItem):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValueItem(self, ctx: OptionHandlerCtxToPrepareSetValueItem) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValueItem
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValueItem is not None

        typeOfOptionValue = type(ctx.OptionValueItem)

        if typeOfOptionValue != str:
            optionName = ctx.OptionName
            assert type(optionName) == str
            RaiseError.BadOptionValueItemType(optionName, typeOfOptionValue, str)

        return ctx.OptionValueItem


# //////////////////////////////////////////////////////////////////////////////
