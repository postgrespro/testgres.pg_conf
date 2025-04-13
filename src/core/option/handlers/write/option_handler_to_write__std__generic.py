# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from .option_handler_to_write__std__int import OptionHandlerToWrite__Std__Int
from .option_handler_to_write__std__str import OptionHandlerToWrite__Std__Str
from .option_handler_to_write__std__bool import OptionHandlerToWrite__Std__Bool

from ....handlers import OptionHandlerToWrite
from ....handlers import OptionHandlerCtxToWrite

from ....bugcheck_error import BugCheckError

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToWrite__Std__Generic


class OptionHandlerToWrite__Std__Generic(OptionHandlerToWrite):
    # fmt off
    sm_Handler_For_Int = OptionHandlerToWrite__Std__Int()

    sm_Handler_For_Str = OptionHandlerToWrite__Std__Str()

    sm_Handler_For_Bool = OptionHandlerToWrite__Std__Bool()
    # fmt on

    # --------------------------------------------------------------------
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def OptionValueToString(self, ctx: OptionHandlerCtxToWrite) -> str:
        assert type(ctx) == OptionHandlerCtxToWrite
        assert ctx.OptionValue is not None

        typeOfOptionValue = type(ctx.OptionValue)

        if typeOfOptionValue == int:
            return __class__.sm_Handler_For_Int.OptionValueToString(ctx)

        if typeOfOptionValue == str:
            return __class__.sm_Handler_For_Str.OptionValueToString(ctx)

        if typeOfOptionValue == bool:
            return __class__.sm_Handler_For_Bool.OptionValueToString(ctx)

        BugCheckError.UnknownOptionValueType(ctx.OptionName, typeOfOptionValue)


# //////////////////////////////////////////////////////////////////////////////
