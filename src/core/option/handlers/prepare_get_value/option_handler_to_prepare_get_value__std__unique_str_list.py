# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToPrepareGetValue
from ....handlers import OptionHandlerCtxToPrepareGetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareGetValue__Std__UniqueStrList


class OptionHandlerToPrepareGetValue__Std__UniqueStrList(
    OptionHandlerToPrepareGetValue
):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareGetValue(self, ctx: OptionHandlerCtxToPrepareGetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareGetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValue is not None
        assert type(ctx.OptionValue) == list

        result = list[str]()

        index = set[str]()

        for x in ctx.OptionValue:
            assert x is not None
            v = str(x)

            if v in index:
                continue

            result.append(v)
            index.add(v)

        return result


# //////////////////////////////////////////////////////////////////////////////
