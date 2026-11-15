# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# fmt: off
from src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from src.implementation.v00.configuration_base import PostgresConfigurationIncludedIfExistsFile_Base as PgCfg_IncludedIfExistFile_Base
from src.implementation.v00.configuration_base import PostgresConfigurationIncludeIfExists_Base as PgCfg_IncludeIfExists_Base
from src.implementation.v00.configuration_base import PostgresConfigurationOption_Base as PgCfg_Option_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFile_Base as PgCfg_File_Base
from src.implementation.v00.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from src.implementation.v00.configuration_base import AddIncludeIfExistsRule as PgCfg_AddIncludeIfExistsRule

from src.implementation.v00.configuration_base import PgCfgModel__OptionData
from src.implementation.v00.configuration_base import PgCfgModel__IncludeIfExistsData
from src.exceptions import PostgresConfigException
# fmt: on

from .......TestServices import TestServices
from .......ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import os
import typing
import logging

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
    def fx_offset001(
        self,
        request: pytest.FixtureRequest,
    ) -> typing.Optional[int]:
        assert isinstance(request, pytest.FixtureRequest)
        assert request.param is None or type(request.param) is int
        return request.param

    # --------------------------------------------------------------------
    def test_001(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_offset001: typing.Optional[int],
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert fx_offset001 is None or type(fx_offset001) is int
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(
            cfg.C_POSTGRESQL_CONF,
        )

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_FILE_NAME = "a.conf"

        __class__.Helper__AddLineAndIncludeIfExists(
            file,
            C_FILE_NAME,
            fx_offset001,
            rootTmpDir,
            fx_add_include_if_exists_rule,
        )
        return

    # --------------------------------------------------------------------
    def test_002__multiple(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_offset001: typing.Optional[int],
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert fx_offset001 is None or type(fx_offset001) is int
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(
            cfg.C_POSTGRESQL_CONF,
        )

        C_FILE_NAME = "a.conf"
        C_INCLUDES = 3

        passN = 0

        while passN < C_INCLUDES:
            passN += 1

            logging.info("------------- pass: {}".format(passN))

            __class__.Helper__AddLineAndIncludeIfExists(
                file,
                C_FILE_NAME,
                fx_offset001,
                rootTmpDir,
                fx_add_include_if_exists_rule,
            )
            continue

        assert len(file.get_Lines()) == C_INCLUDES
        assert len(file.m_FileData.m_Lines) == C_INCLUDES

        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__AddLineAndIncludeIfExists(
        file: PgCfg_File_Base,
        name: str,
        offset: typing.Optional[int],
        rootTmpDir: str,
        rule: PgCfg_AddIncludeIfExistsRule,
    ) -> typing.Tuple[PgCfg_FileLine_Base, PgCfg_IncludeIfExists_Base]:
        assert type(rule) is PgCfg_AddIncludeIfExistsRule

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        C_FILE_NAME = "a.conf"

        include = fileLine.AddIncludeIfExists(
            name,
            offset,
            rule=rule,
        )

        assert len(fileLine) == 1

        assert include is not None
        assert type(include) is PgCfg_IncludeIfExists_Base
        assert include.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert include.m_FileLine is fileLine
        assert type(include.m_IncludeIfExistsData) is PgCfgModel__IncludeIfExistsData
        assert include.m_IncludeIfExistsData.m_Offset == offset

        assert include.m_IncludeIfExistsData.IsAlive()
        assert include.m_IncludeIfExistsData.m_Path == C_FILE_NAME
        assert include.m_IncludeIfExistsData.m_Parent == fileLine.m_FileLineData

        assert include.get_Configuration() is file.get_Configuration()
        assert include.get_Parent() is fileLine

        includedFile = include.get_File()

        if rule == PgCfg_AddIncludeIfExistsRule.without_file:
            assert includedFile is None
            pass
        else:
            assert rule == PgCfg_AddIncludeIfExistsRule.with_file
            assert type(includedFile) is PgCfg_IncludedIfExistFile_Base
            # assert include.get_File() is includedFile
            assert includedFile.get_Path() == os.path.join(rootTmpDir, C_FILE_NAME)
            assert includedFile.get_Parent() is include
            pass

        return (fileLine, include)

    # --------------------------------------------------------------------
    def test_E01__after_option(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        fileLine = file.AddEmptyLine()

        assert len(fileLine) == 0

        option = fileLine.AddOption("port", 123, 2)

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddIncludeIfExists(
                "a.conf",
                222,
                fx_add_include_if_exists_rule,
            )

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasOption(
            "port",
        )

        assert len(fileLine) == 1

        assert option is not None
        assert type(option) is PgCfg_Option_Base
        assert option.m_FileLine.m_FileLineData is fileLine.m_FileLineData
        assert type(option.m_OptionData) is PgCfgModel__OptionData
        assert option.m_OptionData.m_Offset == 2

        assert option.m_OptionData.IsAlive()
        assert option.m_OptionData.m_Name == "port"
        assert option.m_OptionData.m_Value == 123
        assert option.m_OptionData.m_Parent == fileLine.m_FileLineData

        assert option.get_Configuration() is cfg
        assert option.get_Parent().m_FileLineData is fileLine.m_FileLineData
        assert option.get_Name() == "port"
        assert option.get_Value() == 123
        return

    # --------------------------------------------------------------------
    def test_E02__after_include(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        include = file.AddInclude(cfg.C_POSTGRESQL_AUTO_CONF)

        fileLine = include.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddIncludeIfExists(
                "a.conf",
                222,
                fx_add_include_if_exists_rule,
            )

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasIncludeDirective()

        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is include.m_IncludeData
        return

    # --------------------------------------------------------------------
    def test_E03__after_comment(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        comment = file.AddComment("comment")

        fileLine = comment.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddIncludeIfExists(
                "a.conf",
                222,
                fx_add_include_if_exists_rule,
            )

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasComment()

        assert len(fileLine) == 1

        assert fileLine.m_FileLineData.m_Items[0].m_Element is comment.m_CommentData
        return

    # --------------------------------------------------------------------
    def test_E04__after_include_if_exists(
        self,
        request: pytest.FixtureRequest,
        pg_conf_strategy: PgCfg_Std.Strategy,
        fx_add_include_if_exists_rule: PgCfg_AddIncludeIfExistsRule,
    ):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(pg_conf_strategy) is PgCfg_Std.Strategy
        assert type(fx_add_include_if_exists_rule) is PgCfg_AddIncludeIfExistsRule

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) is str

        cfg = PgCfg_Std(
            rootTmpDir,
            strategy=pg_conf_strategy,
        )

        file = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)

        include = file.AddIncludeIfExists(
            cfg.C_POSTGRESQL_AUTO_CONF,
            rule=PgCfg_AddIncludeIfExistsRule.with_file,
        )

        fileLine = include.m_FileLine

        assert len(fileLine) == 1

        with pytest.raises(PostgresConfigException) as x:
            fileLine.AddIncludeIfExists(
                "a.conf",
                222,
                fx_add_include_if_exists_rule,
            )

        assert (
            str(x.value)
            == ErrorMessageBuilder.FileLineAlreadyHasIncludeIfExistsDirective()
        )

        assert len(fileLine) == 1

        assert (
            fileLine.m_FileLineData.m_Items[0].m_Element
            is include.m_IncludeIfExistsData
        )
        return


# //////////////////////////////////////////////////////////////////////////////
