# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__withLine(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment")

        assert len(fileLine) == 1

        assert type(comment) is PgCfg_Comment_Base

        comment.Delete(True)

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
            comment.Delete(True)

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

    # --------------------------------------------------------------------
    def test_002__withoutLine(
        self,
        request: pytest.FixtureRequest,
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(rootTmpDir)

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment")

        assert len(fileLine) == 1

        assert type(comment) is PgCfg_Comment_Base

        comment.Delete(False)

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
            comment.Delete(False)

        assert str(x.value) == ErrorMessageBuilder.CommentObjectWasDeleted()

        assert fileLine.get_Configuration() is cfg

        assert fileLine.get_Parent() is file

        assert len(fileLine) == 0
        return


# //////////////////////////////////////////////////////////////////////////////
