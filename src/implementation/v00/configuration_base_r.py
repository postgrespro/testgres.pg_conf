# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

# fmt: off
from .configuration_base import PostgresConfiguration_Base
from .configuration_base import PostgresConfigurationFileLine_Base
from .configuration_base import PostgresConfigurationFile_Base
from .configuration_base import PostgresConfigurationTopLevelFile_Base
from .configuration_base import PostgresConfigurationFactory_Base

from ...core.model import CommentData as PgCfgModel__CommentData
from ...core.model import OptionData as PgCfgModel__OptionData
from ...core.model import IncludeData as PgCfgModel__IncludeData
from ...core.model import FileLineData as PgCfgModel__FileLineData
from ...core.model import FileData as PgCfgModel__FileData
from ...core.model import FileStatus as PgCfgModel__FileStatus

from ...core.helpers import Helpers
from ...core.read_utils import ReadUtils
from ...core.read_utils import LineReader as ReadUtils__LineReader
from ...core.raise_error import RaiseError
from ...core.bugcheck_error import BugCheckError
# fmt: on

from ...os.abstract.configuration_os_ops import ConfigurationFileReader
from ...os.abstract.configuration_os_ops import ConfigurationOsFile

import typing
import datetime

# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationReader_Base


class PostgresConfigurationReader_Base:
    @staticmethod
    def LoadConfigurationFile(
        cfg: PostgresConfiguration_Base,
        filePath: str,
    ) -> PostgresConfigurationTopLevelFile_Base:
        assert cfg is not None

        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(filePath) is str
        assert filePath != ""

        existFileDatas: typing.Dict[str, PgCfgModel__FileData] = dict()

        for fileName in cfg.m_Data.m_AllFilesByName.keys():
            assert type(fileName) is str
            assert fileName != ""

            indexData = cfg.m_Data.m_AllFilesByName[fileName]
            assert indexData is not None

            if type(indexData) is PgCfgModel__FileData:
                fileData: PgCfgModel__FileData = indexData
                assert type(fileData.m_Path) is str
                assert fileData.m_Path not in existFileDatas.keys()
                existFileDatas[fileData.m_Path] = fileData
                continue

            if type(indexData) is list:
                for fileData in indexData:
                    assert type(fileData) is PgCfgModel__FileData
                    assert type(fileData.m_Path) is str
                    assert fileData.m_Path not in existFileDatas.keys()
                    existFileDatas[fileData.m_Path] = fileData
                    continue
                continue

            BugCheckError.UnkFileObjectDataType(
                fileName,
                type(indexData),
            )

        # ----------------------------------------------------------------
        filePath_n = Helpers.NormalizeFilePath(
            cfg.m_Data.OsOps,
            cfg.m_Data.m_DataDir,
            filePath,
        )
        assert type(filePath_n) is str

        if filePath_n in existFileDatas:
            file = PostgresConfigurationFactory_Base.GetObject(
                cfg,
                existFileDatas[filePath_n],
            )
            assert type(file) is PostgresConfigurationTopLevelFile_Base
            return file

        # ----------------------------------------------------------------
        rootFile = cfg.AddTopLevelFile(filePath)
        assert type(rootFile) is PostgresConfigurationTopLevelFile_Base
        assert type(rootFile.m_FileData) is PgCfgModel__FileData
        assert type(rootFile.m_FileData.m_Lines) is list
        assert rootFile.m_FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
        assert rootFile.m_FileData.m_LastModifiedTimestamp is None
        assert len(rootFile.m_FileData.m_Lines) == 0

        queuedFileDatas: typing.Set[PgCfgModel__FileData] = set()

        queuedFileDatas.add(rootFile.m_FileData)

        while len(queuedFileDatas) != 0:
            currentFileData = queuedFileDatas.pop()
            assert isinstance(currentFileData, PgCfgModel__FileData)

            # load content
            # process content

            with cfg.m_Data.OsOps.OpenFileToRead(currentFileData.m_Path) as f:
                assert isinstance(f, ConfigurationOsFile)
                currentFile = PostgresConfigurationFactory_Base.GetObject(
                    cfg,
                    currentFileData,
                )
                assert isinstance(currentFile, PostgresConfigurationFile_Base)
                __class__.Helper__LoadFileContent(
                    currentFile,
                    f,
                )  # raise

                lastMDate = f.GetModificationTS()
                assert type(lastMDate) is datetime.datetime

                currentFileData.m_LastModifiedTimestamp = lastMDate
                currentFileData.m_Status = PgCfgModel__FileStatus.EXISTS

            assert currentFileData.m_Path not in existFileDatas.keys()
            existFileDatas[currentFileData.m_Path] = currentFileData

            # enumerate all the includes
            for fileLineData in currentFileData.m_Lines:
                assert type(fileLineData) is PgCfgModel__FileLineData
                assert type(fileLineData.m_Items) is list

                for fileLineItem in fileLineData.m_Items:
                    assert type(fileLineItem) is PgCfgModel__FileLineData.tagItem

                    fileLineElementData = fileLineItem.m_Element

                    if type(fileLineElementData) is PgCfgModel__CommentData:
                        continue

                    if type(fileLineElementData) is PgCfgModel__OptionData:
                        continue

                    if type(fileLineElementData) is PgCfgModel__IncludeData:
                        # look at existFileDatas
                        includeData: PgCfgModel__IncludeData = fileLineElementData
                        assert type(includeData.m_File) is PgCfgModel__FileData
                        assert type(includeData.m_File.m_Path) is str

                        if includeData.m_File.m_Path in existFileDatas:
                            continue  # it is an old file

                        assert (
                            includeData.m_File.m_Status == PgCfgModel__FileStatus.IS_NEW
                        )
                        assert includeData.m_File.m_LastModifiedTimestamp is None

                        if includeData.m_File in queuedFileDatas:
                            continue  # already in queue

                        queuedFileDatas.add(includeData.m_File)
                        continue

                    BugCheckError.UnkObjectDataType(type(fileLineElementData))

        assert len(queuedFileDatas) == 0
        assert isinstance(rootFile, PostgresConfigurationTopLevelFile_Base)

        return rootFile

    # --------------------------------------------------------------------
    @staticmethod
    def LoadFileContent(
        file: PostgresConfigurationFile_Base,
        fileContent: ConfigurationFileReader,
    ) -> None:
        assert isinstance(file, PostgresConfigurationFile_Base)
        assert isinstance(fileContent, ConfigurationFileReader)

        return __class__.Helper__LoadFileContent(
            file,
            fileContent,
        )

    # Helper methods -----------------------------------------------------
    @staticmethod
    def Helper__LoadFileContent(
        file: PostgresConfigurationFile_Base,
        fileContent: ConfigurationFileReader,
    ) -> None:
        assert isinstance(file, PostgresConfigurationFile_Base)
        assert isinstance(fileContent, ConfigurationFileReader)

        lineReader = ReadUtils__LineReader()

        while True:
            lineData = fileContent.ReadLine()

            if not lineData:
                assert lineData is None
                break

            assert type(lineData) is str

            lineReader.SetData(lineData)

            __class__.Helper__ProcessLineData(
                file,
                lineReader,
            )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ProcessLineData(
        file: PostgresConfigurationFile_Base,
        lineReader: ReadUtils__LineReader,
    ) -> None:
        assert isinstance(file, PostgresConfigurationFile_Base)
        assert type(lineReader) is ReadUtils__LineReader

        fileLine = file.AddEmptyLine()
        assert type(fileLine) is PostgresConfigurationFileLine_Base

        ch: typing.Optional[str]

        while True:
            # skeep spaces
            while True:
                ch = lineReader.ReadSymbol()
                if ch is None:
                    return

                if ReadUtils.IsSpace(ch):
                    continue

                break

            assert not ReadUtils.IsSpace(ch)

            if ReadUtils.IsEOL(ch):
                return

            if ch == "#":
                return __class__.Helper__ProcessLineData__Comment(
                    fileLine,
                    lineReader,
                )

            if len(fileLine) == 0 and ReadUtils.IsValidSeqCh1(ch):
                # Read sequence
                sequenceOffset = lineReader.GetColOffset()
                sequence = ch

                while True:
                    ch = lineReader.ReadSymbol()

                    if not ch:
                        assert ch is None
                        break

                    assert type(ch) is str

                    if ReadUtils.IsValidSeqCh2(ch):
                        sequence += ch
                        continue

                    if ch == ".":
                        sequence += ch
                        continue

                    break

                if sequence.lower() == "include":
                    if ch is not None:
                        lineReader.StepBack()

                    __class__.Helper__ProcessLineData__Include(
                        fileLine,
                        lineReader,
                        sequenceOffset,
                    )
                else:
                    if ch is not None:
                        lineReader.StepBack()

                    __class__.Helper__ProcessLineData__Option(
                        fileLine,
                        lineReader,
                        sequenceOffset,
                        sequence,
                    )
                continue

            RaiseError.CfgReader__UnexpectedSymbol(
                lineReader.GetLineNum(),
                lineReader.GetColNum(),
                ch,
            )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ProcessLineData__Comment(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
    ) -> None:
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(lineReader) is ReadUtils__LineReader

        commentText = ""
        commentOffset = lineReader.GetColOffset()

        while True:
            ch = lineReader.ReadSymbol()

            if not ch:
                assert ch is None
                break

            assert type(ch) is str

            if ReadUtils.IsEOL(ch):
                break
            commentText += ch

        fileLine.AddComment(
            commentText,
            commentOffset,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ProcessLineData__Include(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        includeOffset: int,
    ) -> None:
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(lineReader) is ReadUtils__LineReader
        assert type(includeOffset) is int
        assert includeOffset >= 0

        # find first quote
        while True:
            ch = lineReader.ReadSymbol()

            if ch is None or ReadUtils.IsEOL(ch) or ch == "#":
                RaiseError.CfgReader__IncludeWithoutPath(
                    lineReader.GetLineNum(),
                )

            if ReadUtils.IsSpace(ch):
                continue

            if ch == "'":
                break

            RaiseError.CfgReader__UnexpectedSymbol(
                lineReader.GetLineNum(),
                lineReader.GetColNum(),
                ch,
            )

        # OK. First quote is found!

        # Let's process this quoted string
        filePath = ""

        while True:
            ch = lineReader.ReadSymbol()

            if ch is None or ReadUtils.IsEOL(ch):
                RaiseError.CfgReader__EndOfIncludePathIsNotFound(
                    lineReader.GetLineNum(),
                )
                break

            if ch == "'":
                ch2 = lineReader.ReadSymbol()

                if ch2 is None:
                    break

                if ReadUtils.IsEOL(ch2):
                    lineReader.StepBack()
                    break

                if ch2 == "'":
                    filePath += ch
                    continue

                break

            if ch == "\\":
                ch = lineReader.ReadSymbol()

                if ch is None or ReadUtils.IsEOL(ch):
                    RaiseError.CfgReader__IncompletedEscapeInInclude(
                        lineReader.GetLineNum(),
                    )

                if ch == "b":
                    filePath += "\b"
                elif ch == "f":
                    filePath += "\f"
                elif ch == "n":
                    filePath += "\n"
                elif ch == "r":
                    filePath += "\r"
                elif ch == "t":
                    filePath += "\t"
                elif ch == "'":
                    filePath += "'"
                elif ch == '"':
                    filePath += '"'
                elif ch >= "0" and ch <= "7":  # octNumber
                    octVal = 0

                    octVal_n = 1

                    while True:
                        d = int(ord(ch) - ord("0"))
                        assert d >= 0 and d <= 7

                        octVal = (octVal * 8) + d

                        if octVal_n == 3:
                            break

                        ch = lineReader.ReadSymbol()

                        if ch is None:
                            break

                        if not (ch >= "0" and ch <= "7"):
                            lineReader.StepBack()
                            break

                        octVal_n += 1
                        continue

                    filePath += chr(octVal)
                else:
                    RaiseError.CfgReader__UnknownEscapedSymbolInInclude(
                        lineReader.GetLineNum(),
                        lineReader.GetColNum(),
                        ch,
                    )

                continue

            filePath += ch
            continue

        assert type(filePath) is str

        if len(filePath) == 0:
            RaiseError.CfgReader__IncludeHasEmptyPath(
                lineReader.GetLineNum(),
            )

        fileLine.AddInclude(
            filePath,
            includeOffset,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ProcessLineData__Option(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        optionOffset: int,
        optionName: str,
    ) -> None:
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(lineReader) is ReadUtils__LineReader
        assert type(optionOffset) is int
        assert type(optionName) is str
        assert optionName != ""

        # skeep spaces
        spaceIsDetected = False

        while True:
            ch = lineReader.ReadSymbol()
            if ch is None or ReadUtils.IsEOL(ch) or ch == "#":
                RaiseError.CfgReader__OptionWithoutValue(
                    optionName,
                    lineReader.GetLineNum(),
                )

            if ReadUtils.IsSpace(ch):
                spaceIsDetected = True
                continue

            if ch == "=":
                while True:
                    ch = lineReader.ReadSymbol()

                    if ch is None or ReadUtils.IsEOL(ch) or ch == "#":
                        RaiseError.CfgReader__OptionWithoutValue(
                            optionName,
                            lineReader.GetLineNum(),
                        )

                    if ReadUtils.IsSpace(ch):
                        continue

                    break
                break

            if spaceIsDetected:
                break

            RaiseError.CfgReader__UnexpectedSymbol(
                lineReader.GetLineNum(),
                lineReader.GetColNum(),
                ch,
            )

        # ch is the first symbol of option value.

        if ch == "'":
            __class__.Helper__ProcessLineData__Option__Quoted(
                fileLine,
                lineReader,
                optionOffset,
                optionName,
            )
        else:
            lineReader.StepBack()

            __class__.Helper__ProcessLineData__Option__Generic(
                fileLine,
                lineReader,
                optionOffset,
                optionName,
            )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ProcessLineData__Option__Quoted(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        optionOffset: int,
        optionName: str,
    ) -> None:
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(lineReader) is ReadUtils__LineReader
        assert type(optionOffset) is int
        assert type(optionName) is str
        assert optionName != ""

        optionValue = ""

        while True:
            ch = lineReader.ReadSymbol()

            if ch is None or ReadUtils.IsEOL(ch):
                RaiseError.CfgReader__EndQuotedOptionValueIsNotFound(
                    optionName,
                    lineReader.GetLineNum(),
                )
                break

            if ch == "'":
                ch2 = lineReader.ReadSymbol()

                if ch2 is None:
                    break

                if ReadUtils.IsEOL(ch2):
                    lineReader.StepBack()
                    break

                if ch2 == "'":
                    optionValue += ch
                    continue

                break

            if ch == "\\":
                ch = lineReader.ReadSymbol()

                if ch is None or ReadUtils.IsEOL(ch):
                    RaiseError.CfgReader__IncompletedEscapeInQuotedOptionValue(
                        optionName,
                        lineReader.GetLineNum(),
                    )

                if ch == "b":
                    optionValue += "\b"
                elif ch == "f":
                    optionValue += "\f"
                elif ch == "n":
                    optionValue += "\n"
                elif ch == "r":
                    optionValue += "\r"
                elif ch == "t":
                    optionValue += "\t"
                elif ch == "'":
                    optionValue += "'"
                elif ch == '"':
                    optionValue += '"'
                elif ch >= "0" and ch <= "7":  # octNumber
                    octVal = 0

                    octVal_n = 1

                    while True:
                        d = int(ord(ch) - ord("0"))
                        assert d >= 0 and d <= 7

                        octVal = (octVal * 8) + d

                        if octVal_n == 3:
                            break

                        ch = lineReader.ReadSymbol()

                        if ch is None:
                            break

                        if not (ch >= "0" and ch <= "7"):
                            lineReader.StepBack()
                            break

                        octVal_n += 1
                        continue

                    optionValue += chr(octVal)
                else:
                    RaiseError.CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
                        optionName,
                        lineReader.GetLineNum(),
                        lineReader.GetColNum(),
                        ch,
                    )

                continue

            optionValue += ch
            continue

        assert type(optionValue) is str

        fileLine.AddOption(
            optionName,
            optionValue,
            optionOffset,
        )
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ProcessLineData__Option__Generic(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        optionOffset: int,
        optionName: str,
    ) -> None:
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(lineReader) is ReadUtils__LineReader
        assert type(optionOffset) is int
        assert type(optionName) is str
        assert optionName != ""

        optionValue = ""

        while True:
            ch = lineReader.ReadSymbol()

            if not ch:
                assert ch is None
                break

            assert type(ch) is str

            if ch == "#" or ReadUtils.IsEOL(ch):
                lineReader.StepBack()
                break

            optionValue += ch
            continue

        optionValue = optionValue.strip()

        assert type(optionValue) is str
        assert optionValue != ""

        fileLine.AddOption(
            optionName,
            optionValue,
            optionOffset,
        )
        return


# //////////////////////////////////////////////////////////////////////////////
