# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from __future__ import annotations

from .TestStartupData import TestStartupData
from .TestConfigHelper import TestConfigHelper

import os
import pytest
import logging
import time
import shutil

# /////////////////////////////////////////////////////////////////////////////
# TestServices


class TestServices:
    def GetRootDir() -> str:
        return TestStartupData.GetRootDir()

    # --------------------------------------------------------------------
    def GetRootTmpDir() -> str:
        return TestStartupData.GetRootTmpDataDirForCurrentTestWorker()

    # --------------------------------------------------------------------
    def MakeRootTmpDirForGlobalResources(globalResourceID: str) -> str:
        assert isinstance(globalResourceID, str)
        return os.path.join(__class__.GetRootTmpDir(), ".global", globalResourceID)

    # --------------------------------------------------------------------
    def GetCurTestTmpDir(request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)
        return __class__.Helper__GetCurTestTmpDir(request)

    # --------------------------------------------------------------------
    def Helper__GetCurTestTmpDir(request: pytest.FixtureRequest) -> str:
        assert isinstance(request, pytest.FixtureRequest)

        rootDir = TestServices.GetRootDir()
        rootTmpDir = TestServices.GetRootTmpDir()

        # [2024-12-18] It is not a fact now.
        # assert rootTmpDir.startswith(rootDir)

        testPath = str(request.path)

        if not testPath.startswith(rootDir):
            raise Exception(
                "Root dir {0} is not found in testPath {1}.".format(rootDir, testPath)
            )

        testPath2 = testPath[len(rootDir) + 1 :]

        result = os.path.join(rootTmpDir, testPath2)

        if request.node.cls is not None:
            clsName = request.node.cls.__name__
            result = os.path.join(result, clsName)

        result = os.path.join(result, request.node.name)

        return result

    # --------------------------------------------------------------------
    def CleanTestTmpDirBeforeExit(request: pytest.FixtureRequest):
        assert isinstance(request, pytest.FixtureRequest)

        if TestConfigHelper.NoCleanup():
            logging.info("A final data cleanup is disabled.")
            return

        tmpDir = __class__.GetCurTestTmpDir(request)
        assert type(tmpDir) == str

        if not os.path.exists(tmpDir):
            return

        logging.info("Tmp directory [{0}] is deleting...".format(tmpDir))
        shutil.rmtree(tmpDir)
        assert not os.path.exists(tmpDir)
        return

    # --------------------------------------------------------------------
    def PrintExceptionOK(e: Exception):
        assert isinstance(e, Exception)

        logging.info(
            "OK. We catch an exception ({0}) - {1}".format(type(e).__name__, e)
        )

    # --------------------------------------------------------------------
    def ThrowWeWaitAnException():
        raise Exception("We wait an exception!")

    # --------------------------------------------------------------------
    def SleepWithPrint(sleepTimeInSec: float):
        logging.info("Sleep {0} second(s).".format(sleepTimeInSec))
        time.sleep(sleepTimeInSec)


# /////////////////////////////////////////////////////////////////////////////
