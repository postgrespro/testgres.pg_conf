# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToWrite
from ....handlers import OptionHandlerCtxToWrite

from ....raise_error import RaiseError

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToWrite__Std__Bool


class OptionHandlerToWrite__Std__Bool(OptionHandlerToWrite):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def OptionValueToString(self, ctx: OptionHandlerCtxToWrite) -> str:
        assert type(ctx) is OptionHandlerCtxToWrite
        assert type(ctx.OptionName) is str
        assert ctx.OptionValue is not None

        typeOfValue = type(ctx.OptionValue)

        if typeOfValue == bool:  # noqa: E721
            typedValue = bool(ctx.OptionValue)
        else:
            RaiseError.BadOptionValueItemType(ctx.OptionName, typeOfValue, bool)

        assert type(typedValue) is bool

        if typedValue:
            result = "on"
        else:
            result = "off"

        return result


# //////////////////////////////////////////////////////////////////////////////
