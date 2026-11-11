# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

# fmt: off
from ...abstract.v00.configuration import PostgresConfiguration
from ...abstract.v00.configuration import PostgresConfigurationObject
from ...abstract.v00.configuration import PostgresConfigurationComment
from ...abstract.v00.configuration import PostgresConfigurationOption
from ...abstract.v00.configuration import PostgresConfigurationOptions
from ...abstract.v00.configuration import PostgresConfigurationOptionsIterator
from ...abstract.v00.configuration import PostgresConfigurationInclude
from ...abstract.v00.configuration import PostgresConfigurationFileLine
from ...abstract.v00.configuration import PostgresConfigurationFileLines
from ...abstract.v00.configuration import PostgresConfigurationFileLinesIterator
from ...abstract.v00.configuration import PostgresConfigurationFile
from ...abstract.v00.configuration import PostgresConfigurationFiles
from ...abstract.v00.configuration import PostgresConfigurationFilesIterator
from ...abstract.v00.configuration import PostgresConfigurationSetOptionValueEventID
from ...abstract.v00.configuration import PostgresConfigurationSetOptionValueResult

from ...core.model import ConfigurationData as PgCfgModel__ConfigurationData
from ...core.model import ObjectData as PgCfgModel__ObjectData
from ...core.model import CommentData as PgCfgModel__CommentData
from ...core.model import OptionData as PgCfgModel__OptionData
from ...core.model import IncludeData as PgCfgModel__IncludeData
from ...core.model import FileLineData as PgCfgModel__FileLineData
from ...core.model import FileData as PgCfgModel__FileData
from ...core.model import MultiIndex as PgCfgModel__MultiIndex

from ...core.handlers import OptionHandlerToPrepareSetValue as PgCfgModel__OptionHandlerToPrepareSetValue
from ...core.handlers import OptionHandlerCtxToPrepareSetValue as PgCfgModel__OptionHandlerCtxPrepareToSetValue
from ...core.handlers import OptionHandlerToPrepareGetValue as PgCfgModel__OptionHandlerToPrepareGetValue
from ...core.handlers import OptionHandlerToPrepareSetValueItem as PgCfgModel__OptionHandlerToPrepareSetValueItem
from ...core.handlers import OptionHandlerCtxToPrepareSetValueItem as PgCfgModel__OptionHandlerCtxPrepareToSetValueItem
from ...core.handlers import OptionHandlerToSetValue as PgCfgModel__OptionHandlerToSetValue
from ...core.handlers import OptionHandlerCtxToSetValue as PgCfgModel__OptionHandlerCtxToSetValue
from ...core.handlers import OptionHandlerToGetValue as PgCfgModel__OptionHandlerToGetValue
from ...core.handlers import OptionHandlerCtxToGetValue as PgCfgModel__OptionHandlerCtxToGetValue
from ...core.handlers import OptionHandlerToAddOption as PgCfgModel__OptionHandlerToAddOption
from ...core.handlers import OptionHandlerCtxToAddOption as PgCfgModel__OptionHandlerCtxToAddOption
from ...core.handlers import OptionHandlerToSetValueItem as PgCfgModel__OptionHandlerToSetValueItem
from ...core.handlers import OptionHandlerCtxToSetValueItem as PgCfgModel__OptionHandlerCtxToSetValueItem
from ...core.handlers import OptionHandlerToWrite as PgCfgModel__OptionHandlerToWrite
from ...core.handlers import ConfigurationDataHandler as PgCfgModel__DataHandler

from ...core.model_utils import ModelUtils as PgCfgModel__ModelUtils
from ...core.data_verificator import DataVerificator
from ...core.raise_error import RaiseError
from ...core.bugcheck_error import BugCheckError
# fmt: on

from ...os.abstract.configuration_os_ops import ConfigurationOsOps

import typing
import dataclasses

# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationComment_Base


class PostgresConfigurationComment_Base(PostgresConfigurationComment):
    m_FileLine: PostgresConfigurationFileLine_Base
    m_CommentData: PgCfgModel__CommentData

    # --------------------------------------------------------------------
    def __init__(
        self,
        fileLine: PostgresConfigurationFileLine_Base,
        commentData: PgCfgModel__CommentData,
    ):
        assert fileLine is not None
        assert commentData is not None
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(commentData) is PgCfgModel__CommentData

        assert commentData.m_Parent is fileLine.m_FileLineData

        super().__init__()

        self.m_FileLine = fileLine
        self.m_CommentData = commentData
        return

    # Object interface ---------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        self.Helper__CheckAlive()
        return self.m_FileLine.get_Configuration()

    # --------------------------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationFileLine_Base:
        self.Helper__CheckAlive()
        return self.m_FileLine

    # Comment interface --------------------------------------------------
    def get_Text(self) -> str:
        self.Helper__CheckAlive()
        assert type(self.m_CommentData) is PgCfgModel__CommentData
        assert type(self.m_CommentData.m_Text) is str
        return self.m_CommentData.m_Text

    # --------------------------------------------------------------------
    def Delete(
        self,
        withLineIfLast: bool,
    ) -> None:
        assert type(withLineIfLast) is bool

        self.Helper__CheckAlive()
        assert type(self.m_CommentData) is PgCfgModel__CommentData
        assert type(self.m_CommentData.m_Parent) is PgCfgModel__FileLineData
        assert type(self.m_CommentData.m_Parent.m_Parent) is PgCfgModel__FileData
        assert (
            type(self.m_CommentData.m_Parent.m_Parent.m_Parent)
            is PgCfgModel__ConfigurationData
        )

        cfgData = self.m_CommentData.m_Parent.m_Parent.m_Parent
        assert type(cfgData) is PgCfgModel__ConfigurationData

        PgCfgModel__ModelUtils.Comment__delete(
            cfgData,
            self.m_CommentData,
            withLineIfLast,
        )
        return

    # Helper interface ---------------------------------------------------
    def Helper__CheckAlive(self) -> None:
        assert self.m_CommentData is not None
        assert type(self.m_CommentData) is PgCfgModel__CommentData

        if not self.m_CommentData.IsAlive():
            RaiseError.CommentObjectWasDeleted()

        assert type(self.m_FileLine) is PostgresConfigurationFileLine_Base
        assert isinstance(self.m_FileLine, PostgresConfigurationFileLine)
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationOption_Base


