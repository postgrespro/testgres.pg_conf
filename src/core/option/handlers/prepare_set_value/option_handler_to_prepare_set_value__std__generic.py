# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....bugcheck_error import BugCheckError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

import typing

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__Generic


class OptionHandlerToPrepareSetValue__Std__Generic(OptionHandlerToPrepareSetValue):
    def __init__(self):
        super().__init__()
        return

    # interface ----------------------------------------------------------
    def PrepareSetValue(
        self,
        ctx: OptionHandlerCtxToPrepareSetValue,
    ) -> typing.Any:
        assert type(ctx) is OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) is str
        assert ctx.OptionValue is not None

        if type(ctx.OptionValue) is int:
            pass  # OK
        elif type(ctx.OptionValue) is str:
            pass  # OK
        elif type(ctx.OptionValue) is bool:
            pass  # OK
        else:
            BugCheckError.UnknownOptionValueType(
                ctx.OptionName,
                type(ctx.OptionValue),
            )

        return ctx.OptionValue


# //////////////////////////////////////////////////////////////////////////////
