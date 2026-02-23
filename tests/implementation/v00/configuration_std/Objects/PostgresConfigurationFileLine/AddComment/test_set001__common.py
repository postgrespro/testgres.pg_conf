# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base

from src.implementation.v00.configuration_base import PgCfgModel__CommentData
# fmt: on

from .......TestServices import TestServices

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
    def offset001(self, request: pytest.FixtureRequest) -> typing.Optional[int]:
        assert isinstance(request, pytest.FixtureRequest)
        assert request.param is None or type(request.param) == int  # noqa: E721
        return request.param

    # --------------------------------------------------------------------
    def test_001(self, request: pytest.FixtureRequest, offset001: typing.Optional[int]):
        assert isinstance(request, pytest.FixtureRequest)
        assert offset001 is None or type(offset001) == int  # noqa: E721

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment", offset001)

        assert len(fileLine) == 1

        assert comment is not None
        assert type(comment) == PgCfg_Comment_Base  # noqa: E721
        assert comment.m_FileLine is fileLine
        assert type(comment.m_CommentData) == PgCfgModel__CommentData  # noqa: E721
        assert comment.m_CommentData.m_Offset == offset001

        assert comment.m_CommentData.IsAlive()
        assert comment.m_CommentData.m_Text == "comment"
        assert comment.m_CommentData.m_Parent == fileLine.m_FileLineData

        assert comment.get_Configuration() is cfg
        assert comment.get_Parent() is fileLine
        assert comment.get_Text() == "comment"

    # --------------------------------------------------------------------
    def test_E01__second_comment_in_line(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment", 3)

        assert len(fileLine) == 1

        with pytest.raises(Exception, match="File line already has a comment."):
            fileLine.AddComment("comment2", 4)

        assert comment is not None
        assert type(comment) == PgCfg_Comment_Base  # noqa: E721
        assert comment.m_FileLine is fileLine
        assert type(comment.m_CommentData) == PgCfgModel__CommentData  # noqa: E721
        assert comment.m_CommentData.m_Offset == 3

        assert comment.m_CommentData.IsAlive()
        assert comment.m_CommentData.m_Text == "comment"
        assert comment.m_CommentData.m_Parent == fileLine.m_FileLineData

        assert comment.get_Configuration() is cfg
        assert comment.get_Parent() is fileLine
        assert comment.get_Text() == "comment"

    # --------------------------------------------------------------------
    def test_E02__bad_symbol(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        with pytest.raises(Exception, match="Comment text contains invalid symbols."):
            fileLine.AddComment("\0", 4)


# //////////////////////////////////////////////////////////////////////////////
