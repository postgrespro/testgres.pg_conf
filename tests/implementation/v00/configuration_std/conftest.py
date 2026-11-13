# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from src.implementation.v00.configuration_std import PostgresConfiguration_Std

import pytest

# //////////////////////////////////////////////////////////////////////////////
# pg_conf_strategy


@pytest.fixture(
    params=list(PostgresConfiguration_Std.Strategy),
)
def pg_conf_strategy(
    request: pytest.FixtureRequest,
) -> PostgresConfiguration_Std.Strategy:
    assert isinstance(request, pytest.FixtureRequest)
    assert type(request.param) is PostgresConfiguration_Std.Strategy
    return request.param


# //////////////////////////////////////////////////////////////////////////////
