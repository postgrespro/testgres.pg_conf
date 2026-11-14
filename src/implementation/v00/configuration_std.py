# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from .configuration_base import PostgresConfiguration_Base
from .configuration_base import PostgresConfigurationFile
from .configuration_base import PgCfgModel__OptionHandlerToPrepareSetValue
from .configuration_base import PgCfgModel__OptionHandlerToPrepareSetValueItem
from .configuration_base import PgCfgModel__OptionHandlerToPrepareGetValue
from .configuration_base import PgCfgModel__OptionHandlerToSetValue
from .configuration_base import PgCfgModel__OptionHandlerToGetValue
from .configuration_base import PgCfgModel__OptionHandlerToAddOption
from .configuration_base import PgCfgModel__OptionHandlerToSetValueItem
from .configuration_base import PgCfgModel__OptionHandlerToWrite

from .configuration_base_r import PostgresConfigurationReader_Base

from .configuration_base_w import PostgresConfigurationWriter_Base
from .configuration_base_w import PostgresConfigurationWriterCtx_Base

from .configuration_base_ds_strict import g_PgCfgBaseDataStrategy__Strict
from .configuration_base_ds_standard import g_PgCfgBaseDataStrategy__Standard

from ...core.option.handlers.instances import g_OptionHandlers__Std__Bool
from ...core.option.handlers.instances import g_OptionHandlers__Std__Int
from ...core.option.handlers.instances import g_OptionHandlers__Std__Str
from ...core.option.handlers.instances import g_OptionHandlers__Std__UniqueStrList
from ...core.option.handlers.instances import g_OptionHandlers__Std__Generic
from ...core.option.handlers.instances import PostgresConfigurationOptionHandlers

from ...os.abstract.configuration_os_ops import ConfigurationOsOps
from ...os.local.configuration_os_ops import SingleInstance as LocalCfgOsOps

from ...core.bugcheck_error import BugCheckError

import typing
import enum

# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Std


