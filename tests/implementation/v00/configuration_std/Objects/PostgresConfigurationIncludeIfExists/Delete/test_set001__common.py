# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationIncludeIfExists_Base as PgCfg_IncludeIfExists_Base
from src.implementation.v00.configuration_base import AddIncludeIfExistsRule as PgCfg_AddIncludeIfExistsRule
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

from src.exceptions import PostgresConfigException

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__withLine(
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

        include = fileLine.AddIncludeIfExists(
            "a.conf",
            None,
            PgCfg_AddIncludeIfExistsRule.with_file,
        )

        assert len(fileLine) == 1

        assert type(include) is PgCfg_IncludeIfExists_Base
        assert include.get_File() is not None
        assert len(cfg.get_AllFiles()) == 2

        include.Delete(True)

        with pytest.raises(PostgresConfigException) as x:
            include.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.get_Parent()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.get_File()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.Delete(True)

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            fileLine.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            fileLine.get_Parent()

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            len(fileLine)

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_002__withoutLine(
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

        include = fileLine.AddIncludeIfExists(
            "a.conf",
            None,
            PgCfg_AddIncludeIfExistsRule.with_file,
        )

        assert len(fileLine) == 1

        assert type(include) is PgCfg_IncludeIfExists_Base
        assert include.get_File() is not None
        assert len(cfg.get_AllFiles()) == 2

        include.Delete(False)

        with pytest.raises(PostgresConfigException) as x:
            include.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.get_Parent()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.get_File()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.Delete(False)

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        assert fileLine.m_FileLineData.IsAlive()

        assert fileLine.get_Configuration() is cfg

        assert fileLine.get_Parent() is file

        assert len(fileLine) == 0
        return

    # --------------------------------------------------------------------

    def test_003__line_with_comment__delete_withLine(
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

        include = fileLine.AddIncludeIfExists(
            "a.conf",
            None,
            PgCfg_AddIncludeIfExistsRule.with_file,
        )
        comment = fileLine.AddComment(
            "aaa",
            None,
        )

        assert len(fileLine) == 2

        assert type(include) is PgCfg_IncludeIfExists_Base
        assert include.get_File() is not None
        assert len(cfg.get_AllFiles()) == 2

        include.Delete(True)

        with pytest.raises(PostgresConfigException) as x:
            include.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.get_Parent()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.get_File()

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            include.Delete(True)

        assert str(x.value) == ErrorMessageBuilder.IncludeIfExistsObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            comment.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.CommentObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            comment.get_Parent()

        assert str(x.value) == ErrorMessageBuilder.CommentObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            comment.get_Text()

        assert str(x.value) == ErrorMessageBuilder.CommentObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            fileLine.get_Configuration()

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            fileLine.get_Parent()

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()

        with pytest.raises(PostgresConfigException) as x:
            len(fileLine)

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()
        return


# //////////////////////////////////////////////////////////////////////////////
