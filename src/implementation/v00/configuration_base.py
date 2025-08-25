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
from ...core.model import FileLineElementData as PgCfgModel__FileLineElementData
from ...core.model import CommentData as PgCfgModel__CommentData
from ...core.model import OptionData as PgCfgModel__OptionData
from ...core.model import IncludeData as PgCfgModel__IncludeData
from ...core.model import FileLineData as PgCfgModel__FileLineData
from ...core.model import FileData as PgCfgModel__FileData
from ...core.model import FileStatus as PgCfgModel__FileStatus

from ...core.handlers import OptionHandlerToPrepareSetValue as PgCfgModel__OptionHandlerToPrepareSetValue
from ...core.handlers import OptionHandlerCtxToPrepareSetValue as PgCfgModel__OptionHandlerCtxPrepareToSetValue
from ...core.handlers import OptionHandlerToPrepareGetValue as PgCfgModel__OptionHandlerToPrepareGetValue
from ...core.handlers import OptionHandlerCtxToPrepareGetValue as PgCfgModel__OptionHandlerCtxPrepareToGetValue
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
from ...core.handlers import OptionHandlerCtxToWrite as PgCfgModel__OptionHandlerCtxToWrite
from ...core.handlers import ConfigurationDataHandler as PgCfgModel__DataHandler

from ...core.controller_utils import DataControllerUtils as PgCfgModel__DataControllerUtils
from ...core.data_verificator import DataVerificator
from ...core.helpers import Helpers
from ...core.write_utils import WriteUtils
from ...core.read_utils import ReadUtils
from ...core.read_utils import LineReader as ReadUtils__LineReader
from ...core.raise_error import RaiseError
from ...core.bugcheck_error import BugCheckError
# fmt: on

from ...os.abstract.configuration_os_ops import ConfigurationFileReader
from ...os.abstract.configuration_os_ops import ConfigurationOsFile
from ...os.abstract.configuration_os_ops import ConfigurationOsOps

import typing
import datetime

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
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(commentData) == PgCfgModel__CommentData

        assert commentData.m_Parent is fileLine.m_FileLineData

        super().__init__()

        self.m_FileLine = fileLine
        self.m_CommentData = commentData

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
        assert type(self.m_CommentData) == PgCfgModel__CommentData
        assert type(self.m_CommentData.m_Text) == str
        return self.m_CommentData.m_Text

    # --------------------------------------------------------------------
    def Delete(self, withLineIfLast: bool):
        assert type(withLineIfLast) == bool

        self.Helper__CheckAlive()
        assert type(self.m_CommentData) == PgCfgModel__CommentData
        assert type(self.m_CommentData.m_Parent) == PgCfgModel__FileLineData
        assert type(self.m_CommentData.m_Parent.m_Parent) == PgCfgModel__FileData
        assert (
            type(self.m_CommentData.m_Parent.m_Parent.m_Parent)
            == PgCfgModel__ConfigurationData
        )

        cfgData = self.m_CommentData.m_Parent.m_Parent.m_Parent
        assert type(cfgData) == PgCfgModel__ConfigurationData

        PgCfgModel__DataControllerUtils.Comment__delete(
            cfgData, self.m_CommentData, withLineIfLast
        )

    # Helper interface ---------------------------------------------------
    def Helper__CheckAlive(self):
        assert self.m_CommentData is not None
        assert type(self.m_CommentData) == PgCfgModel__CommentData

        if not self.m_CommentData.IsAlive():
            RaiseError.CommentObjectWasDeleted()

        assert type(self.m_FileLine) == PostgresConfigurationFileLine_Base
        assert isinstance(self.m_FileLine, PostgresConfigurationFileLine)


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
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(optionData) == PgCfgModel__OptionData

        super().__init__()

        self.m_FileLine = fileLine
        self.m_OptionData = optionData

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
    def get_Value(self) -> any:
        self.Helper__CheckAlive()

        configuration = self.m_FileLine.get_Configuration()

        assert configuration is not None
        assert isinstance(configuration, PostgresConfiguration_Base)
        assert isinstance(configuration, PgCfgModel__DataHandler)

        r = PostgresConfigurationController__Base.GetOptionValue(
            configuration, self.m_OptionData, self.m_OptionData.m_Name
        )

        return r

    # --------------------------------------------------------------------
    def set_Value(self, value: any) -> PostgresConfigurationSetOptionValueResult_Base:
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

        assert type(r) == PostgresConfigurationSetOptionValueResult_Base

        assert r.m_OptData is None or r.m_OptData is self.m_OptionData
        assert r.m_Opt is None

        if r.m_OptData is not None:
            r.m_Opt = self  # Optimization

        return r

    # --------------------------------------------------------------------
    def set_ValueItem(
        self, value_item: any
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

        assert type(r) == PostgresConfigurationSetOptionValueResult_Base

        assert r.m_OptData is not None
        assert r.m_OptData is self.m_OptionData
        assert r.m_Opt is None

        if r.m_OptData is not None:
            r.m_Opt = self  # Optimization

        return r

    # Helper methods -----------------------------------------------------
    def Helper__CheckAlive(self):
        assert self.m_OptionData is not None
        assert type(self.m_OptionData) == PgCfgModel__OptionData

        if not self.m_OptionData.IsAlive():
            RaiseError.OptionObjectWasDeleted()

        assert type(self.m_FileLine) == PostgresConfigurationFileLine_Base
        assert isinstance(self.m_FileLine, PostgresConfigurationFileLine)


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
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(includeData) == PgCfgModel__IncludeData

        super().__init__()

        self.m_FileLine = fileLine
        self.m_IncludeData = includeData

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

        return PostgresConfigurationIncludedFile_Base(self, self.m_IncludeData.m_File)

    # --------------------------------------------------------------------
    def Delete(self, withLine: bool):
        assert type(withLine) == bool

        self.Helper__CheckAlive()
        assert type(self.m_IncludeData) == PgCfgModel__IncludeData
        assert type(self.m_IncludeData.m_Parent) == PgCfgModel__FileLineData
        assert type(self.m_IncludeData.m_Parent.m_Parent) == PgCfgModel__FileData
        assert (
            type(self.m_IncludeData.m_Parent.m_Parent.m_Parent)
            == PgCfgModel__ConfigurationData
        )

        cfgData = self.m_IncludeData.m_Parent.m_Parent.m_Parent
        assert type(cfgData) == PgCfgModel__ConfigurationData

        PgCfgModel__DataControllerUtils.Include__delete(
            cfgData, self.m_IncludeData, withLine
        )

    # Private interface --------------------------------------------------
    def Private__CheckAlive(self):
        self.Helper__CheckAlive()

    # Helper methods -----------------------------------------------------
    def Helper__CheckAlive(self):
        assert self.m_IncludeData is not None
        assert type(self.m_IncludeData) == PgCfgModel__IncludeData

        if not self.m_IncludeData.IsAlive():
            RaiseError.IncludeObjectWasDeleted()

        assert type(self.m_FileLine) == PostgresConfigurationFileLine_Base
        assert isinstance(self.m_FileLine, PostgresConfigurationFileLine)


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
        assert type(fileLineData) == PgCfgModel__FileLineData

        super().__init__()

        self.m_Parent = parent
        self.m_FileLineData = fileLineData

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
        assert type(self.m_FileLineData) == PgCfgModel__FileLineData
        assert type(self.m_FileLineData.m_Items) == list
        return len(self.m_FileLineData.m_Items)

    # --------------------------------------------------------------------
    def AddComment(
        self, text: str, offset: typing.Optional[int] = None
    ) -> PostgresConfigurationComment_Base:
        assert type(text) == str
        assert offset is None or type(offset) == int

        self.Helper__CheckAlive()

        DataVerificator.CheckCommentText(text)

        commentData = PgCfgModel__DataControllerUtils.FileLine__add_Comment(
            self.m_FileLineData, offset, text
        )
        assert commentData is not None
        assert type(commentData) == PgCfgModel__CommentData
        assert commentData.m_Parent is self.m_FileLineData
        assert type(commentData.m_Parent) == PgCfgModel__FileLineData
        assert type(commentData.m_Parent.m_Items) == list
        assert len(commentData.m_Parent.m_Items) > 0
        assert commentData.m_Parent.m_Items[-1].m_Element is commentData

        try:
            fileLineComment = PostgresConfigurationComment_Base(self, commentData)

            assert fileLineComment is not None
            assert type(fileLineComment) == PostgresConfigurationComment_Base
        except:  # rollback
            cfg = self.m_Parent.get_Configuration()
            assert cfg is not None
            assert isinstance(cfg, PostgresConfiguration_Base)
            assert cfg.m_Data is not None
            assert type(cfg.m_Data) == PgCfgModel__ConfigurationData

            PgCfgModel__DataControllerUtils.Comment__delete(
                cfg.m_Data, commentData, False
            )
            raise

        assert fileLineComment
        assert type(fileLineComment) == PostgresConfigurationComment_Base
        return fileLineComment

    # --------------------------------------------------------------------
    def AddOption(
        self, name: str, value: any, offset: typing.Optional[int]
    ) -> PostgresConfigurationOption_Base:
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
            cfg, self.m_FileLineData, name, value, offset
        )

        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        return option

    # --------------------------------------------------------------------
    def AddInclude(
        self, path: str, offset: typing.Optional[int]
    ) -> PostgresConfigurationInclude_Base:
        DataVerificator.CheckStringOfFilePath(path)

        assert type(path) == str
        assert path != ""

        self.Helper__CheckAlive()

        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)

        cfg = self.m_Parent.m_Cfg
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData

        # Add/Get file
        # Add include element

        baseFolder = cfg.m_Data.OsOps.Path_DirName(self.m_FileLineData.m_Parent.m_Path)
        assert type(baseFolder) == str

        fileData = PgCfgModel__DataControllerUtils.Cfg__GetOrCreateFile__USER(
            cfg.m_Data, baseFolder, path
        )

        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData

        try:
            includeData = PgCfgModel__DataControllerUtils.FileLine__add_Include(
                self.m_FileLineData, path, fileData, offset
            )
            assert includeData is not None
            assert type(includeData) == PgCfgModel__IncludeData
            assert includeData.m_Path == path
            assert includeData.m_File is fileData
            assert includeData.m_Parent == self.m_FileLineData

            try:
                # -----------
                include = PostgresConfigurationInclude_Base(self, includeData)
                assert include.m_FileLine is self
                assert include.m_IncludeData is includeData
            except:  # rollback an include
                PgCfgModel__DataControllerUtils.Include__delete(
                    cfg.m_Data, includeData, False
                )
                raise
        except:  # TODO: rollback a file
            raise

        return include

    # --------------------------------------------------------------------
    def Clear(self) -> None:
        self.Helper__CheckAlive()
        assert type(self.m_FileLineData) == PgCfgModel__FileLineData

        cfg = self.m_Parent.get_Configuration()
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert cfg.m_Data is not None
        assert type(cfg.m_Data) == PgCfgModel__ConfigurationData

        PgCfgModel__DataControllerUtils.FileLine__clear(cfg.m_Data, self.m_FileLineData)

    # Helper methods -----------------------------------------------------
    def Helper__CheckAlive(self):
        assert self.m_FileLineData is not None
        assert type(self.m_FileLineData) == PgCfgModel__FileLineData

        if not self.m_FileLineData.IsAlive():
            RaiseError.FileLineObjectWasDeleted()

        assert isinstance(self.m_Parent, PostgresConfigurationFile_Base)
        assert isinstance(self.m_Parent, PostgresConfigurationFile)


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
        assert type(fileLineData) == PgCfgModel__FileLineData

        file = PostgresConfigurationFactory_Base.GetObject(self.m_Cfg, fileLineData)
        assert file is not None
        assert isinstance(file, PostgresConfigurationFileLine_Base)

        return file


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFileLines_Base


