# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....bugcheck_error import BugCheckError

from ....handlers import OptionHandlerToPrepareGetValue
from ....handlers import OptionHandlerCtxToPrepareGetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareGetValue__Std__Generic


class OptionHandlerToPrepareGetValue__Std__Generic(OptionHandlerToPrepareGetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareGetValue(self, ctx: OptionHandlerCtxToPrepareGetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareGetValue  # noqa: E721
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) is str
        assert ctx.OptionValue is not None

        typeOfOptionValue = type(ctx.OptionValue)

        if typeOfOptionValue is int:
            pass  # OK
        elif typeOfOptionValue is str:
            pass  # OK
        elif typeOfOptionValue is bool:
            pass  # OK
        else:
            BugCheckError.UnknownOptionValueType(ctx.OptionName, typeOfOptionValue)

        return ctx.OptionValue


# //////////////////////////////////////////////////////////////////////////////
