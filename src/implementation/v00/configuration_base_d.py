# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from .configuration_base import PgCfgModel__OptionHandlerToPrepareSetValue
from .configuration_base import PgCfgModel__OptionHandlerToPrepareSetValueItem
from .configuration_base import PgCfgModel__OptionHandlerToPrepareGetValue
from .configuration_base import PgCfgModel__OptionHandlerToSetValue
from .configuration_base import PgCfgModel__OptionHandlerToGetValue
from .configuration_base import PgCfgModel__OptionHandlerToAddOption
from .configuration_base import PgCfgModel__OptionHandlerToSetValueItem
from .configuration_base import PgCfgModel__OptionHandlerToWrite

# fmt: off
from ...core.option.handlers.prepare_set_value.option_handler_to_prepare_set_value__std__generic \
    import OptionHandlerToPrepareSetValue__Std__Generic

from ...core.option.handlers.prepare_set_value.option_handler_to_prepare_set_value__std__int \
    import OptionHandlerToPrepareSetValue__Std__Int

from ...core.option.handlers.prepare_set_value.option_handler_to_prepare_set_value__std__str \
    import OptionHandlerToPrepareSetValue__Std__Str

from ...core.option.handlers.prepare_set_value.option_handler_to_prepare_set_value__std__bool \
    import OptionHandlerToPrepareSetValue__Std__Bool

from ...core.option.handlers.prepare_set_value.option_handler_to_prepare_set_value__std__unique_str_list \
    import OptionHandlerToPrepareSetValue__Std__UniqueStrList

# -------------
from ...core.option.handlers.prepare_set_value_item.option_handler_to_prepare_set_value_item__std__str \
    import OptionHandlerToPrepareSetValueItem__Std__Str

# -------------
from ...core.option.handlers.prepare_get_value.option_handler_to_prepare_get_value__std__generic \
    import OptionHandlerToPrepareGetValue__Std__Generic

from ...core.option.handlers.prepare_get_value.option_handler_to_prepare_get_value__std__int \
    import OptionHandlerToPrepareGetValue__Std__Int

from ...core.option.handlers.prepare_get_value.option_handler_to_prepare_get_value__std__str \
    import OptionHandlerToPrepareGetValue__Std__Str

from ...core.option.handlers.prepare_get_value.option_handler_to_prepare_get_value__std__bool \
    import OptionHandlerToPrepareGetValue__Std__Bool

# -------------
from ...core.option.handlers.prepare_get_value.option_handler_to_prepare_get_value__std__unique_str_list \
    import OptionHandlerToPrepareGetValue__Std__UniqueStrList

# -------------
from ...core.option.handlers.set_value.option_handler_to_set_value__std__simple \
    import OptionHandlerToSetValue__Std__Simple

# -------------
from ...core.option.handlers.get_value.option_handler_to_get_value__std__simple \
    import OptionHandlerToGetValue__Std__Simple

from ...core.option.handlers.get_value.option_handler_to_get_value__std__union_list \
    import OptionHandlerToGetValue__Std__UnionList

# -------------
from ...core.option.handlers.add.option_handler_to_add__std \
    import OptionHandlerToAddOption__Std

# -------------
from ...core.option.handlers.set_value_item.option_handler_to_set_value_item__std__unique \
    import OptionHandlerToSetValueItem__Std__Unique

# -------------
from ...core.option.handlers.write.option_handler_to_write__std__generic \
    import OptionHandlerToWrite__Std__Generic

from ...core.option.handlers.write.option_handler_to_write__std__int \
    import OptionHandlerToWrite__Std__Int

from ...core.option.handlers.write.option_handler_to_write__std__str \
    import OptionHandlerToWrite__Std__Str

from ...core.option.handlers.write.option_handler_to_write__std__bool \
    import OptionHandlerToWrite__Std__Bool

from ...core.option.handlers.write.option_handler_to_write__std__unique_str_list \
    import OptionHandlerToWrite__Std__UniqueStrList
# fmt: on

import typing
import dataclasses

# //////////////////////////////////////////////////////////////////////////////


# fmt: off
g_OptionHandlerToPrepareSetValue__Std__Generic = \
    OptionHandlerToPrepareSetValue__Std__Generic()

g_OptionHandlerToPrepareSetValue__Std__Int = \
    OptionHandlerToPrepareSetValue__Std__Int()

g_OptionHandlerToPrepareSetValue__Std__Str = \
    OptionHandlerToPrepareSetValue__Std__Str()

g_OptionHandlerToPrepareSetValue__Std__Bool = \
    OptionHandlerToPrepareSetValue__Std__Bool()

g_OptionHandlerToPrepareSetValue__Std__UniqueStrList = \
    OptionHandlerToPrepareSetValue__Std__UniqueStrList()

# ---------
g_OptionHandlerToPrepareSetValueItem__Std__Str = \
    OptionHandlerToPrepareSetValueItem__Std__Str()

# ---------
g_OptionHandlerToPrepareGetValue__Std__Generic = \
    OptionHandlerToPrepareGetValue__Std__Generic()

g_OptionHandlerToPrepareGetValue__Std__Int = \
    OptionHandlerToPrepareGetValue__Std__Int()

g_OptionHandlerToPrepareGetValue__Std__Str = \
    OptionHandlerToPrepareGetValue__Std__Str()

g_OptionHandlerToPrepareGetValue__Std__Bool = \
    OptionHandlerToPrepareGetValue__Std__Bool()

g_OptionHandlerToPrepareGetValue__Std__UniqueStrList = \
    OptionHandlerToPrepareGetValue__Std__UniqueStrList()

