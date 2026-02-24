# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from .TestConfigProp import TestConfigPropNames
from .ThrowError import ThrowError

import os
import typing

# /////////////////////////////////////////////////////////////////////////////
# TestConfigHelper


class TestConfigHelper:
    @staticmethod
    def NoCleanup() -> bool:
        if TestConfigPropNames.TEST_CFG__NO_CLEANUP not in os.environ.keys():
            return False

        v = os.environ[TestConfigPropNames.TEST_CFG__NO_CLEANUP]

        return __class__.Helper__ToBoolean(v, TestConfigPropNames.TEST_CFG__NO_CLEANUP)

    # Helper methods -----------------------------------------------------
    sm_YES: typing.List[str] = ["1", "TRUE", "YES"]

    sm_NO: typing.List[str] = ["0", "FALSE", "NO"]

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ToBoolean(v, envVarName: str) -> bool:
        assert type(envVarName) is str

        typeV = type(v)

        if typeV is bool:
            return v

        if typeV is str:
            vv = str(v).upper()

            if vv in __class__.sm_YES:
                return True

            if vv in __class__.sm_NO:
                return False

            ThrowError.EnvVarHasBadValue(envVarName)

        if typeV is int:
            if v == 0:
                return False

            if v == 1:
                return True

            ThrowError.EnvVarHasBadValue(envVarName)

        ThrowError.EnvVarHasBadValue(envVarName)


# /////////////////////////////////////////////////////////////////////////////
