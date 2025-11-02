# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationReader_Base as PgCfg_Reader_Base

from src.implementation.v00.configuration_base import PgCfgModel__FileData
from src.implementation.v00.configuration_base import PgCfgModel__CommentData
from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__IncludeData
# fmt: on

from .......TestServices import TestServices
from .......CfgFileReader import CfgFileReader

import pytest
import typing
import re
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__empty(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(rootTmpDir)

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert isinstance(file1, PgCfg_File_Base)
        assert isinstance(file1, PgCfg_TopLevelFile_Base)
        assert file1.m_FileData is not None
        assert type(file1.m_FileData) == PgCfgModel__FileData
        assert file1.m_FileData.m_Lines is not None
        assert type(file1.m_FileData.m_Lines) == list
        assert type(file1.m_FileData.m_Path) == str
        assert file1.m_FileData.m_Path == os.path.join(
            rootTmpDir,
            cfg.C_POSTGRESQL_CONF,
        )

        src = CfgFileReader("")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 0
        assert file1.m_FileData is not None
        assert type(file1.m_FileData) == PgCfgModel__FileData
        assert file1.m_FileData.m_Lines is not None
        assert type(file1.m_FileData.m_Lines) == list
        assert len(file1.m_FileData.m_Lines) == 0

    # --------------------------------------------------------------------
    def test_002__space(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader(" ")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1
        assert len(file1.m_FileData.m_Lines[0].m_Items) == 0

    # --------------------------------------------------------------------
    def test_003__empty_line_with_eol(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1
        assert len(file1.m_FileData.m_Lines[0].m_Items) == 0

    # --------------------------------------------------------------------
    def test_101__comment(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader(" #  comment   \n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__CommentData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 1
        assert fileLineData0.m_Items[0].m_Element.m_Text == "  comment   "

    # --------------------------------------------------------------------
    def test_102__two_comments(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("#comment1\n\t#comment2")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 2
        assert len(file1.m_FileData.m_Lines) == 2

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__CommentData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Text == "comment1"

        fileLineData1 = file1.m_FileData.m_Lines[1]
        assert len(fileLineData1.m_Items) == 1
        assert type(fileLineData1.m_Items[0].m_Element) == PgCfgModel__CommentData
        assert fileLineData1.m_Items[0].m_Element.m_Offset == 4
        assert fileLineData1.m_Items[0].m_Element.m_Text == "comment2"

    # --------------------------------------------------------------------
    sm_data201__assign: typing.List[typing.Tuple[str, str]] = [
        ("assign", "="),
        ("space", " "),
        ("tab", "\t"),
        ("space_assign", " ="),
        ("assign_space", "= "),
        ("space_assign_space", " = "),
        ("tab_assign", "\t="),
        ("assign_tab", "=\t"),
        ("tab_assign_tab", "\t=\t"),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data201__assign, ids=[x[0] for x in sm_data201__assign])
    def data201__assign(self, request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple
        assert len(request.param) == 2
        assert type(request.param[1]) == str
        return request.param[1]

    # --------------------------------------------------------------------
    def test_201__option(self, request: pytest.FixtureRequest, data201__assign: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data201__assign) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port" + data201__assign + "123\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "port"
        assert fileLineData0.m_Items[0].m_Element.m_Value == 123

    # --------------------------------------------------------------------
    def test_202__option(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port=234")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "port"
        assert fileLineData0.m_Items[0].m_Element.m_Value == 234

    # --------------------------------------------------------------------
    def test_203__option__without_assign(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port 234")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "port"
        assert fileLineData0.m_Items[0].m_Element.m_Value == 234

    # --------------------------------------------------------------------
    sm_data204: typing.List[typing.Tuple[str, str]] = [
        ("EOF", ""),
        ("EOL", "\n"),
        ("space_and_EOF", " "),
        ("tab_and_EOF", "\t"),
        ("space_and_EOL", " \n"),
        ("tab_and_EOL", "\t\n"),
        ("empty_comment_EOF", "#"),
        ("empty_comment_EOL", "#\n"),
        ("comment_EOF", "#123"),
        ("comment_EOL", "#123\n"),
        ("space_comment_EOF", " #123"),
        ("space_comment_EOL", " #123\n"),
        ("tab_comment_EOF", " #123"),
        ("tab_comment_EOL", " #123\n"),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data204, ids=[x[0] for x in sm_data204])
    def data204_tail(self, request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple
        assert len(request.param) == 2
        assert type(request.param[1]) == str
        return request.param[1]

    # --------------------------------------------------------------------
    def test_204__option_without_value(
        self, request: pytest.FixtureRequest, data204_tail: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data204_tail) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port" + data204_tail)

        with pytest.raises(
            Exception, match=re.escape("Option [port] in line 1 does not have a value.")
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    def test_211__option_with_comment(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port=123 #comment\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 2
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "port"
        assert fileLineData0.m_Items[0].m_Element.m_Value == 123

        assert type(fileLineData0.m_Items[1].m_Element) == PgCfgModel__CommentData
        assert fileLineData0.m_Items[1].m_Element.m_Offset == 9
        assert fileLineData0.m_Items[1].m_Element.m_Text == "comment"

    # --------------------------------------------------------------------
    def test_212__option_with_comment_immediate(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port=123#comment \n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 2
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "port"
        assert fileLineData0.m_Items[0].m_Element.m_Value == 123

        assert type(fileLineData0.m_Items[1].m_Element) == PgCfgModel__CommentData
        assert fileLineData0.m_Items[1].m_Element.m_Offset == 8
        assert fileLineData0.m_Items[1].m_Element.m_Text == "comment "

    # --------------------------------------------------------------------
    def test_301__optionQ(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("port='123'\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "port"
        assert fileLineData0.m_Items[0].m_Element.m_Value == 123

    # --------------------------------------------------------------------
    def test_302__optionQ__empty(
        self, request: pytest.FixtureRequest, data201__assign: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data201__assign) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("listen_addresses" + data201__assign + "''\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "listen_addresses"
        assert fileLineData0.m_Items[0].m_Element.m_Value == ""

    # --------------------------------------------------------------------
    def test_303__optionQ__two_quote(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("listen_addresses=''''\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "listen_addresses"
        assert fileLineData0.m_Items[0].m_Element.m_Value == "'"

    # --------------------------------------------------------------------
    sm_endData304: typing.List[typing.Tuple[str, str, str]] = [
        ("b", "\\b", "\b"),
        ("f", "\\f", "\f"),
        ("n", "\\n", "\n"),
        ("r", "\\r", "\r"),
        ("t", "\\t", "\t"),
        ("quote", "\\'", "'"),
        ("double_quote", '\\"', '"'),
        ("0", "\\0", "\0"),
        ("1", "\\1", "\1"),
        ("007", "\\007", "\7"),
        ("0071", "\\0071", "\0071"),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_endData304, ids=[x[0] for x in sm_endData304])
    def endData304(self, request: pytest.FixtureRequest) -> typing.Tuple[str, str, str]:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple
        assert len(request.param) == 3
        return request.param

    # --------------------------------------------------------------------
    def test_304__optionQ__escape(
        self, request: pytest.FixtureRequest, endData304: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(endData304) == tuple

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("listen_addresses='" + endData304[1] + "'")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__OptionData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Name == "listen_addresses"
        assert fileLineData0.m_Items[0].m_Element.m_Value == endData304[2]

    # --------------------------------------------------------------------
    sm_data3E01: typing.List[typing.Tuple[str, str]] = [
        ("EOF", ""),
        ("EOL", "\n"),
        ("space_EOF", " "),
        ("space_EOL", " \n"),
        ("twoQuote_EOF", "'' "),
        ("twoQuote_EOL", "'' \n"),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data3E01, ids=[x[0] for x in sm_data3E01])
    def endData3E01(self, request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple
        assert type(request.param[1]) == str
        return request.param[1]

    # --------------------------------------------------------------------
    def test_3E01__optionQ__no_end_quote(
        self, request: pytest.FixtureRequest, endData3E01: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(endData3E01) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("listen_addresses='" + endData3E01)

        with pytest.raises(
            Exception,
            match=re.escape(
                "Value of quoted option [listen_addresses] is not completed. Line 1."
            ),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    sm_data3E02: typing.List[typing.Tuple[str, str]] = [
        ("EOF", ""),
        ("EOL", "\n"),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_data3E02, ids=[x[0] for x in sm_data3E02])
    def endData3E02(self, request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == tuple
        assert type(request.param[1]) == str
        return request.param[1]

    # --------------------------------------------------------------------
    def test_3E02__optionQ__incompleted_escape(
        self, request: pytest.FixtureRequest, endData3E02: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(endData3E02) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("listen_addresses='\\" + endData3E02)

        with pytest.raises(
            Exception,
            match=re.escape(
                "Escape in a value of quoted option [listen_addresses] is not completed. Line 1."
            ),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    def test_3E03__optionQ__unk_escaped_symbol(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("listen_addresses='\\a")

        with pytest.raises(
            Exception,
            match=re.escape(
                "Unknown escape symbol [a] in a value of quoted option [listen_addresses]. Line 1. Column 20."
            ),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    def test_401__include(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("include 'a.conf'\n")

        PgCfg_Reader_Base.LoadFileContent(file1, src)

        assert len(file1) == 1
        assert len(file1.m_FileData.m_Lines) == 1

        fileLineData0 = file1.m_FileData.m_Lines[0]
        assert len(fileLineData0.m_Items) == 1
        assert type(fileLineData0.m_Items[0].m_Element) == PgCfgModel__IncludeData
        assert fileLineData0.m_Items[0].m_Element.m_Offset == 0
        assert fileLineData0.m_Items[0].m_Element.m_Path == "a.conf"

        file_A = cfg.get_AllFiles().GetFileByName("a.conf")
        assert file_A.get_Path() == os.path.join(rootTmpDir, "a.conf")

    # --------------------------------------------------------------------
    def test_4E01__empty_path(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("include ''\n")

        with pytest.raises(
            Exception, match=re.escape("Include in line 1 has an empty path.")
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    sm_dataE4E02: typing.List[typing.Tuple[str, str]] = [
        ("EOF", ""),
        ("EOL", "\n"),
        ("a_EOF", "a"),
        ("a_EOL", "a\n"),
    ]

    # --------------------------------------------------------------------
    @pytest.mark.parametrize(
        "data4E02", [x[1] for x in sm_dataE4E02], ids=[x[0] for x in sm_dataE4E02]
    )
    def test_4E02__incompleted_path(
        self, request: pytest.FixtureRequest, data4E02: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data4E02) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("include '" + data4E02)

        with pytest.raises(
            Exception,
            match=re.escape("The end of an include path is not found. Line 1."),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    def test_4E03__unknown_escape_symbol(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("include '\\a")

        with pytest.raises(
            Exception,
            match=re.escape(
                "Unknown escape symbol [a] in an include path. Line 1. Column 11."
            ),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    sm_dataE4E04: typing.List[typing.Tuple[str, str]] = [
        ("EOF", ""),
        ("EOL", "\n"),
    ]

    # --------------------------------------------------------------------
    @pytest.mark.parametrize(
        "data4E04", [x[1] for x in sm_dataE4E04], ids=[x[0] for x in sm_dataE4E04]
    )
    def test_4E04__incompleted_escape(
        self, request: pytest.FixtureRequest, data4E04: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data4E04) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("include '\\" + data4E04)

        with pytest.raises(
            Exception,
            match=re.escape("Escape in an include path is not completed. Line 1."),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)

    # --------------------------------------------------------------------
    sm_dataE4E05: typing.List[typing.Tuple[str, str]] = [
        ("EOF", ""),
        ("EOL", "\n"),
        ("space_EOF", " "),
        ("space_EOL", " \n"),
        ("tab_EOF", "\t"),
        ("tab_EOL", "\t\n"),
        ("empty_comment_EOF", "#"),
        ("empty_comment_EOL", "#\n"),
        ("comment_EOF", "#123"),
        ("comment_EOL", "#123\n"),
        ("space_comment_EOF", " #123"),
        ("space_comment_EOL", " #123\n"),
        ("tab_comment_EOF", " #123"),
        ("tab_comment_EOL", " #123\n"),
    ]

    # --------------------------------------------------------------------
    @pytest.mark.parametrize(
        "data4E05", [x[1] for x in sm_dataE4E05], ids=[x[0] for x in sm_dataE4E05]
    )
    def test_4E05__include_without_path(
        self, request: pytest.FixtureRequest, data4E05: str
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data4E05) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        src = CfgFileReader("include" + data4E05)

        with pytest.raises(
            Exception,
            match=re.escape("Include directive in line 1 does not have a path."),
        ):
            PgCfg_Reader_Base.LoadFileContent(file1, src)


# //////////////////////////////////////////////////////////////////////////////
