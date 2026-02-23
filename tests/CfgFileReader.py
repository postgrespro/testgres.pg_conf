# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from src.os.abstract.configuration_os_ops import ConfigurationFileReader

import io
import typing

# //////////////////////////////////////////////////////////////////////////////
# class CfgFileReader


class CfgFileReader(ConfigurationFileReader):
    m_file: io.StringIO

    # --------------------------------------------------------------------
    def __init__(self, text: str):
        super().__init__()

        self.m_file = io.StringIO(text)

    # --------------------------------------------------------------------
    def ReadLine(self) -> typing.Optional[str]:
        assert type(self.m_file) == io.StringIO  # noqa: E721

        r = self.m_file.readline()
        assert type(r) == str  # noqa: E721
        if not r:
            assert r == ""
            return None

        assert r != ""
        return r


# //////////////////////////////////////////////////////////////////////////////
