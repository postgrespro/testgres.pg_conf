# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationWriter_Base as PgCfg_Writer_Base
from src.implementation.v00.configuration_base import PostgresConfigurationWriterCtx_Base as PgCfg_WriterCtx_Base

from src.implementation.v00.configuration_base import PgCfgModel__FileData

from ......TestServices import TestServices
# fmt: on

import pytest
import typing

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    sm_OPTS001: typing.List[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) is str

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue(optName, 234)

        assert len(cfg.m_Data.m_Files) == 1
        fileData = cfg.m_Data.m_Files[0]
        assert type(fileData) is PgCfgModel__FileData

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        fileContent = PgCfg_Writer_Base.MakeFileDataContent(cfgWriterCtx, fileData)

        assert fileContent == optName + " = 234\n"

    # --------------------------------------------------------------------
    def test_002__two_opts(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue("port", 234)
        cfg.SetOptionValue("proxima.port", 345)

        assert len(cfg.m_Data.m_Files) == 1
        fileData = cfg.m_Data.m_Files[0]
        assert type(fileData) is PgCfgModel__FileData

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, fileData
        )

        expectedFileContent = "port = 234\nproxima.port = 345\n"

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    def test_003__opt1_emptyline_opt2(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue("port", 234)
        assert len(cfg.get_AllFiles()) == 1
        assert len(list(cfg.get_AllFiles())) == 1
        list(cfg.get_AllFiles())[0].AddEmptyLine()
        cfg.SetOptionValue("proxima.port", 345)
        assert len(list(cfg.get_AllFiles())[0].get_Lines()) == 3

        assert len(cfg.m_Data.m_Files) == 1
        fileData = cfg.m_Data.m_Files[0]
        assert type(fileData) is PgCfgModel__FileData

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, fileData
        )

        expectedFileContent = "port = 234\n\nproxima.port = 345\n"

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    def test_004__opt1_comment_opt2(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        cfg.SetOptionValue("port", 234)
        assert len(cfg.get_AllFiles()) == 1
        assert len(list(cfg.get_AllFiles())) == 1
        list(cfg.get_AllFiles())[0].AddComment("It is a comment!")
        cfg.SetOptionValue("proxima.port", 345)
        assert len(list(cfg.get_AllFiles())[0].get_Lines()) == 3

        assert len(cfg.m_Data.m_Files) == 1
        fileData = cfg.m_Data.m_Files[0]
        assert type(fileData) is PgCfgModel__FileData

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, fileData
        )

        expectedFileContent = "port = 234\n#It is a comment!\nproxima.port = 345\n"

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    def test_005__opt_with_list(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        C_OPT_NAME = "shared_preload_libraries"

        file.SetOptionValueItem(C_OPT_NAME, "a")

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, file.m_FileData
        )

        expectedFileContent = "shared_preload_libraries = 'a'\n"

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    def test_006__opt_with_list__empty(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        C_OPT_NAME = "shared_preload_libraries"

        r = file.SetOptionValueItem(C_OPT_NAME, "a")

        assert type(r.Option.m_OptionData.m_Value) is list
        r.Option.m_OptionData.m_Value.clear()

        assert len(r.Option.m_OptionData.m_Value) == 0

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, file.m_FileData
        )

        expectedFileContent = "shared_preload_libraries = ''\n"

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    def test_007__opt_with_list__mix(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        C_OPT_NAME = "shared_preload_libraries"

        file.SetOptionValueItem(C_OPT_NAME, "a")
        file.SetOptionValueItem(C_OPT_NAME, "")
        file.SetOptionValueItem(C_OPT_NAME, "\0")
        file.SetOptionValueItem(C_OPT_NAME, ",")
        file.SetOptionValueItem(C_OPT_NAME, "\n")
        file.SetOptionValueItem(C_OPT_NAME, "\r")
        file.SetOptionValueItem(C_OPT_NAME, "\f")
        file.SetOptionValueItem(C_OPT_NAME, "\t")
        file.SetOptionValueItem(C_OPT_NAME, "'")
        file.SetOptionValueItem(C_OPT_NAME, '"')

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, file.m_FileData
        )

        expectedFileContent = 'shared_preload_libraries = \'a,"",\\000,",",\\n,\\r,\\f,"\\t",\\\',""""\'\n'

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    def test_008__include(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        C_INCLUDED_FILE_NAME = "postgresql.proxima.conf"

        file2 = file.AddInclude("postgresql.proxima.conf").get_File()

        assert (
            file2.get_Parent().get_Parent().get_Parent() is file
        )  # check a references

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, file.m_FileData
        )

        expectedFileContent = "include '{0}'\n".format(C_INCLUDED_FILE_NAME)

        assert actualFileContent == expectedFileContent

    # --------------------------------------------------------------------
    class tagData009:
        descr: str
        fileName: str
        result: str

        def __init__(self, d: str, f: str, r: str):
            assert type(d) is str
            assert type(f) is str
            assert type(r) is str

            self.descr = d
            self.fileName = f
            self.result = r

    # --------------------------------------------------------------------
    sm_Data009 = [
        # fmt: off
        tagData009(
            "a_space_a_conf",
            "a a.conf",
            "include 'a a.conf'\n"
        ),
        tagData009(
            "quote_a_quote_conf",
            "'a'.conf",
            "include '\\'a\\'.conf'\n"
        ),
        tagData009(
            "quote2_a_quote2_conf",
            "\"a\".conf",
            "include '\"a\".conf'\n"
        ),
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_Data009, ids=[x.descr for x in sm_Data009])
    def data009(self, request: pytest.FixtureRequest) -> tagData009:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) is __class__.tagData009
        return request.param

    # --------------------------------------------------------------------
    def test_009__include__mix(
        self, request: pytest.FixtureRequest, data009: tagData009
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(data009) is __class__.tagData009

        rootTmpDir = TestServices.GetRootTmpDir()
        cfg = PgCfg_Std(rootTmpDir)
        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_AUTO_CONF)

        file2 = file.AddInclude(data009.fileName).get_File()

        assert (
            file2.get_Parent().get_Parent().get_Parent() is file
        )  # check a references

        cfgWriterCtx = PgCfg_WriterCtx_Base(cfg)

        actualFileContent = PgCfg_Writer_Base.MakeFileDataContent(
            cfgWriterCtx, file.m_FileData
        )

        assert actualFileContent == data009.result


# //////////////////////////////////////////////////////////////////////////////
