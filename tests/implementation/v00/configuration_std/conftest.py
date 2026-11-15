# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from src.implementation.v00.configuration_std import PostgresConfiguration_Std
from src.implementation.v00.configuration_base import AddIncludeIfExistsRule

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


@pytest.fixture(
    params=[
        pytest.param(
            x,
            id="rule={}".format(x.name),
        )
        for x in list(AddIncludeIfExistsRule)
    ],
)
def fx_add_include_if_exists_rule(
    request: pytest.FixtureRequest,
) -> AddIncludeIfExistsRule:
    assert isinstance(request, pytest.FixtureRequest)
    assert type(request.param) is AddIncludeIfExistsRule
    return request.param


# //////////////////////////////////////////////////////////////////////////////
