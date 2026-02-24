# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__Int


class OptionHandlerToPrepareSetValue__Std__Int(OptionHandlerToPrepareSetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValue(self, ctx: OptionHandlerCtxToPrepareSetValue) -> any:
        assert type(ctx) is OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) is str
        assert ctx.OptionValue is not None

        typeOfOptionValue = type(ctx.OptionValue)

        if typeOfOptionValue is int:
            return ctx.OptionValue

        optionName = ctx.OptionName
        assert type(optionName) is str

        if typeOfOptionValue is str:
            if not str(ctx.OptionValue).isnumeric():
                RaiseError.CantConvertOptionValue(optionName, typeOfOptionValue, int)

            return int(ctx.OptionValue)

        RaiseError.BadOptionValueType(optionName, typeOfOptionValue, int)


# //////////////////////////////////////////////////////////////////////////////
