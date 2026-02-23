# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationInclude_Base as PgCfg_Include_Base
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

        include = fileLine.AddInclude("a.conf", None)

        assert len(fileLine) == 1

        assert type(include) is PgCfg_Include_Base

        include.Delete(True)

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_Configuration()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_Parent()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_File()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.Delete(True)

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

        include = fileLine.AddInclude("a.conf", None)

        assert len(fileLine) == 1

        assert type(include) is PgCfg_Include_Base

        include.Delete(False)

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_Configuration()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_Parent()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_File()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.Delete(False)

        assert fileLine.m_FileLineData.IsAlive()

        assert fileLine.get_Configuration() is cfg

        assert fileLine.get_Parent() is file

        assert len(fileLine) == 0

    # --------------------------------------------------------------------

    def test_003__line_with_comment__delete_withLine(
        self, request: pytest.FixtureRequest
    ):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        include = fileLine.AddInclude("a.conf", None)
        comment = fileLine.AddComment("aaa", None)

        assert len(fileLine) == 2

        assert type(include) is PgCfg_Include_Base

        include.Delete(True)

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_Configuration()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_Parent()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.get_File()

        with pytest.raises(Exception, match=re.escape("Include object was deleted.")):
            include.Delete(True)

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Configuration()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Parent()

        with pytest.raises(Exception, match=re.escape("Comment object was deleted.")):
            comment.get_Text()

        with pytest.raises(Exception, match=re.escape("FileLine object was deleted.")):
            fileLine.get_Configuration()

        with pytest.raises(Exception, match=re.escape("FileLine object was deleted.")):
            fileLine.get_Parent()

        with pytest.raises(Exception, match=re.escape("FileLine object was deleted.")):
            len(fileLine)


# //////////////////////////////////////////////////////////////////////////////
