# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from ..exceptions import PostgresConfigException

import datetime
import typing

# //////////////////////////////////////////////////////////////////////////////
# RaiseError


class RaiseError:
    @staticmethod
    def MethodIsNotImplemented(
        classType: type,
        methodName: str,
    ) -> typing.NoReturn:
        assert type(classType) is type
        assert type(methodName) is str
        assert methodName != ""

        errMsg = "Method {}::{} is not implemented.".format(
            classType.__name__,
            methodName,
        )
        raise NotImplementedError(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def GetPropertyIsNotImplemented(
        classType: type,
        methodName: str,
    ) -> typing.NoReturn:
        assert type(classType) is type
        assert type(methodName) is str
        assert methodName != ""

        errMsg = "Get property {}::{} is not implemented.".format(
            classType.__name__,
            methodName,
        )
        raise NotImplementedError(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameIsNone() -> typing.NoReturn:
        errMsg = "Option name is None."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameHasBadType(
        nameType: type,
    ) -> typing.NoReturn:
        assert nameType is not None
        assert type(nameType) is type

        errMsg = "Option name has a bad type [{}].".format(
            nameType.__name__,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameIsEmpty() -> typing.NoReturn:
        errMsg = "Option name is empty."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def NoneValueIsNotSupported() -> typing.NoReturn:
        errMsg = "None value is not supported."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def NoneOptionValueItemIsNotSupported(
        optionName: str,
    ) -> typing.NoReturn:
        assert type(optionName) is str
        assert optionName != ""

        errMsg = "None value item of option [{}] is not supported.".format(
            optionName,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CommentObjectWasDeleted() -> typing.NoReturn:
        errMsg = "Comment object was deleted."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionObjectWasDeleted() -> typing.NoReturn:
        errMsg = "Option object was deleted."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def IncludeObjectWasDeleted() -> typing.NoReturn:
        errMsg = "Include object was deleted."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineObjectWasDeleted() -> typing.NoReturn:
        errMsg = "FileLine object was deleted."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileObjectWasDeleted() -> typing.NoReturn:
        errMsg = "File object was deleted."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def BadOptionValueType(
        optionName: str,
        optionValueType: type,
        expectedType: type,
    ) -> typing.NoReturn:
        assert type(optionName) is str
        assert type(optionValueType) is type
        assert type(expectedType) is type

        errMsg = "Bad option [{}] value type [{}]. Expected type is [{}].".format(
            optionName,
            optionValueType.__name__,
            expectedType.__name__,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CantConvertOptionValue(
        optionName: str,
        sourceType: type,
        targetType: type,
    ) -> typing.NoReturn:
        assert type(optionName) is str
        assert type(sourceType) is type
        assert type(targetType) is type

        errMsg = "Can't convert option [{}] value from type [{}] to type [{}].".format(
            optionName,
            sourceType.__name__,
            targetType.__name__,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def BadOptionValueItemType(
        optionName: str,
        optionValueItemType: type,
        expectedType: type,
    ) -> typing.NoReturn:
        assert type(optionName) is str
        assert type(optionValueItemType) is type
        assert type(expectedType) is type

        errMsg = "Bad option [{}] value item type [{}]. Expected type is [{}].".format(
            optionName,
            optionValueItemType.__name__,
            expectedType.__name__,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CommentTextContainsInvalidSymbols() -> typing.NoReturn:
        errMsg = "Comment text contains invalid symbols."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileIsAlreadyRegistered(
        file_path: str,
    ) -> typing.NoReturn:
        errMsg = "File [{0}] is already registered.".format(file_path)

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInThisFile(
        filePath: str,
        optionName: str,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in this file [{1}].".format(
            optionName, filePath
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInAnotherFile(
        filePath: str,
        optionName: str,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{}] already exist in another file [{}].".format(
            optionName,
            filePath,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInFile(
        filePath: str,
        optionName: str,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{}] already exist in the file [{}].".format(
            optionName,
            filePath,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionValueItemIsAlreadyDefined(
        filePath: str,
        optName: str,
        valueItem: typing.Any,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert type(optName) is str

        errMsg = "Another definition of option [{}] value item [{}] is found in the file [{}].".format(
            filePath,
            optName,
            valueItem,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def OptionValueItemIsAlreadyDefinedInAnotherFile(
        filePath: str,
        optName: str,
        valueItem: typing.Any,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert type(optName) is str

        errMsg = "Definition of option [{}] value item [{}] is found in another file [{}].".format(
            optName,
            valueItem,
            filePath,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def UnknownFileName(fileName: str) -> typing.NoReturn:
        assert type(fileName) is str

        errMsg = "Unknown file name [{}].".format(
            fileName,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfFileIsFound(
        fileName: str,
        count: int,
    ) -> typing.NoReturn:
        assert type(fileName) is str
        assert type(count) is int

        errMsg = "Multiple definitition of file [{}] is found - {}.".format(
            fileName,
            count,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FilePathIsEmpty() -> typing.NoReturn:
        errMsg = "File path is empty."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileWasModifiedExternally(
        filePath: str,
        ourLastMDate: datetime.datetime,
        curLastMDate: datetime.datetime,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert type(ourLastMDate) is datetime.datetime
        assert type(curLastMDate) is datetime.datetime

        errMsg = "File [{}] was modified externally. Our timestamp is [{}]. The current file timestamp is [{}].".format(
            filePath,
            ourLastMDate,
            curLastMDate,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasComment() -> typing.NoReturn:
        errMsg = "File line already has a comment."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasOption(optionName: str) -> typing.NoReturn:
        assert type(optionName) is str

        errMsg = "File line already has the option [{}].".format(
            optionName,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasIncludeDirective() -> typing.NoReturn:
        errMsg = "File line already has an include directive."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnexpectedSymbol(
        lineNum: int,
        colNum: int,
        ch: str,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert type(colNum) is int
        assert type(ch) is str

        errMsg = "Unexpected symbol in line {}, column {}: {!r}".format(
            lineNum,
            colNum,
            ch,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncludeWithoutPath(lineNum: int) -> typing.NoReturn:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Include directive in line {} does not have a path.".format(
            lineNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__EndOfIncludePathIsNotFound(lineNum: int) -> typing.NoReturn:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "The end of an include path is not found. Line {}.".format(
            lineNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncompletedEscapeInInclude(lineNum: int) -> typing.NoReturn:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Escape in an include path is not completed. Line {}.".format(
            lineNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnknownEscapedSymbolInInclude(
        lineNum: int,
        colNum: int,
        ch: str,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert type(colNum) is int
        assert type(ch) is str
        assert lineNum >= 0
        assert colNum >= 0
        assert ch != ""

        errMsg = (
            "Unknown escape symbol {!r} in an include path. Line {}. Column {}.".format(
                ch,
                lineNum,
                colNum,
            )
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncludeHasEmptyPath(
        lineNum: int,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Include in line {} has an empty path.".format(
            lineNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__OptionWithoutValue(
        optionName: str,
        lineNum: int,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Option [{}] in line {} does not have a value.".format(
            optionName,
            lineNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__EndQuotedOptionValueIsNotFound(
        optionName: str,
        lineNum: int,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Value of quoted option [{}] is not completed. Line {}.".format(
            optionName,
            lineNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncompletedEscapeInQuotedOptionValue(
        optionName: str,
        lineNum: int,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = (
            "Escape in a value of quoted option [{}] is not completed. Line {}.".format(
                optionName,
                lineNum,
            )
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
        optionName: str,
        lineNum: int,
        colNum: int,
        ch: str,
    ) -> typing.NoReturn:
        assert type(lineNum) is int
        assert type(optionName) is str
        assert type(ch) is str
        assert lineNum >= 0
        assert optionName != ""
        assert ch != ""

        errMsg = "Unknown escape symbol {!r} in a value of quoted option [{}]. Line {}. Column {}.".format(
            ch,
            optionName,
            lineNum,
            colNum,
        )

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def BadFormatOfCommaSeparatedList() -> typing.NoReturn:
        errMsg = "Bad format of comma separated list."

        __class__.Helper__RaiseErr__PostgresConfigException(
            errMsg,
        )

    # --------------------------------------------------------------------
    @staticmethod
    def Helper__RaiseErr__PostgresConfigException(
        errMsg: str,
    ) -> typing.NoReturn:
        assert type(errMsg) is str

        raise PostgresConfigException(errMsg)


# //////////////////////////////////////////////////////////////////////////////
