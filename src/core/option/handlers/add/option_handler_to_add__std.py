# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToAddOption
from ....handlers import OptionHandlerCtxToAddOption
from ....handlers import ConfigurationDataHandler
from ....handlers import FileData
from ....handlers import FileLineData

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToAddOption__Std


class OptionHandlerToAddOption__Std(OptionHandlerToAddOption):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def AddOption(self, ctx: OptionHandlerCtxToAddOption) -> any:
        assert type(ctx) == OptionHandlerCtxToAddOption  # noqa: E721
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert (
            ctx.Target is None
            or type(ctx.Target) is FileData
            or type(ctx.Target) is FileLineData
        )
        assert ctx.OptionOffset is None or type(ctx.OptionOffset) is int
        assert type(ctx.OptionName) is str
        assert ctx.OptionName is not None

        return ctx.DataHandler.DataHandler__AddSimpleOption(
            ctx.Target, ctx.OptionOffset, ctx.OptionName, ctx.OptionValue
        )


# //////////////////////////////////////////////////////////////////////////////
