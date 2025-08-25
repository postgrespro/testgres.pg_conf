# /////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from ..src.os.abstract.configuration_os_ops import ConfigurationFileReader

import io

# //////////////////////////////////////////////////////////////////////////////
# class CfgFileReader


class CfgFileReader(ConfigurationFileReader):
    m_file: io.StringIO

    # --------------------------------------------------------------------
    def __init__(self, text: str):
        super().__init__()

        self.m_file = io.StringIO(text)

    # --------------------------------------------------------------------
    def ReadLine(self) -> str:
        assert type(self.m_file) == io.StringIO
        return self.m_file.readline()


# //////////////////////////////////////////////////////////////////////////////
