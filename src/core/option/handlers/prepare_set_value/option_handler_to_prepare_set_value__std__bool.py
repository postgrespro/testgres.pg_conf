# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__Bool


class OptionHandlerToPrepareSetValue__Std__Bool(OptionHandlerToPrepareSetValue):
    def __init__(self):
        super().__init__()

        # check
        assert not any(set(__class__.sm_Str_True).intersection(__class__.sm_Str_False))

        # prefixes are checked
        assert not any(
            [
                x1
                for x1 in __class__.sm_Str_True
                if any([x2 for x2 in __class__.sm_Str_False if x2.startswith(x1)])
            ]
        )
        assert not any(
            [
                x1
                for x1 in __class__.sm_Str_False
                if any([x2 for x2 in __class__.sm_Str_True if x2.startswith(x1)])
            ]
        )

    # interface ----------------------------------------------------------
    def PrepareSetValue(self, ctx: OptionHandlerCtxToPrepareSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValue is not None

        optionValue = ctx.OptionValue
        optionValueType = type(optionValue)

        if optionValueType == bool:
            return optionValue

        if optionValueType == int:
            assert type(optionValue) == int

            if optionValue == 0:
                return False

            if optionValue == 1:
                return True

            RaiseError.CantConvertOptionValue(ctx.OptionName, optionValueType, bool)

        if optionValueType == str:
            assert type(optionValue) == str

            if len(optionValue) < __class__.C_MIN_STR_VALUE_LENGTH:
                pass
            elif len(optionValue) > __class__.C_MAX_STR_VALUE_LENGTH:
                pass
            else:
                optionValue_lower = optionValue.lower()

                if optionValue_lower in __class__.sm_Str_False:
                    return False

                if optionValue_lower in __class__.sm_Str_True:
                    return True

            RaiseError.CantConvertOptionValue(ctx.OptionName, optionValueType, bool)

        RaiseError.BadOptionValueType(ctx.OptionName, optionValueType, bool)

    # Private data -------------------------------------------------------
    C_MIN_STR_VALUE_LENGTH = 1
    C_MAX_STR_VALUE_LENGTH = 5

    sm_Str_False: list[str] = [
        "of",
        "off",
        "f",
        "fa",
        "fal",
        "fals",
        "false",
        "n",
        "no",
        "0",
    ]

    sm_Str_True: list[str] = [
        "on",
        "t",
        "tr",
        "tru",
        "true",
        "y",
        "ye",
        "yes",
        "1",
    ]


# //////////////////////////////////////////////////////////////////////////////
