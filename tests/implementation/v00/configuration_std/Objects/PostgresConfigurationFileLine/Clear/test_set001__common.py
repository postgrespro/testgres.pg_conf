# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base

from src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from src.implementation.v00.configuration_base import PgCfgModel__CommentData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData

from src.abstract.v00.configuration import PostgresConfigurationComment as PgCfg_Comment
from src.abstract.v00.configuration import PostgresConfigurationFileLine as PgCfg_FileLine
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
    def test_001__line_with_option(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        set_r = cfg.SetOptionValue("port", 123)
        assert set_r is not None
        assert type(set_r) is PgCfg_SetOptionResult_Base
        assert set_r.EventID == PgCfg_SetOptionEventID.OPTION_WAS_ADDED
        assert set_r.Option.get_Configuration() is cfg
        assert set_r.Option.get_Parent().get_Parent().get_Parent() is cfg
        assert set_r.Option.get_Name() == "port"
        assert set_r.Option.get_Value() == 123

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().__iter__().__next__()
        assert file is not None
        assert type(file) is PgCfg_TopLevelFile_Base

        assert file.get_Path() == os.path.join(rootTmpDir, "postgresql.auto.conf")

        fileLines = file.get_Lines()
        assert fileLines is not None
        assert type(fileLines) == PgCfg_FileLines_Base  # noqa: E721
        assert isinstance(fileLines, PgCfg_FileLines)

        assert len(fileLines) == 1

        fileLine = fileLines.__iter__().__next__()
        assert fileLine is not None
        assert type(fileLine) == PgCfg_FileLine_Base  # noqa: E721
        assert isinstance(fileLine, PgCfg_FileLine)

        assert len(fileLine) == 1

        assert set_r.m_OptData is not None
        assert type(set_r.m_OptData) is PgCfgModel__OptionData
        assert type(set_r.m_OptData.m_Parent) is PgCfgModel__FileLineData

        fileLine.Clear()

        assert len(fileLine) == 0

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            set_r.Option.get_Name()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            set_r.Option.get_Value()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            set_r.Option.set_Value(123)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            set_r.Option.set_Value(None)

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            set_r.Option.get_Parent()

        with pytest.raises(Exception, match=re.escape("Option object was deleted.")):
            set_r.Option.get_Configuration()

        assert set_r.m_OptData is not None
        assert type(set_r.m_OptData) is PgCfgModel__OptionData
        assert set_r.m_OptData.m_Parent is None

    # --------------------------------------------------------------------
    def test_002__line_with_comment(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        cfg.SetOptionValue("port", 123)

        assert len(cfg.get_AllFiles()) == 1

        file = cfg.get_AllFiles().__iter__().__next__()
        assert file is not None
        assert type(file) is PgCfg_TopLevelFile_Base
        assert isinstance(file, PgCfg_File_Base)
        assert isinstance(file, PgCfg_File)
        assert len(file) == 1

        comment1 = file.AddComment("1")
        assert comment1 is not None
        assert type(comment1) == PgCfg_Comment_Base  # noqa: E721
        assert isinstance(comment1, PgCfg_Comment)
        assert comment1.get_Text() == "1"
        assert len(file) == 2

        fileLine = comment1.get_Parent()
        assert fileLine is not None
        assert type(fileLine) == PgCfg_FileLine_Base  # noqa: E721
        assert len(fileLine) == 1

        assert (
            comment1.get_Parent().get_Parent().Private__GetFileData() is file.m_FileData
        )

        fileLine.Clear()

        assert len(fileLine) == 0
        assert comment1.m_CommentData is not None
        assert type(comment1.m_CommentData) is PgCfgModel__CommentData

        assert comment1.m_CommentData.m_Parent is None


# //////////////////////////////////////////////////////////////////////////////
