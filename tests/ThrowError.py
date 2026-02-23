# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

# /////////////////////////////////////////////////////////////////////////////
# ThrowError


class ThrowError:
    def EnvVarIsNotDefined(envVarName: str):
        assert type(envVarName) == str  # noqa: E721
        raise Exception("System env variable [{0}] is not defined.".format(envVarName))

    # --------------------------------------------------------------------
    def EnvVarHasBadValue(envVarName: str):
        assert type(envVarName) == str  # noqa: E721
        raise Exception("System env variable [{0}] has bad value.".format(envVarName))


# /////////////////////////////////////////////////////////////////////////////
