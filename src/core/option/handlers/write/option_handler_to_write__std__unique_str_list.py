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
        assert type(ctx) is OptionHandlerCtxToWrite
        assert ctx.OptionValue is not None
        assert type(ctx.OptionValue) is list

        result = WriteUtils.Pack_StrList2(ctx.OptionValue)
        assert type(result) is str

        result = WriteUtils.Pack_Str(result)
        assert type(result) is str
        assert len(result) >= 2
        assert result[0] == "'"
        assert result[-1] == "'"

        return result


# //////////////////////////////////////////////////////////////////////////////
