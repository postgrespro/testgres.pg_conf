# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# /////////////////////////////////////////////////////////////////////////////
# ThrowError


class ThrowError:
    @staticmethod
    def EnvVarIsNotDefined(envVarName: str):
        assert type(envVarName) is str
        raise Exception("System env variable [{0}] is not defined.".format(envVarName))

    # --------------------------------------------------------------------
    @staticmethod
    def EnvVarHasBadValue(envVarName: str):
        assert type(envVarName) is str
        raise Exception("System env variable [{0}] has bad value.".format(envVarName))


# /////////////////////////////////////////////////////////////////////////////
