# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ......src.implementation.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ......src.implementation.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
from ......src.implementation.configuration_base import PostgresConfigurationFileLine_Base as PgCfg_FileLine_Base
from ......src.implementation.configuration_base import PostgresConfigurationFileLines_Base as PgCfg_FileLines_Base

from ......src.abstract.configuration import PostgresConfigurationFileLine as PgCfg_FileLine
from ......src.abstract.configuration import PostgresConfigurationFileLines as PgCfg_FileLines
# fmt: on

from .....TestServices import TestServices

import pytest
import os

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

        fileLine2 = file.AddEmptyLine()
        assert fileLine2 is not None
        assert type(fileLine2) == PgCfg_FileLine_Base
        assert isinstance(fileLine2, PgCfg_FileLine)

        assert len(fileLines) == 2
        assert (
            list[PgCfg_FileLine_Base](fileLines)[-1].m_FileLineData
            is fileLine2.m_FileLineData
        )

        assert len(fileLine2.m_FileLineData.m_Items) == 0

        assert cfg.GetOptionValue("port") == 123


# //////////////////////////////////////////////////////////////////////////////