class PostgresConfigurationFileLines_Base(PostgresConfigurationFileLines):
    m_Cfg: PostgresConfiguration_Base
    m_File: PostgresConfigurationFile_Base

    # --------------------------------------------------------------------
    def __init__(
        self, cfg: PostgresConfiguration_Base, file: PostgresConfigurationFile_Base
    ):
        assert cfg is not None
        assert file is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert isinstance(file, PostgresConfigurationFile_Base)

        self.m_Cfg = cfg
        self.m_File = file

    # interface ----------------------------------------------------------
    def __len__(self) -> int:
        assert self.m_File is not None
        assert isinstance(self.m_File, PostgresConfigurationFile_Base)

        fileData = self.m_File.Private__GetFileData()
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert fileData.m_Lines is not None
        assert type(fileData.m_Lines) == list

        return len(fileData.m_Lines)

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfigurationFileLinesIterator_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_File is not None
        assert isinstance(self.m_File, PostgresConfigurationFile_Base)

        fileData = self.m_File.Private__GetFileData()
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert fileData.m_Lines is not None
        assert type(fileData.m_Lines) == list

        fileLineDataIterator = fileData.m_Lines.__iter__()
        assert fileLineDataIterator is not None
        assert isinstance(fileLineDataIterator, typing.Iterator)

        return PostgresConfigurationFileLinesIterator_Base(
            self.m_Cfg, fileLineDataIterator
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFile_Base


class PostgresConfigurationFile_Base(PostgresConfigurationFile):
    m_Cfg: PostgresConfiguration_Base
    m_FileData: PgCfgModel__FileData

    m_Lines: PostgresConfigurationFileLines_Base

    # --------------------------------------------------------------------
    def __init__(self, cfg: PostgresConfiguration_Base, fileData: PgCfgModel__FileData):
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) == PgCfgModel__FileData

        super().__init__()

        self.m_Cfg = cfg
        self.m_FileData = fileData
        self.m_Lines = None

    # Object interface ---------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        self.Internal__CheckAlive()
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)
        return self.m_Cfg

    # File interface -----------------------------------------------------
    def __len__(self) -> int:
        self.Internal__CheckAlive()
        assert type(self.m_FileData) == PgCfgModel__FileData
        assert type(self.m_FileData.m_Lines) == list
        return len(self.m_FileData.m_Lines)

    # --------------------------------------------------------------------
    def get_Path(self) -> str:
        self.Internal__CheckAlive()
        assert type(self.m_FileData) == PgCfgModel__FileData
        assert type(self.m_FileData.m_Path) == str
        return self.m_FileData.m_Path

    # --------------------------------------------------------------------
    def get_Lines(self) -> PostgresConfigurationFileLines_Base:
        self.Internal__CheckAlive()

        if self.m_Lines is None:
            self.m_Lines = PostgresConfigurationFileLines_Base(self.m_Cfg, self)

        assert self.m_Lines is not None
        assert type(self.m_Lines) == PostgresConfigurationFileLines_Base
        assert self.m_Lines.m_Cfg is self.m_Cfg
        assert self.m_FileData is self.m_FileData

        return self.m_Lines

    # interface ----------------------------------------------------------
    def AddEmptyLine(self) -> PostgresConfigurationFileLine_Base:
        self.Internal__CheckAlive()

        fileLineData = PgCfgModel__DataControllerUtils.File__add_Line(self.m_FileData)

        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert fileLineData.IsAlive()
        assert fileLineData.m_Items is not None
        assert type(fileLineData.m_Items) == list
        assert len(fileLineData.m_Items) == 0

        assert self.m_FileData is not None
        assert type(self.m_FileData) == PgCfgModel__FileData
        assert self.m_FileData.m_Lines is not None
        assert type(self.m_FileData.m_Lines) == list
        assert len(self.m_FileData.m_Lines) > 0
        assert self.m_FileData.m_Lines[-1] is fileLineData

        try:
            fileLine = PostgresConfigurationFileLine_Base(self, fileLineData)

            assert fileLine is not None
            assert type(fileLine) == PostgresConfigurationFileLine_Base
            assert fileLine.m_FileLineData is fileLineData
            assert fileLine.m_Parent is self
        except:  # rollback
            PgCfgModel__DataControllerUtils.FileLine__delete(
                self.m_Cfg.m_Data, fileLineData
            )
            raise

        assert fileLine is not None
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        return fileLine

    # --------------------------------------------------------------------
    def AddComment(self, text: str) -> PostgresConfigurationComment_Base:
        assert type(text) == str

        self.Internal__CheckAlive()

        DataVerificator.CheckCommentText(text)

        fileLineData = PgCfgModel__DataControllerUtils.File__add_Line(self.m_FileData)

        assert self.m_FileData is not None
        assert type(self.m_FileData) == PgCfgModel__FileData
        assert self.m_FileData.m_Lines is not None
        assert type(self.m_FileData.m_Lines) == list
        assert len(self.m_FileData.m_Lines) > 0
        assert self.m_FileData.m_Lines[-1] is fileLineData

        try:
            commentData = PgCfgModel__DataControllerUtils.FileLine__add_Comment(
                fileLineData, None, text
            )
            assert commentData is not None
            assert type(commentData) == PgCfgModel__CommentData
            assert commentData.m_Parent is fileLineData
            assert type(commentData.m_Parent) == PgCfgModel__FileLineData
            assert type(commentData.m_Parent.m_Items) == list
            assert len(commentData.m_Parent.m_Items) == 1
            assert commentData.m_Parent.m_Items[0].m_Element is commentData

            # -----------------------
            fileLine = PostgresConfigurationFileLine_Base(self, fileLineData)

            assert fileLine is not None
            assert type(fileLine) == PostgresConfigurationFileLine_Base
            assert fileLine.m_FileLineData is fileLineData
            assert fileLine.m_Parent is self

            fileLineComment = PostgresConfigurationComment_Base(fileLine, commentData)

            assert fileLineComment is not None
            assert type(fileLineComment) == PostgresConfigurationComment_Base
        except:  # rollback
            PgCfgModel__DataControllerUtils.FileLine__delete(
                self.m_Cfg.m_Data, fileLineData
            )
            raise

        assert fileLineComment
        assert type(fileLineComment) == PostgresConfigurationComment_Base
        return fileLineComment

    # --------------------------------------------------------------------
    def AddOption(self, name: str, value: any) -> PostgresConfigurationOption_Base:
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
            self.m_Cfg, self.m_FileData, name, value, None
        )

        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        return option

    # --------------------------------------------------------------------
    def AddInclude(self, path: str) -> PostgresConfigurationInclude_Base:
        DataVerificator.CheckStringOfFilePath(path)

        assert type(path) == str
        assert path != ""

        self.Internal__CheckAlive()

        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) == PgCfgModel__ConfigurationData

        # Add/Get file
        # Add empty line
        # Add include element

        baseFolder = self.m_Cfg.m_Data.OsOps.Path_DirName(self.m_FileData.m_Path)
        assert type(baseFolder) == str

        fileData = PgCfgModel__DataControllerUtils.Cfg__GetOrCreateFile__USER(
            self.m_Cfg.m_Data, baseFolder, path
        )

        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData

        try:
            fileLineData = PgCfgModel__DataControllerUtils.File__add_Line(
                self.m_FileData
            )

            assert self.m_FileData is not None
            assert type(self.m_FileData) == PgCfgModel__FileData
            assert self.m_FileData.m_Lines is not None
            assert type(self.m_FileData.m_Lines) == list
            assert len(self.m_FileData.m_Lines) > 0
            assert self.m_FileData.m_Lines[-1] is fileLineData

            try:
                includeData = PgCfgModel__DataControllerUtils.FileLine__add_Include(
                    fileLineData, path, fileData, None
                )
                assert includeData is not None
                assert type(includeData) == PgCfgModel__IncludeData
                assert includeData.m_Path == path
                assert includeData.m_File is fileData
                assert includeData.m_Parent == fileLineData

                # -----------
                fileLine = PostgresConfigurationFileLine_Base(self, fileLineData)
                assert fileLine is not None
                assert type(fileLine) == PostgresConfigurationFileLine_Base
                assert fileLine.m_FileLineData is fileLineData
                assert fileLine.m_Parent is self

                # -----------
                include = PostgresConfigurationInclude_Base(fileLine, includeData)
                assert include.m_FileLine is fileLine
                assert include.m_IncludeData is includeData
            except:  # rollback a line
                PgCfgModel__DataControllerUtils.FileLine__delete(
                    self.m_Cfg.m_Data, fileLineData
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
        self, name: str, value: any
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
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
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
    def GetOptionValue(self, name: str) -> any:
        self.Internal__CheckAlive()

        DataVerificator.CheckOptionName(name)

        r = PostgresConfigurationController__Base.GetOptionValue(
            self.m_Cfg, self.m_FileData, name
        )

        return r

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        self, name: str, value_item: any
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        self.Internal__CheckAlive()

        DataVerificator.CheckOptionName(name)

        result = PostgresConfigurationController__Base.SetOptionValueItem(
            self.m_Cfg, self.m_FileData, name, value_item  # target
        )

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        assert result.m_Cfg is self.m_Cfg
        assert result.m_OptData is not None
        assert type(result.m_OptData) == PgCfgModel__OptionData
        assert result.m_OptData.m_Name == name
        return result

    # PostgresConfigurationFile_Base private interface -------------------
    def Private__GetFileData(self) -> PgCfgModel__FileData:
        self.Internal__CheckAlive()
        return self.m_FileData

    # Internal interface -------------------------------------------------
    def Internal__CheckAlive(self):
        RaiseError.MethodIsNotImplemented(__class__, "Internal__CheckAlive")


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationTopLevelFile_Base


class PostgresConfigurationTopLevelFile_Base(PostgresConfigurationFile_Base):
    def __init__(self, cfg: PostgresConfiguration_Base, fileData: PgCfgModel__FileData):
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(fileData) == PgCfgModel__FileData

        super().__init__(cfg, fileData)

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> PostgresConfiguration_Base:
        self.Internal__CheckAlive()
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)
        return self.m_Cfg

    # Internal interface -------------------------------------------------
    def Internal__CheckAlive(self):
        assert self.m_FileData is not None
        assert type(self.m_FileData) == PgCfgModel__FileData

        if not self.m_FileData.IsAlive():
            RaiseError.FileObjectWasDeleted()

        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationIncludedFile_Base


class PostgresConfigurationIncludedFile_Base(PostgresConfigurationFile_Base):
    m_Include: PostgresConfigurationInclude_Base

    # --------------------------------------------------------------------
    def __init__(
        self, include: PostgresConfigurationInclude_Base, fileData: PgCfgModel__FileData
    ):
        assert type(include) == PostgresConfigurationInclude_Base
        assert type(fileData) == PgCfgModel__FileData

        super().__init__(include.get_Configuration(), fileData)

        self.m_Include = include

    # Object interface ---------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationInclude_Base:
        self.Internal__CheckAlive()
        assert isinstance(self.m_Include, PostgresConfigurationInclude_Base)
        assert isinstance(self.m_Include, PostgresConfigurationInclude)
        return self.m_Include

    # Internal interface -------------------------------------------------
    def Internal__CheckAlive(self):
        assert self.m_FileData is not None
        assert self.m_Include is not None
        assert type(self.m_FileData) == PgCfgModel__FileData
        assert type(self.m_Include) == PostgresConfigurationInclude_Base

        if not self.m_FileData.IsAlive():
            RaiseError.FileObjectWasDeleted()

        self.m_Include.Private__CheckAlive()

        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert isinstance(self.m_Cfg, PostgresConfiguration)


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationSetOptionValueResult_Base


class PostgresConfigurationSetOptionValueResult_Base(
    PostgresConfigurationSetOptionValueResult
):
    m_Cfg: PostgresConfiguration_Base
    m_Opt: PostgresConfigurationOption_Base
    m_OptData: PgCfgModel__OptionData
    m_EventID: PostgresConfigurationSetOptionValueEventID

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        optData: PgCfgModel__OptionData,
        eventID: PostgresConfigurationSetOptionValueEventID,
    ):
        assert cfg is None or isinstance(cfg, PostgresConfiguration_Base)
        assert optData is None or type(optData) == PgCfgModel__OptionData
        assert (cfg is None) == (optData is None)
        assert type(eventID) == PostgresConfigurationSetOptionValueEventID

        self.m_Cfg = cfg
        self.m_Opt = None
        self.m_OptData = optData
        self.m_EventID = eventID

    # ---------------------------------------------------------------------
    def Create__OptWasUpdated(
        cfg: PostgresConfiguration_Base, optData: PgCfgModel__OptionData
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) == PgCfgModel__OptionData

        return __class__(
            cfg, optData, PostgresConfigurationSetOptionValueEventID.OPTION_WAS_UPDATED
        )

    # ---------------------------------------------------------------------
    def Create__OptWasAdded(
        cfg: PostgresConfiguration_Base, optData: PgCfgModel__OptionData
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) == PgCfgModel__OptionData

        return __class__(
            cfg, optData, PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )

    # ---------------------------------------------------------------------
    def Create__OptWasDeleted() -> PostgresConfigurationSetOptionValueResult_Base:
        return __class__(
            None, None, PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED
        )

    # ---------------------------------------------------------------------
    def Create__OptValueItemWasAlreadyDefined(
        cfg: PostgresConfiguration_Base, optData: PgCfgModel__OptionData
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) == PgCfgModel__OptionData

        return __class__(
            cfg,
            optData,
            PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ALREADY_DEFINED,
        )

    # ---------------------------------------------------------------------
    def Create__OptValueItemWasAdded(
        cfg: PostgresConfiguration_Base, optData: PgCfgModel__OptionData
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optData) == PgCfgModel__OptionData

        return __class__(
            cfg,
            optData,
            PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ADDED,
        )

    # ---------------------------------------------------------------------
    @property
    def Option(self) -> PostgresConfigurationOption_Base:
        assert self.m_Cfg is None or isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_OptData is None or type(self.m_OptData) == PgCfgModel__OptionData
        assert (self.m_Cfg is None) == (self.m_OptData is None)
        assert type(self.m_EventID) == PostgresConfigurationSetOptionValueEventID

        if self.m_OptData is None:
            assert (
                self.m_EventID
                == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED
                or self.m_EventID == PostgresConfigurationSetOptionValueEventID.NONE
            )

            assert self.m_Opt is None
            return None

        assert (
            self.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
            or self.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_UPDATED
            or self.m_EventID
            == PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ADDED
            or self.m_EventID
            == PostgresConfigurationSetOptionValueEventID.VALUE_ITEM_WAS_ALREADY_DEFINED
        )

        if self.m_Opt is None:
            self.m_Opt = PostgresConfigurationFactory_Base.GetObject(
                self.m_Cfg, self.m_OptData
            )

        assert self.m_Opt is not None
        assert type(self.m_Opt) == PostgresConfigurationOption_Base
        return self.m_Opt

    # ---------------------------------------------------------------------
    @property
    def EventID(self) -> PostgresConfigurationSetOptionValueEventID:
        assert type(self.m_EventID) == PostgresConfigurationSetOptionValueEventID
        return self.m_EventID


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllFilesIterator


class PostgresConfiguration_Base__AllFilesIterator(PostgresConfigurationFilesIterator):
    m_Cfg: PostgresConfiguration_Base
    m_FileDataIterator: typing.Iterator[PgCfgModel__FileData]

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        fileDataIterator: typing.Iterator[PgCfgModel__FileData],
    ):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert fileDataIterator is not None
        assert isinstance(fileDataIterator, typing.Iterator)

        self.m_Cfg = cfg
        self.m_FileDataIterator = fileDataIterator

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
        assert type(fileData) == PgCfgModel__FileData

        file = PostgresConfigurationFactory_Base.GetObject(self.m_Cfg, fileData)
        assert file is not None
        assert isinstance(file, PostgresConfigurationFile_Base)

        return file


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllFiles


