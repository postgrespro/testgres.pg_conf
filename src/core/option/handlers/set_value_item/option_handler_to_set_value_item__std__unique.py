# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToSetValueItem
from ....handlers import OptionHandlerCtxToSetValueItem
from ....handlers import ConfigurationDataHandler

from ....model import FileData
from ....model import OptionData

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToSetValueItem__Std__Unique


class OptionHandlerToSetValueItem__Std__Unique(OptionHandlerToSetValueItem):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def SetOptionValueItem(self, ctx: OptionHandlerCtxToSetValueItem) -> any:
        assert type(ctx) == OptionHandlerCtxToSetValueItem
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert (
            ctx.TargetData is None
            or type(ctx.TargetData) == FileData
            or type(ctx.TargetData) == OptionData
        )
        assert type(ctx.OptionName) == str
        assert ctx.OptionValueItem is not None

        return ctx.DataHandler.DataHandler__SetUniqueOptionValueItem(
            ctx.TargetData, ctx.OptionName, ctx.OptionValueItem
        )


# //////////////////////////////////////////////////////////////////////////////
