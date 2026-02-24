# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests

import datetime
import typing


# //////////////////////////////////////////////////////////////////////////////
# class ErrorMessageBuilder


class ErrorMessageBuilder:
    @staticmethod
    def MethodIsNotImplemented(classType: type, methodName: str):
        assert type(classType) is type
        assert type(methodName) is str
        assert methodName != ""

        errMsg = "Method {0}::{1} is not implemented.".format(
            classType.__name__, methodName
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def GetPropertyIsNotImplemented(classType: type, methodName: str):
        assert type(classType) is type
        assert type(methodName) is str
        assert methodName != ""

        errMsg = "Get property {0}::{1} is not implemented.".format(
            classType.__name__, methodName
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameIsNone():
        errMsg = "Option name is None."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameHasBadType(nameType: type):
        assert nameType is not None
        assert type(nameType) is type

        errMsg = "Option name has nad type [{0}]".format(nameType.__name__)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionNameIsEmpty():
        errMsg = "Option name is empty."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def NoneValueIsNotSupported():
        errMsg = "None value is not supported."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def NoneOptionValueItemIsNotSupported(optionName: str):
        assert type(optionName) is str
        assert optionName != ""

        errMsg = "None value item of option [{0}] is not supported.".format(optionName)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CommentObjectWasDeleted():
        errMsg = "Comment object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionObjectWasDeleted():
        errMsg = "Option object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def IncludeObjectWasDeleted():
        errMsg = "Include object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineObjectWasDeleted():
        errMsg = "FileLine object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileObjectWasDeleted():
        errMsg = "File object was deleted."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def BadOptionValueType(optionName: str, optionValueType: type, expectedType: type):
        assert type(optionName) is str
        assert type(optionValueType) is type
        assert type(expectedType) is type

        errMsg = "Bad option [{0}] value type [{1}]. Expected type is [{2}].".format(
            optionName, optionValueType.__name__, expectedType.__name__
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CantConvertOptionValue(optionName: str, sourceType: type, targetType: type):
        assert type(optionName) is str
        assert type(sourceType) is type
        assert type(targetType) is type

        errMsg = (
            "Can't convert option [{0}] value from type [{1}] to type [{2}].".format(
                optionName, sourceType.__name__, targetType.__name__
            )
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def BadOptionValueItemType(
        optionName: str, optionValueItemType: type, expectedType: type
    ):
        assert type(optionName) is str
        assert type(optionValueItemType) is type
        assert type(expectedType) is type

        errMsg = (
            "Bad option [{0}] value item type [{1}]. Expected type is [{2}].".format(
                optionName, optionValueItemType.__name__, expectedType.__name__
            )
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CommentTextContainsInvalidSymbols():
        errMsg = "Comment text contains invalid symbols."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def FileIsAlreadyRegistered(file_path: str):
        errMsg = "File [{0}] is already registered.".format(file_path)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInThisFile(filePath: str, optionName: str):
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in this file [{1}].".format(
            optionName, filePath
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInAnotherFile(filePath: str, optionName: str):
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in another file [{1}].".format(
            optionName, filePath
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsAlreadyExistInFile(filePath: str, optionName: str):
        assert type(filePath) is str
        assert type(optionName) is str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in the file [{1}].".format(
            optionName, filePath
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionValueItemIsAlreadyDefined(
        filePath: str, optName: str, valueItem: typing.Any
    ):
        assert type(filePath) is str
        assert type(optName) is str

        errMsg = "Another definition of option [{1}] value item [{2}] is found in the file [{0}].".format(
            filePath, optName, valueItem
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def OptionValueItemIsAlreadyDefinedInAnotherFile(
        filePath: str, optName: str, valueItem: typing.Any
    ):
        assert type(filePath) is str
        assert type(optName) is str

        errMsg = "Definition of option [{1}] value item [{2}] is found in another file [{0}].".format(
            filePath, optName, valueItem
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def UnknownFileName(fileName: str):
        assert type(fileName) is str

        errMsg = "Unknown file name [{0}].".format(fileName)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfFileIsFound(fileName: str, count: int):
        assert type(fileName) is str
        assert type(count) is int

        errMsg = "Multiple definitition of file [{0}] is found - {1}.".format(
            fileName, count
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FilePathIsEmpty():
        errMsg = "File path is empty."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileWasModifiedExternally(
        filePath: str,
        ourLastMDate: datetime.datetime,
        curLastMDate: datetime.datetime,
    ):
        assert type(filePath) is str
        assert type(ourLastMDate) is datetime.datetime
        assert type(curLastMDate) is datetime.datetime

        errMsg = "File [{0}] was modified externally. Our timestamp is [{1}]. The current file timestamp is [{2}].".format(
            filePath, ourLastMDate, curLastMDate
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasComment():
        errMsg = "File line already has a comment."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasOption(optionName: str):
        assert type(optionName) is str

        errMsg = "File line already has the option [{0}].".format(optionName)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineAlreadyHasIncludeDirective():
        errMsg = "File line already has an include directive."
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnexpectedSymbol(lineNum: int, colNum: int, ch: str):
        assert type(lineNum) is int
        assert type(colNum) is int
        assert type(ch) is str

        errMsg = "Unexpected symbol in line {0}, column {1}: [{2}]".format(
            lineNum, colNum, ch
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncludeWithoutPath(lineNum: int):
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Include directive in line {0} does not have a path.".format(lineNum)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__EndOfIncludePathIsNotFound(lineNum: int):
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "The end of an include path is not found. Line {0}.".format(lineNum)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncompletedEscapeInInclude(lineNum: int):
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Escape in an include path is not completed. Line {0}.".format(lineNum)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnknownEscapedSymbolInInclude(lineNum: int, colNum: int, ch: str):
        assert type(lineNum) is int
        assert type(colNum) is int
        assert type(ch) is str
        assert lineNum >= 0
        assert colNum >= 0
        assert ch != ""

        errMsg = "Unknown escape symbol [{2}] in an include path. Line {0}. Column {1}.".format(
            lineNum, colNum, ch
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncludeHasEmptyPath(lineNum: int):
        assert type(lineNum) is int
        assert lineNum >= 0

        errMsg = "Include in line {0} has an empty path.".format(lineNum)
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__OptionWithoutValue(optionName: str, lineNum: int):
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Option [{0}] in line {1} does not have a value.".format(
            optionName, lineNum
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__EndQuotedOptionValueIsNotFound(optionName: str, lineNum: int):
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Value of quoted option [{0}] is not completed. Line {1}.".format(
            optionName, lineNum
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__IncompletedEscapeInQuotedOptionValue(optionName: str, lineNum: int):
        assert type(lineNum) is int
        assert type(optionName) is str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Escape in a value of quoted option [{0}] is not completed. Line {1}.".format(
            optionName, lineNum
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
        optionName: str, lineNum: int, colNum: int, ch: str
    ):
        assert type(lineNum) is int
        assert type(optionName) is str
        assert type(ch) is str
        assert lineNum >= 0
        assert optionName != ""
        assert ch != ""

        errMsg = "Unknown escape symbol [{3}] in a value of quoted option [{0}]. Line {1}. Column {2}.".format(
            optionName, lineNum, colNum, ch
        )
        return errMsg

    # --------------------------------------------------------------------
    @staticmethod
    def BadFormatOfCommaSeparatedList():
        errMsg = "Bad format of comma separated list."
        return errMsg


# //////////////////////////////////////////////////////////////////////////////
