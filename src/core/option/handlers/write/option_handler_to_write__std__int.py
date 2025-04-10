# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToWrite
from ....handlers import OptionHandlerCtxToWrite

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToWrite__Std__Int


class OptionHandlerToWrite__Std__Int(OptionHandlerToWrite):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def OptionValueToString(self, ctx: OptionHandlerCtxToWrite) -> str:
        assert type(ctx) == OptionHandlerCtxToWrite
        assert ctx.OptionValue is not None

        typedValue = int(ctx.OptionValue)

        return str(typedValue)


# //////////////////////////////////////////////////////////////////////////////