class PostgresConfigurationOption_Base(PostgresConfigurationOption):
    m_FileLine: PostgresConfigurationFileLine_Base
    m_OptionData: PgCfgModel__OptionData

    # --------------------------------------------------------------------
    def __init__(
        self,
        fileLine: PostgresConfigurationFileLine_Base,
        optionData: PgCfgModel__OptionData,
    ):
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(optionData) is PgCfgModel__OptionData

        super().__init__()

        self.m_FileLine = fileLine
        self.m_OptionData = optionData
        return

    # Object interface ---------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        self.Helper__CheckAlive()
        return self.m_FileLine.get_Configuration()

    # --------------------------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationFileLine_Base:
        self.Helper__CheckAlive()
        return self.m_FileLine

    # Option interface ---------------------------------------------------
    def get_Name(self) -> str:
        self.Helper__CheckAlive()
        return self.m_OptionData.m_Name

    # --------------------------------------------------------------------
    def get_Value(self) -> typing.Any:
        self.Helper__CheckAlive()

        configuration = self.m_FileLine.get_Configuration()

        assert configuration is not None
        assert isinstance(configuration, PostgresConfiguration_Base)
        assert isinstance(configuration, PgCfgModel__DataHandler)

        r = PostgresConfigurationController__Base.GetOptionValue(
            configuration,
            self.m_OptionData,
            self.m_OptionData.m_Name,
        )

        return r

    # --------------------------------------------------------------------
    def set_Value(
        self,
        value: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        self.Helper__CheckAlive()

        configuration = self.m_FileLine.get_Configuration()

        assert configuration is not None
        assert isinstance(configuration, PostgresConfiguration_Base)
        assert isinstance(configuration, PgCfgModel__DataHandler)

        r = PostgresConfigurationController__Base.SetOptionValue(
            configuration,
            self.m_OptionData,  # target
            self.m_OptionData.m_Name,
            value,
            None,  # offset
        )

        assert type(r) is PostgresConfigurationSetOptionValueResult_Base

        assert r.m_OptData is None or r.m_OptData is self.m_OptionData
        assert r.m_Opt is None

        if r.m_OptData is not None:
            r.m_Opt = self  # Optimization

        return r

    # --------------------------------------------------------------------
    def set_ValueItem(
        self,
        value_item: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult:
        self.Helper__CheckAlive()

        configuration = self.m_FileLine.get_Configuration()

        assert configuration is not None
        assert isinstance(configuration, PostgresConfiguration_Base)
        assert isinstance(configuration, PgCfgModel__DataHandler)

        r = PostgresConfigurationController__Base.SetOptionValueItem(
            configuration,
            self.m_OptionData,  # target
            self.m_OptionData.m_Name,
            value_item,
        )

        assert type(r) is PostgresConfigurationSetOptionValueResult_Base

        assert r.m_OptData is not None
        assert r.m_OptData is self.m_OptionData
        assert r.m_Opt is None

        if r.m_OptData is not None:
            r.m_Opt = self  # Optimization

        return r

    # Helper methods -----------------------------------------------------
    def Helper__CheckAlive(self) -> None:
        assert self.m_OptionData is not None
        assert type(self.m_OptionData) is PgCfgModel__OptionData

        if not self.m_OptionData.IsAlive():
            RaiseError.OptionObjectWasDeleted()

        assert type(self.m_FileLine) is PostgresConfigurationFileLine_Base
        assert isinstance(self.m_FileLine, PostgresConfigurationFileLine)
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationInclude_Base


class PostgresConfigurationInclude_Base(PostgresConfigurationInclude):
    m_FileLine: PostgresConfigurationFileLine_Base
    m_IncludeData: PgCfgModel__IncludeData

    # --------------------------------------------------------------------
    def __init__(
        self,
        fileLine: PostgresConfigurationFileLine_Base,
        includeData: PgCfgModel__IncludeData,
    ):
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        assert type(includeData) is PgCfgModel__IncludeData

        super().__init__()

        self.m_FileLine = fileLine
        self.m_IncludeData = includeData
        return

    # Object interface ---------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        self.Helper__CheckAlive()
        return self.m_FileLine.get_Configuration()

    # --------------------------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationFileLine_Base:
        self.Helper__CheckAlive()
        return self.m_FileLine

    # Include interface --------------------------------------------------
    def get_File(self) -> PostgresConfigurationIncludedFile_Base:
        self.Helper__CheckAlive()

        return PostgresConfigurationIncludedFile_Base(
            self,
            self.m_IncludeData.m_File,
        )

    # --------------------------------------------------------------------
    def Delete(
        self,
        withLine: bool,
    ) -> None:
        assert type(withLine) is bool

        self.Helper__CheckAlive()
        assert type(self.m_IncludeData) is PgCfgModel__IncludeData
        assert type(self.m_IncludeData.m_Parent) is PgCfgModel__FileLineData
        assert type(self.m_IncludeData.m_Parent.m_Parent) is PgCfgModel__FileData
        assert (
            type(self.m_IncludeData.m_Parent.m_Parent.m_Parent)
            is PgCfgModel__ConfigurationData
        )

        cfgData = self.m_IncludeData.m_Parent.m_Parent.m_Parent
        assert type(cfgData) is PgCfgModel__ConfigurationData

        PgCfgModel__ModelUtils.Include__delete(
            cfgData,
            self.m_IncludeData,
            withLine,
        )
        return

    # Private interface --------------------------------------------------
    def Private__CheckAlive(self) -> None:
        self.Helper__CheckAlive()
        return

    # Helper methods -----------------------------------------------------
    def Helper__CheckAlive(self) -> None:
        assert self.m_IncludeData is not None
        assert type(self.m_IncludeData) is PgCfgModel__IncludeData

        if not self.m_IncludeData.IsAlive():
            RaiseError.IncludeObjectWasDeleted()

        assert type(self.m_FileLine) is PostgresConfigurationFileLine_Base
        assert isinstance(self.m_FileLine, PostgresConfigurationFileLine)
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLine_Base


class PostgresConfigurationFileLine_Base(PostgresConfigurationFileLine):
    m_Parent: PostgresConfigurationFile_Base
    m_FileLineData: PgCfgModel__FileLineData

    # --------------------------------------------------------------------
    def __init__(
        self,
        parent: PostgresConfigurationFile_Base,
        fileLineData: PgCfgModel__FileLineData,
    ):
        assert parent is not None
        assert isinstance(parent, PostgresConfigurationFile_Base)
        assert type(fileLineData) is PgCfgModel__FileLineData

        super().__init__()

        self.m_Parent = parent
        self.m_FileLineData = fileLineData
        return

    # Object interface ---------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        self.Helper__CheckAlive()
        assert self.m_Parent is not None
        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)
        return self.m_Parent.get_Configuration()

    # --------------------------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationFile_Base:
        self.Helper__CheckAlive()
        assert self.m_Parent is not None
        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)
        return self.m_Parent

    # FileLine interface -------------------------------------------------
    def __len__(self) -> int:
        self.Helper__CheckAlive()
        assert type(self.m_FileLineData) is PgCfgModel__FileLineData
        assert type(self.m_FileLineData.m_Items) is list
        return len(self.m_FileLineData.m_Items)

    # --------------------------------------------------------------------
    def AddComment(
        self,
        text: str,
        offset: typing.Optional[int] = None,
    ) -> PostgresConfigurationComment_Base:
        assert type(text) is str
        assert offset is None or type(offset) is int

        self.Helper__CheckAlive()

        DataVerificator.CheckCommentText(text)

        commentData = PgCfgModel__ModelUtils.FileLine__add_Comment(
            self.m_FileLineData,
            offset,
            text,
        )
        assert commentData is not None
        assert type(commentData) is PgCfgModel__CommentData
        assert commentData.m_Parent is self.m_FileLineData
        assert type(commentData.m_Parent) is PgCfgModel__FileLineData
        assert type(commentData.m_Parent.m_Items) is list
        assert len(commentData.m_Parent.m_Items) > 0
        assert commentData.m_Parent.m_Items[-1].m_Element is commentData

        try:
            fileLineComment = PostgresConfigurationComment_Base(
                self,
                commentData,
            )

            assert fileLineComment is not None
            assert type(fileLineComment) is PostgresConfigurationComment_Base
        except:  # rollback
            cfg = self.m_Parent.get_Configuration()
            assert cfg is not None
            assert isinstance(cfg, PostgresConfiguration_Base)
            assert cfg.m_Data is not None
            assert type(cfg.m_Data) is PgCfgModel__ConfigurationData

            PgCfgModel__ModelUtils.Comment__delete(
                cfg.m_Data,
                commentData,
                False,
            )
            raise

        assert fileLineComment
        assert type(fileLineComment) is PostgresConfigurationComment_Base
        return fileLineComment

    # --------------------------------------------------------------------
    def AddOption(
        self,
        name: str,
        value: typing.Any,
        offset: typing.Optional[int],
    ) -> PostgresConfigurationOption_Base:
        assert offset is None or type(offset) is int
        assert offset is None or offset >= 0

        DataVerificator.CheckOptionName(name)

        assert name is not None
        assert name != ""

        if value is None:
            RaiseError.NoneValueIsNotSupported()

        assert value is not None

        self.Helper__CheckAlive()
        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)

        cfg = self.m_Parent.m_Cfg
        assert isinstance(cfg, PostgresConfiguration_Base)

        option = PostgresConfigurationController__Base.AddOption(
            cfg,
            self.m_FileLineData,
            name,
            value,
            offset,
        )

        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        return option

    # --------------------------------------------------------------------
    def AddInclude(
        self,
        path: str,
        offset: typing.Optional[int],
    ) -> PostgresConfigurationInclude_Base:
        assert offset is None or type(offset) is int
        assert offset is None or offset >= 0

        DataVerificator.CheckStringOfFilePath(path)

        assert type(path) is str
        assert path != ""

        self.Helper__CheckAlive()

        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)

        cfg = self.m_Parent.m_Cfg
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData

        # Add/Get file
        # Add include element

        assert self.m_FileLineData.m_Parent is not None

        baseFolder = cfg.m_Data.OsOps.Path_DirName(
            self.m_FileLineData.m_Parent.m_Path,
        )
        assert type(baseFolder) is str

        fileData = PgCfgModel__ModelUtils.Cfg__GetOrCreateFile__USER(
            cfg.m_Data,
            baseFolder,
            path,
        )
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData

        try:
            includeData = PgCfgModel__ModelUtils.FileLine__add_Include(
                self.m_FileLineData,
                path,
                fileData,
                offset,
            )
            assert includeData is not None
            assert type(includeData) is PgCfgModel__IncludeData
            assert includeData.m_Path == path
            assert includeData.m_File is fileData
            assert includeData.m_Parent == self.m_FileLineData

            try:
                # -----------
                include = PostgresConfigurationInclude_Base(
                    self,
                    includeData,
                )
                assert include.m_FileLine is self
                assert include.m_IncludeData is includeData
            except:  # rollback an include
                PgCfgModel__ModelUtils.Include__delete(
                    cfg.m_Data,
                    includeData,
                    False,
                )
                raise
        except:  # TODO: rollback a file
            raise

        return include

    # --------------------------------------------------------------------
    def Clear(self) -> None:
        self.Helper__CheckAlive()
        assert type(self.m_FileLineData) is PgCfgModel__FileLineData

        cfg = self.m_Parent.get_Configuration()
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert cfg.m_Data is not None
        assert type(cfg.m_Data) is PgCfgModel__ConfigurationData

        PgCfgModel__ModelUtils.FileLine__clear(
            cfg.m_Data,
            self.m_FileLineData,
        )
        return

    # Helper methods -----------------------------------------------------
    def Helper__CheckAlive(self) -> None:
        assert self.m_FileLineData is not None
        assert type(self.m_FileLineData) is PgCfgModel__FileLineData

        if not self.m_FileLineData.IsAlive():
            RaiseError.FileLineObjectWasDeleted()

        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)
        assert isinstance(self.m_Parent, PostgresConfigurationFile)
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLinesIterator_Base


