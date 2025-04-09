# //////////////////////////////////////////////////////////////////////////////

# fmt: off
from ......src.configuration_std import PostgresConfiguration_Std as PgCfg_Std

from ......src.configuration_base import PostgresConfigurationTopLevelFile_Base as PgCfg_TopLevelFile_Base
# fmt: on

from .....TestServices import TestServices

import pytest
import re

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        file1 = cfg.AddTopLevelFile(cfg.C_POSTGRESQL_CONF)
        assert file1 is not None
        assert type(file1) == PgCfg_TopLevelFile_Base

        assert (
            cfg.get_AllFiles()
            .GetFileByName(cfg.C_POSTGRESQL_CONF)
            .Private__GetFileData()
            == file1.m_FileData
        )

    # --------------------------------------------------------------------
    def test_002__unk_file_name(self, request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        rootTmpDir = TestServices.GetRootTmpDir()
        assert type(rootTmpDir) == str

        cfg = PgCfg_Std(TestServices.GetRootTmpDir())

        C_FILE_NAME = "a.conf"

        errMsg = "Unknown file name [{0}].".format(C_FILE_NAME)

        with pytest.raises(Exception, match=re.escape(errMsg)):
            cfg.get_AllFiles().GetFileByName(C_FILE_NAME)


# //////////////////////////////////////////////////////////////////////////////
