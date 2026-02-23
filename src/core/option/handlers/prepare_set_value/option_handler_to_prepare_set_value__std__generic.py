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
        assert type(ctx) == OptionHandlerCtxToPrepareSetValue  # noqa: E721
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
