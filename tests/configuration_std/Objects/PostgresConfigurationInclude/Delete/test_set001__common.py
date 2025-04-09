# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ......src.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ......src.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ......src.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from ......src.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from ......src.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ......src.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ......src.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
from ......src.configuration_base import PostgresConfigurationInclude_Base as PgCfg_Include_Base
from ......src.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base

from ......src.configuration_base import PgCfgModel__FileLineData
from ......src.configuration_base import PgCfgModel__CommentData
from ......src.configuration_base import PgCfgModel__OptionData

from ......src.configuration import PostgresConfigurationComment as PgCfg_Comment
from ......src.configuration import PostgresConfigurationFileLine as PgCfg_FileLine
from ......src.configuration import PostgresConfigurationFileLines as PgCfg_FileLines
from ......src.configuration import PostgresConfigurationFile as PgCfg_File
# fmt: on

from .....TestServices import TestServices

import pytest
import os
import re
import typing

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__withLine(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        include = fileLine.AddInclude("a.conf", None)

        assert len(fileLine) == 1

        assert type(include) == PgCfg_Include_Base

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
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        include = fileLine.AddInclude("a.conf", None)

        assert len(fileLine) == 1

        assert type(include) == PgCfg_Include_Base

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
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        include = fileLine.AddInclude("a.conf", None)
        comment = fileLine.AddComment("aaa", None)

        assert len(fileLine) == 2

        assert type(include) == PgCfg_Include_Base

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
