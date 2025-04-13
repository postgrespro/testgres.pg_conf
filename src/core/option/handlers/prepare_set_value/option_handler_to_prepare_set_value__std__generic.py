# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....bugcheck_error import BugCheckError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__Generic


class OptionHandlerToPrepareSetValue__Std__Generic(OptionHandlerToPrepareSetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValue(self, ctx: OptionHandlerCtxToPrepareSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValue is not None

        typeOfOptionValue = type(ctx.OptionValue)

        if typeOfOptionValue == int:
            pass  # OK
        elif typeOfOptionValue == str:
            pass  # OK
        elif typeOfOptionValue == bool:
            pass  # OK
        else:
            BugCheckError.UnknownOptionValueType(ctx.OptionName, typeOfOptionValue)

        return ctx.OptionValue


# //////////////////////////////////////////////////////////////////////////////
