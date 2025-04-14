# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from ........src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationSetOptionValueEventID as PgCfg_SetOptionEventID
from ........src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationIncludedFile_Base as PgCfg_IncludedFile_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationInclude_Base as PgCfg_Include_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationComment_Base as PgCfg_Comment_Base
from ........src.implementation.v00.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base

from ........src.implementation.v00.configuration_base import PgCfgModel__FileLineData
from ........src.implementation.v00.configuration_base import PgCfgModel__CommentData
from ........src.implementation.v00.configuration_base import PgCfgModel__OptionData
from ........src.implementation.v00.configuration_base import PgCfgModel__IncludeData

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
    sm_data001__offsets: list[typing.Optional[int]] = [None, 1, 2, 3, 10]

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
        assert request.param is None or type(request.param) == int
        return request.param

    # --------------------------------------------------------------------
    def test_001(self, request: pytest.FixtureRequest, offset001: typing.Optional[int]):
        assert isinstance(request, pytest.FixtureRequest)
        assert offset001 is None or type(offset001) == int

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_FILE_NAME = "a.conf"

        include = fileLine.AddInclude(C_FILE_NAME, offset001)

        assert len(fileLine) == 1

        assert include is not None
        assert type(include) == PgCfg_Include_Base
        assert include.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert include.m_FileLine is fileLine
        assert type(include.m_IncludeData) == PgCfgModel__IncludeData
        assert include.m_IncludeData.m_Offset == offset001

        assert include.m_IncludeData.IsAlive()
        assert include.m_IncludeData.m_Path == C_FILE_NAME
        assert include.m_IncludeData.m_Parent == fileLine.m_FileLineData

        assert include.get_Configuration() is cfg
        assert include.get_Parent() is fileLine

        includedFile = include.get_File()
        assert type(includedFile) == PgCfg_IncludedFile_Base
        # assert include.get_File() is includedFile
        assert includedFile.get_Path() == os.path.join(rootTmpDir, C_FILE_NAME)
        assert includedFile.get_Parent() is include

    # --------------------------------------------------------------------
    def test_E01__after_option(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        option = fileLine.AddOption("port", 123, 2)

        with pytest.raises(
            Exception, match=re.escape("File line already has the option [port].")
        ):
            fileLine.AddInclude("a.conf", 222)

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) == PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) == PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123

    # --------------------------------------------------------------------
    def test_E02__after_include(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        include = file.AddInclude(cfg.C_POSTGRESQL_AUTO_CONF)

        fileLine = include.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(
            Exception, match=re.escape("File line already has an include directive.")
        ):
            fileLine.AddInclude("a.conf", 222)

        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is include.m_IncludeData

    # --------------------------------------------------------------------
    def test_E03__after_comment(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        comment = file.AddComment("comment")

        fileLine = comment.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(
            Exception, match=re.escape("File line already has a comment.")
        ):
            fileLine.AddInclude("a.conf", 222)

        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is comment.m_CommentData


# //////////////////////////////////////////////////////////////////////////////
