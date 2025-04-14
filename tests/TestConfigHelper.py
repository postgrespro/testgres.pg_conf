# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from .TestConfigProp import TestConfigPropNames
from .ThrowError import ThrowError

import os

# /////////////////////////////////////////////////////////////////////////////
# TestConfigHelper


class TestConfigHelper:
    def NoCleanup() -> bool:
        if not (TestConfigPropNames.TEST_CFG__NO_CLEANUP in os.environ.keys()):
            return False

        v = os.environ[TestConfigPropNames.TEST_CFG__NO_CLEANUP]

        return __class__.Helper__ToBoolean(v, TestConfigPropNames.TEST_CFG__NO_CLEANUP)

    # Helper methods -----------------------------------------------------
    sm_YES: list[str] = ["1", "TRUE", "YES"]

    sm_NO: list[str] = ["0", "FALSE", "NO"]

    # --------------------------------------------------------------------
    def Helper__ToBoolean(v, envVarName: str) -> bool:
        assert type(envVarName) == str

        typeV = type(v)

        if typeV == bool:
            return v

        if typeV == str:
            vv = str(v).upper()

            if vv in __class__.sm_YES:
                return True

            if vv in __class__.sm_NO:
                return False

            ThrowError.EnvVarHasBadValue(envVarName)

        if typeV == int:
            if v == 0:
                return False

            if v == 1:
                return True

            ThrowError.EnvVarHasBadValue(envVarName)

        ThrowError.EnvVarHasBadValue(envVarName)


# /////////////////////////////////////////////////////////////////////////////
