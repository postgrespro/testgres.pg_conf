# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from .configuration_base import PostgresConfiguration_Base
from .configuration_base import PostgresConfigurationReader_Base
from .configuration_base import PostgresConfigurationWriter_Base
from .configuration_base import PostgresConfigurationWriterCtx_Base
from .configuration_base import PgCfgModel__OptionHandlerToPrepareSetValue
from .configuration_base import PgCfgModel__OptionHandlerToPrepareSetValueItem
from .configuration_base import PgCfgModel__OptionHandlerToPrepareGetValue
from .configuration_base import PgCfgModel__OptionHandlerToSetValue
from .configuration_base import PgCfgModel__OptionHandlerToGetValue
from .configuration_base import PgCfgModel__OptionHandlerToAddOption
from .configuration_base import PgCfgModel__OptionHandlerToSetValueItem
from .configuration_base import PgCfgModel__OptionHandlerToWrite

from ...os.abstract.configuration_os_ops import ConfigurationOsOps
from ...os.local.configuration_os_ops import SingleInstance as LocalCfgOsOps

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

from ...core.bugcheck_error import BugCheckError

# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Std


class PostgresConfiguration_Std(PostgresConfiguration_Base):
    C_POSTGRESQL_CONF = "postgresql.conf"
    C_POSTGRESQL_AUTO_CONF = "postgresql.auto.conf"

    # --------------------------------------------------------------------
    # fmt: off
    sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Generic = \
        OptionHandlerToPrepareSetValue__Std__Generic()

    sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Int = \
        OptionHandlerToPrepareSetValue__Std__Int()

    sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Str = \
        OptionHandlerToPrepareSetValue__Std__Str()

    sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Bool = \
        OptionHandlerToPrepareSetValue__Std__Bool()

    sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__UniqueStrList = \
        OptionHandlerToPrepareSetValue__Std__UniqueStrList()

    # ---------
    sm_SingleInstance__OptionHandlerToPrepareSetValueItem__Std__Str = \
        OptionHandlerToPrepareSetValueItem__Std__Str()

    # ---------
    sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Generic = \
        OptionHandlerToPrepareGetValue__Std__Generic()

    sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Int = \
        OptionHandlerToPrepareGetValue__Std__Int()

    sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Str = \
        OptionHandlerToPrepareGetValue__Std__Str()

    sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Bool = \
        OptionHandlerToPrepareGetValue__Std__Bool()

    sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__UniqueStrList = \
        OptionHandlerToPrepareGetValue__Std__UniqueStrList()

    # ---------
    sm_SingleInstance__OptionHandlerToSetValue__Std__Simple = \
        OptionHandlerToSetValue__Std__Simple()

    # ---------
    sm_SingleInstance__OptionHandlerToGetValue__Std__Simple = \
        OptionHandlerToGetValue__Std__Simple()

    sm_SingleInstance__OptionHandlerToGetValue__Std__UnionList = \
        OptionHandlerToGetValue__Std__UnionList()

    # ---------
    sm_SingleInstance__OptionHandlerToAddOption__Std = \
        OptionHandlerToAddOption__Std()

    # ---------
    sm_SingleInstance__OptionHandlerToSetValueItem__Std__Unique = \
        OptionHandlerToSetValueItem__Std__Unique()

    # ---------
    sm_SingleInstance__OptionHandlerToWrite__Std__Generic = \
        OptionHandlerToWrite__Std__Generic()

    sm_SingleInstance__OptionHandlerToWrite__Std__Int = \
        OptionHandlerToWrite__Std__Int()

    sm_SingleInstance__OptionHandlerToWrite__Std__Str = \
        OptionHandlerToWrite__Std__Str()

    sm_SingleInstance__OptionHandlerToWrite__Std__Bool = \
        OptionHandlerToWrite__Std__Bool()

    sm_SingleInstance__OptionHandlerToWrite__Std__UniqueStrList = \
        OptionHandlerToWrite__Std__UniqueStrList()
    # fmt: on

    # --------------------------------------------------------------------
    class tagOptionHandlers:
        PrepareSetValue: PgCfgModel__OptionHandlerToPrepareSetValue
        PrepareGetValue: PgCfgModel__OptionHandlerToPrepareGetValue
        PrepareSetValueItem: PgCfgModel__OptionHandlerToPrepareSetValueItem
        SetValue: PgCfgModel__OptionHandlerToSetValue
        GetValue: PgCfgModel__OptionHandlerToGetValue
        AddOption: PgCfgModel__OptionHandlerToAddOption
        SetValueItem: PgCfgModel__OptionHandlerToSetValueItem
        Write: PgCfgModel__OptionHandlerToWrite

        # ----------------------------------------------------------------
        def __init__(
            self,
            prepareSetValue: PgCfgModel__OptionHandlerToPrepareSetValue,
            prepareGetValue: PgCfgModel__OptionHandlerToPrepareGetValue,
            prepareSetValueItem: PgCfgModel__OptionHandlerToPrepareSetValueItem,
            setValue: PgCfgModel__OptionHandlerToSetValue,
            getValue: PgCfgModel__OptionHandlerToGetValue,
            addIntoFile: PgCfgModel__OptionHandlerToAddOption,
            setValueItem: PgCfgModel__OptionHandlerToSetValueItem,
            write: PgCfgModel__OptionHandlerToGetValue,
        ):
            assert prepareSetValue is None or isinstance(
                prepareSetValue, PgCfgModel__OptionHandlerToPrepareSetValue
            )
            assert prepareGetValue is None or isinstance(
                prepareGetValue, PgCfgModel__OptionHandlerToPrepareGetValue
            )
            assert prepareSetValueItem is None or isinstance(
                prepareSetValueItem, PgCfgModel__OptionHandlerToPrepareSetValueItem
            )
            assert setValue is None or isinstance(
                setValue, PgCfgModel__OptionHandlerToSetValue
            )
            assert getValue is None or isinstance(
                getValue, PgCfgModel__OptionHandlerToGetValue
            )
            assert setValueItem is None or isinstance(
                setValueItem, PgCfgModel__OptionHandlerToSetValueItem
            )
            assert addIntoFile is None or isinstance(
                addIntoFile, PgCfgModel__OptionHandlerToAddOption
            )
            assert write is None or isinstance(write, PgCfgModel__OptionHandlerToWrite)

            self.PrepareSetValue = prepareSetValue
            self.PrepareGetValue = prepareGetValue
            self.PrepareSetValueItem = prepareSetValueItem
            self.SetValue = setValue
            self.AddOption = addIntoFile
            self.GetValue = getValue
            self.SetValueItem = setValueItem
            self.Write = write

    # --------------------------------------------------------------------
    # fmt: off
    sm_OptionHandlers__Std__Generic = \
        tagOptionHandlers(
            sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Generic,
            sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Generic,
            None,
            sm_SingleInstance__OptionHandlerToSetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToGetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToAddOption__Std,
            None,
            sm_SingleInstance__OptionHandlerToWrite__Std__Generic,
        )

    sm_OptionHandlers__Std__Int = \
        tagOptionHandlers(
            sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Int,
            sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Int,
            None,
            sm_SingleInstance__OptionHandlerToSetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToGetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToAddOption__Std,
            None,
            sm_SingleInstance__OptionHandlerToWrite__Std__Int,
        )

    sm_OptionHandlers__Std__Str = \
        tagOptionHandlers(
            sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Str,
            sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Str,
            None,
            sm_SingleInstance__OptionHandlerToSetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToGetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToAddOption__Std,
            None,
            sm_SingleInstance__OptionHandlerToWrite__Std__Str,
        )

    sm_OptionHandlers__Std__Bool = \
        tagOptionHandlers(
            sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__Bool,
            sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__Bool,
            None,
            sm_SingleInstance__OptionHandlerToSetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToGetValue__Std__Simple,
            sm_SingleInstance__OptionHandlerToAddOption__Std,
            None,
            sm_SingleInstance__OptionHandlerToWrite__Std__Bool,
        )

    sm_OptionHandlers__Std__UniqueStrList = \
        tagOptionHandlers(
            sm_SingleInstance__OptionHandlerToPrepareSetValue__Std__UniqueStrList,
            sm_SingleInstance__OptionHandlerToPrepareGetValue__Std__UniqueStrList,
            sm_SingleInstance__OptionHandlerToPrepareSetValueItem__Std__Str,
            None,
            sm_SingleInstance__OptionHandlerToGetValue__Std__UnionList,
            sm_SingleInstance__OptionHandlerToAddOption__Std,
            sm_SingleInstance__OptionHandlerToSetValueItem__Std__Unique,
            sm_SingleInstance__OptionHandlerToWrite__Std__UniqueStrList,
        )
    # fmt: on

    # --------------------------------------------------------------------
    sm_OptionHandlers: dict[str, tagOptionHandlers] = {
        # fmt: off
        # STANDARD -------------------------------------------------------
        "port": sm_OptionHandlers__Std__Int,
        "listen_addresses": sm_OptionHandlers__Std__Str,
        "shared_preload_libraries": sm_OptionHandlers__Std__UniqueStrList,
        "restart_after_crash": sm_OptionHandlers__Std__Bool,

        # PROXIMA --------------------------------------------------------
        "proxima.port": sm_OptionHandlers__Std__Int,
        # fmt: on
    }

    # --------------------------------------------------------------------
    def __init__(self, data_dir: str, cfgOsOps: ConfigurationOsOps = None):
        assert type(data_dir) == str
        assert cfgOsOps is None or isinstance(cfgOsOps, ConfigurationOsOps)

        if cfgOsOps is None:
            cfgOsOps = LocalCfgOsOps

        assert isinstance(cfgOsOps, ConfigurationOsOps)

        super().__init__(data_dir, LocalCfgOsOps)

    # --------------------------------------------------------------------
    @staticmethod
    def Create(data_dir: str) -> PostgresConfiguration_Std:
        assert type(data_dir) == str
        assert isinstance(LocalCfgOsOps, ConfigurationOsOps)
        return __class__(data_dir, LocalCfgOsOps)

    # --------------------------------------------------------------------
    @staticmethod
    def CreateWithCfgOsOps(
        data_dir: str,
        cfgOsOps: ConfigurationOsOps
    ) -> PostgresConfiguration_Std:
        assert type(data_dir) == str
        assert isinstance(cfgOsOps, ConfigurationOsOps)
        return __class__(data_dir, cfgOsOps)

    # PostgresConfiguration_Base interface -------------------------------
    def Internal__GetAutoConfFileName(self):
        assert type(__class__.C_POSTGRESQL_AUTO_CONF) == str
        assert __class__.C_POSTGRESQL_AUTO_CONF != ""
        return __class__.C_POSTGRESQL_AUTO_CONF

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToPrepareSetValue:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.PrepareSetValue is None:
            BugCheckError.OptionHandlerToPrepareSetValueIsNotDefined(name)

        assert isinstance(
            optionHandlers.PrepareSetValue, PgCfgModel__OptionHandlerToPrepareSetValue
        )

        return optionHandlers.PrepareSetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareGetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToPrepareSetValue:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.PrepareGetValue is None:
            BugCheckError.OptionHandlerToPrepareGetValueIsNotDefined(name)

        assert isinstance(
            optionHandlers.PrepareGetValue, PgCfgModel__OptionHandlerToPrepareGetValue
        )

        return optionHandlers.PrepareGetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValueItem(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToPrepareSetValueItem:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.PrepareSetValueItem is None:
            BugCheckError.OptionHandlerToPrepareSetValueItemIsNotDefined(name)

        assert isinstance(
            optionHandlers.PrepareSetValueItem,
            PgCfgModel__OptionHandlerToPrepareSetValueItem,
        )

        return optionHandlers.PrepareSetValueItem

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToSetValue:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.SetValue is None:
            BugCheckError.OptionHandlerToSetValueIsNotDefined(name)

        assert isinstance(optionHandlers.SetValue, PgCfgModel__OptionHandlerToSetValue)

        return optionHandlers.SetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToGetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToGetValue:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.GetValue is None:
            BugCheckError.OptionHandlerToGetValueIsNotDefined(name)

        assert isinstance(optionHandlers.GetValue, PgCfgModel__OptionHandlerToGetValue)

        return optionHandlers.GetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToAddOption(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToAddOption:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.AddOption is None:
            BugCheckError.OptionHandlerToAddOptionIsNotDefined(name)

        assert isinstance(
            optionHandlers.AddOption, PgCfgModel__OptionHandlerToAddOption
        )

        return optionHandlers.AddOption

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValueItem(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToSetValueItem:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.SetValueItem is None:
            BugCheckError.OptionHandlerToSetValueIsNotDefined(name)

        assert isinstance(
            optionHandlers.SetValueItem, PgCfgModel__OptionHandlerToSetValueItem
        )

        return optionHandlers.SetValueItem

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToWrite(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToWrite:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) == __class__.tagOptionHandlers

        if optionHandlers.Write is None:
            BugCheckError.OptionHandlerToWriteIsNotDefined(name)

        assert isinstance(optionHandlers.Write, PgCfgModel__OptionHandlerToWrite)

        return optionHandlers.Write

    # Helper methods -----------------------------------------------------
    def Helper__GetOptionHandlers(self, name: str) -> tagOptionHandlers:
        assert type(name) == str
        assert type(self.sm_OptionHandlers) == dict

        if not (name in self.sm_OptionHandlers.keys()):
            return __class__.sm_OptionHandlers__Std__Generic

        optionHandlers = self.sm_OptionHandlers[name]

        assert optionHandlers is not None
        assert type(optionHandlers) == __class__.tagOptionHandlers

        return self.sm_OptionHandlers[name]


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationReader_Std


class PostgresConfigurationReader_Std:
    def LoadConfiguration(cfg: PostgresConfiguration_Std) -> None:
        assert isinstance(cfg, PostgresConfiguration_Std)

        # We expect that both files exist
        PostgresConfigurationReader_Base.LoadConfigurationFile(
            cfg, cfg.C_POSTGRESQL_CONF
        )
        PostgresConfigurationReader_Base.LoadConfigurationFile(
            cfg, cfg.C_POSTGRESQL_AUTO_CONF
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriter_Std


class PostgresConfigurationWriter_Std:
    def WriteConfiguration(cfg: PostgresConfiguration_Std) -> None:
        assert isinstance(cfg, PostgresConfiguration_Std)

        writeCtx = PostgresConfigurationWriterCtx_Base(cfg)

        PostgresConfigurationWriter_Base.DoWork(writeCtx)


# //////////////////////////////////////////////////////////////////////////////
