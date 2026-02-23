# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ....raise_error import RaiseError

from ....handlers import OptionHandlerToPrepareSetValue
from ....handlers import OptionHandlerCtxToPrepareSetValue
from ....handlers import ConfigurationDataHandler

from ....read_utils import ReadUtils

import typing

# //////////////////////////////////////////////////////////////////////////////
# OptionHandlerToPrepareSetValue__Std__UniqueStrList


class OptionHandlerToPrepareSetValue__Std__UniqueStrList(
    OptionHandlerToPrepareSetValue
):
    def __init__(self):
        super().__init__()

    # interface ----------------------------------------------------------
    def PrepareSetValue(self, ctx: OptionHandlerCtxToPrepareSetValue) -> any:
        assert type(ctx) == OptionHandlerCtxToPrepareSetValue
        assert isinstance(ctx.DataHandler, ConfigurationDataHandler)
        assert type(ctx.OptionName) == str
        assert ctx.OptionValue is not None

        typeOfOptionValue = type(ctx.OptionValue)

        if typeOfOptionValue == str:
            result = ReadUtils.Unpack_StrList2(ctx.OptionValue)
            assert result is not None
            assert type(result) == list
            return result
        elif typeOfOptionValue == list:
            result: typing.List[str] = list()
            index: typing.Set[str] = set()

            for x in ctx.OptionValue:
                if x is None:
                    RaiseError.NoneOptionValueItemIsNotSupported(ctx.OptionName)

                v = str(x)

                if v in index:
                    continue

                result.append(v)
                index.add(v)

            return result

        optionName = ctx.OptionName
        assert type(optionName) == str  # noqa: E721
        RaiseError.BadOptionValueType(optionName, typeOfOptionValue, list)


# //////////////////////////////////////////////////////////////////////////////
