# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

import typing

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__Int


class OptionHandlerToPrepareSetValue__Std__Int(OptionHandlerToPrepareSetValue):
    def __init__(self):
        super().__init__()
        return

    # interface ----------------------------------------------------------
    def PrepareSetValue(
        self,
        ctx: OptionHandlerCtxToPrepareSetValue,
    ) -> typing.Any:
        assert type(ctx) is OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) is str
        assert ctx.OptionValue is not None

        if type(ctx.OptionValue) is int:
            return ctx.OptionValue

        optionName = ctx.OptionName
        assert type(optionName) is str

        if type(ctx.OptionValue) is str:
            if not str(ctx.OptionValue).isnumeric():
                RaiseError.CantConvertOptionValue(
                    optionName,
                    type(ctx.OptionValue),
                    int,
                )

            return int(ctx.OptionValue)

        RaiseError.BadOptionValueType(
            optionName,
            type(ctx.OptionValue),
            int,
        )


# //////////////////////////////////////////////////////////////////////////////