class PostgresConfiguration_Base__AllFiles(PostgresConfigurationFiles):
    m_Cfg: PostgresConfiguration_Base

    # --------------------------------------------------------------------
    def __init__(self, cfg: PostgresConfiguration_Base):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        self.m_Cfg = cfg

    # PostgresConfigurationFiles interface -------------------------------
    def __len__(self) -> int:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllFilesByName) == dict
        return len(self.m_Cfg.m_Data.m_AllFilesByName.values())

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfiguration_Base__AllFilesIterator:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllFilesByName) == dict

        fileDataIterator = self.m_Cfg.m_Data.m_AllFilesByName.values().__iter__()
        assert fileDataIterator is not None
        assert isinstance(fileDataIterator, typing.Iterator)

        return PostgresConfiguration_Base__AllFilesIterator(
            self.m_Cfg, fileDataIterator
        )

    # --------------------------------------------------------------------
    def GetFileByName(self, file_name: str) -> PostgresConfigurationFile_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllFilesByName) == dict

        file_name2 = self.m_Cfg.m_Data.OsOps.Path_NormCase(file_name)

        if not (file_name2 in self.m_Cfg.m_Data.m_AllFilesByName.keys()):
            RaiseError.UnknownFileName(file_name)

        indexData = self.m_Cfg.m_Data.m_AllFilesByName[file_name2]

        assert indexData is not None

        typeOfIndexData = type(indexData)

        if typeOfIndexData == PgCfgModel__FileData:
            assert self.m_Cfg.m_Data.OsOps.Path_BaseName(indexData.m_Path) == file_name2
            file = PostgresConfigurationFactory_Base.GetObject(self.m_Cfg, indexData)
            assert file is not None
            assert isinstance(file, PostgresConfigurationFile_Base)
            return file

        if typeOfIndexData == list:
            assert len(typeOfIndexData) > 1
            RaiseError.MultipleDefOfFileIsFound(file_name, len(indexData))

        BugCheckError.UnkFileObjectDataType(file_name, typeOfIndexData)


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllOptionsIterator


class PostgresConfiguration_Base__AllOptionsIterator(
    PostgresConfigurationOptionsIterator
):
    m_Cfg: PostgresConfiguration_Base
    m_OptionDataIterator: typing.Iterator[PgCfgModel__OptionData]

    # --------------------------------------------------------------------
    def __init__(
        self,
        cfg: PostgresConfiguration_Base,
        optionDataIterator: typing.Iterator[PgCfgModel__OptionData],
    ):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert optionDataIterator is not None
        assert isinstance(optionDataIterator, typing.Iterator)

        self.m_Cfg = cfg
        self.m_OptionDataIterator = optionDataIterator

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
    def __next__(self) -> PostgresConfigurationFile_Base:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert self.m_OptionDataIterator is not None
        assert isinstance(self.m_OptionDataIterator, typing.Iterator)

        optionData = self.m_OptionDataIterator.__next__()
        assert optionData is not None
        assert type(optionData) == PgCfgModel__OptionData

        option = PostgresConfigurationFactory_Base.GetObject(self.m_Cfg, optionData)
        assert option is not None
        assert isinstance(option, PostgresConfigurationOption_Base)

        return option


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base__AllOptions


class PostgresConfiguration_Base__AllOptions(PostgresConfigurationOptions):
    m_Cfg: PostgresConfiguration_Base

    # --------------------------------------------------------------------
    def __init__(self, cfg: PostgresConfiguration_Base):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        self.m_Cfg = cfg

    # PostgresConfigurationOptions interface -----------------------------
    def __len__(self) -> int:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllOptionsByName) == dict
        return len(self.m_Cfg.m_Data.m_AllOptionsByName.values())

    # --------------------------------------------------------------------
    def __iter__(self) -> PostgresConfiguration_Base__AllFilesIterator:
        assert self.m_Cfg is not None
        assert isinstance(self.m_Cfg, PostgresConfiguration_Base)
        assert type(self.m_Cfg.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Cfg.m_Data.m_AllOptionsByName) == dict

        optionDataIterator = self.m_Cfg.m_Data.m_AllOptionsByName.values().__iter__()
        assert optionDataIterator is not None
        assert isinstance(optionDataIterator, typing.Iterator)

        return PostgresConfiguration_Base__AllOptionsIterator(
            self.m_Cfg, optionDataIterator
        )


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfiguration_Base


