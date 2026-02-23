# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std
from src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
# fmt: on

from .......TestServices import TestServices

import pytest
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__withLine(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment")

        assert len(fileLine) == 1

        assert type(comment) is PgCfg_Comment_Base

        comment.Delete(True)

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Configuration()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Parent()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Text()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.Delete(True)

        with pytest.raises(Exception, match=re.escape("FileLine object was deleted.")):
            fileLine.get_Configuration()

        with pytest.raises(Exception, match=re.escape("FileLine object was deleted.")):
            fileLine.get_Parent()

        with pytest.raises(Exception, match=re.escape("FileLine object was deleted.")):
            len(fileLine)

    # --------------------------------------------------------------------
    def test_002__withoutLine(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment")

        assert len(fileLine) == 1

        assert type(comment) is PgCfg_Comment_Base

        comment.Delete(False)

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Configuration()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Parent()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Text()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.Delete(False)

        assert fileLine.get_Configuration() is cfg

        assert fileLine.get_Parent() is file

        assert len(fileLine) == 0


# //////////////////////////////////////////////////////////////////////////////
