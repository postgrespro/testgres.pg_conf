# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ..abstract import configuration_os_ops as abstract

import os

# //////////////////////////////////////////////////////////////////////////////
# class ConfigurationOsOps


class ConfigurationOsOps(abstract.ConfigurationOsOps):
    def Path_IsAbs(self, a: str) -> bool:
        assert type(a) == str  # noqa: E721
        return os.path.isabs(a)

    def Path_Join(self, a: str, *p: tuple) -> str:
        assert type(a) == str  # noqa: E721
        assert type(p) == tuple  # noqa: E721
        return os.path.join(a, *p)

    def Path_NormPath(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        return os.path.normpath(a)

    def Path_AbsPath(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        return os.path.abspath(a)

    def Path_NormCase(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        return os.path.normcase(a)

    def Path_DirName(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        return os.path.dirname(a)

    def Path_BaseName(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        return os.path.basename(a)

    def Remove(self, a: str) -> str:
        assert type(a) == str  # noqa: E721
        os.remove(a)


# //////////////////////////////////////////////////////////////////////////////


SingleInstance = ConfigurationOsOps()


# //////////////////////////////////////////////////////////////////////////////
