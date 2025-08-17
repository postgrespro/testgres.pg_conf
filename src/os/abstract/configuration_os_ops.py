# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ...core.raise_error import RaiseError

# //////////////////////////////////////////////////////////////////////////////
# class ConfigurationOsOps


class ConfigurationOsOps:
    def Path_IsAbs(self, a: str) -> bool:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_IsAbs")

    def Path_Join(self, a: str, *p: tuple) -> str:
        assert type(a) == str  # noqa: E721
        assert type(p) == tuple  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_Join")

    def Path_NormPath(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_NormPath")

    def Path_AbsPath(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_AbsPath")

    def Path_NormCase(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_NormCase")

    def Path_DirName(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_DirName")

    def Path_BaseName(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Path_BaseName")

    def Remove(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        RaiseError.MethodIsNotImplemented(__class__, "Remove")


# //////////////////////////////////////////////////////////////////////////////
