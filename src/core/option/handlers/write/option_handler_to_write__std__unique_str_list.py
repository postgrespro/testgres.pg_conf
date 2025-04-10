# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToWrite
from ....handlers import OptionHandlerCtxToWrite

from ....write_utils import WriteUtils

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToWrite__Std__UniqueStrList


class OptionHandlerToWrite__Std__UniqueStrList(OptionHandlerToWrite):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def OptionValueToString(self, ctx: OptionHandlerCtxToWrite) -> str:
        assert type(ctx) == OptionHandlerCtxToWrite
        assert ctx.OptionValue is not None
        assert type(ctx.OptionValue) == list

        result = WriteUtils.Pack_StrList2(ctx.OptionValue)
        assert type(result) == str

        result = WriteUtils.Pack_Str(result)
        assert type(result) == str
        assert len(result) >= 2
        assert result[0] == "'"
        assert result[-1] == "'"

        return result


# //////////////////////////////////////////////////////////////////////////////
