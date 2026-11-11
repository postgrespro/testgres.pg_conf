# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

# fmt: off
from .configuration_base import PostgresConfiguration_Base

from ...core.model import ConfigurationData as PgCfgModel__ConfigurationData
from ...core.model import FileLineElementData as PgCfgModel__FileLineElementData
from ...core.model import CommentData as PgCfgModel__CommentData
from ...core.model import OptionData as PgCfgModel__OptionData
from ...core.model import IncludeData as PgCfgModel__IncludeData
from ...core.model import FileLineData as PgCfgModel__FileLineData
from ...core.model import FileData as PgCfgModel__FileData
from ...core.model import FileStatus as PgCfgModel__FileStatus

from ...core.handlers import OptionHandlerToWrite as PgCfgModel__OptionHandlerToWrite
from ...core.handlers import OptionHandlerCtxToWrite as PgCfgModel__OptionHandlerCtxToWrite

from ...core.data_verificator import DataVerificator
from ...core.write_utils import WriteUtils
from ...core.raise_error import RaiseError
from ...core.bugcheck_error import BugCheckError
# fmt: on

from ...os.abstract.configuration_os_ops import ConfigurationOsFile

import typing
import datetime

# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriterFileCtx_Base


class PostgresConfigurationWriterFileCtx_Base:
    FileData: PgCfgModel__FileData
    Content: typing.Optional[str]
    File: typing.Optional[ConfigurationOsFile]

    # TODO: We can use filelock (it is a separated lock file)
    # to provide an exclusive access to our File

    # --------------------------------------------------------------------
    def __init__(self, fileData: PgCfgModel__FileData):
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData

        self.FileData = fileData
        self.Content = None
        self.File = None
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriterCtx_Base


class PostgresConfigurationWriterCtx_Base:
    Cfg: PostgresConfiguration_Base

    AllFiles: typing.List[PostgresConfigurationWriterFileCtx_Base]
    NewFiles: typing.List[PostgresConfigurationWriterFileCtx_Base]
    UpdFiles: typing.List[PostgresConfigurationWriterFileCtx_Base]

    # --------------------------------------------------------------------
    def __init__(self, cfg: PostgresConfiguration_Base):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)

        self.Cfg = cfg

        self.AllFiles = list()
        self.NewFiles = list()
        self.UpdFiles = list()

        assert type(self.AllFiles) is list
        assert type(self.NewFiles) is list
        assert type(self.UpdFiles) is list
        return

    # --------------------------------------------------------------------
    def Init(self) -> None:
        assert type(self.AllFiles) is list
        assert type(self.NewFiles) is list
        assert type(self.UpdFiles) is list

        self.AllFiles.clear()
        self.NewFiles.clear()
        self.UpdFiles.clear()
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriter_Base


