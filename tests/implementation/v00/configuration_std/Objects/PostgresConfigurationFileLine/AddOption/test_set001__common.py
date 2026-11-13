# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base

from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import typing

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_data001__offsets: typing.List[typing.Optional[int]] = [None, 1, 2, 3, 10]

    # --------------------------------------------------------------------
    @pytest.fixture(
        params=sm_data001__offsets,
        ids=[
            ("offset_" + (str(x) if x is not None else "None"))
            for x in sm_data001__offsets
        ],
    )
    def offset001(
        self,
        request: pytest.FixtureRequest,
    ) -> typing.Optional[int]:
        assert isinstance(request, pytest.FixtureRequest)
        assert request.param is None or type(request.param) is int
        return request.param

    # --------------------------------------------------------------------
    def test_001(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        offset001: typing.Optional[int],
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert offset001 is None or type(offset001) is int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        option = fileLine.AddOption("port", 123, offset001)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == offset001

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123
        return

    # --------------------------------------------------------------------
    def test_002__shared_preload_libraries(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        offset001: typing.Optional[int],
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert offset001 is None or type(offset001) is int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_OPT_NAME = "shared_preload_libraries"

        optValue_set = ["a", "b", "c"]
        optValue_get = optValue_set.copy()

        option = fileLine.AddOption(C_OPT_NAME, optValue_set, offset001)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == offset001

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == C_OPT_NAME
        assert option.m_OptionData.m_Value == optValue_get
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == optValue_get
        return

    # --------------------------------------------------------------------
    def test_003__shared_preload_libraries__as_str(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        offset001: typing.Optional[int],
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert offset001 is None or type(offset001) is int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_OPT_NAME = "shared_preload_libraries"

        optValue_set = '"a", "b", "c"'
        optValue_get = ["a", "b", "c"]

        option = fileLine.AddOption(C_OPT_NAME, optValue_set, offset001)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == offset001

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == C_OPT_NAME
        assert option.m_OptionData.m_Value == optValue_get
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == C_OPT_NAME
        assert option.get_Value() == optValue_get
        return

    # --------------------------------------------------------------------
    def test_004__shared_preload_libraries__with_None_item(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_OPT_NAME = "shared_preload_libraries"

        optValue_set = ["a", None, "c"]

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddOption(C_OPT_NAME, optValue_set, None)

        assert str(x.value) == ErrorMessageBuilder.NoneOptionValueItemIsNotSupported(
            "shared_preload_libraries",
        )
        assert len(fileLine) == 0
        return

    # --------------------------------------------------------------------
    def test_E01__after_option(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        option = fileLine.AddOption("port", 123, 2)

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddOption("proxima.port", 321, 432)

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasOption(
            "port",
        )
        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123
        return

    # --------------------------------------------------------------------
    def test_E02__after_include(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        include = file.AddInclude(cfg.C_POSTGRESQL_AUTO_CONF)

        fileLine = include.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddOption("proxima.port", 321, 11)

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasIncludeDirective()
        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is include.m_IncludeData
        return

    # --------------------------------------------------------------------
    def test_E03__after_comment(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        comment = file.AddComment("comment")

        fileLine = comment.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddOption("proxima.port", 321, 11)

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasComment()
        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is comment.m_CommentData
        return

    # --------------------------------------------------------------------
    def test_X04__00A__conflict_with_this_file__Strict(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Standard:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()
        assert len(fileLine) == 0
        option = fileLine.AddOption("port", 123, 2)

        fileLine2 = file.AddEmptyLine()
        assert len(fileLine2) == 0

        with pytest.raises(PostgresConfigException) as x:
            fileLine2.AddOption("port", 321, 22)

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInThisFile(
            file.get_Path(),
            "port",
        )
        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123
        return

    # --------------------------------------------------------------------
    def test_X04__00B__conflict_with_this_file__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine1 = file.AddEmptyLine()
        assert len(fileLine1) == 0
        option1 = fileLine1.AddOption("port", 123, 2)

        fileLine2 = file.AddEmptyLine()
        assert len(fileLine2) == 0
        option2 = fileLine2.AddOption("port", 321, 22)

        assert len(fileLine1) == 1
        assert len(fileLine2) == 1

        assert option1.m_OptionData.IsAlive()
        assert fileLine1.m_FileLineData.IsAlive()
        assert fileLine1.m_FileLineData.m_Parent is not None
        assert fileLine1.m_FileLineData.m_Parent.IsAlive()

        assert option2.m_OptionData.IsAlive()
        assert fileLine2.m_FileLineData.IsAlive()
        assert fileLine2.m_FileLineData.m_Parent is not None
        assert fileLine2.m_FileLineData.m_Parent.IsAlive()

        assert fileLine1.m_FileLineData is not fileLine2.m_FileLineData
        assert option1.m_OptionData is not option2.m_OptionData
        assert fileLine1.m_FileLineData.m_Parent is fileLine2.m_FileLineData.m_Parent

        # -------------
        assert option1 is not None
        assert type(option1) is PgCfg_Option_Base
        assert option1.m_FileLine.m_FileLineData is fileLine1.m_FileLineData
        assert type(option1.m_OptionData) is PgCfgModel__OptionData
        assert option1.m_OptionData.m_Offset == 2

        assert option1.m_OptionData.IsAlive()
        assert option1.m_OptionData.m_Name == "port"
        assert option1.m_OptionData.m_Value == 123
        assert option1.m_OptionData.m_Parent == fileLine1.m_FileLineData

        assert option1.get_Configuration() is cfg
        assert option1.get_Parent().m_FileLineData is fileLine1.m_FileLineData
        assert option1.get_Name() == "port"
        assert option1.get_Value() == 123

        # -------------
        assert option2 is not None
        assert type(option2) is PgCfg_Option_Base
        assert option2.m_FileLine.m_FileLineData is fileLine2.m_FileLineData
        assert type(option2.m_OptionData) is PgCfgModel__OptionData
        assert option2.m_OptionData.m_Offset == 22

        assert option2.m_OptionData.IsAlive()
        assert option2.m_OptionData.m_Name == "port"
        assert option2.m_OptionData.m_Value == 321
        assert option2.m_OptionData.m_Parent == fileLine2.m_FileLineData

        assert option2.get_Configuration() is cfg
        assert option2.get_Parent().m_FileLineData is fileLine2.m_FileLineData
        assert option2.get_Name() == "port"
        assert option2.get_Value() == 321

        return

    # --------------------------------------------------------------------
    def test_X05__00A__conflict_with_another_file__Strict(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Standard:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        fileLine = file.AddEmptyLine()
        assert len(fileLine) == 0
        option = fileLine.AddOption("port", 123, 2)

        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)
        fileLine2 = file2.AddEmptyLine()
        assert len(fileLine2) == 0

        with pytest.raises(PostgresConfigException) as x:
            fileLine2.AddOption("port", 321, 2)

        assert str(x.value) == ErrorMessageBuilder.OptionIsAlreadyExistInAnotherFile(
            file.get_Path(),
            "port",
        )
        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123
        return

    # --------------------------------------------------------------------
    def test_X05__00B__conflict_with_another_file__Standard(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy

        if pg_conf_strategy == PgCfg_Std.Strategy.Strict:
            TestServices.RaiseSkip_NotApplicable()

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        fileLine1 = file1.AddEmptyLine()
        assert len(fileLine1) == 0
        option1 = fileLine1.AddOption("port", 123, 2)
        assert option1 is not None
        assert len(fileLine1) == 1

        file2 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)
        fileLine2 = file2.AddEmptyLine()
        assert len(fileLine2) == 0
        option2 = fileLine2.AddOption("port", 321, 22)
        assert option2 is not None
        assert len(fileLine2) == 1

        # again
        assert len(fileLine1) == 1

        # ---------
        assert option1.m_OptionData.IsAlive()
        assert fileLine1.m_FileLineData.IsAlive()
        assert fileLine1.m_FileLineData.m_Parent is not None
        assert fileLine1.m_FileLineData.m_Parent.IsAlive()

        assert option2.m_OptionData.IsAlive()
        assert fileLine2.m_FileLineData.IsAlive()
        assert fileLine2.m_FileLineData.m_Parent is not None
        assert fileLine2.m_FileLineData.m_Parent.IsAlive()

        assert fileLine1.m_FileLineData is not fileLine2.m_FileLineData
        assert option1.m_OptionData is not option2.m_OptionData
        assert (
            fileLine1.m_FileLineData.m_Parent is not fileLine2.m_FileLineData.m_Parent
        )

        assert fileLine1.m_FileLineData.m_Parent is file1.m_FileData
        assert fileLine2.m_FileLineData.m_Parent is file2.m_FileData

        # ---------
        assert option1 is not None
        assert type(option1) is PgCfg_Option_Base
        assert option1.m_FileLine.m_FileLineData is fileLine1.m_FileLineData
        assert type(option1.m_OptionData) is PgCfgModel__OptionData
        assert option1.m_OptionData.m_Offset == 2

        assert option1.m_OptionData.IsAlive()
        assert option1.m_OptionData.m_Name == "port"
        assert option1.m_OptionData.m_Value == 123
        assert option1.m_OptionData.m_Parent == fileLine1.m_FileLineData

        assert option1.get_Configuration() is cfg
        assert option1.get_Parent().m_FileLineData is fileLine1.m_FileLineData
        assert option1.get_Name() == "port"
        assert option1.get_Value() == 123

        # ---------
        assert option2 is not None
        assert type(option2) is PgCfg_Option_Base
        assert option2.m_FileLine.m_FileLineData is fileLine2.m_FileLineData
        assert type(option2.m_OptionData) is PgCfgModel__OptionData
        assert option2.m_OptionData.m_Offset == 22

        assert option2.m_OptionData.IsAlive()
        assert option2.m_OptionData.m_Name == "port"
        assert option2.m_OptionData.m_Value == 321
        assert option2.m_OptionData.m_Parent == fileLine2.m_FileLineData

        assert option2.get_Configuration() is cfg
        assert option2.get_Parent().m_FileLineData is fileLine2.m_FileLineData
        assert option2.get_Name() == "port"
        assert option2.get_Value() == 321

        return


# //////////////////////////////////////////////////////////////////////////////
