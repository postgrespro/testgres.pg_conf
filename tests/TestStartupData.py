# /////////////////////////////////////////////////////////////////////////////
# Test Services

from __future__ import annotations

from .TestConfigProp import TestConfigPropNames

import os
import datetime

# /////////////////////////////////////////////////////////////////////////////

C_ROOT_DIR__RELATIVE = ".."

# /////////////////////////////////////////////////////////////////////////////
# TestStartupData__Helper


class TestStartupData__Helper:
    sm_StartTS = datetime.datetime.now()

    # --------------------------------------------------------------------
    def GetStartTS() -> datetime.datetime:
        assert type(__class__.sm_StartTS) == datetime.datetime
        return __class__.sm_StartTS

    # --------------------------------------------------------------------
    def CalcRootDir() -> str:
        r = os.path.abspath(__file__)
        r = os.path.dirname(r)
        r = os.path.join(r, C_ROOT_DIR__RELATIVE)
        r = os.path.abspath(r)
        return r

    # --------------------------------------------------------------------
    def CalcRootTmpDir() -> str:
        if TestConfigPropNames.TEST_CFG__TEMP_DIR in os.environ:
            resultPath = os.environ[TestConfigPropNames.TEST_CFG__TEMP_DIR]
        else:
            rootDir = __class__.CalcRootDir()
            resultPath = os.path.join(rootDir, "tmp")

        assert type(resultPath) == str
        return resultPath

    # --------------------------------------------------------------------
    def CalcCurrentTestWorkerSignature() -> str:
        currentPID = os.getpid()
        assert type(currentPID)

        startTS = __class__.sm_StartTS
        assert type(startTS)

        result = "pytest-{0:04d}{1:02d}{2:02d}_{3:02d}{4:02d}{5:02d}".format(
            startTS.year,
            startTS.month,
            startTS.day,
            startTS.hour,
            startTS.minute,
            startTS.second,
        )

        gwid = os.environ.get("PYTEST_XDIST_WORKER")

        if gwid is not None:
            result += "--xdist_" + str(gwid)

        result += "--" + "pid" + str(currentPID)
        return result


# /////////////////////////////////////////////////////////////////////////////
# TestStartupData


class TestStartupData:
    sm_RootDir: str = TestStartupData__Helper.CalcRootDir()
    sm_RootTmpDir: str = TestStartupData__Helper.CalcRootTmpDir()
    sm_RootTmpDataDir: str = os.path.join(sm_RootTmpDir, "data")
    sm_CurrentTestWorkerSignature: str = (
        TestStartupData__Helper.CalcCurrentTestWorkerSignature()
    )
    sm_RootTmpDataDirForCurrentTestWorker: str = os.path.join(
        sm_RootTmpDataDir, sm_CurrentTestWorkerSignature
    )

    # --------------------------------------------------------------------
    def GetRootDir() -> str:
        assert type(__class__.sm_RootDir) == str
        return __class__.sm_RootDir

    # --------------------------------------------------------------------
    def GetCurrentTestWorkerSignature() -> str:
        assert type(__class__.sm_CurrentTestWorkerSignature) == str
        return __class__.sm_CurrentTestWorkerSignature

    # --------------------------------------------------------------------
    def GetRootTmpDataDirForCurrentTestWorker() -> str:
        assert type(__class__.sm_RootTmpDataDirForCurrentTestWorker) == str
        return __class__.sm_RootTmpDataDirForCurrentTestWorker


# /////////////////////////////////////////////////////////////////////////////
