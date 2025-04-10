# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__Str


class OptionHandlerToPrepareSetValue__Std__Str(OptionHandlerToPrepareSetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValue(self, ctx: OptionHandlerCtxToPrepareSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValue is not None

        typeOfOptionValue = type(ctx.OptionValue)

        if typeOfOptionValue != str:
            optionName = ctx.OptionName
            assert type(optionName) == str
            RaiseError.BadOptionValueType(optionName, typeOfOptionValue, str)

        return ctx.OptionValue


# //////////////////////////////////////////////////////////////////////////////