# ---------
g_OptionHandlerToSetValue__Std__Simple = \
    OptionHandlerToSetValue__Std__Simple()

# ---------
g_OptionHandlerToGetValue__Std__Simple = \
    OptionHandlerToGetValue__Std__Simple()

g_OptionHandlerToGetValue__Std__UnionList = \
    OptionHandlerToGetValue__Std__UnionList()

# ---------
g_OptionHandlerToAddOption__Std = \
    OptionHandlerToAddOption__Std()

# ---------
g_OptionHandlerToSetValueItem__Std__Unique = \
    OptionHandlerToSetValueItem__Std__Unique()

# ---------
g_OptionHandlerToWrite__Std__Generic = \
    OptionHandlerToWrite__Std__Generic()

g_OptionHandlerToWrite__Std__Int = \
    OptionHandlerToWrite__Std__Int()

g_OptionHandlerToWrite__Std__Str = \
    OptionHandlerToWrite__Std__Str()

g_OptionHandlerToWrite__Std__Bool = \
    OptionHandlerToWrite__Std__Bool()

g_OptionHandlerToWrite__Std__UniqueStrList = \
    OptionHandlerToWrite__Std__UniqueStrList()
# fmt: on


# //////////////////////////////////////////////////////////////////////////////
# PostgresConfigurationOptionHandlers


@dataclasses.dataclass
class PostgresConfigurationOptionHandlers:
    PrepareSetValue: PgCfgModel__OptionHandlerToPrepareSetValue
    PrepareGetValue: PgCfgModel__OptionHandlerToPrepareGetValue
    PrepareSetValueItem: typing.Optional[PgCfgModel__OptionHandlerToPrepareSetValueItem]
    SetValue: typing.Optional[PgCfgModel__OptionHandlerToSetValue]
    GetValue: PgCfgModel__OptionHandlerToGetValue
    AddOption: PgCfgModel__OptionHandlerToAddOption
    SetValueItem: typing.Optional[PgCfgModel__OptionHandlerToSetValueItem]
    Write: PgCfgModel__OptionHandlerToWrite


# //////////////////////////////////////////////////////////////////////////////
# fmt: off

g_OptionHandlers__Std__Generic = \
    PostgresConfigurationOptionHandlers(
        g_OptionHandlerToPrepareSetValue__Std__Generic,
        g_OptionHandlerToPrepareGetValue__Std__Generic,
        None,
        g_OptionHandlerToSetValue__Std__Simple,
        g_OptionHandlerToGetValue__Std__Simple,
        g_OptionHandlerToAddOption__Std,
        None,
        g_OptionHandlerToWrite__Std__Generic,
    )

# ------------------------------------------------------------------------
g_OptionHandlers__Std__Int = \
    PostgresConfigurationOptionHandlers(
        g_OptionHandlerToPrepareSetValue__Std__Int,
        g_OptionHandlerToPrepareGetValue__Std__Int,
        None,
        g_OptionHandlerToSetValue__Std__Simple,
        g_OptionHandlerToGetValue__Std__Simple,
        g_OptionHandlerToAddOption__Std,
        None,
        g_OptionHandlerToWrite__Std__Int,
    )

# ------------------------------------------------------------------------
g_OptionHandlers__Std__Str = \
    PostgresConfigurationOptionHandlers(
        g_OptionHandlerToPrepareSetValue__Std__Str,
        g_OptionHandlerToPrepareGetValue__Std__Str,
        None,
        g_OptionHandlerToSetValue__Std__Simple,
        g_OptionHandlerToGetValue__Std__Simple,
        g_OptionHandlerToAddOption__Std,
        None,
        g_OptionHandlerToWrite__Std__Str,
    )

# ------------------------------------------------------------------------
g_OptionHandlers__Std__Bool = \
    PostgresConfigurationOptionHandlers(
        g_OptionHandlerToPrepareSetValue__Std__Bool,
        g_OptionHandlerToPrepareGetValue__Std__Bool,
        None,
        g_OptionHandlerToSetValue__Std__Simple,
        g_OptionHandlerToGetValue__Std__Simple,
        g_OptionHandlerToAddOption__Std,
        None,
        g_OptionHandlerToWrite__Std__Bool,
    )

# ------------------------------------------------------------------------
g_OptionHandlers__Std__UniqueStrList = \
    PostgresConfigurationOptionHandlers(
        g_OptionHandlerToPrepareSetValue__Std__UniqueStrList,
        g_OptionHandlerToPrepareGetValue__Std__UniqueStrList,
        g_OptionHandlerToPrepareSetValueItem__Std__Str,
        g_OptionHandlerToSetValue__Std__Simple,
        g_OptionHandlerToGetValue__Std__UnionList,
        g_OptionHandlerToAddOption__Std,
        g_OptionHandlerToSetValueItem__Std__Unique,
        g_OptionHandlerToWrite__Std__UniqueStrList,
    )
# fmt: on

# //////////////////////////////////////////////////////////////////////////////


g_OptionHandlers: typing.Dict[
    str,
    PostgresConfigurationOptionHandlers,
] = {
    # fmt: off
    # STANDARD -----------------------------------------------------------
    "port": g_OptionHandlers__Std__Int,
    "listen_addresses": g_OptionHandlers__Std__Str,
    "shared_preload_libraries": g_OptionHandlers__Std__UniqueStrList,
    "restart_after_crash": g_OptionHandlers__Std__Bool,

    # PROXIMA ------------------------------------------------------------
    "proxima.port": g_OptionHandlers__Std__Int,
    # fmt: on
}


# //////////////////////////////////////////////////////////////////////////////
