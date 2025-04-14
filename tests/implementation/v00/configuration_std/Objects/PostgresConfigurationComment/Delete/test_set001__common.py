# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from ........src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from ........src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base

from ........src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from ........src.implementation.v00.configuration_base import PgCfgModel__CommentData
from ........src.implementation.v00.configuration_base import PgCfgModel__OptionData

from ........src.abstract.v00.configuration import PostgresConfigurationComment as PgCfg_Comment
from ........src.abstract.v00.configuration import PostgresConfigurationFileLine as PgCfg_FileLine
from ........src.abstract.v00.configuration import PostgresConfigurationFileLines as PgCfg_FileLines
from ........src.abstract.v00.configuration import PostgresConfigurationFile as PgCfg_File
# fmt: on

from .......TestServices import TestServices

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

        comment = fileLine.AddComment("comment")

        assert len(fileLine) == 1

        assert type(comment) == PgCfg_Comment_Base

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
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        comment = fileLine.AddComment("comment")

        assert len(fileLine) == 1

        assert type(comment) == PgCfg_Comment_Base

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
