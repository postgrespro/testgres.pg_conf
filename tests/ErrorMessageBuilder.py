# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests

import datetime
import typing

# //////////////////////////////////////////////////////////////////////////////
# class ErrorMessageBuilder


class ErrorMessageBuilder:
    @staticmethod
    def MethodIsNotImplemented(
        classType: type,
        methodName: str,
    ) -> str:
        assert type(classType) is type
        assert type(methodName) is str
        assert methodName != ""

        errMsg = "Method {}::{} is not implemented.".format(
            classType.__name__,
            methodName,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def GetPropertyIsNotImplemented(
        classType: type,
        methodName: str,
    ) -> str:
        assert type(classType) is type
        assert type(methodName) is str
        assert methodName != ""

        errMsg = "Get property {}::{} is not implemented.".format(
            classType.__name__,
            methodName,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameIsNone() -> str:
        errMsg = "Option name is None."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameHasBadType(
        nameType: type,
    ) -> str:
        assert nameType is not None
        assert type(nameType) is type

        errMsg = "Option name has a bad type [{}].".format(
            nameType.__name__,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameIsEmpty() -> str:
        errMsg = "Option name is empty."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def NoneValueIsNotSupported() -> str:
        errMsg = "None value is not supported."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def NoneOptionValueItemIsNotSupported(
        optionName: str,
    ) -> str:
        assert type(optionName) is str
        assert optionName != ""

        errMsg = "None value item of option [{}] is not supported.".format(
            optionName,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CommentObjectWasDeleted() -> str:
        errMsg = "Comment object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionObjectWasDeleted() -> str:
        errMsg = "Option object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def IncludeObjectWasDeleted() -> str:
        errMsg = "Include object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineObjectWasDeleted() -> str:
        errMsg = "FileLine object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileObjectWasDeleted() -> str:
        errMsg = "File object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def BadOptionValueType(
        optionName: str,
        optionValueType: type,
        expectedType: type,
    ) -> str:
        assert type(optionName) is str
        assert type(optionValueType) is type
        assert type(expectedType) is type

        errMsg = "Bad option [{}] value type [{}]. Expected type is [{}].".format(
            optionName,
            optionValueType.__name__,
            expectedType.__name__,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CantConvertOptionValue(
        optionName: str,
        sourceType: type,
        targetType: type,
    ) -> str:
        assert type(optionName) is str
        assert type(sourceType) is type
        assert type(targetType) is type

        errMsg = "Can't convert option [{}] value from type [{}] to type [{}].".format(
            optionName,
            sourceType.__name__,
            targetType.__name__,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def BadOptionValueItemType(
        optionName: str,
        optionValueItemType: type,
        expectedType: type,
    ) -> str:
        assert type(optionName) is str
        assert type(optionValueItemType) is type
        assert type(expectedType) is type

        errMsg = "Bad option [{}] value item type [{}]. Expected type is [{}].".format(
            optionName,
            optionValueItemType.__name__,
            expectedType.__name__,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CommentTextContainsInvalidSymbols() -> str:
        errMsg = "Comment text contains invalid symbols."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileIsAlreadyRegistered(
        file_path: str,
    ) -> str:
        errMsg = "File [{}] is already registered.".format(
            file_path,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInThisFile(
        filePath: str,
        optionName: str,
    ) -> str:
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{}] already exist in this file [{}].".format(
            optionName,
            filePath,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInAnotherFile(
        filePath: str,
        optionName: str,
    ) -> str:
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{}] already exist in another file [{}].".format(
            optionName,
            filePath,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInFile(
        filePath: str,
        optionName: str,
    ) -> str:
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{}] already exist in the file [{}].".format(
            optionName,
            filePath,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionValueItemIsAlreadyDefined(
        filePath: str,
        optName: str,
        valueItem: typing.Any,
    ) -> str:
        assert type(filePath) is str
        assert type(optName) is str

        errMsg = "Another definition of option [{}] value item [{}] is found in the file [{}].".format(
            optName,
            valueItem,
            filePath,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionValueItemIsAlreadyDefinedInAnotherFile(
        filePath: str,
        optName: str,
        valueItem: typing.Any,
    ) -> str:
        assert type(filePath) is str
        assert type(optName) is str

        errMsg = "Definition of option [{}] value item [{}] is found in another file [{}].".format(
            optName,
            valueItem,
            filePath,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def UnknownFileName(
        fileName: str,
    ) -> str:
        assert type(fileName) is str

        errMsg = "Unknown file name [{}].".format(
            fileName,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfFileIsFound(
        fileName: str,
        count: int,
    ) -> str:
        assert type(fileName) is str
        assert type(count) is int

        errMsg = "Multiple definitition of file [{}] is found - {}.".format(
            fileName,
            count,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FilePathIsEmpty() -> str:
        errMsg = "File path is empty."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileWasModifiedExternally(
        filePath: str,
        ourLastMDate: datetime.datetime,
        curLastMDate: datetime.datetime,
    ) -> str:
        assert type(filePath) is str
        assert type(ourLastMDate) is datetime.datetime
        assert type(curLastMDate) is datetime.datetime

        errMsg = "File [{}] was modified externally. Our timestamp is [{}]. The current file timestamp is [{}].".format(
            filePath,
            ourLastMDate,
            curLastMDate,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasComment() -> str:
        errMsg = "File line already has a comment."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasOption(
        optionName: str,
    ) -> str:
        assert type(optionName) is str

        errMsg = "File line already has the option [{}].".format(
            optionName,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasIncludeDirective() -> str:
        errMsg = "File line already has an include directive."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnexpectedSymbol(
        lineNum: int,
        colNum: int,
        ch: str,
    ) -> str:
        assert type(lineNum) is int
        assert type(colNum) is int
        assert type(ch) is str

        errMsg = "Unexpected symbol in line {}, column {}: {!r}".format(
            lineNum,
            colNum,
            ch,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncludeWithoutPath(
        lineNum: int,
    ) -> str:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Include directive in line {} does not have a path.".format(
            lineNum,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__EndOfIncludePathIsNotFound(
        lineNum: int,
    ) -> str:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "The end of an include path is not found. Line {}.".format(
            lineNum,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncompletedEscapeInInclude(
        lineNum: int,
    ) -> str:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Escape in an include path is not completed. Line {}.".format(
            lineNum,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnknownEscapedSymbolInInclude(
        lineNum: int,
        colNum: int,
        ch: str,
    ) -> str:
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
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncludeHasEmptyPath(
        lineNum: int,
    ) -> str:
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Include in line {} has an empty path.".format(
            lineNum,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__OptionWithoutValue(
        optionName: str,
        lineNum: int,
    ) -> str:
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Option [{}] in line {} does not have a value.".format(
            optionName,
            lineNum,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__EndQuotedOptionValueIsNotFound(
        optionName: str,
        lineNum: int,
    ) -> str:
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Value of quoted option [{}] is not completed. Line {}.".format(
            optionName,
            lineNum,
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncompletedEscapeInQuotedOptionValue(
        optionName: str,
        lineNum: int,
    ) -> str:
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
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
        optionName: str,
        lineNum: int,
        colNum: int,
        ch: str,
    ) -> str:
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
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def BadFormatOfCommaSeparatedList() -> str:
        errMsg = "Bad format of comma separated list."
        return errMsg


# //////////////////////////////////////////////////////////////////////////////