class PostgresConfigurationFileLinesIterator_Base(
    PostgresConfigurationFileLinesIterator
):
    m_Cfg: PostgresConfiguration_Base
    m_FileLineDataIterator: typing.Iterator[PgCfgModel__FileLineData]

    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        fileLineDataIterator: typing.Iterator[PgCfgModel__FileLineData],
    ):
        assert cfg is not None
        assert fileLineDataIterator is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert isinstance(fileLineDataIterator, typing.Iterator)

        self.m_Cfg = cfg
        self.m_FileLineDataIterator = fileLineDataIterator

    # interface ----------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFileLinesIterator_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_FileLineDataIterator is not None
        assert isinstance(self.m_FileLineDataIterator, typing.Iterator)

        it = self.m_FileLineDataIterator.__iter__()
        assert it is not None
        assert isinstance(it, typing.Iterator)

        if it is self.m_FileLineDataIterator:
            return self

        return __class__(self.m_Cfg, it)

    # --------------------------------------------------------------------
    def __next__(self) -> PostgresConfigurationFileLine_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_FileLineDataIterator is not None
        assert isinstance(self.m_FileLineDataIterator, typing.Iterator)

        fileLineData = self.m_FileLineDataIterator.__next__()
        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData

        fileLine = PostgresConfigurationFactory_Base.GetObject(
            self.m_Cfg,
            fileLineData,
        )
        assert fileLine is not None
        assert isinstance(fileLine, PostgresConfigurationFileLine_Base)

        return fileLine


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLines_Base


