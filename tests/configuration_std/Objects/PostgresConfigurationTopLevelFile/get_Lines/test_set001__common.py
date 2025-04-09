# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ......src.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ......src.configuration_base import PostgresConfigurationSetOptionValueResult_Base as PgCfg_SetOptionResult_Base
from ......src.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ......src.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ......src.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base
from ......src.configuration_base import PostgresConfigurationFileLinesIterator_Base as PgCfg_FileLinesIterator_Base

from ......src.configuration_base import PostgresConfigurationSetOptionValueResult as PgCfg_SetOptionResult

from ......src.configuration import PostgresConfigurationFileLine as PgCfg_FileLine
from ......src.configuration import PostgresConfigurationFileLines as PgCfg_FileLines
from ......src.configuration import PostgresConfigurationFileLinesIterator as PgCfg_FileLinesIterator
# fmt: on

from .....TestServices import TestServices

import pytest
import os

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__Lines(self, request: pytest.FixtureRequest):
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

        fileLines2 = file.get_Lines()
        assert fileLines2 is fileLines  # check cache

        fileLines_it = fileLines.__iter__()
        assert fileLines_it is not None
        assert type(fileLines_it) == PgCfg_FileLinesIterator_Base
        assert isinstance(fileLines_it, PgCfg_FileLinesIterator)

        fileLine = fileLines_it.__next__()
        assert fileLine is not None
        assert type(fileLine) == PgCfg_FileLine_Base
        assert isinstance(fileLine, PgCfg_FileLine)

        cfg.SetOptionValue("port", None)

        assert len(fileLines) == 0

        fileLines_v = list(fileLines)
        assert len(fileLines_v) == 0

    # --------------------------------------------------------------------
    def test_001__Lines__iterator(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        set_r = cfg.SetOptionValue("port", 123)
        assert type(set_r) == PgCfg_SetOptionResult_Base
        assert isinstance(set_r, PgCfg_SetOptionResult)

        file = set_r.Option.get_Parent().get_Parent()

        assert type(file) == PgCfg_TopLevelFile_Base

        it1 = file.get_Lines().__iter__()
        assert type(it1) == PgCfg_FileLinesIterator_Base
        assert isinstance(it1, PgCfg_FileLinesIterator)

        it1a = it1.__iter__()
        assert it1a == it1


# //////////////////////////////////////////////////////////////////////////////
