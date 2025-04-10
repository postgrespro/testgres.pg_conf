# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToWrite
from ....handlers import OptionHandlerCtxToWrite

from ....write_utils import WriteUtils

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToWrite__Std__Str


class OptionHandlerToWrite__Std__Str(OptionHandlerToWrite):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def OptionValueToString(self, ctx: OptionHandlerCtxToWrite) -> str:
        assert type(ctx) == OptionHandlerCtxToWrite
        assert ctx.OptionValue is not None

        typedValue = str(ctx.OptionValue)

        result = WriteUtils.Pack_Str(typedValue)

        assert type(result) == str
        assert len(result) >= 2
        assert result[0] == "'"
        assert result[-1] == "'"

        return result


# //////////////////////////////////////////////////////////////////////////////