class PostgresConfigurationFileLines_Base(PostgresConfigurationFileLines):
    m_Cfg: PostgresConfiguration_Base
    m_File: PostgresConfigurationFile_Base

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        file: PostgresConfigurationFile_Base,
    ):
        assert cfg is not None
        assert file is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert isinstance(file, PostgresConfigurationFile_Base)

        self.m_Cfg = cfg
        self.m_File = file
        return

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        assert self.m_File is not None
        assert isinstance(self.m_File, PostgresConfigurationFile_Base)

        fileData = self.m_File.Private__GetFileData()
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.m_Lines is not None
        assert type(fileData.m_Lines) is list

        return len(fileData.m_Lines)

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFileLinesIterator_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_File is not None
        assert isinstance(self.m_File, PostgresConfigurationFile_Base)

        fileData = self.m_File.Private__GetFileData()
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData
        assert fileData.m_Lines is not None
        assert type(fileData.m_Lines) is list

        fileLineDataIterator = fileData.m_Lines.__iter__()
        assert fileLineDataIterator is not None
        assert isinstance(fileLineDataIterator, typing.Iterator)

        return PostgresConfigurationFileLinesIterator_Base(
            self.m_Cfg,
            fileLineDataIterator,
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFile_Base


class PostgresConfigurationFile_Base(PostgresConfigurationFile):
    m_Cfg: PostgresConfiguration_Base
    m_FileData: PgCfgModel__FileData

    m_Lines: typing.Optional[PostgresConfigurationFileLines_Base]

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        fileData: PgCfgModel__FileData,
    ):
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) is PgCfgModel__FileData

        super().__init__()

        self.m_Cfg = cfg
        self.m_FileData = fileData
        self.m_Lines = None
        return

    # Object interface ---------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        self.Internal__CheckAlive()
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)
        return self.m_Cfg

    # File interface -----------------------------------------------------
    def __len__(self) -> int:
        self.Internal__CheckAlive()
        assert type(self.m_FileData) is PgCfgModel__FileData
        assert type(self.m_FileData.m_Lines) is list
        return len(self.m_FileData.m_Lines)

    # --------------------------------------------------------------------
    def get_Path(self) -> str:
        self.Internal__CheckAlive()
        assert type(self.m_FileData) is PgCfgModel__FileData
        assert type(self.m_FileData.m_Path) is str
        return self.m_FileData.m_Path

    # --------------------------------------------------------------------
    def get_Lines(self) -> PostgresConfigurationFileLines_Base:
        self.Internal__CheckAlive()

        if self.m_Lines is None:
            self.m_Lines = PostgresConfigurationFileLines_Base(
                self.m_Cfg,
                self,
            )

        assert self.m_Lines is not None
        assert type(self.m_Lines) is PostgresConfigurationFileLines_Base
        assert self.m_Lines.m_Cfg is self.m_Cfg
        assert self.m_FileData is self.m_FileData

        return self.m_Lines

    # interface ----------------------------------------------------------
    def AddEmptyLine(self) -> PostgresConfigurationFileLine_Base:
        self.Internal__CheckAlive()

        fileLineData = PgCfgModel__ModelUtils.File__add_Line(
            self.m_FileData,
        )

        assert fileLineData is not None
        assert type(fileLineData) is PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) is list
        assert len(fileLineData.m_Items) == 0

        assert self.m_FileData is not None
        assert type(self.m_FileData) is PgCfgModel__FileData
        assert self.m_FileData.m_Lines is not None
        assert type(self.m_FileData.m_Lines) is list
        assert len(self.m_FileData.m_Lines) > 0
        assert self.m_FileData.m_Lines[-1] is fileLineData

        try:
            fileLine = PostgresConfigurationFileLine_Base(
                self,
                fileLineData,
            )

            assert fileLine is not None
            assert type(fileLine) is PostgresConfigurationFileLine_Base
            assert fileLine.m_FileLineData is fileLineData
            assert fileLine.m_Parent is self
        except:  # rollback
            PgCfgModel__ModelUtils.FileLine__delete(
                self.m_Cfg.m_Data,
                fileLineData,
            )
            raise

        assert fileLine is not None
        assert type(fileLine) is PostgresConfigurationFileLine_Base
        return fileLine

    # --------------------------------------------------------------------
    def AddComment(
        self,
        text: str,
    ) -> PostgresConfigurationComment_Base:
        assert type(text) is str

        self.Internal__CheckAlive()

        DataVerificator.CheckCommentText(text)

        fileLineData = PgCfgModel__ModelUtils.File__add_Line(self.m_FileData)

        assert self.m_FileData is not None
        assert type(self.m_FileData) is PgCfgModel__FileData
        assert self.m_FileData.m_Lines is not None
        assert type(self.m_FileData.m_Lines) is list
        assert len(self.m_FileData.m_Lines) > 0
        assert self.m_FileData.m_Lines[-1] is fileLineData

        try:
            commentData = PgCfgModel__ModelUtils.FileLine__add_Comment(
                fileLineData,
                None,
                text,
            )
            assert commentData is not None
            assert type(commentData) is PgCfgModel__CommentData
            assert commentData.m_Parent is fileLineData
            assert type(commentData.m_Parent) is PgCfgModel__FileLineData
            assert type(commentData.m_Parent.m_Items) is list
            assert len(commentData.m_Parent.m_Items) == 1
            assert commentData.m_Parent.m_Items[0].m_Element is commentData

            # -----------------------
            fileLine = PostgresConfigurationFileLine_Base(
                self,
                fileLineData,
            )

            assert fileLine is not None
            assert type(fileLine) is PostgresConfigurationFileLine_Base
            assert fileLine.m_FileLineData is fileLineData
            assert fileLine.m_Parent is self

            fileLineComment = PostgresConfigurationComment_Base(
                fileLine,
                commentData,
            )

            assert fileLineComment is not None
            assert type(fileLineComment) is PostgresConfigurationComment_Base
        except:  # rollback
            PgCfgModel__ModelUtils.FileLine__delete(
                self.m_Cfg.m_Data,
                fileLineData,
            )
            raise

        assert fileLineComment
        assert type(fileLineComment) is PostgresConfigurationComment_Base
        return fileLineComment

    # --------------------------------------------------------------------
    def AddOption(
        self,
        name: str,
        value: typing.Any,
    ) -> PostgresConfigurationOption_Base:
        DataVerificator.CheckOptionName(name)

        assert name is not None
        assert name != ""

        if value is None:
            RaiseError.NoneValueIsNotSupported()

        assert value is not None

        self.Internal__CheckAlive()

        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)

        option = PostgresConfigurationController__Base.AddOption(
            self.m_Cfg,
            self.m_FileData,
            name,
            value,
            None,
        )

        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        return option

    # --------------------------------------------------------------------
    def AddInclude(
        self,
        path: str,
    ) -> PostgresConfigurationInclude_Base:
        DataVerificator.CheckStringOfFilePath(path)

        assert type(path) is str
        assert path != ""

        self.Internal__CheckAlive()

        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) is PgCfgModel__ConfigurationData

        # Add/Get file
        # Add empty line
        # Add include element

        baseFolder = self.m_Cfg.m_Data.OsOps.Path_DirName(self.m_FileData.m_Path)
        assert type(baseFolder) is str

        fileData = PgCfgModel__ModelUtils.Cfg__GetOrCreateFile__USER(
            self.m_Cfg.m_Data,
            baseFolder,
            path,
        )

        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData

        try:
            fileLineData = PgCfgModel__ModelUtils.File__add_Line(
                self.m_FileData,
            )

            assert self.m_FileData is not None
            assert type(self.m_FileData) is PgCfgModel__FileData
            assert self.m_FileData.m_Lines is not None
            assert type(self.m_FileData.m_Lines) is list
            assert len(self.m_FileData.m_Lines) > 0
            assert self.m_FileData.m_Lines[-1] is fileLineData

            try:
                includeData = PgCfgModel__ModelUtils.FileLine__add_Include(
                    fileLineData,
                    path,
                    fileData,
                    None,
                )
                assert includeData is not None
                assert type(includeData) is PgCfgModel__IncludeData
                assert includeData.m_Path == path
                assert includeData.m_File is fileData
                assert includeData.m_Parent == fileLineData

                # -----------
                fileLine = PostgresConfigurationFileLine_Base(
                    self,
                    fileLineData,
                )
                assert fileLine is not None
                assert type(fileLine) is PostgresConfigurationFileLine_Base
                assert fileLine.m_FileLineData is fileLineData
                assert fileLine.m_Parent is self

                # -----------
                include = PostgresConfigurationInclude_Base(
                    fileLine,
                    includeData,
                )
                assert include.m_FileLine is fileLine
                assert include.m_IncludeData is includeData
            except:  # rollback a line
                PgCfgModel__ModelUtils.FileLine__delete(
                    self.m_Cfg.m_Data,
                    fileLineData,
                )
                raise
        except:  # TODO: rollback a file
            raise

        return include

    # --------------------------------------------------------------------
    #
    # Method for inserting, updating and deleting of an option.
    #
    # It finds a suitable file or uses/creates default file (auto.conf).
    #
    # Set of None will delete an option from all files.
    #
    # Return:
    #  PostgresConfigurationSetOptionValueResult_Base.
    #
    def SetOptionValue(
        self,
        name: str,
        value: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        self.Internal__CheckAlive()

        DataVerificator.CheckOptionName(name)

        result = PostgresConfigurationController__Base.SetOptionValue(
            self.m_Cfg,
            self.m_FileData,  # target
            name,
            value,
            None,  # offset
        )

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        return result

    # --------------------------------------------------------------------
    #
    # Method for getting a value of option.
    #
    # Return:
    #  - Value of option.
    #  - None if option is not found in this file.
    #
    def GetOptionValue(
        self,
        name: str,
    ) -> typing.Any:
        self.Internal__CheckAlive()

        DataVerificator.CheckOptionName(name)

        r = PostgresConfigurationController__Base.GetOptionValue(
            self.m_Cfg,
            self.m_FileData,
            name,
        )

        return r

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        self,
        name: str,
        value_item: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        self.Internal__CheckAlive()

        DataVerificator.CheckOptionName(name)

        result = PostgresConfigurationController__Base.SetOptionValueItem(
            self.m_Cfg,
            self.m_FileData,  # target
            name,
            value_item,
        )

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        assert result.m_Cfg is self.m_Cfg
        assert result.m_OptData is not None
        assert type(result.m_OptData) is PgCfgModel__OptionData
        assert result.m_OptData.m_Name == name
        return result

    # PostgresConfigurationFile_Base private interface -------------------
    def Private__GetFileData(self) -> PgCfgModel__FileData:
        self.Internal__CheckAlive()
        return self.m_FileData

    # Internal interface -------------------------------------------------
    def Internal__CheckAlive(self) -> None:
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__CheckAlive",
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationTopLevelFile_Base


class PostgresConfigurationTopLevelFile_Base(PostgresConfigurationFile_Base):
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        fileData: PgCfgModel__FileData,
    ):
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) is PgCfgModel__FileData

        super().__init__(cfg, fileData)
        return

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> PostgresConfiguration_Base:
        self.Internal__CheckAlive()
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)
        return self.m_Cfg

    # Internal interface -------------------------------------------------
    def Internal__CheckAlive(self) -> None:
        assert self.m_FileData is not None
        assert type(self.m_FileData) is PgCfgModel__FileData

        if not self.m_FileData.IsAlive():
            RaiseError.FileObjectWasDeleted()

        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationIncludedFile_Base