class PostgresConfiguration_Std(PostgresConfiguration_Base):
    class Strategy(enum.Enum):
        Standard = "Standard"
        Strict = "Strict"

    # --------------------------------------------------------------------
    C_POSTGRESQL_CONF = "postgresql.conf"
    C_POSTGRESQL_AUTO_CONF = "postgresql.auto.conf"

    # --------------------------------------------------------------------
    sm_OptionHandlers: typing.Dict[
        str,
        PostgresConfigurationOptionHandlers,
    ] = {
        # fmt: off
        # STANDARD -------------------------------------------------------
        "port": g_OptionHandlers__Std__Int,
        "listen_addresses": g_OptionHandlers__Std__Str,
        "shared_preload_libraries": g_OptionHandlers__Std__UniqueStrList,
        "restart_after_crash": g_OptionHandlers__Std__Bool,
        "max_connections": g_OptionHandlers__Std__Int,

        # PROXIMA ------------------------------------------------------------
        "proxima.port": g_OptionHandlers__Std__Int,
        "proxima.pool_size": g_OptionHandlers__Std__Int,

        # BIHA ------------------------------------------------------------
        "biha.node_id": g_OptionHandlers__Std__Int,
        # fmt: on
    }

    # --------------------------------------------------------------------
    def __init__(
        self,
        data_dir: str,
        cfgOsOps: typing.Optional[ConfigurationOsOps] = None,
        strategy: Strategy = Strategy.Standard,
    ):
        assert type(data_dir) is str
        assert cfgOsOps is None or isinstance(cfgOsOps, ConfigurationOsOps)

        if cfgOsOps is None:
            cfgOsOps = LocalCfgOsOps

        assert isinstance(cfgOsOps, ConfigurationOsOps)

        dataStrategy = __class__.Helper__GetDataStrategy(
            strategy,
        )
        assert dataStrategy is not None

        super().__init__(
            data_dir,
            cfgOsOps,
            dataStrategy,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Create(
        data_dir: str,
    ) -> PostgresConfiguration_Std:
        assert type(data_dir) is str
        assert isinstance(LocalCfgOsOps, ConfigurationOsOps)
        return __class__(data_dir, LocalCfgOsOps)

    # --------------------------------------------------------------------
    @staticmethod
    def CreateWithCfgOsOps(
        data_dir: str,
        cfgOsOps: ConfigurationOsOps,
    ) -> PostgresConfiguration_Std:
        assert type(data_dir) is str
        assert isinstance(cfgOsOps, ConfigurationOsOps)
        return __class__(data_dir, cfgOsOps)

    # PostgresConfiguration_Base interface -------------------------------
    def Internal__GetAutoConfFileName(
        self,
    ) -> str:
        assert type(__class__.C_POSTGRESQL_AUTO_CONF) is str
        assert __class__.C_POSTGRESQL_AUTO_CONF != ""
        return __class__.C_POSTGRESQL_AUTO_CONF

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToPrepareSetValue:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.PrepareSetValue is None:
            BugCheckError.OptionHandlerToPrepareSetValueIsNotDefined(name)

        assert isinstance(
            optionHandlers.PrepareSetValue,
            PgCfgModel__OptionHandlerToPrepareSetValue,
        )

        return optionHandlers.PrepareSetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareGetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToPrepareGetValue:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.PrepareGetValue is None:
            BugCheckError.OptionHandlerToPrepareGetValueIsNotDefined(name)

        assert isinstance(
            optionHandlers.PrepareGetValue,
            PgCfgModel__OptionHandlerToPrepareGetValue,
        )

        return optionHandlers.PrepareGetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValueItem(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToPrepareSetValueItem:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.PrepareSetValueItem is None:
            BugCheckError.OptionHandlerToPrepareSetValueItemIsNotDefined(name)

        assert isinstance(
            optionHandlers.PrepareSetValueItem,
            PgCfgModel__OptionHandlerToPrepareSetValueItem,
        )

        return optionHandlers.PrepareSetValueItem

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToSetValue:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.SetValue is None:
            BugCheckError.OptionHandlerToSetValueIsNotDefined(name)

        assert isinstance(optionHandlers.SetValue, PgCfgModel__OptionHandlerToSetValue)

        return optionHandlers.SetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToGetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToGetValue:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.GetValue is None:
            BugCheckError.OptionHandlerToGetValueIsNotDefined(name)

        assert isinstance(optionHandlers.GetValue, PgCfgModel__OptionHandlerToGetValue)

        return optionHandlers.GetValue

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToAddOption(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToAddOption:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.AddOption is None:
            BugCheckError.OptionHandlerToAddOptionIsNotDefined(name)

        assert isinstance(
            optionHandlers.AddOption,
            PgCfgModel__OptionHandlerToAddOption,
        )

        return optionHandlers.AddOption

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValueItem(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToSetValueItem:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.SetValueItem is None:
            BugCheckError.OptionHandlerToSetValueIsNotDefined(name)

        assert isinstance(
            optionHandlers.SetValueItem,
            PgCfgModel__OptionHandlerToSetValueItem,
        )

        return optionHandlers.SetValueItem

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToWrite(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToWrite:
        assert type(name) is str

        optionHandlers = self.Helper__GetOptionHandlers(name)
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        if optionHandlers.Write is None:
            BugCheckError.OptionHandlerToWriteIsNotDefined(name)

        assert isinstance(optionHandlers.Write, PgCfgModel__OptionHandlerToWrite)

        return optionHandlers.Write

    # Helper methods -----------------------------------------------------
    @staticmethod
    def Helper__GetDataStrategy(
        strategy: Strategy,
    ) -> PostgresConfiguration_Base.tagDataStrategy:
        assert type(strategy) is __class__.Strategy

        if strategy == __class__.Strategy.Standard:
            return g_PgCfgBaseDataStrategy__Standard

        if strategy == __class__.Strategy.Strict:
            return g_PgCfgBaseDataStrategy__Strict

        BugCheckError.UnsupportedPgConfStrategy(
            strategy,
        )

    # --------------------------------------------------------------------
    def Helper__GetOptionHandlers(
        self,
        name: str,
    ) -> PostgresConfigurationOptionHandlers:
        assert type(name) is str
        assert type(__class__.sm_OptionHandlers) is dict

        optionHandlers = __class__.sm_OptionHandlers.get(name)

        if optionHandlers is None:
            return g_OptionHandlers__Std__Generic

        assert optionHandlers is not None
        assert type(optionHandlers) is PostgresConfigurationOptionHandlers

        return __class__.sm_OptionHandlers[name]


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationReader_Std


class PostgresConfigurationReader_Std:
    @staticmethod
    def LoadConfiguration(
        cfg: PostgresConfiguration_Std,
    ) -> None:
        assert isinstance(cfg, PostgresConfiguration_Std)

        # We expect that both files exist
        __class__.LoadConfigurationFile(
            cfg,
            cfg.C_POSTGRESQL_CONF,
        )
        __class__.LoadConfigurationFile(
            cfg,
            cfg.C_POSTGRESQL_AUTO_CONF,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def LoadConfigurationFile(
        cfg: PostgresConfiguration_Std,
        filePath: str,
    ) -> PostgresConfigurationFile:
        assert isinstance(cfg, PostgresConfiguration_Std)
        assert type(filePath) is str

        return PostgresConfigurationReader_Base.LoadConfigurationFile(
            cfg,
            filePath,
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriter_Std


class PostgresConfigurationWriter_Std:
    @staticmethod
    def WriteConfiguration(cfg: PostgresConfiguration_Std) -> None:
        assert isinstance(cfg, PostgresConfiguration_Std)

        writeCtx = PostgresConfigurationWriterCtx_Base(cfg)

        PostgresConfigurationWriter_Base.DoWork(writeCtx)
        return


# //////////////////////////////////////////////////////////////////////////////
