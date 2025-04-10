# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToGetValue
from ....handlers import OptionHandlerCtxToGetValue
from ....handlers import ConfigurationDataHandler
from ....handlers import FileData
from ....handlers import OptionData

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToGetValue__Std__Simple


class OptionHandlerToGetValue__Std__Simple(OptionHandlerToGetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def GetOptionValue(self, ctx: OptionHandlerCtxToGetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToGetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert (
            ctx.SourceData is None
            or type(ctx.SourceData) == FileData
            or type(ctx.SourceData) == OptionData
        )
        assert type(ctx.OptionName) == str

        return ctx.DataHandler.DataHandler__GetOptionValue__Simple(
            ctx.SourceData, ctx.OptionName
        )


# //////////////////////////////////////////////////////////////////////////////