class PostgresConfigurationIncludedFile_Base(PostgresConfigurationFile_Base):
    m_Include: PostgresConfigurationInclude_Base

    # --------------------------------------------------------------------
    def __init__(
        self,
        include: PostgresConfigurationInclude_Base,
        fileData: PgCfgModel__FileData,
    ):
        assert type(include) is PostgresConfigurationInclude_Base
        assert type(fileData) is PgCfgModel__FileData

        super().__init__(
            include.get_Configuration(),
            fileData,
        )

        self.m_Include = include

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationInclude_Base:
        self.Internal__CheckAlive()
        assert isinstance(self.m_Include, PostgresConfigurationInclude_Base)
        assert isinstance(self.m_Include, PostgresConfigurationInclude)
        return self.m_Include

    # Internal interface -------------------------------------------------
    def Internal__CheckAlive(self) -> None:
        assert self.m_FileData is not None
        assert self.m_Include is not None
        assert type(self.m_FileData) is PgCfgModel__FileData
        assert type(self.m_Include) is PostgresConfigurationInclude_Base

        if not self.m_FileData.IsAlive():
            RaiseError.FileObjectWasDeleted()

        self.m_Include.Private__CheckAlive()

        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationSetOptionValueResult_Base


class PostgresConfigurationSetOptionValueResult_Base(
    PostgresConfigurationSetOptionValueResult
):
    m_Cfg: typing.Optional[PostgresConfiguration_Base]
    m_Opt: typing.Optional[PostgresConfigurationOption_Base]
    m_OptData: typing.Optional[PgCfgModel__OptionData]
    m_EventID: PostgresConfigurationSetOptionValueEventID

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: typing.Optional[PostgresConfiguration_Base],
        optData: typing.Optional[PgCfgModel__OptionData],
        eventID: PostgresConfigurationSetOptionValueEventID,
    ):
        assert cfg is None or isinstance(cfg, PostgresConfiguration_Base)
        assert optData is None or type(optData) is PgCfgModel__OptionData
        assert (cfg is None) == (optData is None)
        assert type(eventID) is PostgresConfigurationSetOptionValueEventID

        self.m_Cfg = cfg
        self.m_Opt = None
        self.m_OptData = optData
        self.m_EventID = eventID
        return

    # ---------------------------------------------------------------------
    @staticmethod
    def Create__OptWasUpdated(
        cfg: PostgresConfiguration_Base,
        optData: PgCfgModel__OptionData,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) is PgCfgModel__OptionData

        return __class__(
            cfg,
            optData,
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_UPDATED,
        )

    # ---------------------------------------------------------------------
    @staticmethod
    def Create__OptWasAdded(
        cfg: PostgresConfiguration_Base, optData: PgCfgModel__OptionData
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) is PgCfgModel__OptionData

        return __class__(
            cfg,
            optData,
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
        )

    # ---------------------------------------------------------------------
    @staticmethod
    def Create__OptWasDeleted() -> PostgresConfigurationSetOptionValueResult_Base:
        return __class__(
            None,
            None,
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED,
        )

    # ---------------------------------------------------------------------
    @staticmethod
    def Create__OptValueItemWasAlreadyDefined(
        cfg: PostgresConfiguration_Base,
        optData: PgCfgModel__OptionData,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) is PgCfgModel__OptionData

        return __class__(
            cfg,
            optData,
            PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ALREADY_DEFINED,
        )

    # ---------------------------------------------------------------------
    @staticmethod
    def Create__OptValueItemWasAdded(
        cfg: PostgresConfiguration_Base,
        optData: PgCfgModel__OptionData,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) is PgCfgModel__OptionData

        return __class__(
            cfg,
            optData,
            PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ADDED,
        )

    # ---------------------------------------------------------------------
    @property
    def Option(self) -> typing.Optional[PostgresConfigurationOption_Base]:
        assert self.m_Cfg is None or isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_OptData is None or type(self.m_OptData) is PgCfgModel__OptionData
        assert (self.m_Cfg is None) is (self.m_OptData is None)
        assert type(self.m_EventID) is PostgresConfigurationSetOptionValueEventID

        if self.m_OptData is None:
            assert self.m_EventID in [
                PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED,
                PostgresConfigurationSetOptionValueEventID.NONE,
            ]

            assert self.m_Opt is None
            assert self.m_Cfg is None
            return None

        assert self.m_Cfg is not None

        assert self.m_EventID in [
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED,
            PostgresConfigurationSetOptionValueEventID.OPTION_WAS_UPDATED,
            PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ADDED,
            PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ALREADY_DEFINED,
        ]

        if self.m_Opt is None:
            x = PostgresConfigurationFactory_Base.GetObject(
                self.m_Cfg,
                self.m_OptData,
            )
            assert type(x) is PostgresConfigurationOption_Base
            self.m_Opt = x

        assert self.m_Opt is not None
        assert type(self.m_Opt) is PostgresConfigurationOption_Base
        return self.m_Opt

    # ---------------------------------------------------------------------
    @property
    def EventID(self) -> PostgresConfigurationSetOptionValueEventID:
        assert type(self.m_EventID) is PostgresConfigurationSetOptionValueEventID
        return self.m_EventID


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllFilesIterator


class PostgresConfiguration_Base__AllFilesIterator(PostgresConfigurationFilesIterator):
    T_FILE_DATA_ITERATOR = typing.Iterator[PgCfgModel__FileData]

    m_Cfg: PostgresConfiguration_Base
    m_FileDataIterator: T_FILE_DATA_ITERATOR

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        fileDataIterator: T_FILE_DATA_ITERATOR,
    ):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert fileDataIterator is not None
        assert isinstance(fileDataIterator, typing.Iterator)

        self.m_Cfg = cfg
        self.m_FileDataIterator = fileDataIterator
        return

    # interface ----------------------------------------------------------
    def __iter__(self) -> PostgresConfiguration_Base__AllFilesIterator:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_FileDataIterator is not None
        assert isinstance(self.m_FileDataIterator, typing.Iterator)

        it = self.m_FileDataIterator.__iter__()
        assert it is not None
        assert isinstance(it, typing.Iterator)

        if it is self.m_FileDataIterator:
            return self

        return __class__(self.m_Cfg, it)

    # --------------------------------------------------------------------
    def __next__(self) -> PostgresConfigurationFile_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_FileDataIterator is not None
        assert isinstance(self.m_FileDataIterator, typing.Iterator)

        fileData = self.m_FileDataIterator.__next__()
        assert fileData is not None
        assert type(fileData) is PgCfgModel__FileData

        file = PostgresConfigurationFactory_Base.GetObject(
            self.m_Cfg,
            fileData,
        )
        assert file is not None
        assert isinstance(file, PostgresConfigurationFile_Base)

        return file


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllFiles


