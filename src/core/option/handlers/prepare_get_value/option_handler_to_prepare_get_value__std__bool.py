# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToPrepareGetValue
from ....handlers import OptionHandlerCtxToPrepareGetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareGetValue__Std__Bool


class OptionHandlerToPrepareGetValue__Std__Bool(OptionHandlerToPrepareGetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareGetValue(self, ctx: OptionHandlerCtxToPrepareGetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareGetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValue is not None

        # [2025-04-13] Research
        assert type(ctx.OptionValue) == bool

        return bool(ctx.OptionValue)


# //////////////////////////////////////////////////////////////////////////////
