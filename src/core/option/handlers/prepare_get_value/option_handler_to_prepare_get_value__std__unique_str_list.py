# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToPrepareGetValue
from ....handlers import OptionHandlerCtxToPrepareGetValue
from ....handlers import ConfigurationDataHandler

import typing

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareGetValue__Std__UniqueStrList


class OptionHandlerToPrepareGetValue__Std__UniqueStrList(
    OptionHandlerToPrepareGetValue
):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareGetValue(self, ctx: OptionHandlerCtxToPrepareGetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareGetValue  # noqa: E721
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) is str
        assert ctx.OptionValue is not None
        assert type(ctx.OptionValue) == list  # noqa: E721

        result: typing.List[str] = list()
        index: set[str] = set()

        for x in ctx.OptionValue:
            assert x is not None
            v = str(x)

            if v in index:
                continue

            result.append(v)
            index.add(v)

        return result


# //////////////////////////////////////////////////////////////////////////////