class PostgresConfiguration_Base(PostgresConfiguration, PgCfgModel__DataHandler):
    m_Data: PgCfgModel__ConfigurationData

    m_AllFiles: PostgresConfiguration_Base__AllFiles
    m_AllOptions: PostgresConfiguration_Base__AllOptions

    # --------------------------------------------------------------------
    def __init__(self, data_dir: str, osOps: ConfigurationOsOps):
        assert type(data_dir) == str  # noqa: E721
        assert isinstance(osOps, ConfigurationOsOps)

        super(PostgresConfiguration, self).__init__()
        super(PgCfgModel__DataHandler, self).__init__()

        self.m_Data = PgCfgModel__ConfigurationData(data_dir, osOps)
        self.m_AllFiles = None
        self.m_AllOptions = None

    # interface ----------------------------------------------------------
    def get_Configuration(self) -> PostgresConfiguration_Base:
        return self

    # --------------------------------------------------------------------
    def get_Parent(self) -> PostgresConfigurationObject:
        return None

    # PostgresConfiguration interface ------------------------------------
    def AddTopLevelFile(self, path: str) -> PostgresConfigurationTopLevelFile_Base:
        assert type(path) == str
        assert path != ""
        assert type(self.m_Data) == PgCfgModel__ConfigurationData  # noqa: E721
        assert isinstance(self.m_Data.OsOps, ConfigurationOsOps)
        assert self.m_Data.OsOps.Path_BaseName(path) != ""

        fileData = PgCfgModel__DataControllerUtils.Cfg__CreateAndAddTopLevelFile__USER(
            self.m_Data, path
        )

        try:
            file = PostgresConfigurationFactory_Base.GetObject(self, fileData)

            assert file is not None
            assert type(file) == PostgresConfigurationTopLevelFile_Base
        except:  # rollback
            raise

        assert file is not None
        assert type(file) == PostgresConfigurationTopLevelFile_Base
        return file

    # --------------------------------------------------------------------
    def AddOption(self, name: str, value: any) -> PostgresConfigurationOption_Base:
        DataVerificator.CheckOptionName(name)

        assert name is not None
        assert name != ""

        if value is None:
            RaiseError.NoneValueIsNotSupported()

        option = PostgresConfigurationController__Base.AddOption(
            self, None, name, value, None
        )

        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        assert isinstance(option, PostgresConfigurationOption_Base)
        assert isinstance(option, PostgresConfigurationOption)
        return option

    # --------------------------------------------------------------------
    def SetOptionValue(
        self, name: str, value: any
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
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        return result

    # --------------------------------------------------------------------
    def GetOptionValue(self, name: str) -> any:
        DataVerificator.CheckOptionName(name)

        r = PostgresConfigurationController__Base.GetOptionValue(self, None, name)

        return r

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        self, name: str, value_item: any
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        DataVerificator.CheckOptionName(name)

        result = PostgresConfigurationController__Base.SetOptionValueItem(
            self, None, name, value_item  # target
        )

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult_Base)

        return result

    # --------------------------------------------------------------------
    def get_AllFiles(self) -> PostgresConfiguration_Base__AllFiles:
        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData

        if self.m_AllFiles is None:
            self.m_AllFiles = PostgresConfiguration_Base__AllFiles(self)

        assert self.m_AllFiles is not None
        assert type(self.m_AllFiles) == PostgresConfiguration_Base__AllFiles
        assert self.m_AllFiles.m_Cfg is self
        return self.m_AllFiles

    # --------------------------------------------------------------------
    def get_AllOptions(self) -> PostgresConfiguration_Base__AllOptions:
        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData

        if self.m_AllOptions is None:
            self.m_AllOptions = PostgresConfiguration_Base__AllOptions(self)

        assert self.m_AllOptions is not None
        assert type(self.m_AllOptions) == PostgresConfiguration_Base__AllOptions
        assert self.m_AllOptions.m_Cfg is self
        return self.m_AllOptions

    # DataHandler interface ----------------------------------------------
    def DataHandler__SetOptionValue__Simple(
        self,
        targetData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
        optionValue: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert (
            targetData is None
            or type(targetData) == PgCfgModel__FileData
            or type(targetData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str
        assert optionValue is not None

        # ------------------------------------------------
        if targetData is None:
            return self.Helper__SetSimpleOptionValue__Common(optionName, optionValue)

        # ------------------------------------------------
        assert targetData is not None

        typeOfTarget = type(targetData)

        if typeOfTarget == PgCfgModel__OptionData:
            return self.Helper__SetSimpleOptionValue__Exact(targetData, optionValue)

        if typeOfTarget == PgCfgModel__FileData:
            return self.Helper__SetSimpleOptionValue__File(
                targetData, optionName, optionValue
            )

        # ------------------------------------------------
        BugCheckError.UnkObjectDataType(typeOfTarget)

    # --------------------------------------------------------------------
    def DataHandler__GetOptionValue__Simple(
        self,
        sourceData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
    ) -> any:
        assert (
            sourceData is None
            or type(sourceData) == PgCfgModel__FileData
            or type(sourceData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str

        # -------------------------------------- ROOT
        if sourceData is None:
            optionData = self.Helper__FindSimpleOption(
                self.m_Data.m_AllOptionsByName, optionName
            )

            if optionData is not None:
                assert type(optionData) == PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                return self.Helper__PrepareGetValue(
                    optionData.m_Name, optionData.m_Value
                )

            return None

        typeOfSource = type(sourceData)

        # -------------------------------------- OPTION DATA
        if typeOfSource == PgCfgModel__OptionData:
            optionData: PgCfgModel__OptionData = sourceData

            assert optionData.IsAlive()
            assert optionData.m_Value is not None
            assert optionData.m_Name == optionName
            return self.Helper__PrepareGetValue(optionData.m_Name, optionData.m_Value)

        # -------------------------------------- FILE DATA
        if typeOfSource == PgCfgModel__FileData:
            fileData: PgCfgModel__FileData = sourceData

            assert fileData.IsAlive()
            assert fileData.m_OptionsByName is not None
            assert type(fileData.m_OptionsByName) == dict

            optionData = self.Helper__FindSimpleOption(
                fileData.m_OptionsByName, optionName
            )

            if optionData is not None:
                assert type(optionData) == PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                return self.Helper__PrepareGetValue(
                    optionData.m_Name, optionData.m_Value
                )

            return None

        BugCheckError.UnkObjectDataType(typeOfSource)

    # --------------------------------------------------------------------
    def DataHandler__GetOptionValue__UnionList(
        self,
        sourceData: typing.Union[
            None, PgCfgModel__FileLineData, PgCfgModel__OptionData
        ],
        optionName: str,
    ) -> any:
        assert (
            sourceData is None
            or type(sourceData) == PgCfgModel__FileData
            or type(sourceData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str

        # -------------------------------------- ROOT
        if sourceData is None:
            unionList = self.Helper__AggregateAllOptionValues(
                self.m_Data.m_AllOptionsByName, optionName
            )

            if unionList is None:
                return None

            assert type(unionList) == list
            return self.Helper__PrepareGetValue(optionName, unionList)

        typeOfSource = type(sourceData)

        # -------------------------------------- OPTION DATA
        if typeOfSource == PgCfgModel__OptionData:
            optionData: PgCfgModel__OptionData = sourceData

            assert optionData.IsAlive()
            assert optionData.m_Value is not None
            self.Debug__CheckOurObjectData(optionData)
            assert optionData.m_Name == optionName
            return self.Helper__PrepareGetValue(optionData.m_Name, optionData.m_Value)

        # -------------------------------------- FILE DATA
        if typeOfSource == PgCfgModel__FileData:
            sourceFileData: PgCfgModel__FileData = sourceData

            assert type(sourceFileData) == PgCfgModel__FileData
            assert sourceFileData.IsAlive()
            assert sourceFileData.m_OptionsByName is not None
            assert type(sourceFileData.m_OptionsByName) == dict

            typeOfOption = type(optionName)

            if typeOfOption == str:
                unionList = self.Helper__AggregateAllOptionValues(
                    sourceFileData.m_OptionsByName, optionName
                )

                if unionList is None:
                    return None

                assert type(unionList) == list
                return self.Helper__PrepareGetValue(optionName, unionList)

            BugCheckError.UnkObjectDataType(typeOfOption)

        BugCheckError.UnkObjectDataType(typeOfSource)

    # --------------------------------------------------------------------
    def DataHandler__ResetOption(
        self,
        targetData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert (
            targetData is None
            or type(targetData) == PgCfgModel__FileData
            or type(targetData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str

        # -------------------------------- target is NONE
        if targetData is None:
            eventID = self.Helper__FindAndDeleteOption(
                self.m_Data.m_AllOptionsByName, optionName
            )

            assert (
                eventID == PostgresConfigurationSetOptionValueEventID.NONE
                or PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED
            )

            return PostgresConfigurationSetOptionValueResult_Base(None, None, eventID)

        # -------------------------------- target is FileData or OptionData
        typeOfTarget = type(targetData)

        if typeOfTarget == PgCfgModel__OptionData:
            self.Debug__CheckOurObjectData(targetData)

            PgCfgModel__DataControllerUtils.Option__delete(
                self.m_Data, targetData, True
            )

            return (
                PostgresConfigurationSetOptionValueResult_Base.Create__OptWasDeleted()
            )

        if typeOfTarget is PgCfgModel__FileData:
            assert type(targetData) == PgCfgModel__FileData

            eventID = self.Helper__FindAndDeleteOption(
                targetData.m_OptionsByName, optionName
            )

            assert (
                eventID == PostgresConfigurationSetOptionValueEventID.NONE
                or PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED
            )

            return PostgresConfigurationSetOptionValueResult_Base(None, None, eventID)

        BugCheckError.UnkObjectDataType(typeOfTarget)

    # --------------------------------------------------------------------
    def DataHandler__AddSimpleOption(
        self,
        target: typing.Union[None, PgCfgModel__FileData, PgCfgModel__FileLineData],
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: any,
    ) -> PostgresConfigurationOption_Base:
        assert (
            target is None
            or type(target) == PgCfgModel__FileData
            or type(target) == PgCfgModel__FileLineData
        )
        assert optionOffset is None or type(optionOffset) == int
        assert type(optionName) == str
        assert optionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert self.m_Data.m_AllOptionsByName is not None
        assert type(self.m_Data.m_AllOptionsByName) == dict

        typeOfTarget = type(target)

        if typeOfTarget == PgCfgModel__FileLineData:
            return self.Helper__AddSimpleOption__FileLine(
                target, optionOffset, optionName, optionValue
            )

        assert optionOffset is None

        if typeOfTarget == PgCfgModel__FileData:
            return self.Helper__AddSimpleOption__File(target, optionName, optionValue)

        if target is None:
            return self.Helper__AddSimpleOption__Common(optionName, optionValue)

        BugCheckError.UnkObjectDataType(typeOfTarget)

    # --------------------------------------------------------------------
    def DataHandler__SetUniqueOptionValueItem(
        self,
        targetData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
        optionValueItem: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert (
            targetData is None
            or type(targetData) == PgCfgModel__FileData
            or type(targetData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str
        assert optionValueItem is not None

        # -------------------------------- target is NONE
        if targetData is None:
            return self.Helper__SetUniqueOptionValueItem__Common(
                optionName, optionValueItem
            )

        # --------------------------------
        typeOfTarget = type(targetData)

        # -------------------------------- target is OPTION DATA
        if typeOfTarget is PgCfgModel__OptionData:
            assert targetData.m_Name == optionName

            return self.Helper__SetUniqueOptionValueItem__Exact(
                targetData, optionValueItem
            )

        # -------------------------------- target is FILE DATA
        if typeOfTarget is PgCfgModel__FileData:
            return self.Helper__SetUniqueOptionValueItem__File(
                targetData, optionName, optionValueItem
            )

        BugCheckError.UnkObjectDataType(typeOfTarget)

    # Internal interface -------------------------------------------------
    def Internal__GetAutoConfFileName(self) -> str:
        RaiseError.MethodIsNotImplemented(__class__, "Internal__GetAutoConfFile")

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToPrepareSetValue:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToPrepareSetValue"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareSetValueItem(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToPrepareSetValueItem:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToPrepareSetValueItem"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToPrepareGetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToPrepareGetValue:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToPrepareGetValue"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToSetValue:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToSetValue"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToGetValue(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToGetValue:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToGetValue"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToAddOption(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToAddOption:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToAddOption"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToSetValueItem(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToSetValueItem:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToSetValueItem"
        )

    # --------------------------------------------------------------------
    def Internal__GetOptionHandlerToWrite(
        self, name: str
    ) -> PgCfgModel__OptionHandlerToWrite:
        assert type(name) == str
        RaiseError.MethodIsNotImplemented(
            __class__, "Internal__GetOptionHandlerToWrite"
        )

    # helper methods -----------------------------------------------------
    def Helper__FindSimpleOption(
        self, allOptionsByName: dict[str, PgCfgModel__OptionData], optionName: str
    ) -> typing.Optional[PgCfgModel__OptionData]:
        assert type(allOptionsByName) == dict
        assert type(optionName) == str

        if not (optionName in allOptionsByName.keys()):
            return None

        data = allOptionsByName[optionName]

        assert data is not None

        if type(data) == PgCfgModel__OptionData:
            assert data.IsAlive()
            assert data.m_Name == optionName
            self.Debug__CheckOurObjectData(data)
            return data

        if type(data) == list:
            assert len(data) > 1
            BugCheckError.MultipleDefOfOptionIsFound(optionName, len(data))

        BugCheckError.UnkOptObjectDataType(optionName, type(data))

    # --------------------------------------------------------------------
    def Helper__AggregateAllOptionValues(
        self, allOptionsByName: dict[str, PgCfgModel__OptionData], optionName: str
    ) -> list:
        assert type(allOptionsByName) == dict
        assert type(optionName) == str

        if not (optionName in allOptionsByName.keys()):
            return None

        data = allOptionsByName[optionName]
        assert data is not None

        typeOfData = type(data)

        if typeOfData == PgCfgModel__OptionData:
            assert data.IsAlive()
            assert data.m_Name == optionName
            assert data.m_Value is not None
            assert type(data.m_Value) == list
            return data.m_Value

        if typeOfData == list:
            assert type(data) == list
            data = data.copy()
            assert type(data) == list

            result = []

            for optionData in data:
                assert optionData is not None
                assert type(optionData) == PgCfgModel__OptionData
                assert optionData.m_Name == optionName
                assert optionData.IsAlive()
                assert optionData.m_Value is not None
                assert type(optionData.m_Value) == list

                result.extend(self.m_Data)

            assert result is not None
            assert type(result) == list

            return result

        # Unknown type of option data in dictionary

        assert type(optionName) == str
        BugCheckError.UnkOptObjectDataType(optionName, typeOfData)

    # --------------------------------------------------------------------
    def Helper__FindAndDeleteOption(
        self, allOptionsByName: dict[str, PgCfgModel__OptionData], optionName: str
    ) -> PostgresConfigurationSetOptionValueEventID:
        assert type(allOptionsByName) == dict
        assert type(optionName) == str

        if not (optionName in allOptionsByName.keys()):
            return PostgresConfigurationSetOptionValueEventID.NONE

        data = allOptionsByName[optionName]
        assert data is not None

        typeOfData = type(data)

        if typeOfData == PgCfgModel__OptionData:
            assert data.IsAlive()
            assert data.m_Name == optionName

            PgCfgModel__DataControllerUtils.Option__delete(self.m_Data, data, True)

            return PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED

        if typeOfData == list:
            assert type(data) == list
            data = data.copy()
            assert type(data) == list

            for optionData in data:
                assert optionData is not None
                assert type(optionData) == PgCfgModel__OptionData
                assert optionData.IsAlive()
                assert optionData.m_Name == optionName

                PgCfgModel__DataControllerUtils.Option__delete(
                    self.m_Data, optionData, True
                )

            # [2025-01-02] It is expected
            assert not (optionName in allOptionsByName.keys())

            return PostgresConfigurationSetOptionValueEventID.OPTION_WAS_DELETED

        # Unknown type of option data in dictionary

        assert type(optionName) == str
        BugCheckError.UnkOptObjectDataType(optionName, typeOfData)

    # --------------------------------------------------------------------
    # returns tuple[FileData, Bool_signal_about_creating_a_new_file]
    def Helper__GetFileForSimpleOption(
        self, option_name: str
    ) -> tuple[PgCfgModel__FileData, bool]:
        assert type(option_name) == str
        assert option_name != ""

        option_name_parts = option_name.split(".")

        assert type(option_name_parts) == list
        assert len(option_name_parts) > 0

        if len(option_name_parts) > 1:
            specFileName = "postgresql." + ".".join(option_name_parts[:-1]) + ".conf"
            assert type(specFileName) == str

            fileData = self.Helper__FindFile(specFileName)

            if fileData is not None:
                assert type(fileData) == PgCfgModel__FileData
                return (fileData, False)

        # Let's use standard "postgresql.auto.conf"

        fileData = self.Helper__FindFile(self.Internal__GetAutoConfFileName())

        if fileData is not None:
            assert type(fileData) == PgCfgModel__FileData
            return (fileData, False)

        assert fileData is None

        fileData = PgCfgModel__DataControllerUtils.Cfg__CreateAndAddTopLevelFile__AUTO(
            self.m_Data, self.Internal__GetAutoConfFileName()
        )

        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData

        return (fileData, True)

    # --------------------------------------------------------------------
    def Helper__FindFile(self, file_name: str) -> PgCfgModel__FileData:
        assert type(file_name) == str
        assert file_name != ""
        assert type(self.m_Data) == PgCfgModel__ConfigurationData  # noqa: E721
        assert isinstance(self.m_Data.OsOps, ConfigurationOsOps)
        assert self.m_Data.OsOps.Path_BaseName(file_name) == file_name

        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Data.m_AllFilesByName) == dict

        file_name_n = self.m_Data.OsOps.Path_NormCase(file_name)

        if not (file_name_n in self.m_Data.m_AllFilesByName.keys()):
            return None

        data = self.m_Data.m_AllFilesByName[file_name_n]

        assert data is not None

        if type(data) == PgCfgModel__FileData:
            return data

        if type(data) == list:
            assert len(data) > 1
            BugCheckError.MultipleDefOfFileIsFound(file_name_n, len(data))

        BugCheckError.UnkFileObjectDataType(file_name_n, type(data))

    # --------------------------------------------------------------------
    def Helper__PrepareGetValue(self, optionName: str, optionValue: any) -> any:
        assert optionName is not None
        assert optionValue is not None
        assert type(optionName) == str

        prepareHandler = self.Internal__GetOptionHandlerToPrepareGetValue(optionName)
        assert prepareHandler is not None
        assert isinstance(prepareHandler, PgCfgModel__OptionHandlerToPrepareGetValue)

        prepareCtx = PgCfgModel__OptionHandlerCtxPrepareToGetValue(
            self, optionName, optionValue
        )

        return prepareHandler.PrepareGetValue(prepareCtx)

    # --------------------------------------------------------------------
    def Helper__AddSimpleOption__Common(
        self,
        optionName: str,
        optionValue: any,
    ) -> PostgresConfigurationOption_Base:
        assert type(optionName) == str
        assert optionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert self.m_Data.m_AllOptionsByName is not None
        assert type(self.m_Data.m_AllOptionsByName) == dict

        if optionName in self.m_Data.m_AllOptionsByName.keys():
            assert self.m_Data.m_AllOptionsByName[optionName] is not None
            indexItem = self.m_Data.m_AllOptionsByName[optionName]
            optionData = Helpers.ExtractFirstOptionFromIndexItem(optionName, indexItem)

            assert optionData is not None
            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.get_Parent() is not None
            assert type(optionData.get_Parent()) == PgCfgModel__FileLineData

            anotherFileData = optionData.get_Parent().get_Parent()

            assert anotherFileData is not None
            assert type(anotherFileData) == PgCfgModel__FileData

            RaiseError.OptionIsAlreadyExistInFile(anotherFileData.m_Path, optionName)

        # OK. Let's add this option
        assert optionValue is not None

        # Let's select the file to append this new option
        getFileData_r = self.Helper__GetFileForSimpleOption(optionName)

        assert type(getFileData_r) == tuple
        assert len(getFileData_r) == 2

        assert type(getFileData_r[0]) == PgCfgModel__FileData
        assert type(getFileData_r[1]) == bool

        fileData = getFileData_r[0]
        assert type(fileData) == PgCfgModel__FileData

        try:
            # may raise
            optionData = PgCfgModel__DataControllerUtils.File__add_Option(
                self.m_Data, fileData, optionName, optionValue
            )

            assert optionData is not None
            assert type(optionData) == PgCfgModel__OptionData

            assert optionName in self.m_Data.m_AllOptionsByName.keys()
            assert optionName in fileData.m_OptionsByName.keys()

            try:
                # may raise
                option = PostgresConfigurationFactory_Base.GetObject(self, optionData)

                assert option is not None
                assert type(option) == PostgresConfigurationOption_Base
                assert option.m_OptionData is optionData
            except:  # rollback line with option
                assert optionData.IsAlive()

                PgCfgModel__DataControllerUtils.FileLine__delete(
                    self.m_Data, optionData.get_Parent()
                )

                assert not optionData.IsAlive()

                assert not (optionName in self.m_Data.m_AllOptionsByName.keys())
                assert not (optionName in fileData.m_OptionsByName.keys())
                raise
        except:  # rollback file
            assert type(getFileData_r) == tuple
            assert len(getFileData_r) == 2

            assert type(getFileData_r[0]) == PgCfgModel__FileData
            assert type(getFileData_r[1]) == bool

            if getFileData_r[1]:
                pass  # TODO: delete file

            raise

        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        assert option.m_OptionData is optionData
        assert option.m_OptionData.IsAlive()
        return option

    # --------------------------------------------------------------------
    def Helper__AddSimpleOption__FileLine(
        self,
        fileLineData: PgCfgModel__FileLineData,
        optionOffset: typing.Optional[int],
        optionName: str,
        optionValue: any,
    ):
        assert fileLineData is not None
        assert type(fileLineData) == PgCfgModel__FileLineData
        assert optionOffset is None or type(optionOffset) == int
        assert type(optionName) == str
        assert optionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert self.m_Data.m_AllOptionsByName is not None
        assert type(self.m_Data.m_AllOptionsByName) == dict

        fileData = fileLineData.m_Parent
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData

        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) == dict

        if optionName in fileData.m_OptionsByName.keys():
            assert fileData.m_OptionsByName[optionName] is not None
            RaiseError.OptionIsAlreadyExistInThisFile(fileData.m_Path, optionName)

        if optionName in self.m_Data.m_AllOptionsByName.keys():
            assert self.m_Data.m_AllOptionsByName[optionName] is not None
            indexItem = self.m_Data.m_AllOptionsByName[optionName]
            optionData = Helpers.ExtractFirstOptionFromIndexItem(optionName, indexItem)

            assert optionData is not None
            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert optionData.get_Parent() is not None
            assert type(optionData.get_Parent()) == PgCfgModel__FileLineData

            anotherFileData = optionData.get_Parent().get_Parent()

            assert anotherFileData is not None
            assert type(anotherFileData) == PgCfgModel__FileData
            assert anotherFileData is not fileData

            RaiseError.OptionIsAlreadyExistInAnotherFile(
                anotherFileData.m_Path, optionName
            )

        assert not (optionName in fileData.m_OptionsByName.keys())
        assert not (optionName in self.m_Data.m_AllOptionsByName.keys())

        # OK. Let's add this option
        assert optionValue is not None

        optionData = PgCfgModel__DataControllerUtils.FileLine__add_Option(
            self.m_Data, fileLineData, optionName, optionValue, optionOffset
        )

        assert optionData is not None
        assert type(optionData) == PgCfgModel__OptionData

        assert optionName in fileData.m_OptionsByName.keys()
        assert optionName in self.m_Data.m_AllOptionsByName.keys()

        try:
            option = PostgresConfigurationFactory_Base.GetObject(self, optionData)

            assert option is not None
            assert type(option) == PostgresConfigurationOption_Base
            assert option.m_OptionData is optionData
        except:
            PgCfgModel__DataControllerUtils.Option__delete(self.m_Data, optionData())

            assert not optionData.IsAlive()
            assert not (optionName in fileData.m_OptionsByName.keys())
            assert not (optionName in self.m_Data.m_AllOptionsByName.keys())
            raise

        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        assert option.m_OptionData is optionData
        assert option.m_OptionData.IsAlive()
        return option

    # --------------------------------------------------------------------
    def Helper__AddSimpleOption__File(
        self,
        fileData: PgCfgModel__FileData,
        optionName: str,
        optionValue: any,
    ):
        assert fileData is not None
        assert type(fileData) == PgCfgModel__FileData
        assert type(optionName) == str
        assert optionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert self.m_Data.m_AllOptionsByName is not None
        assert type(self.m_Data.m_AllOptionsByName) == dict

        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) == dict

        if optionName in fileData.m_OptionsByName.keys():
            assert fileData.m_OptionsByName[optionName] is not None
            RaiseError.OptionIsAlreadyExistInThisFile(fileData.m_Path, optionName)

        if optionName in self.m_Data.m_AllOptionsByName.keys():
            assert self.m_Data.m_AllOptionsByName[optionName] is not None
            indexItem = self.m_Data.m_AllOptionsByName[optionName]
            optionData = Helpers.ExtractFirstOptionFromIndexItem(optionName, indexItem)

            assert optionData is not None
            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert optionData.get_Parent() is not None
            assert type(optionData.get_Parent()) == PgCfgModel__FileLineData

            anotherFileData = optionData.get_Parent().get_Parent()

            assert anotherFileData is not None
            assert type(anotherFileData) == PgCfgModel__FileData
            assert anotherFileData is not fileData

            RaiseError.OptionIsAlreadyExistInAnotherFile(
                anotherFileData.m_Path, optionName
            )

        assert not (optionName in fileData.m_OptionsByName.keys())
        assert not (optionName in self.m_Data.m_AllOptionsByName.keys())

        # OK. Let's add this option
        assert optionValue is not None

        optionData = PgCfgModel__DataControllerUtils.File__add_Option(
            self.m_Data, fileData, optionName, optionValue
        )

        assert optionData is not None
        assert type(optionData) == PgCfgModel__OptionData

        assert optionName in fileData.m_OptionsByName.keys()
        assert optionName in self.m_Data.m_AllOptionsByName.keys()

        try:
            option = PostgresConfigurationFactory_Base.GetObject(self, optionData)

            assert option is not None
            assert type(option) == PostgresConfigurationOption_Base
            assert option.m_OptionData is optionData
        except:
            PgCfgModel__DataControllerUtils.FileLine__delete(
                self.m_Data, optionData.get_Parent()
            )

            assert not optionData.IsAlive()
            assert not (optionName in fileData.m_OptionsByName.keys())
            assert not (optionName in self.m_Data.m_AllOptionsByName.keys())
            raise

        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        assert option.m_OptionData is optionData
        assert option.m_OptionData.IsAlive()
        return option

    # --------------------------------------------------------------------
    def Helper__SetSimpleOptionValue__Common(
        self,
        optionName: str,
        optionValue: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(optionName) == str
        assert optionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Data.m_AllOptionsByName) == dict

        # ------------------------------------------------
        optionData = self.Helper__FindSimpleOption(
            self.m_Data.m_AllOptionsByName, optionName
        )

        if optionData is not None:
            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName

            PgCfgModel__DataControllerUtils.Option__set_Value(optionData, optionValue)

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
                self, optionData
            )

        assert optionData is None

        result = self.Helper__FinalRegSimpleOptionValue__Common(optionName, optionValue)

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        assert (
            result.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )
        assert result.m_OptData is not None
        assert type(result.m_OptData) == PgCfgModel__OptionData
        assert result.m_Cfg is self

        return result

    # --------------------------------------------------------------------
    def Helper__SetSimpleOptionValue__File(
        self,
        fileData: PgCfgModel__FileData,
        optionName: str,
        optionValue: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(fileData) == PgCfgModel__FileData
        assert type(fileData.m_OptionsByName) == dict
        assert type(optionName) == str
        assert optionValue is not None

        # ------------------------------------------------
        optionData = self.Helper__FindSimpleOption(fileData.m_OptionsByName, optionName)

        if optionData is not None:
            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName

            PgCfgModel__DataControllerUtils.Option__set_Value(optionData, optionValue)

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
                self, optionData
            )

        assert optionData is None

        # Let's append this new option
        if optionName in self.m_Data.m_AllOptionsByName.keys():
            optionData = Helpers.ExtractFirstOptionFromIndexItem(
                optionName, self.m_Data.m_AllOptionsByName[optionName]
            )

            assert optionData is not None
            assert type(optionData) == PgCfgModel__OptionData
            assert optionData.IsAlive()
            assert optionData.m_Name == optionName
            assert type(optionData.m_Parent) == PgCfgModel__FileLineData
            assert optionData.m_Parent.IsAlive()
            assert type(optionData.m_Parent.m_Parent) == PgCfgModel__FileData
            assert optionData.m_Parent.m_Parent.IsAlive()

            RaiseError.OptionIsAlreadyExistInAnotherFile(
                optionData.m_Parent.m_Parent.m_Path, optionName
            )

        result = self.Helper__FinalRegSimpleOptionValue__File(
            fileData, optionName, optionValue
        )

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert (
            result.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )
        assert result.m_OptData is not None
        assert type(result.m_OptData) == PgCfgModel__OptionData
        assert result.m_OptData.IsAlive()
        assert result.m_OptData.m_Name == optionName
        return result

    # --------------------------------------------------------------------
    def Helper__SetSimpleOptionValue__Exact(
        self,
        optionData: PgCfgModel__OptionData,
        optionValue: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(optionData) == PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionValue is not None

        # ------------------------------------------------
        self.Debug__CheckOurObjectData(optionData)

        # ------------------------------------------------
        PgCfgModel__DataControllerUtils.Option__set_Value(optionData, optionValue)

        return PostgresConfigurationSetOptionValueResult_Base.Create__OptWasUpdated(
            self, optionData
        )

    # --------------------------------------------------------------------
    def Helper__SetUniqueOptionValueItem__Common(
        self,
        optionName: str,
        optionValueItem: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(optionName) == str
        assert optionValueItem is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Data.m_AllOptionsByName) == dict

        # ------------------------------------------------
        while True:
            if not (optionName in self.m_Data.m_AllOptionsByName.keys()):
                break

            data = self.m_Data.m_AllOptionsByName[optionName]

            typeOfData = type(data)

            if typeOfData == PgCfgModel__OptionData:
                assert type(data) == PgCfgModel__OptionData
                assert data.m_Name == optionName
                assert data.m_Value is not None
                assert type(data.m_Value) == list

                if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                    data, optionValueItem
                ):
                    return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                        self, data
                    )

                PgCfgModel__DataControllerUtils.Option__add_ValueItem(
                    data, optionValueItem
                )

                return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAdded(
                    self, data
                )

            if typeOfData == list:
                assert type(data) == list
                assert len(data) > 1

                for optionData in data:
                    assert optionData is not None
                    assert type(optionData) == PgCfgModel__OptionData
                    assert optionData.m_Name == optionName
                    assert optionData.m_Value is not None
                    assert type(optionData.m_Value) == list

                    if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                        optionData, optionValueItem
                    ):
                        return PostgresConfigurationSetOptionValueResult_Base.Create__OptWithThisValueItemAlreadyExist(
                            self, optionData
                        )

                # [2025-01-07] Postgres does not able to join multiple list
                # TODO: We have to take into account overriding the values of postgresql.conf
                BugCheckError.MultipleDefOfOptionIsFound(optionName, len(data))

            BugCheckError.UnkOptObjectDataType(optionName, typeOfData)

        # ------------------------------------------------
        assert not (optionName in self.m_Data.m_AllOptionsByName.keys())

        # OK. Let's add a new option with list that contains our optionValueItem

        result = self.Helper__FinalRegSimpleOptionValue__Common(
            optionName, [optionValueItem]
        )

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert isinstance(result, PostgresConfigurationSetOptionValueResult)
        assert (
            result.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )
        assert result.m_OptData is not None
        assert type(result.m_OptData) == PgCfgModel__OptionData
        assert result.m_OptData.m_Name == optionName
        assert result.m_Cfg is self

        return result

    # --------------------------------------------------------------------
    def Helper__SetUniqueOptionValueItem__Exact(
        self,
        optionData: PgCfgModel__OptionData,
        optionValueItem: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(optionData) == PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionValueItem is not None

        return self.Helper__SetUniqueOptionPreparedValueItem__Exact(
            optionData, optionValueItem
        )

    # --------------------------------------------------------------------
    def Helper__SetUniqueOptionPreparedValueItem__Exact(
        self,
        optionData: PgCfgModel__OptionData,
        optionPreparedValueItem: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(optionData) == PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionData.m_Value is not None
        assert type(optionData.m_Value) == list
        assert optionPreparedValueItem is not None

        # ------------------------------------------------
        if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
            optionData, optionPreparedValueItem
        ):
            return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                self, optionData
            )

        # ------------------------------------------------
        self.Debug__CheckOurObjectData(optionData)

        assert optionData.m_Name in self.m_Data.m_AllOptionsByName.keys()

        data = self.m_Data.m_AllOptionsByName[optionData.m_Name]

        typeOfData = type(data)

        if typeOfData == PgCfgModel__OptionData:
            assert type(data) == PgCfgModel__OptionData
            # It is the single property!
            assert data is optionData
            assert type(data.m_Value) == list

            PgCfgModel__DataControllerUtils.Option__add_ValueItem(
                data, optionPreparedValueItem
            )

            return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAdded(
                self, data
            )

        if typeOfData == list:
            assert type(data) == list
            assert len(data) > 1

            for optionData2 in data:
                if optionData2 is optionData:
                    continue

                assert optionData2 is not None
                assert type(optionData2) == PgCfgModel__OptionData
                assert optionData2.IsAlive()
                assert optionData2.m_Name == optionData.m_Name
                assert optionData2.m_Value is not None
                assert type(optionData2.m_Value) == list
                assert optionData2.m_Parent.IsAlive()

                fileData2 = optionData2.m_Parent.m_Parent
                assert type(fileData2) == PgCfgModel__FileData
                assert fileData2.IsAlive()

                if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                    optionData2.m_Value, optionPreparedValueItem
                ):
                    RaiseError.OptionValueItemIsAlreadyDefined(
                        fileData2.m_Path, optionData2.m_Name, optionPreparedValueItem
                    )

            # [2025-01-07] Postgres does not able to join multiple list
            # TODO: We have to take into account overriding the values of postgresql.conf
            BugCheckError.MultipleDefOfOptionIsFound(optionData.m_Name, len(data))

        assert typeOfData != PgCfgModel__OptionData
        assert typeOfData != list

        BugCheckError.UnkOptObjectDataType(optionData.m_Name, typeOfData)

    # --------------------------------------------------------------------
    def Helper__SetUniqueOptionValueItem__File(
        self,
        fileData: PgCfgModel__FileData,
        optionName: str,
        optionValueItem: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(fileData) == PgCfgModel__FileData
        assert type(optionName) == str
        assert fileData.IsAlive()
        assert optionValueItem is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Data.m_AllOptionsByName) == dict

        assert fileData.m_OptionsByName is not None
        assert type(fileData.m_OptionsByName) == dict

        # ------------------------------------------------
        C_BUGCHECK_SRC = __class__.__name__ + "::Helper__SetUniqueOptionValueItem__File"

        # ------------------------------------------------
        while True:
            if not (optionName in self.m_Data.m_AllOptionsByName.keys()):
                # It is an absolutely new option
                assert not (optionName in fileData.m_OptionsByName.keys())
                break

            if optionName in fileData.m_OptionsByName.keys():
                data = fileData.m_OptionsByName[optionName]
                assert data is not None

                typeOfData = type(data)

                if typeOfData == PgCfgModel__OptionData:
                    assert data.IsAlive()
                    assert data.m_Name == optionName
                    assert data.m_Value is not None
                    assert type(data.m_Value) == list

                    if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                        data, optionValueItem
                    ):
                        return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                            self, data
                        )

                    # this option value does not have this item

                    return self.Helper__SetUniqueOptionPreparedValueItem__Exact(
                        data, optionValueItem
                    )

                assert typeOfData != PgCfgModel__OptionData

                if typeOfData == list:
                    assert type(data) == list
                    assert len(data) > 1

                    for optionData in data:
                        assert optionData is not None
                        assert type(optionData) == PgCfgModel__OptionData
                        assert optionData.IsAlive()
                        assert optionData.m_Name == optionName
                        assert optionData.m_Value is not None
                        assert type(optionData.m_Value) == list

                        if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                            optionData, optionValueItem
                        ):
                            return PostgresConfigurationSetOptionValueResult_Base.Create__OptValueItemWasAlreadyDefined(
                                self, optionData
                            )

                    # Our optionValueItem is not found
                    # Postgres does not support a concatention of option lists
                    BugCheckError.MultipleDefOfOptionIsFound(optionName, len(data))

                assert typeOfData != list

                BugCheckError.UnkOptObjectDataType(optionName, typeOfData)

            assert not (optionName in fileData.m_OptionsByName.keys())

            assert optionName in self.m_Data.m_AllOptionsByName.keys()

            data = self.m_Data.m_AllOptionsByName[optionName]
            assert data is not None

            typeOfData = type(data)

            if typeOfData == PgCfgModel__OptionData:
                assert type(data) == PgCfgModel__OptionData
                assert data.IsAlive()
                assert data.m_Name == optionName
                assert data.m_Value is not None
                assert type(data.m_Value) == list
                assert data.get_Parent().IsAlive()

                fileData2 = data.get_Parent().get_Parent()
                assert fileData2 is not None
                assert type(fileData2) == PgCfgModel__FileData
                assert fileData2.IsAlive()
                assert not (fileData2 is fileData)

                if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                    data, optionValueItem
                ):
                    RaiseError.OptionValueItemIsAlreadyDefinedInAnotherFile(
                        fileData2.m_Path, optionName, optionValueItem
                    )

                RaiseError.OptionIsAlreadyExistInAnotherFile(
                    fileData2.m_Path, optionName
                )

            if typeOfData == list:
                assert type(data) == list
                assert len(data) > 1

                for optionData2 in data:
                    assert optionData2 is not None
                    assert type(optionData2) == PgCfgModel__OptionData
                    assert optionData2.IsAlive()
                    assert optionData2.m_Name == optionName
                    assert optionData2.m_Value is not None
                    assert type(optionData2.m_Value) == list

                    fileData2 = optionData2.get_Parent().get_Parent()
                    assert fileData2 is not None
                    assert type(fileData2) == PgCfgModel__FileData
                    assert fileData2.IsAlive()
                    assert not (fileData2 is fileData)

                    if __class__.Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
                        optionData2, optionValueItem
                    ):
                        RaiseError.OptionValueItemIsAlreadyDefinedInAnotherFile(
                            fileData2.m_Path, optionName, optionValueItem
                        )

                    RaiseError.OptionIsAlreadyExistInAnotherFile(
                        fileData2.m_Path, optionName
                    )

                BugCheckError.UnexpectedSituation(
                    C_BUGCHECK_SRC, "#001", "optionName=[{0}].".format(optionName)
                )

            BugCheckError.UnkOptObjectDataType(optionName, typeOfData)

        assert not (optionName is fileData.m_OptionsByName.keys())
        assert not (optionName in self.m_Data.m_AllOptionsByName.keys())

        result = self.Helper__FinalRegSimpleOptionValue__File(
            fileData, optionName, [optionValueItem]
        )

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert (
            result.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )
        assert result.m_OptData is not None
        assert type(result.m_OptData) == PgCfgModel__OptionData
        assert result.m_OptData.IsAlive()
        assert result.m_OptData.m_Name == optionName
        return result

    # --------------------------------------------------------------------
    def Helper__FinalRegSimpleOptionValue__Common(
        self,
        optionName: str,
        preparedOptionValue: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(optionName) == str
        assert preparedOptionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Data.m_AllOptionsByName) == dict

        assert not (optionName in self.m_Data.m_AllOptionsByName.keys())

        # Select the file to append this new option
        getFileData_r = self.Helper__GetFileForSimpleOption(optionName)

        assert getFileData_r is not None
        assert type(getFileData_r) == tuple
        assert len(getFileData_r) == 2
        assert type(getFileData_r[0]) == PgCfgModel__FileData
        assert type(getFileData_r[1]) == bool

        fileData = getFileData_r[0]
        assert type(fileData) == PgCfgModel__FileData

        try:
            result = self.Helper__FinalRegSimpleOptionValue__File(
                fileData, optionName, preparedOptionValue
            )
        except:  # rollback file
            assert type(getFileData_r) == tuple
            assert len(getFileData_r) == 2

            assert type(getFileData_r[0]) == PgCfgModel__FileData
            assert type(getFileData_r[1]) == bool

            if getFileData_r[1]:
                pass  # TODO: delete file

            raise

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert (
            result.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )
        assert result.m_OptData is not None
        assert type(result.m_OptData) == PgCfgModel__OptionData
        assert result.m_OptData.IsAlive()
        assert result.m_OptData.m_Name == optionName
        return result

    # --------------------------------------------------------------------
    def Helper__FinalRegSimpleOptionValue__File(
        self,
        fileData: PgCfgModel__FileData,
        optionName: str,
        preparedOptionValue: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert type(fileData) == PgCfgModel__FileData
        assert type(optionName) == str
        assert preparedOptionValue is not None

        assert self.m_Data is not None
        assert type(self.m_Data) == PgCfgModel__ConfigurationData
        assert type(self.m_Data.m_AllOptionsByName) == dict

        assert not (optionName in fileData.m_OptionsByName.keys())
        assert not (optionName in self.m_Data.m_AllOptionsByName.keys())

        optionData = PgCfgModel__DataControllerUtils.File__add_Option(
            self.m_Data, fileData, optionName, preparedOptionValue
        )

        assert optionData is not None
        assert type(optionData) == PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionData.m_Name == optionName
        assert type(optionData.m_Parent) == PgCfgModel__FileLineData
        assert optionData.m_Parent.m_Parent is fileData
        assert optionName in fileData.m_OptionsByName.keys()
        assert optionName in self.m_Data.m_AllOptionsByName.keys()

        try:
            result = PostgresConfigurationSetOptionValueResult_Base.Create__OptWasAdded(
                self, optionData
            )
            assert result is not None
            assert type(result) == PostgresConfigurationSetOptionValueResult_Base
            assert (
                result.m_EventID
                == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
            )
            assert result.m_OptData is optionData
        except:  # rollback line with option
            assert optionData.IsAlive()

            PgCfgModel__DataControllerUtils.FileLine__delete(
                self.m_Data, optionData.get_Parent()
            )

            assert not optionData.IsAlive()

            assert not (optionName in fileData.m_OptionsByName.keys())
            assert not (optionName in self.m_Data.m_AllOptionsByName.keys())
            raise

        assert result is not None
        assert type(result) == PostgresConfigurationSetOptionValueResult_Base
        assert (
            result.m_EventID
            == PostgresConfigurationSetOptionValueEventID.OPTION_WAS_ADDED
        )
        assert result.m_OptData is optionData

        return result

    # --------------------------------------------------------------------
    def Helper__DoesOptionValueAlreadyHaveThisUniqueItem(
        optionData: PgCfgModel__OptionData, optionValueItem: any
    ) -> bool:
        assert optionData is not None
        assert optionValueItem is not None
        assert type(optionData) == PgCfgModel__OptionData
        assert optionData.IsAlive()
        assert optionData.m_Value is not None
        assert type(optionData.m_Value) == list

        return Helpers.DoesContainerContainsValue__NotNullAndExact(
            optionData.m_Value, optionValueItem
        )

    # Debug methods ------------------------------------------------------
    def Debug__CheckOurObjectData(self, data: PgCfgModel__ObjectData):
        assert data is not None
        assert isinstance(data, PgCfgModel__ObjectData)

        stack = set[PgCfgModel__ObjectData]()

        ptr = data
        while ptr is not self.m_Data:
            assert ptr is not None
            assert isinstance(ptr, PgCfgModel__ObjectData)
            assert not (ptr in stack)
            stack.add(ptr)
            ptr = ptr.get_Parent()


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationFactory_Base


class PostgresConfigurationFactory_Base:
    def GetObject(
        cfg: PostgresConfiguration_Base, objectData: PgCfgModel__ObjectData
    ) -> PostgresConfigurationObject:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert objectData is not None
        assert isinstance(objectData, PgCfgModel__ObjectData)

        # Build stack
        stack = list[PostgresConfigurationObject]()

        while True:
            stack.append(objectData)

            objectData = objectData.get_Parent()

            if objectData is None:
                break

            assert isinstance(objectData, PgCfgModel__ObjectData)

        assert type(stack) == list
        assert len(stack) > 0

        # Build ConfigurationObjects

        cfgObject: PostgresConfigurationObject = None

        while True:
            assert len(stack) > 0
            assert stack[-1] is not None
            assert isinstance(stack[-1], PgCfgModel__ObjectData)

            cfgObject = __class__.Helper__CreateObject(cfg, stack[-1], cfgObject)
            assert cfgObject is not None
            assert isinstance(cfgObject, PostgresConfigurationObject)

            stack.pop()

            if len(stack) == 0:
                break

        return cfgObject

    # --------------------------------------------------------------------
    def Helper__CreateObject(
        cfg: PostgresConfiguration_Base,
        objectData: PgCfgModel__ObjectData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationObject:
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert objectData is not None
        assert isinstance(objectData, PgCfgModel__ObjectData)
        assert objectParent is None or isinstance(
            objectParent, PostgresConfigurationObject
        )

        typeOfObjectData = type(objectData)
        assert typeOfObjectData is not None

        if typeOfObjectData == PgCfgModel__ConfigurationData:
            assert objectData is cfg.m_Data
            return cfg

        if typeOfObjectData == PgCfgModel__FileData:
            return __class__.Helper__CreateFile(objectData, objectParent)

        if typeOfObjectData == PgCfgModel__FileLineData:
            return __class__.Helper__CreateFileLine(objectData, objectParent)

        if typeOfObjectData == PgCfgModel__OptionData:
            return __class__.Helper__CreateOption(objectData, objectParent)

        BugCheckError.UnkObjectDataType(typeOfObjectData)

    # --------------------------------------------------------------------
    def Helper__CreateFile(
        objectData: PgCfgModel__FileData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationFile_Base:
        assert objectData is not None
        assert objectParent is not None
        assert type(objectData) == PgCfgModel__FileData
        assert isinstance(objectParent, PostgresConfigurationObject)

        if isinstance(objectParent, PostgresConfiguration_Base):
            return PostgresConfigurationTopLevelFile_Base(objectParent, objectData)

        assert not isinstance(objectParent, PostgresConfiguration)

        RaiseError.MethodIsNotImplemented(__class__, "Helper__CreateFile")

    # --------------------------------------------------------------------
    def Helper__CreateFileLine(
        objectData: PgCfgModel__FileLineData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationFile_Base:
        assert objectData is not None
        assert objectParent is not None
        assert type(objectData) == PgCfgModel__FileLineData
        assert isinstance(objectParent, PostgresConfigurationFile_Base)

        return PostgresConfigurationFileLine_Base(objectParent, objectData)

    # --------------------------------------------------------------------
    def Helper__CreateFileLineComment(
        fileLineDataItem: PgCfgModel__FileLineData.tagItem,
        fileLine: PostgresConfigurationObject,
    ) -> PostgresConfigurationFile_Base:
        assert fileLineDataItem is not None
        assert fileLine is not None
        assert type(fileLineDataItem) == PgCfgModel__FileLineData.tagItem
        assert isinstance(fileLine, PostgresConfigurationFileLine_Base)

        return PostgresConfigurationComment_Base(fileLine, fileLineDataItem)

    # --------------------------------------------------------------------
    def Helper__CreateOption(
        objectData: PgCfgModel__OptionData,
        objectParent: PostgresConfigurationObject,
    ) -> PostgresConfigurationFile_Base:
        assert objectData is not None
        assert objectParent is not None
        assert type(objectData) == PgCfgModel__OptionData
        assert isinstance(objectParent, PostgresConfigurationFileLine_Base)

        return PostgresConfigurationOption_Base(objectParent, objectData)


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationReader_Base


class PostgresConfigurationReader_Base:
    def LoadConfigurationFile(
        cfg: PostgresConfiguration_Base, filePath: str
    ) -> PostgresConfigurationTopLevelFile_Base:
        assert cfg is not None

        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(filePath) == str
        assert filePath != ""

        existFileDatas = dict[str, PgCfgModel__FileData]()

        for fileName in cfg.m_Data.m_AllFilesByName.keys():
            assert type(fileName) == str
            assert fileName != ""

            indexData = cfg.m_Data.m_AllFilesByName[fileName]
            assert indexData is not None

            typeOfIndexData = type(indexData)

            if typeOfIndexData == PgCfgModel__FileData:
                fileData: PgCfgModel__FileData = indexData
                assert type(fileData.m_Path) == str
                assert not (fileData.m_Path in existFileDatas.keys())
                existFileDatas[fileData.m_Path] = fileData
                continue

            if typeOfIndexData == list:
                for fileData in indexData:
                    assert type(fileData) == PgCfgModel__FileData
                    assert type(fileData.m_Path) == str
                    assert not (fileData.m_Path in existFileDatas.keys())
                    existFileDatas[fileData.m_Path] = fileData
                    continue
                continue

            BugCheckError.UnkFileObjectDataType(fileName, typeOfIndexData)

        # ----------------------------------------------------------------
        filePath_n = Helpers.NormalizeFilePath(cfg.m_Data.OsOps, cfg.m_Data.m_DataDir, filePath)
        assert type(filePath_n) == str

        if filePath_n in existFileDatas:
            return PostgresConfigurationFactory_Base.GetObject(
                cfg, existFileDatas[filePath_n]
            )

        # ----------------------------------------------------------------
        rootFile = cfg.AddTopLevelFile(filePath)
        assert type(rootFile) == PostgresConfigurationTopLevelFile_Base
        assert type(rootFile.m_FileData) == PgCfgModel__FileData
        assert type(rootFile.m_FileData.m_Lines) == list
        assert rootFile.m_FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
        assert rootFile.m_FileData.m_LastModifiedTimestamp is None
        assert len(rootFile.m_FileData.m_Lines) == 0

        queuedFileDatas = set[PgCfgModel__FileData]()

        queuedFileDatas.add(rootFile.m_FileData)

        while len(queuedFileDatas) != 0:
            currentFileData = queuedFileDatas.pop()
            assert isinstance(currentFileData, PgCfgModel__FileData)

            # load content
            # process content

            with cfg.m_Data.OsOps.OpenFileToRead(currentFileData.m_Path) as f:
                assert isinstance(f, ConfigurationOsFile)
                currentFile = PostgresConfigurationFactory_Base.GetObject(
                    cfg, currentFileData
                )
                __class__.Helper__LoadFileContent(currentFile, f)  # raise

                lastMDate = f.GetModificationTS()
                assert type(lastMDate) == datetime.datetime

                currentFileData.m_LastModifiedTimestamp = lastMDate
                currentFileData.m_Status = PgCfgModel__FileStatus.EXISTS

            assert not (currentFileData.m_Path in existFileDatas.keys())
            existFileDatas[currentFileData.m_Path] = currentFileData

            # enumerate all the includes
            for fileLineData in currentFileData.m_Lines:
                assert type(fileLineData) == PgCfgModel__FileLineData
                assert type(fileLineData.m_Items) == list

                for fileLineItem in fileLineData.m_Items:
                    assert type(fileLineItem) == PgCfgModel__FileLineData.tagItem

                    fileLineElementData = fileLineItem.m_Element

                    typeOfFileLineElementData = type(fileLineElementData)

                    if typeOfFileLineElementData == PgCfgModel__CommentData:
                        continue

                    if typeOfFileLineElementData == PgCfgModel__OptionData:
                        continue

                    if typeOfFileLineElementData == PgCfgModel__IncludeData:
                        # look at existFileDatas
                        includeData: PgCfgModel__IncludeData = fileLineElementData
                        assert type(includeData.m_File) == PgCfgModel__FileData
                        assert type(includeData.m_File.m_Path) == str

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

                    BugCheckError.UnkObjectDataType(typeOfFileLineElementData)

        assert len(queuedFileDatas) == 0
        assert isinstance(rootFile, PostgresConfigurationTopLevelFile_Base)

        return rootFile

    # --------------------------------------------------------------------
    def LoadFileContent(
        file: PostgresConfigurationFile_Base, fileContent: ConfigurationFileReader
    ) -> None:
        assert isinstance(file, PostgresConfigurationFile_Base)
        assert isinstance(fileContent, ConfigurationFileReader)

        return __class__.Helper__LoadFileContent(file, fileContent)

    # Helper methods -----------------------------------------------------
    def Helper__LoadFileContent(
        file: PostgresConfigurationFile_Base, fileContent: ConfigurationFileReader
    ) -> None:
        assert isinstance(file, PostgresConfigurationFile_Base)
        assert isinstance(fileContent, ConfigurationFileReader)

        lineReader = ReadUtils__LineReader()

        while lineData := fileContent.ReadLine():
            assert type(lineData) == str

            lineReader.SetData(lineData)

            __class__.Helper__ProcessLineData(file, lineReader)

    # --------------------------------------------------------------------
    def Helper__ProcessLineData(
        file: PostgresConfigurationFile_Base, lineReader: ReadUtils__LineReader
    ):
        assert isinstance(file, PostgresConfigurationFile_Base)
        assert type(lineReader) == ReadUtils__LineReader

        fileLine = file.AddEmptyLine()
        assert type(fileLine) == PostgresConfigurationFileLine_Base

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
                return __class__.Helper__ProcessLineData__Comment(fileLine, lineReader)

            if len(fileLine) == 0 and ReadUtils.IsValidSeqCh1(ch):
                # Read sequence
                sequenceOffset = lineReader.GetColOffset()
                sequence = ch

                while ch := lineReader.ReadSymbol():
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
                        fileLine, lineReader, sequenceOffset
                    )
                else:
                    if ch is not None:
                        lineReader.StepBack()

                    __class__.Helper__ProcessLineData__Option(
                        fileLine, lineReader, sequenceOffset, sequence
                    )
                continue

            RaiseError.CfgReader__UnexpectedSymbol(
                lineReader.GetLineNum(), lineReader.GetColNum(), ch
            )

    # --------------------------------------------------------------------
    def Helper__ProcessLineData__Comment(
        fileLine: PostgresConfigurationFileLine_Base, lineReader: ReadUtils__LineReader
    ):
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(lineReader) == ReadUtils__LineReader

        commentText = ""
        commentOffset = lineReader.GetColOffset()

        ch: str
        while ch := lineReader.ReadSymbol():
            if ReadUtils.IsEOL(ch):
                break
            commentText += ch

        fileLine.AddComment(commentText, commentOffset)

    # --------------------------------------------------------------------
    def Helper__ProcessLineData__Include(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        includeOffset: int,
    ):
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(lineReader) == ReadUtils__LineReader
        assert type(includeOffset) == int
        assert includeOffset >= 0

        # find first quote
        while True:
            ch = lineReader.ReadSymbol()

            if ch is None or ReadUtils.IsEOL(ch) or ch == "#":
                RaiseError.CfgReader__IncludeWithoutPath(lineReader.GetLineNum())

            if ReadUtils.IsSpace(ch):
                continue

            if ch == "'":
                break

            RaiseError.CfgReader__UnexpectedSymbol(
                lineReader.GetLineNum(), lineReader.GetColNum(), ch
            )

        # OK. First quote is found!

        # Let's process this quoted string
        filePath = ""

        while True:
            ch = lineReader.ReadSymbol()

            if ch is None or ReadUtils.IsEOL(ch):
                RaiseError.CfgReader__EndOfIncludePathIsNotFound(
                    lineReader.GetLineNum()
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
                        lineReader.GetLineNum()
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
                        lineReader.GetLineNum(), lineReader.GetColNum(), ch
                    )

                continue

            filePath += ch
            continue

        assert type(filePath) == str

        if len(filePath) == 0:
            RaiseError.CfgReader__IncludeHasEmptyPath(lineReader.GetLineNum())

        fileLine.AddInclude(filePath, includeOffset)

    # --------------------------------------------------------------------
    def Helper__ProcessLineData__Option(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        optionOffset: int,
        optionName: str,
    ):
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(lineReader) == ReadUtils__LineReader
        assert type(optionOffset) == int
        assert type(optionName) == str
        assert optionName != ""

        # skeep spaces
        spaceIsDetected = False

        while True:
            ch = lineReader.ReadSymbol()
            if ch is None or ReadUtils.IsEOL(ch) or ch == "#":
                RaiseError.CfgReader__OptionWithoutValue(
                    optionName, lineReader.GetLineNum()
                )

            if ReadUtils.IsSpace(ch):
                spaceIsDetected = True
                continue

            if ch == "=":
                while True:
                    ch = lineReader.ReadSymbol()

                    if ch is None or ReadUtils.IsEOL(ch) or ch == "#":
                        RaiseError.CfgReader__OptionWithoutValue(
                            optionName, lineReader.GetLineNum()
                        )

                    if ReadUtils.IsSpace(ch):
                        continue

                    break
                break

            if spaceIsDetected:
                break

            RaiseError.CfgReader__UnexpectedSymbol(
                lineReader.GetLineNum(), lineReader.GetColNum(), ch
            )

        # ch is the first symbol of option value.

        if ch == "'":
            __class__.Helper__ProcessLineData__Option__Quoted(
                fileLine, lineReader, optionOffset, optionName
            )
        else:
            lineReader.StepBack()

            __class__.Helper__ProcessLineData__Option__Generic(
                fileLine, lineReader, optionOffset, optionName
            )

    # --------------------------------------------------------------------
    def Helper__ProcessLineData__Option__Quoted(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        optionOffset: int,
        optionName: str,
    ):
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(lineReader) == ReadUtils__LineReader
        assert type(optionOffset) == int
        assert type(optionName) == str
        assert optionName != ""

        optionValue = ""

        while True:
            ch = lineReader.ReadSymbol()

            if ch is None or ReadUtils.IsEOL(ch):
                RaiseError.CfgReader__EndQuotedOptionValueIsNotFound(
                    optionName, lineReader.GetLineNum()
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
                        optionName, lineReader.GetLineNum()
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
                        optionName, lineReader.GetLineNum(), lineReader.GetColNum(), ch
                    )

                continue

            optionValue += ch
            continue

        assert type(optionValue) == str

        fileLine.AddOption(optionName, optionValue, optionOffset)

    # --------------------------------------------------------------------
    def Helper__ProcessLineData__Option__Generic(
        fileLine: PostgresConfigurationFileLine_Base,
        lineReader: ReadUtils__LineReader,
        optionOffset: int,
        optionName: str,
    ):
        assert type(fileLine) == PostgresConfigurationFileLine_Base
        assert type(lineReader) == ReadUtils__LineReader
        assert type(optionOffset) == int
        assert type(optionName) == str
        assert optionName != ""

        optionValue = ""

        ch: str

        while ch := lineReader.ReadSymbol():
            if ch == "#" or ReadUtils.IsEOL(ch):
                lineReader.StepBack()
                break

            optionValue += ch
            continue

        optionValue = optionValue.strip()

        assert type(optionValue) == str
        assert optionValue != ""

        fileLine.AddOption(optionName, optionValue, optionOffset)


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
        assert type(fileData) == PgCfgModel__FileData

        self.FileData = fileData
        self.Content = None
        self.File = None


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriterCtx_Base


class PostgresConfigurationWriterCtx_Base:
    Cfg: PostgresConfiguration_Base

    AllFiles: list[PostgresConfigurationWriterFileCtx_Base]
    NewFiles: list[PostgresConfigurationWriterFileCtx_Base]
    UpdFiles: list[PostgresConfigurationWriterFileCtx_Base]

    # --------------------------------------------------------------------
    def __init__(self, cfg: PostgresConfiguration_Base):
        assert cfg is not None
        assert isinstance(cfg, PostgresConfiguration_Base)

        self.Cfg = cfg

        self.AllFiles = list[PostgresConfigurationWriterFileCtx_Base]()
        self.NewFiles = list[PostgresConfigurationWriterFileCtx_Base]()
        self.UpdFiles = list[PostgresConfigurationWriterFileCtx_Base]()

    # --------------------------------------------------------------------
    def Init(self):
        assert type(self.AllFiles) == list
        assert type(self.NewFiles) == list
        assert type(self.UpdFiles) == list

        self.AllFiles.clear()
        self.NewFiles.clear()
        self.UpdFiles.clear()


# //////////////////////////////////////////////////////////////////////////////
# class PostgresConfigurationWriter_Base


class PostgresConfigurationWriter_Base:
    def MakeFileDataContent(
        ctx: PostgresConfigurationWriterCtx_Base, fileData: PgCfgModel__FileData
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert type(fileData) == PgCfgModel__FileData

        return __class__.Helper__MakeFileDataContent(ctx, fileData)

    # --------------------------------------------------------------------
    def DoWork(ctx: PostgresConfigurationWriterCtx_Base):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) == PgCfgModel__ConfigurationData

        return __class__.Helper__DoWork(ctx)

    # Helper Methods -----------------------------------------------------
    def Helper__DoWork(ctx: PostgresConfigurationWriterCtx_Base):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) == PgCfgModel__ConfigurationData

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

        # 4.
        __class__.Helper__DoWork__Stage05__WriteContents(ctx)

        # OK. Go HOME!
        return

    # --------------------------------------------------------------------
    def Helper__DoWork__Stage01__CreateFileContexts(
        ctx: PostgresConfigurationWriterCtx_Base,
    ):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) == PgCfgModel__ConfigurationData

        for fileData in ctx.Cfg.m_Data.m_AllFilesByName.values():
            assert fileData is not None
            assert type(fileData) == PgCfgModel__FileData

            fileCtx = PostgresConfigurationWriterFileCtx_Base(fileData)

            assert fileCtx.FileData is fileData
            assert fileCtx.Content is None
            assert fileCtx.File is None

            assert not (fileCtx in ctx.AllFiles)
            assert not (fileCtx in ctx.NewFiles)
            assert not (fileCtx in ctx.UpdFiles)

            ctx.AllFiles.append(fileCtx)

            if fileData.m_Status == PgCfgModel__FileStatus.IS_NEW:
                ctx.NewFiles.append(fileCtx)
            elif fileData.m_Status == PgCfgModel__FileStatus.EXISTS:
                ctx.UpdFiles.append(fileCtx)
            else:
                BugCheckError.UnkFileDataStatus(fileData.m_Path, fileData.m_Status)

    # --------------------------------------------------------------------
    def Helper__DoWork__Stage02__MakeFileDataContents(
        ctx: PostgresConfigurationWriterCtx_Base,
    ):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) == PgCfgModel__ConfigurationData

        for fileCtx in ctx.AllFiles:
            assert fileCtx is not None
            assert type(fileCtx) == PostgresConfigurationWriterFileCtx_Base
            assert type(fileCtx.FileData) == PgCfgModel__FileData
            assert fileCtx.Content is None

            fileCtx.Content = __class__.Helper__MakeFileDataContent(
                ctx, fileCtx.FileData
            )

    # --------------------------------------------------------------------
    def Helper__DoWork__Stage03__OpenUpdFilesToWrite(
        ctx: PostgresConfigurationWriterCtx_Base,
    ):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) == PgCfgModel__ConfigurationData

        for fileCtx in ctx.UpdFiles:
            assert fileCtx is not None
            assert type(fileCtx) == PostgresConfigurationWriterFileCtx_Base
            assert type(fileCtx.FileData) == PgCfgModel__FileData

            assert fileCtx.FileData.m_Status == PgCfgModel__FileStatus.EXISTS
            assert fileCtx.FileData.m_LastModifiedTimestamp is not None
            assert type(fileCtx.FileData.m_LastModifiedTimestamp) == datetime.datetime
            assert fileCtx.File is None

            # Let's open an exist file to read and write without truncation
            fileCtx.File = ctx.Cfg.m_Data.OsOps.OpenFileToWrite(fileCtx.FileData.m_Path)  # raise

            assert fileCtx.File is not None
            assert isinstance(fileCtx.File, ConfigurationOsFile)

            lastMDate = fileCtx.File.GetModificationTS()
            assert type(lastMDate) == datetime.datetime

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
    def Helper__DoWork__Stage04__OpenNewFilesToWrite(
        ctx: PostgresConfigurationWriterCtx_Base,
    ):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(ctx.Cfg.m_Data) == PgCfgModel__ConfigurationData
        assert type(ctx.NewFiles) == list

        iFile = 0

        try:
            for iFile in range(len(ctx.NewFiles)):
                fileCtx = ctx.NewFiles[iFile]

                assert fileCtx is not None
                assert type(fileCtx) == PostgresConfigurationWriterFileCtx_Base
                assert type(fileCtx.FileData) == PgCfgModel__FileData

                assert fileCtx.FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
                assert fileCtx.File is None

                fileCtx.File = ctx.Cfg.m_Data.OsOps.CreateFile(fileCtx.FileData.m_Path)  # raise                

                assert fileCtx.File is not None
                assert isinstance(fileCtx.File, ConfigurationOsFile)

                # OK
                continue

        except:  # Rollback new files
            assert type(iFile) == int
            assert iFile >= 0
            assert iFile <= len(ctx.NewFiles)

            for iFile2 in range(iFile):
                fileCtx = ctx.NewFiles[iFile2]

                assert fileCtx is not None
                assert type(fileCtx) == PostgresConfigurationWriterFileCtx_Base
                assert type(fileCtx.FileData) == PgCfgModel__FileData

                assert fileCtx.FileData.m_Status == PgCfgModel__FileStatus.IS_NEW
                assert fileCtx.File is not None
                assert isinstance(fileCtx.File, ConfigurationOsFile)

                assert not fileCtx.File.IsClosed

                filePath = fileCtx.File.Name
                assert filePath is not None
                assert type(filePath) == str
                assert filePath == fileCtx.FileData.m_Path

                fileCtx.File.Close()  # raise

                ctx.Cfg.m_Data.OsOps.Remove(filePath)  # raise
                continue

            raise

        # OK, Go HOME!
        return

    # --------------------------------------------------------------------
    def Helper__DoWork__Stage05__WriteContents(
        ctx: PostgresConfigurationWriterCtx_Base,
    ):
        assert type(ctx) == PostgresConfigurationWriterCtx_Base

        for iFile in range(len(ctx.AllFiles)):
            fileCtx = ctx.AllFiles[iFile]

            assert fileCtx is not None
            assert type(fileCtx) == PostgresConfigurationWriterFileCtx_Base
            assert type(fileCtx.FileData) == PgCfgModel__FileData

            assert fileCtx.File is not None
            assert isinstance(fileCtx.File, ConfigurationOsFile)

            assert fileCtx.Content is not None
            assert type(fileCtx.Content) == str

            fileCtx.File.Overwrite(fileCtx.Content)

            lastMDate = fileCtx.File.GetModificationTS()
            assert type(lastMDate) == datetime.datetime

            fileCtx.File.Close()

            fileCtx.FileData.m_LastModifiedTimestamp = lastMDate
            fileCtx.FileData.m_Status = PgCfgModel__FileStatus.EXISTS

    # --------------------------------------------------------------------
    def Helper__MakeFileDataContent(
        ctx: PostgresConfigurationWriterCtx_Base, fileData: PgCfgModel__FileData
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert type(fileData) == PgCfgModel__FileData

        fileContent = ""

        for fileLineData in fileData.m_Lines:
            assert type(fileLineData) == PgCfgModel__FileLineData
            lineContent = __class__.Helper__FileLineToString(ctx, fileLineData)
            assert type(lineContent) == str
            fileContent += lineContent
            fileContent += "\n"

        return fileContent

    # --------------------------------------------------------------------
    def Helper__FileLineToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        fileLineData: PgCfgModel__FileLineData,
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert type(fileLineData) == PgCfgModel__FileLineData

        fileLineItemCount = len(fileLineData.m_Items)

        if fileLineItemCount == 0:
            return ""

        lineContent = ""

        for lineItem in fileLineData.m_Items:
            assert type(lineItem) == PgCfgModel__FileLineData.tagItem
            assert type(lineItem) == PgCfgModel__FileLineData.tagItem
            assert lineItem.m_Element is not None
            assert isinstance(lineItem.m_Element, PgCfgModel__FileLineElementData)
            assert (
                lineItem.m_Element.m_Offset is None
                or type(lineItem.m_Element.m_Offset) == int
            )
            assert (
                lineItem.m_Element.m_Offset is None or lineItem.m_Element.m_Offset >= 0
            )

            itemContent = __class__.Helper__ElementToString(ctx, lineItem.m_Element)
            assert type(itemContent) == str

            lineContent = __class__.Helper__AppendItemToLine(
                lineContent, lineItem.m_Element.m_Offset, itemContent
            )
            assert type(lineContent) == str

        assert type(lineContent) == str
        return lineContent

    # --------------------------------------------------------------------
    def Helper__AppendItemToLine(lineContent: str, offset: int, text: str) -> str:
        assert type(lineContent) == str
        assert offset is None or type(offset) == int
        assert type(text) == str
        assert offset is None or offset >= 0

        if text == "":
            return lineContent

        lineContentLen = len(lineContent)

        assert type(lineContentLen) == int
        assert lineContentLen >= 0

        if offset is not None and lineContentLen < offset:
            lineContent += " " * (offset - lineContentLen)
        elif lineContentLen > 0:
            lineContent += " "

        lineContent += text
        return lineContent

    # --------------------------------------------------------------------
    def Helper__ElementToString(
        ctx: PostgresConfigurationWriterCtx_Base,
        elementData: PgCfgModel__FileLineElementData,
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert elementData is not None
        assert isinstance(elementData, PgCfgModel__FileLineElementData)

        typeOfElementData = type(elementData)

        if typeOfElementData == PgCfgModel__OptionData:
            return __class__.Helper__OptionToString(ctx, elementData)

        if typeOfElementData == PgCfgModel__CommentData:
            return __class__.Helper__CommentToString(ctx, elementData)

        if typeOfElementData == PgCfgModel__IncludeData:
            return __class__.Helper__IncludeToString(ctx, elementData)

        BugCheckError.UnkObjectDataType(typeOfElementData)

    # --------------------------------------------------------------------
    def Helper__OptionToString(
        ctx: PostgresConfigurationWriterCtx_Base, optionData: PgCfgModel__OptionData
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert ctx.Cfg is not None
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(optionData) == PgCfgModel__OptionData
        assert type(optionData.m_Name) == str
        assert optionData.m_Name != ""
        assert optionData.m_Value is not None

        writeHandler = ctx.Cfg.Internal__GetOptionHandlerToWrite(optionData.m_Name)

        assert writeHandler is not None
        assert isinstance(writeHandler, PgCfgModel__OptionHandlerToWrite)

        writeHandlerCtx = PgCfgModel__OptionHandlerCtxToWrite(
            ctx.Cfg, optionData.m_Name, optionData.m_Value
        )

        optValueAsText = writeHandler.OptionValueToString(writeHandlerCtx)

        assert type(optValueAsText) == str
        assert optValueAsText != ""

        result = optionData.m_Name + " = " + optValueAsText
        return result

    # --------------------------------------------------------------------
    def Helper__CommentToString(
        ctx: PostgresConfigurationWriterCtx_Base, commentData: PgCfgModel__CommentData
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert ctx.Cfg is not None
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(commentData) == PgCfgModel__CommentData
        assert commentData.m_Text is not None
        assert type(commentData.m_Text) == str

        assert DataVerificator.IsValidCommentText(commentData.m_Text)

        result = "#" + commentData.m_Text
        return result

    # --------------------------------------------------------------------
    def Helper__IncludeToString(
        ctx: PostgresConfigurationWriterCtx_Base, includeData: PgCfgModel__IncludeData
    ) -> str:
        assert type(ctx) == PostgresConfigurationWriterCtx_Base
        assert ctx.Cfg is not None
        assert isinstance(ctx.Cfg, PostgresConfiguration_Base)
        assert type(includeData) == PgCfgModel__IncludeData
        assert includeData.m_Path is not None
        assert type(includeData.m_Path) == str
        assert includeData.m_Path != ""

        result = "include " + WriteUtils.Pack_Str(includeData.m_Path)

        assert type(result) == str
        assert result != ""
        return result


# //////////////////////////////////////////////////////////////////////////////
# PostgresConfigurationController__Base


class PostgresConfigurationController__Base:
    def AddOption(
        cfg: PostgresConfiguration_Base,
        target: typing.Union[None, PgCfgModel__FileData, PgCfgModel__FileLineData],
        optionName: str,
        optionValue: any,
        optionOffset: typing.Union[int],
    ) -> PostgresConfigurationOption_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            target is None
            or type(target) == PgCfgModel__FileData
            or type(target) == PgCfgModel__FileLineData
        )
        assert type(optionName) == str
        assert optionValue is not None
        assert optionOffset is None or type(optionOffset) == int

        # ----------------------
        preparedOptionValue = __class__.Helper__PrepareSetValue(
            cfg, optionName, optionValue
        )

        assert preparedOptionValue is not None

        # ----------------------
        addHandler = cfg.Internal__GetOptionHandlerToAddOption(optionName)

        assert isinstance(addHandler, PgCfgModel__OptionHandlerToAddOption)

        ctx = PgCfgModel__OptionHandlerCtxToAddOption(
            cfg,
            target,
            optionOffset,
            optionName,
            preparedOptionValue,
        )

        option = addHandler.AddOption(ctx)
        assert option is not None
        assert type(option) == PostgresConfigurationOption_Base
        return option

    # --------------------------------------------------------------------
    def SetOptionValue(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
        optionValue: any,
        optionOffset: typing.Union[int],
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) == PgCfgModel__FileData
            or type(targetData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str
        assert optionOffset is None or type(optionOffset) == int

        # ----------------------
        if optionValue is None:
            return cfg.DataHandler__ResetOption(targetData, optionName)

        assert optionValue is not None

        # ----------------------
        preparedOptionValue = __class__.Helper__PrepareSetValue(
            cfg, optionName, optionValue
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

        assert type(r) == PostgresConfigurationSetOptionValueResult_Base

        return r

    # --------------------------------------------------------------------
    def SetOptionValueItem(
        cfg: PostgresConfiguration_Base,
        targetData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
        optionValueItem: any,
    ) -> PostgresConfigurationSetOptionValueResult_Base:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            targetData is None
            or type(targetData) == PgCfgModel__FileData
            or type(targetData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str

        # ---------------------------------------
        if optionValueItem is None:
            RaiseError.NoneValueIsNotSupported()

        assert optionValueItem is not None

        # ---------------------------------------
        optionValueItem_p = __class__.Helper__PrepareSetValueItem(
            cfg, optionName, optionValueItem
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

        assert type(r) == PostgresConfigurationSetOptionValueResult_Base

        return r

    # --------------------------------------------------------------------
    def GetOptionValue(
        cfg: PostgresConfiguration_Base,
        sourceData: typing.Union[None, PgCfgModel__FileData, PgCfgModel__OptionData],
        optionName: str,
    ) -> any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert (
            sourceData is None
            or type(sourceData) == PgCfgModel__FileData
            or type(sourceData) == PgCfgModel__OptionData
        )
        assert type(optionName) == str

        getHandler = cfg.Internal__GetOptionHandlerToGetValue(optionName)

        assert isinstance(getHandler, PgCfgModel__OptionHandlerToGetValue)

        ctx = PgCfgModel__OptionHandlerCtxToGetValue(cfg, sourceData, optionName)

        r = getHandler.GetOptionValue(ctx)
        return r

    # Helper methods -----------------------------------------------------
    def Helper__PrepareSetValue(
        cfg: PostgresConfiguration_Base, optionName: str, optionValue: any
    ) -> any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) == str
        assert optionValue is not None

        assert type(optionName) == str
        assert optionValue is not None

        prepareHandler = cfg.Internal__GetOptionHandlerToPrepareSetValue(optionName)
        assert prepareHandler is not None
        assert isinstance(prepareHandler, PgCfgModel__OptionHandlerToPrepareSetValue)

        prepareCtx = PgCfgModel__OptionHandlerCtxPrepareToSetValue(
            cfg, optionName, optionValue
        )

        return prepareHandler.PrepareSetValue(prepareCtx)

    # --------------------------------------------------------------------
    def Helper__PrepareSetValueItem(
        cfg: PostgresConfiguration_Base, optionName: str, optionValueItem: any
    ) -> any:
        assert isinstance(cfg, PostgresConfiguration_Base)
        assert type(optionName) == str
        assert optionValueItem is not None

        prepareHandler = cfg.Internal__GetOptionHandlerToPrepareSetValueItem(optionName)
        assert prepareHandler is not None
        assert isinstance(
            prepareHandler, PgCfgModel__OptionHandlerToPrepareSetValueItem
        )

        prepareCtx = PgCfgModel__OptionHandlerCtxPrepareToSetValueItem(
            cfg, optionName, optionValueItem
        )

        return prepareHandler.PrepareSetValueItem(prepareCtx)


# //////////////////////////////////////////////////////////////////////////////
