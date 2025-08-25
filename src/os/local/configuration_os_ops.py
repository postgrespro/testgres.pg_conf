# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from ..abstract import configuration_os_ops as abstract

import os
import io
import datetime

# //////////////////////////////////////////////////////////////////////////////
# class ConfigurationOsFile


class ConfigurationOsFile(abstract.ConfigurationOsFile):
    m_file: io.TextIOWrapper

    # --------------------------------------------------------------------
    def __init__(self, file: io.TextIOWrapper):
        assert isinstance(file, io.TextIOWrapper)

        super().__init__()

        self.m_file = file

    # --------------------------------------------------------------------
    def __enter__(self) -> ConfigurationOsFile:
        assert isinstance(self.m_file, io.TextIOWrapper)
        return self

    # --------------------------------------------------------------------
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.m_file is not None:
            self.Close()

        assert self.m_file is None
        return

    # --------------------------------------------------------------------
    @property
    def Name(self) -> str:
        assert isinstance(self.m_file, io.TextIOWrapper)
        return self.m_file.name

    # --------------------------------------------------------------------
    @property
    def IsClosed(self) -> bool:
        return self.m_file is None

    # --------------------------------------------------------------------
    def ReadLine(self) -> str:
        assert isinstance(self.m_file, io.TextIOWrapper)
        return self.m_file.readline()

    # --------------------------------------------------------------------
    def Overwrite(self, text: str) -> None:
        assert type(text) == str  # noqa: E721
        assert isinstance(self.m_file, io.TextIOWrapper)
        self.m_file.seek(0)
        self.m_file.write(text)
        self.m_file.truncate()
        self.m_file.flush()

    # --------------------------------------------------------------------
    def Close(self):
        assert isinstance(self.m_file, io.TextIOWrapper)
        f = self.m_file
        self.m_file = None
        f.close()
        # Returning False (or None) re-raises the exception
        return False

    # --------------------------------------------------------------------
    def GetModificationTS(self) -> datetime.datetime:
        assert isinstance(self.m_file, io.TextIOWrapper)

        fd = self.m_file.fileno()
        assert type(fd) == int  # noqa: E721

        lastMDate = datetime.datetime.fromtimestamp(os.path.getmtime(fd))
        assert type(lastMDate) == datetime.datetime  # noqa: E721
        return lastMDate


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

    def OpenFileToRead(self, filePath: str) -> ConfigurationOsFile:
        assert type(filePath) == str  # noqa: E721
        f = open(filePath)
        return ConfigurationOsFile(f)

    def OpenFileToWrite(self, filePath: str) -> ConfigurationOsFile:
        assert type(filePath) == str  # noqa: E721
        f = open(filePath, mode="r+")
        return ConfigurationOsFile(f)

    def CreateFile(self, filePath: str) -> ConfigurationOsFile:
        assert type(filePath) == str  # noqa: E721
        f = open(filePath, mode="x")
        return ConfigurationOsFile(f)


# //////////////////////////////////////////////////////////////////////////////


SingleInstance = ConfigurationOsOps()


# //////////////////////////////////////////////////////////////////////////////
