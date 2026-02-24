# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToSetValueItem
from ....handlers import OptionHandlerCtxToSetValueItem
from ....handlers import ConfigurationDataHandler

from ....model import FileData
from ....model import OptionData

import typing

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToSetValueItem__Std__Unique


class OptionHandlerToSetValueItem__Std__Unique(OptionHandlerToSetValueItem):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def SetOptionValueItem(self, ctx: OptionHandlerCtxToSetValueItem) -> typing.Any:
        assert type(ctx) is OptionHandlerCtxToSetValueItem
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert (
            ctx.TargetData is None
            or type(ctx.TargetData) is FileData
            or type(ctx.TargetData) is OptionData
        )
        assert type(ctx.OptionName) is str
        assert ctx.OptionValueItem is not None

        return ctx.DataHandler.DataHandler__SetUniqueOptionValueItem(
            ctx.TargetData, ctx.OptionName, ctx.OptionValueItem
        )


# //////////////////////////////////////////////////////////////////////////////
