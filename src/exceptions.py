# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from testgres.common.exceptions import TestgresException

import typing

# //////////////////////////////////////////////////////////////////////////////
# PostgresConfigExceptionBase


class PostgresConfigExceptionBase(TestgresException):
    """Common base class for all exceptions raised by the pg_conf library.

    Serves as a single entry point for catching any library-specific errors,
    whether they are user configuration faults or internal bugs.
    """

    pass


# //////////////////////////////////////////////////////////////////////////////
# PostgresConfigException


class PostgresConfigException(PostgresConfigExceptionBase):
    """Base exception for all expected, user-facing configuration errors.

    Inherit from this class for bad value types, syntax errors,
    missing files, or external modifications.
    """

    pass


# //////////////////////////////////////////////////////////////////////////////
# PostgresConfigBugCheckException


class PostgresConfigBugCheckException(PostgresConfigExceptionBase):
    """Fatal internal error indicating a bug inside the library itself.

    Raised when internal invariants, indexing, or handlers are broken.
    This signifies an issue with the library code, not the user input.
    """

    _description: str
    _source: typing.Optional[str]

    # --------------------------------------------------------------------
    def __init__(
        self,
        description: str,
        source: typing.Optional[str] = None,
    ):
        assert type(description) is str
        assert source is None or type(source) is str
        super().__init__()
        self._description = description
        self._source = source
        return

    # TestgresException interface ----------------------------------------
    @property
    def message(self) -> str:
        assert type(self._description) is str
        return "[BUG CHECK] " + self._description

    # --------------------------------------------------------------------
    @property
    def source(self) -> typing.Optional[str]:
        assert self._source is None or type(self._source) is str
        return self._source

    # --------------------------------------------------------------------
    def __repr__(self) -> str:
        # It must be overrided!
        assert type(self) is PostgresConfigBugCheckException
        r = "{}({}, {})".format(
            __class__.__name__,
            repr(self._description),
            repr(self._source),
        )
        assert type(r) is str
        return r

    # PostgresConfigBugCheckException interface --------------------------
    @property
    def description(self) -> str:
        assert type(self._description) is str
        return self._description


# //////////////////////////////////////////////////////////////////////////////
