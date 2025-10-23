# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base

from src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from src.implementation.v00.configuration_base import PgCfgModel__CommentData

from src.abstract.v00.configuration import PostgresConfigurationComment as PgCfg_Comment
from src.abstract.v00.configuration import PostgresConfigurationFileLines as PgCfg_FileLines
from src.abstract.v00.configuration import PostgresConfigurationFile as PgCfg_File
# fmt: on

from .......TestServices import TestServices

import pytest
import os
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        cfg.SetOptionValue("port", 123)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().__iter__().__next__()
        assert file is not None
        assert type(file) == PgCfg_TopLevelFile_Base

        assert file.get_Path() == os.path.join(rootTmpDir, "postgresql.auto.conf")

        fileLines = file.get_Lines()
        assert fileLines is not None
        assert type(fileLines) == PgCfg_FileLines_Base
        assert isinstance(fileLines, PgCfg_FileLines)

        assert len(fileLines) == 1

        comment2 = file.AddComment("HELLO!")
        assert comment2 is not None
        assert type(comment2) == PgCfg_Comment_Base
        assert isinstance(comment2, PgCfg_Comment)

        assert len(fileLines) == 2
        fileLines_v: list[PgCfg_FileLine_Base] = list(fileLines)
        assert len(fileLines_v) == 2
        assert type(fileLines_v[-1]) == PgCfg_FileLine_Base
        assert type(fileLines_v[-1].m_FileLineData) == PgCfgModel__FileLineData
        assert type(fileLines_v[-1].m_FileLineData.m_Items) == list
        assert len(fileLines_v[-1].m_FileLineData.m_Items) == 1
        assert (
            type(fileLines_v[-1].m_FileLineData.m_Items[0])
            == PgCfgModel__FileLineData.tagItem
        )
        assert (
            type(fileLines_v[-1].m_FileLineData.m_Items[0].m_Element)
            == PgCfgModel__CommentData
        )
        assert fileLines_v[-1].m_FileLineData.m_Items[0].m_Element.m_Offset is None
        assert fileLines_v[-1].m_FileLineData.m_Items[0].m_Element.m_Text == "HELLO!"
        assert (
            fileLines_v[-1].m_FileLineData.m_Items[0].m_Element.m_Parent
            is fileLines_v[-1].m_FileLineData
        )

        assert (
            fileLines_v[-1].m_FileLineData.m_Items[0].m_Element
            is comment2.m_CommentData
        )

        assert comment2.get_Configuration() is cfg
        assert comment2.get_Parent().get_Parent().get_Configuration() is cfg
        assert comment2.get_Parent().get_Parent().get_Parent() is cfg
        assert comment2.get_Text() == "HELLO!"

        assert cfg.GetOptionValue("port") == 123

    # --------------------------------------------------------------------
    def test_002(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        cfg.SetOptionValue("port", 123)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().__iter__().__next__()
        assert file is not None
        assert type(file) == PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert len(file) == 1

        comment1 = file.AddComment("1")
        assert comment1 is not None
        assert type(comment1) == PgCfg_Comment_Base
        assert isinstance(comment1, PgCfg_Comment)
        assert comment1.get_Text() == "1"
        assert len(file) == 2

        comment2 = file.AddComment("")
        assert comment2 is not None
        assert type(comment2) == PgCfg_Comment_Base
        assert isinstance(comment2, PgCfg_Comment)
        assert comment2.get_Text() == ""
        assert len(file) == 3

        assert comment1.get_Text() == "1"

        invalidSymbols = "\r\n\0"

        for ch in invalidSymbols:
            with pytest.raises(
                Exception, match=re.escape("Comment text contains invalid symbols.")
            ):
                file.AddComment("1234" + ch)

            assert len(file) == 3

            assert comment1.get_Text() == "1"
            assert comment2.get_Text() == ""


# //////////////////////////////////////////////////////////////////////////////
