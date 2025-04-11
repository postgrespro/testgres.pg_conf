# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ........src.implementation.v00.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ........src.implementation.v00.configuration_base import PostgresConfiguration_Base__AllFiles as PgCfg_Base__AllFiles
from ........src.implementation.v00.configuration_base import PostgresConfiguration_Base__AllFilesIterator as PgCfg_Base__AllFilesIterator
from ........src.implementation.v00.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base

from ........src.abstract.v00.configuration import PostgresConfigurationFiles as PgCfg_Files
from ........src.abstract.v00.configuration import PostgresConfigurationFilesIterator as PgCfg_FilesIterator
# fmt: on

from .......TestServices import TestServices

import pytest
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_000(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        allFiles1 = cfg.get_AllFiles()
        assert allFiles1 is not None
        assert type(allFiles1) == PgCfg_Base__AllFiles
        assert isinstance(allFiles1, PgCfg_Files)
        assert len(allFiles1) == 0

        allFiles2 = cfg.get_AllFiles()
        assert allFiles2 is allFiles1  # check cache

    # --------------------------------------------------------------------
    sm_OPTS001: list[str] = ["port", "proxima.port"]

    @pytest.mark.parametrize("optName", sm_OPTS001, ids=lambda x: f"{x}")
    def test_001(self, request: pytest.FixtureRequest, optName: str):
        assert isinstance(request, pytest.FixtureRequest)
        assert type(optName) == str

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        cfg.SetOptionValue(optName, 123)

        allFiles1 = cfg.get_AllFiles()
        assert allFiles1 is not None
        assert type(allFiles1) == PgCfg_Base__AllFiles
        assert isinstance(allFiles1, PgCfg_Files)
        assert len(allFiles1) == 1

        allFiles1_list: list[PgCfg_TopLevelFile_Base] = []
        for file in allFiles1:
            assert file is not None
            assert type(file) == PgCfg_TopLevelFile_Base
            allFiles1_list.append(file)

        assert allFiles1_list is not None
        assert len(allFiles1_list) == 1

        assert allFiles1_list[0].get_Path() == os.path.join(
            rootTmpDir, "postgresql.auto.conf"
        )

    # --------------------------------------------------------------------
    def test_002__iter(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        allFiles1 = cfg.get_AllFiles()
        assert type(allFiles1) == PgCfg_Base__AllFiles

        it1 = allFiles1.__iter__()
        assert it1 is not None
        assert type(it1) == PgCfg_Base__AllFilesIterator
        assert isinstance(it1, PgCfg_FilesIterator)
        assert it1.m_Cfg is cfg
        assert it1.m_FileDataIterator is not None

        it1a = it1.__iter__()
        assert it1a is not None
        assert type(it1a) == PgCfg_Base__AllFilesIterator
        assert isinstance(it1a, PgCfg_FilesIterator)
        assert it1a.m_Cfg is cfg

        # NOTE: it may change in the future
        assert it1a.m_FileDataIterator is it1.m_FileDataIterator
        assert it1a is it1

    # --------------------------------------------------------------------
    def test_003__transform_to_list(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        allFiles1 = cfg.get_AllFiles()
        v = list(allFiles1)
        assert len(v) == 0

        cfg.SetOptionValue("port", 333)
        v = list(allFiles1)
        assert len(v) == 1


# //////////////////////////////////////////////////////////////////////////////