class PostgresConfigurationWriter_Base:
    @staticmethod
    def MakeFileDataContent(
        ctx: PostgresConfigurationWriterCtx_Base,
        fileData: PgCfgModel__FileData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert type(fileData) is PgCfgModel__FileData

        return __class__.Helper__MakeFileDataContent(
            ctx,
            fileData,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def DoWork(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) is PgCfgModel__ConfigurationData

        return __class__.Helper__DoWork(ctx)

    # Helper Methods -----------------------------------------------------
    @staticmethod
    def Helper__DoWork(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) is PgCfgModel__ConfigurationData

        # 0.
        ctx.Init()

        # 1.
        __class__.Helper__DoWork__Stage01__CreateFileContexts(ctx)

        # 2.
        __class__.Helper__DoWork__Stage02__MakeFileDataContents(ctx)

        # 3.
        __class__.Helper__DoWork__Stage03__OpenUpdFilesToWrite(ctx)

        # 4.
        __class__.Helper__DoWork__Stage04__OpenNewFilesToWrite(ctx)

        # 5.
        __class__.Helper__DoWork__Stage05__WriteContents(ctx)

        # OK. Go HOME!
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DoWork__Stage01__CreateFileContexts(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) is PgCfgModel__ConfigurationData

        for fileData in ctx.Cfg.m_Data.m_AllFilesByName.elements():
            assert fileData is not None
            assert type(fileData) is PgCfgModel__FileData

            fileCtx = PostgresConfigurationWriterFileCtx_Base(fileData)

            assert fileCtx.FileData is fileData
            assert fileCtx.Content is None
            assert fileCtx.File is None

            assert fileCtx not in ctx.AllFiles
            assert fileCtx not in ctx.NewFiles
            assert fileCtx not in ctx.UpdFiles

            ctx.AllFiles.append(fileCtx)

            if fileData.m_Status == PgCfgModel__FileStatus.IS_NEW:
                ctx.NewFiles.append(fileCtx)
            elif fileData.m_Status == PgCfgModel__FileStatus.EXISTS:
                ctx.UpdFiles.append(fileCtx)
            else:
                BugCheckError.UnkFileDataStatus(
                    fileData.m_Path,
                    fileData.m_Status,
                )
            continue
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DoWork__Stage02__MakeFileDataContents(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) is PgCfgModel__ConfigurationData

        for fileCtx in ctx.AllFiles:
            assert fileCtx is not None
            assert type(fileCtx) is PostgresConfigurationWriterFileCtx_Base
            assert type(fileCtx.FileData) is PgCfgModel__FileData
            assert fileCtx.Content is None

            fileCtx.Content = __class__.Helper__MakeFileDataContent(
                ctx,
                fileCtx.FileData,
            )
            continue
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DoWork__Stage03__OpenUpdFilesToWrite(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) is PgCfgModel__ConfigurationData

        for fileCtx in ctx.UpdFiles:
            assert fileCtx is not None
            assert type(fileCtx) is PostgresConfigurationWriterFileCtx_Base
            assert type(fileCtx.FileData) is PgCfgModel__FileData

            assert fileCtx.FileData.m_Status == PgCfgModel__FileStatus.EXISTS
            assert fileCtx.FileData.m_LastModifiedTimestamp is not None
            assert type(fileCtx.FileData.m_LastModifiedTimestamp) is datetime.datetime
            assert fileCtx.File is None

            # Let's open an exist file to read and write without truncation
            fileCtx.File = ctx.Cfg.m_Data.OsOps.OpenFileToWrite(
                fileCtx.FileData.m_Path,
            )  # raise

            assert fileCtx.File is not None
            assert isinstance(fileCtx.File, ConfigurationOsFile)

            lastMDate = fileCtx.File.GetModificationTS()
            assert type(lastMDate) is datetime.datetime

            if fileCtx.FileData.m_LastModifiedTimestamp != lastMDate:
                RaiseError.FileWasModifiedExternally(
                    fileCtx.FileData.m_Path,
                    fileCtx.FileData.m_LastModifiedTimestamp,
                    lastMDate,
                )

            # OK!
            continue

        # OK, Go HOME!
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DoWork__Stage04__OpenNewFilesToWrite(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(ctx.NewFiles) is list

        iFile = 0

        try:
            for iFile in range(len(ctx.NewFiles)):
                fileCtx = ctx.NewFiles[iFile]

                assert fileCtx is not None
                assert type(fileCtx) is PostgresConfigurationWriterFileCtx_Base
                assert type(fileCtx.FileData) is PgCfgModel__FileData

                assert fileCtx.FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
                assert fileCtx.File is None

                fileCtx.File = ctx.Cfg.m_Data.OsOps.CreateFile(
                    fileCtx.FileData.m_Path
                )  # raise

                assert fileCtx.File is not None
                assert isinstance(fileCtx.File, ConfigurationOsFile)

                # OK
                continue

        except:  # Rollback new files
            assert type(iFile) is int
            assert iFile >= 0
            assert iFile <= len(ctx.NewFiles)

            for iFile2 in range(iFile):
                fileCtx = ctx.NewFiles[iFile2]

                assert fileCtx is not None
                assert type(fileCtx) is PostgresConfigurationWriterFileCtx_Base
                assert type(fileCtx.FileData) is PgCfgModel__FileData

                assert fileCtx.FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
                assert fileCtx.File is not None
                assert isinstance(fileCtx.File, ConfigurationOsFile)

                assert not fileCtx.File.IsClosed

                filePath = fileCtx.File.Name
                assert filePath is not None
                assert type(filePath) is str
                assert filePath == fileCtx.FileData.m_Path

                fileCtx.File.Close()  # raise

                ctx.Cfg.m_Data.OsOps.Remove(filePath)  # raise
                continue

            raise

        # OK, Go HOME!
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__DoWork__Stage05__WriteContents(
        ctx: PostgresConfigurationWriterCtx_Base,
    ) -> None:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base

        for iFile in range(len(ctx.AllFiles)):
            fileCtx = ctx.AllFiles[iFile]

            assert fileCtx is not None
            assert type(fileCtx) is PostgresConfigurationWriterFileCtx_Base
            assert type(fileCtx.FileData) is PgCfgModel__FileData

            assert fileCtx.File is not None
            assert isinstance(fileCtx.File, ConfigurationOsFile)

            assert fileCtx.Content is not None
            assert type(fileCtx.Content) is str

            fileCtx.File.Overwrite(fileCtx.Content)

            lastMDate = fileCtx.File.GetModificationTS()
            assert type(lastMDate) is datetime.datetime

            fileCtx.File.Close()

            fileCtx.FileData.m_LastModifiedTimestamp = lastMDate
            fileCtx.FileData.m_Status = PgCfgModel__FileStatus.EXISTS
            continue
        return

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__MakeFileDataContent(
        ctx: PostgresConfigurationWriterCtx_Base,
        fileData: PgCfgModel__FileData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert type(fileData) is PgCfgModel__FileData

        fileContent = ""

        for fileLineData in fileData.m_Lines:
            assert type(fileLineData) is PgCfgModel__FileLineData
            lineContent = __class__.Helper__FileLineToString(
                ctx,
                fileLineData,
            )
            assert type(lineContent) is str
            fileContent += lineContent
            fileContent += "\n"
            continue

        return fileContent

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__FileLineToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        fileLineData: PgCfgModel__FileLineData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert type(fileLineData) is PgCfgModel__FileLineData

        fileLineItemCount = len(fileLineData.m_Items)

        if fileLineItemCount == 0:
            return ""

        lineContent = ""

        for lineItem in fileLineData.m_Items:
            assert type(lineItem) is PgCfgModel__FileLineData.tagItem
            assert lineItem.m_Element is not None
            assert isinstance(lineItem.m_Element, PgCfgModel__FileLineElementData)
            assert (
                lineItem.m_Element.m_Offset is None
                or type(lineItem.m_Element.m_Offset) is int
            )
            assert (
                lineItem.m_Element.m_Offset is None or lineItem.m_Element.m_Offset >= 0
            )

            itemContent = __class__.Helper__ElementToString(
                ctx,
                lineItem.m_Element,
            )
            assert type(itemContent) is str

            lineContent = __class__.Helper__AppendItemToLine(
                lineContent,
                lineItem.m_Element.m_Offset,
                itemContent,
            )
            assert type(lineContent) is str
            continue

        assert type(lineContent) is str
        return lineContent

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__AppendItemToLine(
        lineContent: str,
        offset: typing.Optional[int],
        text: str,
    ) -> str:
        assert type(lineContent) is str
        assert offset is None or type(offset) is int
        assert type(text) is str
        assert offset is None or offset >= 0

        if text == "":
            return lineContent

        lineContentLen = len(lineContent)

        assert type(lineContentLen) is int
        assert lineContentLen >= 0

        if offset is not None and lineContentLen < offset:
            lineContent += " " * (offset - lineContentLen)
        elif lineContentLen > 0:
            lineContent += " "

        lineContent += text
        return lineContent

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__ElementToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        elementData: PgCfgModel__FileLineElementData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert elementData is not None
        assert isinstance(elementData, PgCfgModel__FileLineElementData)

        if type(elementData) is PgCfgModel__OptionData:
            return __class__.Helper__OptionToString(
                ctx,
                elementData,
            )

        if type(elementData) is PgCfgModel__CommentData:
            return __class__.Helper__CommentToString(
                ctx,
                elementData,
            )

        if type(elementData) is PgCfgModel__IncludeData:
            return __class__.Helper__IncludeToString(
                ctx,
                elementData,
            )

        BugCheckError.UnkObjectDataType(type(elementData))

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__OptionToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        optionData: PgCfgModel__OptionData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert ctx.Cfg is not None
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(optionData) is PgCfgModel__OptionData
        assert type(optionData.m_Name) is str
        assert optionData.m_Name != ""
        assert optionData.m_Value is not None

        writeHandler = ctx.Cfg.Internal__GetOptionHandlerToWrite(
            optionData.m_Name,
        )

        assert writeHandler is not None
        assert isinstance(writeHandler, PgCfgModel__OptionHandlerToWrite)

        writeHandlerCtx = PgCfgModel__OptionHandlerCtxToWrite(
            ctx.Cfg,
            optionData.m_Name,
            optionData.m_Value,
        )

        optValueAsText = writeHandler.OptionValueToString(
            writeHandlerCtx,
        )

        assert type(optValueAsText) is str
        assert optValueAsText != ""

        result = optionData.m_Name + " = " + optValueAsText
        return result

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CommentToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        commentData: PgCfgModel__CommentData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert ctx.Cfg is not None
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(commentData) is PgCfgModel__CommentData
        assert commentData.m_Text is not None
        assert type(commentData.m_Text) is str

        assert DataVerificator.IsValidCommentText(commentData.m_Text)

        result = "#" + commentData.m_Text
        return result

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__IncludeToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        includeData: PgCfgModel__IncludeData,
    ) -> str:
        assert type(ctx) is PostgresConfigurationWriterCtx_Base
        assert ctx.Cfg is not None
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(includeData) is PgCfgModel__IncludeData
        assert includeData.m_Path is not None
        assert type(includeData.m_Path) is str
        assert includeData.m_Path != ""

        result = "include " + WriteUtils.Pack_Str(includeData.m_Path)

        assert type(result) is str
        assert result != ""
        return result


# //////////////////////////////////////////////////////////////////////////////