class PostgresConfiguration_Base__AllFiles(PostgresConfigurationFiles):
    m_Cfg: PostgresConfiguration_Base

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
    ):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        self.m_Cfg = cfg
        return

    # PostgresConfigurationFiles interface -------------------------------
    def __len__(self) -> int:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllFilesByName) is PgCfgModel__MultiIndex
        return self.m_Cfg.m_Data.m_AllFilesByName.get_elements_count()

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfiguration_Base__AllFilesIterator:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllFilesByName) is PgCfgModel__MultiIndex

        fileDataIterator = self.m_Cfg.m_Data.m_AllFilesByName.elements().__iter__()
        assert fileDataIterator is not None
        assert isinstance(fileDataIterator, typing.Iterator)

        return PostgresConfiguration_Base__AllFilesIterator(
            self.m_Cfg,
            fileDataIterator,
        )

    # --------------------------------------------------------------------
    def GetFileByName(
        self,
        file_name: str,
    ) -> PostgresConfigurationFile_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllFilesByName) is PgCfgModel__MultiIndex

        file_name2 = self.m_Cfg.m_Data.OsOps.Path_NormCase(file_name)

        if file_name2 not in self.m_Cfg.m_Data.m_AllFilesByName.keys():
            RaiseError.UnknownFileName(file_name)

        indexData = self.m_Cfg.m_Data.m_AllFilesByName[file_name2]

        assert indexData is not None

        if type(indexData) is PgCfgModel__FileData:
            assert self.m_Cfg.m_Data.OsOps.Path_BaseName(indexData.m_Path) == file_name2
            file = PostgresConfigurationFactory_Base.GetObject(
                self.m_Cfg,
                indexData,
            )
            assert file is not None
            assert isinstance(file, PostgresConfigurationFile_Base)
            return file

        if type(indexData) is list:
            assert len(indexData) > 1
            RaiseError.MultipleDefOfFileIsFound(
                file_name,
                len(indexData),
            )

        BugCheckError.UnkFileObjectDataType(
            file_name,
            type(indexData),
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllOptionsIterator


class PostgresConfiguration_Base__AllOptionsIterator(
    PostgresConfigurationOptionsIterator
):
    T_OPTION_DATA_ITERATOR = typing.Iterator[PgCfgModel__OptionData]

    m_Cfg: PostgresConfiguration_Base
    m_OptionDataIterator: T_OPTION_DATA_ITERATOR

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        optionDataIterator: T_OPTION_DATA_ITERATOR,
    ):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert optionDataIterator is not None
        assert isinstance(optionDataIterator, typing.Iterator)

        self.m_Cfg = cfg
        self.m_OptionDataIterator = optionDataIterator
        return

    # interface ----------------------------------------------------------
    def __iter__(self) -> PostgresConfiguration_Base__AllOptionsIterator:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_OptionDataIterator is not None
        assert isinstance(self.m_OptionDataIterator, typing.Iterator)

        it = self.m_OptionDataIterator.__iter__()
        assert it is not None
        assert isinstance(it, typing.Iterator)

        if it is self.m_OptionDataIterator:
            return self

        return __class__(self.m_Cfg, it)

    # --------------------------------------------------------------------
    def __next__(self) -> PostgresConfigurationOption_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_OptionDataIterator is not None
        assert isinstance(self.m_OptionDataIterator, typing.Iterator)

        optionData = self.m_OptionDataIterator.__next__()
        assert optionData is not None
        assert type(optionData) is PgCfgModel__OptionData

        option = PostgresConfigurationFactory_Base.GetObject(
            self.m_Cfg,
            optionData,
        )
        assert option is not None
        assert isinstance(option, PostgresConfigurationOption_Base)

        return option


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllOptions


