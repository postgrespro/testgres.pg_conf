# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....handlers import OptionHandlerToSetValue
from ....handlers import OptionHandlerCtxToSetValue
from ....handlers import ConfigurationDataHandler

from ....model import FileData
from ....model import OptionData

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToSetValue__Std__Simple


class OptionHandlerToSetValue__Std__Simple(OptionHandlerToSetValue):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def SetOptionValue(self, ctx: OptionHandlerCtxToSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert (
            ctx.TargetData is None
            or type(ctx.TargetData) == FileData
            or type(ctx.TargetData) == OptionData
        )
        assert ctx.OptionName is not None
        assert ctx.OptionValue is not None

        return ctx.DataHandler.DataHandler__SetOptionValue__Simple(
            ctx.TargetData, ctx.OptionName, ctx.OptionValue
        )


# //////////////////////////////////////////////////////////////////////////////