class PostgresConfiguration_Base__AllOptions(PostgresConfigurationOptions):
    m_Cfg: PostgresConfiguration_Base

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
    ):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        self.m_Cfg = cfg
        return

    # PostgresConfigurationOptions interface -----------------------------
    def __len__(self) -> int:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex
        return self.m_Cfg.m_Data.m_AllOptionsByName.get_elements_count()

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfiguration_Base__AllOptionsIterator:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) is PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        optionDataIterator = self.m_Cfg.m_Data.m_AllOptionsByName.elements().__iter__()
        assert optionDataIterator is not None
        assert isinstance(optionDataIterator, typing.Iterator)

        return PostgresConfiguration_Base__AllOptionsIterator(
            self.m_Cfg,
            optionDataIterator,
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base


class PostgresConfiguration_Base(PostgresConfiguration, PgCfgModel__DataHandler):
    @dataclasses.dataclass
    class tagDataHandlers:
        SetOptionValue__Simple: typing.Callable[
            [
                PostgresConfiguration_Base,
                typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
                str,
                typing.Any,
            ],
            typing.Any,
        ]
        GetOptionValue__Simple: typing.Callable[
            [
                PostgresConfiguration_Base,
                typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
                str,
            ],
            typing.Any,
        ]
        GetOptionValue__UnionList: typing.Callable[
            [
                PostgresConfiguration_Base,
                typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
                str,
            ],
            typing.Any,
        ]
        ResetOption: typing.Callable[
            [
                PostgresConfiguration_Base,
                typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
                str,
            ],
            typing.Any,
        ]
        AddSimpleOption: typing.Callable[
            [
                PostgresConfiguration_Base,
                typing.Union[None, PgCfgModel__FileData, PgCfgModel__FileLineData],
                typing.Optional[int],
                str,
                typing.Any,
            ],
            typing.Any,
        ]
        SetUniqueOptionValueItem: typing.Callable[
            [
                PostgresConfiguration_Base,
                typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
                str,
                typing.Any,
            ],
            typing.Any,
        ]

    # --------------------------------------------------------------------
    m_Data: PgCfgModel__ConfigurationData

    m_AllFiles: typing.Optional[PostgresConfiguration_Base__AllFiles]
    m_AllOptions: typing.Optional[PostgresConfiguration_Base__AllOptions]

    m_Handlers: tagDataHandlers

    # --------------------------------------------------------------------
    def __init__(
        self,
        data_dir: str,
        osOps: ConfigurationOsOps,
        handlers: tagDataHandlers,
    ):
        assert type(data_dir) is str
        assert isinstance(osOps, ConfigurationOsOps)
        assert type(handlers) is __class__.tagDataHandlers

        super(PostgresConfiguration, self).__init__()
        super(PgCfgModel__DataHandler, self).__init__()

        self.m_Data = PgCfgModel__ConfigurationData(data_dir, osOps)
        self.m_AllFiles = None
        self.m_AllOptions = None

        self.m_Handlers = handlers
        return

    # interface ----------------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        return self

    # --------------------------------------------------------------------
    def get_Parent(self) -> typing.Optional[PostgresConfigurationObject]:
        return None

    # PostgresConfiguration interface ------------------------------------
    def AddTopLevelFile(
        self,
        path: str,
    ) -> PostgresConfigurationTopLevelFile_Base:
        assert type(path) is str
        assert path != ""
        assert type(self.m_Data) is PgCfgModel__ConfigurationData
        assert isinstance(self.m_Data.OsOps, ConfigurationOsOps)
        assert self.m_Data.OsOps.Path_BaseName(path) != ""

        fileData = PgCfgModel__ModelUtils.Cfg__CreateAndAddTopLevelFile__USER(
            self.m_Data,
            path,
        )

        try:
            file = PostgresConfigurationFactory_Base.GetObject(
                self,
                fileData,
            )

            assert file is not None
            assert type(file) is PostgresConfigurationTopLevelFile_Base
        except:  # rollback
            raise

        assert file is not None
        assert type(file) is PostgresConfigurationTopLevelFile_Base
        return file

    # --------------------------------------------------------------------
    def AddOption(
        self,
        name: str,
        value: typing.Any,
    ) -> PostgresConfigurationOption_Base:
        DataVerificator.CheckOptionName(name)

        assert name is not None
        assert name != ""

        if value is None:
            RaiseError.NoneValueIsNotSupported()

        option = PostgresConfigurationController__Base.AddOption(
            self,
            None,
            name,
            value,
            None,
        )

        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        assert isinstance(option, PostgresConfigurationOption_Base)
        assert isinstance(option, PostgresConfigurationOption)
        return option

    # --------------------------------------------------------------------
    def SetOptionValue(
        self,
        name: str,
        value: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        DataVerificator.CheckOptionName(name)

        result = PostgresConfigurationController__Base.SetOptionValue(
            self,
            None,  # target
            name,
            value,
            None,  # offset
        )

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        return result

    # --------------------------------------------------------------------
    def GetOptionValue(
        self,
        name: str,
    ) -> typing.Any:
        DataVerificator.CheckOptionName(name)

        r = PostgresConfigurationController__Base.GetOptionValue(
            self,
            None,
            name,
        )

        return r

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        self,
        name: str,
        value_item: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        DataVerificator.CheckOptionName(name)

        result = PostgresConfigurationController__Base.SetOptionValueItem(
            self,
            None,  # target
            name,
            value_item,
        )

        assert result is not None
        assert type(result) is PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult_Base)

        return result

    # --------------------------------------------------------------------
    def get_AllFiles(self) -> PostgresConfiguration_Base__AllFiles:
        assert self.m_Data is not None
        assert type(self.m_Data) is PgCfgModel__ConfigurationData

        if self.m_AllFiles is None:
            self.m_AllFiles = PostgresConfiguration_Base__AllFiles(self)

        assert self.m_AllFiles is not None
        assert type(self.m_AllFiles) is PostgresConfiguration_Base__AllFiles
        assert self.m_AllFiles.m_Cfg is self
        return self.m_AllFiles

    # --------------------------------------------------------------------
    def get_AllOptions(self) -> PostgresConfiguration_Base__AllOptions:
        assert self.m_Data is not None
        assert type(self.m_Data) is PgCfgModel__ConfigurationData

        if self.m_AllOptions is None:
            self.m_AllOptions = PostgresConfiguration_Base__AllOptions(self)

        assert self.m_AllOptions is not None
        assert type(self.m_AllOptions) is PostgresConfiguration_Base__AllOptions
        assert self.m_AllOptions.m_Cfg is self
        return self.m_AllOptions

    # DataHandler interface ----------------------------------------------
    def DataHandler__SetOptionValue__Simple(
        self,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str
        assert optionValue is not None

        assert type(self.m_Handlers) is __class__.tagDataHandlers
        assert isinstance(self.m_Handlers.SetOptionValue__Simple, typing.Callable)

        return self.m_Handlers.SetOptionValue__Simple(
            self,
            targetData,
            optionName,
            optionValue,
        )

    # --------------------------------------------------------------------
    def DataHandler__GetOptionValue__Simple(
        self,
        sourceData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
    ) -> typing.Any:
        assert (
            sourceData is None
            or type(sourceData) is PgCfgModel__FileData
            or type(sourceData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        assert type(self.m_Handlers) is __class__.tagDataHandlers
        assert isinstance(self.m_Handlers.GetOptionValue__Simple, typing.Callable)

        return self.m_Handlers.GetOptionValue__Simple(
            self,
            sourceData,
            optionName,
        )

    # --------------------------------------------------------------------
    def DataHandler__GetOptionValue__UnionList(
        self,
        sourceData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
    ) -> typing.Any:
        assert (
            sourceData is None
            or type(sourceData) is PgCfgModel__FileData
            or type(sourceData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        assert type(self.m_Handlers) is __class__.tagDataHandlers
        assert isinstance(self.m_Handlers.GetOptionValue__UnionList, typing.Callable)

        return self.m_Handlers.GetOptionValue__UnionList(
            self,
            sourceData,
            optionName,
        )

    # --------------------------------------------------------------------
    def DataHandler__ResetOption(
        self,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        assert type(self.m_Handlers) is __class__.tagDataHandlers
        assert isinstance(self.m_Handlers.ResetOption, typing.Callable)

        return self.m_Handlers.ResetOption(
            self,
            targetData,
            optionName,
        )

    # --------------------------------------------------------------------
    def DataHandler__AddSimpleOption(
        self,
        target: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__FileLineData,
        ],
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: typing.Any,
    ) -> PostgresConfigurationOption_Base:
        assert (
            target is None
            or type(target) is PgCfgModel__FileData
            or type(target) is PgCfgModel__FileLineData
        )
        assert optionOffset is None or type(optionOffset) is int
        assert type(optionName) is str
        assert optionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) is PgCfgModel__ConfigurationData
        assert self.m_Data.m_AllOptionsByName is not None
        assert type(self.m_Data.m_AllOptionsByName) is PgCfgModel__MultiIndex

        assert type(self.m_Handlers) is __class__.tagDataHandlers
        assert isinstance(self.m_Handlers.AddSimpleOption, typing.Callable)

        return self.m_Handlers.AddSimpleOption(
            self,
            target,
            optionOffset,
            optionName,
            optionValue,
        )

    # --------------------------------------------------------------------
    def DataHandler__SetUniqueOptionValueItem(
        self,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
        optionValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str
        assert optionValueItem is not None

        assert type(self.m_Handlers) is __class__.tagDataHandlers
        assert isinstance(self.m_Handlers.SetUniqueOptionValueItem, typing.Callable)

        return self.m_Handlers.SetUniqueOptionValueItem(
            self,
            targetData,
            optionName,
            optionValueItem,
        )

    # Internal interface -------------------------------------------------
    def Internal__GetAutoConfFileName(self) -> str:
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetAutoConfFile",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToPrepareSetValue:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToPrepareSetValue",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValueItem(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToPrepareSetValueItem:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToPrepareSetValueItem",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareGetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToPrepareGetValue:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToPrepareGetValue",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToSetValue:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToSetValue",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToGetValue(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToGetValue:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToGetValue",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToAddOption(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToAddOption:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToAddOption",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValueItem(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToSetValueItem:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToSetValueItem",
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToWrite(
        self,
        name: str,
    ) -> PgCfgModel__OptionHandlerToWrite:
        assert type(name) is str
        RaiseError.MethodIsNotImplemented(
            __class__,
            "Internal__GetOptionHandlerToWrite",
        )

    # Debug methods ------------------------------------------------------
    def Debug__CheckOurObjectData(
        self,
        data: PgCfgModel__ObjectData,
    ) -> None:
        assert data is not None
        assert isinstance(data, PgCfgModel__ObjectData)

        stack: typing.Set[PgCfgModel__ObjectData] = set()
        assert type(stack) is set

        ptr = data
        while ptr is not self.m_Data:
            assert ptr is not None
            assert isinstance(ptr, PgCfgModel__ObjectData)
            assert ptr not in stack
            stack.add(ptr)
            ptr = ptr.get_Parent()
        return


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFactory_Base


class PostgresConfigurationFactory_Base:
    @staticmethod
    def GetObject(
        cfg: PostgresConfiguration_Base,
        objectData: PgCfgModel__ObjectData,
    ) -> PostgresConfigurationObject:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert objectData is not None
        assert isinstance(objectData, PgCfgModel__ObjectData)

        # Build stack
        stack: typing.List[PgCfgModel__ObjectData] = []

        while True:
            stack.append(objectData)

            objectData2 = objectData.get_Parent()

            if objectData2 is None:
                break

            assert isinstance(objectData2, PgCfgModel__ObjectData)
            objectData = objectData2
            continue

        assert type(stack) is list
        assert len(stack) > 0

        # Build ConfigurationObjects

        cfgObject: typing.Optional[PostgresConfigurationObject] = None

        while True:
            assert len(stack) > 0
            assert stack[-1] is not None
            assert isinstance(stack[-1], PgCfgModel__ObjectData)

            cfgObject = __class__.Helper__CreateObject(
                cfg,
                stack[-1],
                cfgObject,
            )
            assert cfgObject is not None
            assert isinstance(cfgObject, PostgresConfigurationObject)

            stack.pop()

            if len(stack) == 0:
                break

        return cfgObject

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CreateObject(
        cfg: PostgresConfiguration_Base,
        objectData: PgCfgModel__ObjectData,
        objectParent: typing.Optional[PostgresConfigurationObject],
    ) -> PostgresConfigurationObject:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert objectData is not None
        assert isinstance(objectData, PgCfgModel__ObjectData)
        assert objectParent is None or isinstance(
            objectParent,
            PostgresConfigurationObject,
        )

        if type(objectData) is PgCfgModel__ConfigurationData:
            assert objectData is cfg.m_Data
            return cfg

        if type(objectData) is PgCfgModel__FileData:
            assert objectParent is not None
            return __class__.Helper__CreateFile(
                objectData,
                objectParent,
            )

        if type(objectData) is PgCfgModel__FileLineData:
            assert objectParent is not None
            return __class__.Helper__CreateFileLine(
                objectData,
                objectParent,
            )

        if type(objectData) is PgCfgModel__OptionData:
            assert objectParent is not None
            return __class__.Helper__CreateOption(
                objectData,
                objectParent,
            )

        BugCheckError.UnkObjectDataType(
            type(objectData),
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CreateFile(
        objectData: PgCfgModel__FileData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationFile_Base:
        assert objectData is not None
        assert objectParent is not None
        assert type(objectData) is PgCfgModel__FileData
        assert isinstance(objectParent, PostgresConfigurationObject)

        if isinstance(objectParent, PostgresConfiguration_Base):
            return PostgresConfigurationTopLevelFile_Base(
                objectParent,
                objectData,
            )

        assert not isinstance(objectParent, PostgresConfiguration)

        RaiseError.MethodIsNotImplemented(
            __class__,
            "Helper__CreateFile",
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CreateFileLine(
        objectData: PgCfgModel__FileLineData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationFileLine_Base:
        assert objectData is not None
        assert objectParent is not None
        assert type(objectData) is PgCfgModel__FileLineData
        assert isinstance(objectParent, PostgresConfigurationFile_Base)

        return PostgresConfigurationFileLine_Base(
            objectParent,
            objectData,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__CreateOption(
        objectData: PgCfgModel__OptionData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationOption_Base:
        assert objectData is not None
        assert objectParent is not None
        assert type(objectData) is PgCfgModel__OptionData
        assert isinstance(objectParent, PostgresConfigurationFileLine_Base)

        return PostgresConfigurationOption_Base(
            objectParent,
            objectData,
        )


# //////////////////////////////////////////////////////////////////////////////
# PostgresConfigurationController__Base


class PostgresConfigurationController__Base:
    @staticmethod
    def AddOption(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__FileLineData,
        ],
        optionName: str,
        optionValue: typing.Any,
        optionOffset: typing.Optional[int],
    ) -> PostgresConfigurationOption_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__FileLineData
        )
        assert type(optionName) is str
        assert optionValue is not None
        assert optionOffset is None or type(optionOffset) is int

        # ----------------------
        preparedOptionValue = __class__.Helper__PrepareSetValue(
            cfg,
            optionName,
            optionValue,
        )

        assert preparedOptionValue is not None

        # ----------------------
        addHandler = cfg.Internal__GetOptionHandlerToAddOption(optionName)

        assert isinstance(addHandler, PgCfgModel__OptionHandlerToAddOption)

        ctx = PgCfgModel__OptionHandlerCtxToAddOption(
            cfg,
            targetData,
            optionOffset,
            optionName,
            preparedOptionValue,
        )

        option = addHandler.AddOption(ctx)
        assert option is not None
        assert type(option) is PostgresConfigurationOption_Base
        return option

    # --------------------------------------------------------------------
    @staticmethod
    def SetOptionValue(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
        optionValue: typing.Any,
        optionOffset: typing.Optional[int],
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str
        assert optionOffset is None or type(optionOffset) is int

        # ----------------------
        if optionValue is None:
            return cfg.DataHandler__ResetOption(
                targetData,
                optionName,
            )

        assert optionValue is not None

        # ----------------------
        preparedOptionValue = __class__.Helper__PrepareSetValue(
            cfg,
            optionName,
            optionValue,
        )

        assert preparedOptionValue is not None

        # ----------------------
        setHandler = cfg.Internal__GetOptionHandlerToSetValue(optionName)

        assert isinstance(setHandler, PgCfgModel__OptionHandlerToSetValue)

        ctx = PgCfgModel__OptionHandlerCtxToSetValue(
            cfg,
            targetData,
            optionName,
            preparedOptionValue,
        )

        r = setHandler.SetOptionValue(ctx)

        assert type(r) is PostgresConfigurationSetOptionValueResult_Base

        return r

    # --------------------------------------------------------------------
    @staticmethod
    def SetOptionValueItem(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
        optionValueItem: typing.Any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) is PgCfgModel__FileData
            or type(targetData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        # ---------------------------------------
        if optionValueItem is None:
            RaiseError.NoneValueIsNotSupported()

        assert optionValueItem is not None

        # ---------------------------------------
        optionValueItem_p = __class__.Helper__PrepareSetValueItem(
            cfg,
            optionName,
            optionValueItem,
        )

        assert optionValueItem_p is not None

        # ---------------------------------------
        setHandler = cfg.Internal__GetOptionHandlerToSetValueItem(optionName)

        assert isinstance(setHandler, PgCfgModel__OptionHandlerToSetValueItem)

        ctx = PgCfgModel__OptionHandlerCtxToSetValueItem(
            cfg,
            targetData,  # target
            optionName,
            optionValueItem_p,
        )

        r = setHandler.SetOptionValueItem(ctx)

        assert type(r) is PostgresConfigurationSetOptionValueResult_Base

        return r

    # --------------------------------------------------------------------
    @staticmethod
    def GetOptionValue(
        cfg: PostgresConfiguration_Base,
        sourceData: typing.Union[
            None,
            PgCfgModel__FileData,
            PgCfgModel__OptionData,
        ],
        optionName: str,
    ) -> typing.Any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            sourceData is None
            or type(sourceData) is PgCfgModel__FileData
            or type(sourceData) is PgCfgModel__OptionData
        )
        assert type(optionName) is str

        getHandler = cfg.Internal__GetOptionHandlerToGetValue(
            optionName,
        )
        assert isinstance(getHandler, PgCfgModel__OptionHandlerToGetValue)

        ctx = PgCfgModel__OptionHandlerCtxToGetValue(
            cfg,
            sourceData,
            optionName,
        )

        r = getHandler.GetOptionValue(ctx)
        return r

    # Helper methods -----------------------------------------------------
    @staticmethod
    def Helper__PrepareSetValue(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        optionValue: typing.Any,
    ) -> typing.Any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str
        assert optionValue is not None

        prepareHandler = cfg.Internal__GetOptionHandlerToPrepareSetValue(
            optionName,
        )
        assert prepareHandler is not None
        assert isinstance(prepareHandler, PgCfgModel__OptionHandlerToPrepareSetValue)

        prepareCtx = PgCfgModel__OptionHandlerCtxPrepareToSetValue(
            cfg,
            optionName,
            optionValue,
        )

        return prepareHandler.PrepareSetValue(prepareCtx)

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__PrepareSetValueItem(
        cfg: PostgresConfiguration_Base,
        optionName: str,
        optionValueItem: typing.Any,
    ) -> typing.Any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) is str
        assert optionValueItem is not None

        prepareHandler = cfg.Internal__GetOptionHandlerToPrepareSetValueItem(
            optionName,
        )
        assert prepareHandler is not None
        assert isinstance(
            prepareHandler,
            PgCfgModel__OptionHandlerToPrepareSetValueItem,
        )

        prepareCtx = PgCfgModel__OptionHandlerCtxPrepareToSetValueItem(
            cfg,
            optionName,
            optionValueItem,
        )

        return prepareHandler.PrepareSetValueItem(prepareCtx)


# //////////////////////////////////////////////////////////////////////////////
