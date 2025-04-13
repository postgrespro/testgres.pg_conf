# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

import datetime

# //////////////////////////////////////////////////////////////////////////////
# RaiseError


class RaiseError:
    def MethodIsNotImplemented(classType: type, methodName: str):
        assert type(classType) == type
        assert type(methodName) == str
        assert methodName != ""

        errMsg = "Method {0}::{1} is not implemented.".format(
            classType.__name__, methodName
        )
        raise NotImplementedError(errMsg)

    # --------------------------------------------------------------------
    def GetPropertyIsNotImplemented(classType: type, methodName: str):
        assert type(classType) == type
        assert type(methodName) == str
        assert methodName != ""

        errMsg = "Get property {0}::{1} is not implemented.".format(
            classType.__name__, methodName
        )
        raise NotImplementedError(errMsg)

    # --------------------------------------------------------------------
    def OptionNameIsNone():
        errMsg = "Option name is None."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionNameHasBadType(nameType: type):
        assert nameType is not None
        assert type(nameType) == type

        errMsg = "Option name has nad type [{0}]".format(nameType.__name__)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionNameIsEmpty():
        errMsg = "Option name is empty."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def NoneValueIsNotSupported():
        errMsg = "None value is not supported."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def NoneOptionValueItemIsNotSupported(optionName: str):
        assert type(optionName) == str
        assert optionName != ""

        errMsg = "None value item of option [{0}] is not supported.".format(optionName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CommentObjectWasDeleted():
        errMsg = "Comment object was deleted."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionObjectWasDeleted():
        errMsg = "Option object was deleted."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def IncludeObjectWasDeleted():
        errMsg = "Include object was deleted."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileLineObjectWasDeleted():
        errMsg = "FileLine object was deleted."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileObjectWasDeleted():
        errMsg = "File object was deleted."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def BadOptionValueType(optionName: str, optionValueType: type, expectedType: type):
        assert type(optionName) == str
        assert type(optionValueType) == type
        assert type(expectedType) == type

        errMsg = "Bad option [{0}] value type [{1}]. Expected type is [{2}].".format(
            optionName, optionValueType.__name__, expectedType.__name__
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CantConvertOptionValue(optionName: str, sourceType: type, targetType: type):
        assert type(optionName) == str
        assert type(sourceType) == type
        assert type(targetType) == type

        errMsg = (
            "Can't convert option [{0}] value from type [{1}] to type [{2}].".format(
                optionName, sourceType.__name__, targetType.__name__
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def BadOptionValueItemType(
        optionName: str, optionValueItemType: type, expectedType: type
    ):
        assert type(optionName) == str
        assert type(optionValueItemType) == type
        assert type(expectedType) == type

        errMsg = (
            "Bad option [{0}] value item type [{1}]. Expected type is [{2}].".format(
                optionName, optionValueItemType.__name__, expectedType.__name__
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CommentTextContainsInvalidSymbols():
        errMsg = "Comment text contains invalid symbols."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileIsAlreadyRegistered(file_path: str):
        errMsg = "File [{0}] is already registered.".format(file_path)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionIsAlreadyExistInThisFile(filePath: str, optionName: str):
        assert type(filePath) == str
        assert type(optionName) == str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in this file [{1}].".format(
            optionName, filePath
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionIsAlreadyExistInAnotherFile(filePath: str, optionName: str):
        assert type(filePath) == str
        assert type(optionName) == str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in another file [{1}].".format(
            optionName, filePath
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionIsAlreadyExistInFile(filePath: str, optionName: str):
        assert type(filePath) == str
        assert type(optionName) == str
        assert filePath != ""
        assert optionName != ""

        errMsg = "Option [{0}] already exist in the file [{1}].".format(
            optionName, filePath
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionValueItemIsAlreadyDefined(filePath: str, optName: str, valueItem: any):
        assert type(filePath) == str
        assert type(optName) == str

        errMsg = "Another definition of option [{1}] value item [{2}] is found in the file [{0}].".format(
            filePath, optName, valueItem
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionValueItemIsAlreadyDefinedInAnotherFile(
        filePath: str, optName: str, valueItem: any
    ):
        assert type(filePath) == str
        assert type(optName) == str

        errMsg = "Definition of option [{1}] value item [{2}] is found in another file [{0}].".format(
            filePath, optName, valueItem
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def UnknownFileName(fileName: str):
        assert type(fileName) == str

        errMsg = "Unknown file name [{0}].".format(fileName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def MultipleDefOfFileIsFound(fileName: str, count: int):
        assert type(fileName) == str
        assert type(count) == int

        errMsg = "Multiple definitition of file [{0}] is found - {1}.".format(
            fileName, count
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FilePathIsEmpty():
        errMsg = "File path is empty."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileWasModifiedExternally(
        filePath: str,
        ourLastMDate: datetime.datetime,
        curLastMDate: datetime.datetime,
    ):
        assert type(filePath) == str
        assert type(ourLastMDate) == datetime.datetime
        assert type(curLastMDate) == datetime.datetime

        errMsg = "File [{0}] was modified externally. Our timestamp is [{1}]. The current file timestamp is [{2}].".format(
            filePath, ourLastMDate, curLastMDate
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileLineAlreadyHasComment():
        errMsg = "File line already has a comment."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileLineAlreadyHasOption(optionName: str):
        assert type(optionName) == str

        errMsg = "File line already has the option [{0}].".format(optionName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileLineAlreadyHasIncludeDirective():
        errMsg = "File line already has an include directive."

        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__UnexpectedSymbol(lineNum: int, colNum: int, ch: str):
        assert type(lineNum) == int
        assert type(colNum) == int
        assert type(ch) == str

        errMsg = "Unexpected symbol in line {0}, column {1}: [{2}]".format(
            lineNum, colNum, ch
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__IncludeWithoutPath(lineNum: int):
        assert type(lineNum) == int
        assert lineNum >= 0

        errMsg = "Include directive in line {0} does not have a path.".format(lineNum)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__EndOfIncludePathIsNotFound(lineNum: int):
        assert type(lineNum) == int
        assert lineNum >= 0

        errMsg = "The end of an include path is not found. Line {0}.".format(lineNum)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__IncompletedEscapeInInclude(lineNum: int):
        assert type(lineNum) == int
        assert lineNum >= 0

        errMsg = "Escape in an include path is not completed. Line {0}.".format(lineNum)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__UnknownEscapedSymbolInInclude(lineNum: int, colNum: int, ch: str):
        assert type(lineNum) == int
        assert type(colNum) == int
        assert type(ch) == str
        assert lineNum >= 0
        assert colNum >= 0
        assert ch != ""

        errMsg = "Unknown escape symbol [{2}] in an include path. Line {0}. Column {1}.".format(
            lineNum, colNum, ch
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__IncludeHasEmptyPath(lineNum: int):
        assert type(lineNum) == int
        assert lineNum >= 0

        errMsg = "Include in line {0} has an empty path.".format(lineNum)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__OptionWithoutValue(optionName: str, lineNum: int):
        assert type(lineNum) == int
        assert type(optionName) == str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Option [{0}] in line {1} does not have a value.".format(
            optionName, lineNum
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__EndQuotedOptionValueIsNotFound(optionName: str, lineNum: int):
        assert type(lineNum) == int
        assert type(optionName) == str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Value of quoted option [{0}] is not completed. Line {1}.".format(
            optionName, lineNum
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__IncompletedEscapeInQuotedOptionValue(optionName: str, lineNum: int):
        assert type(lineNum) == int
        assert type(optionName) == str
        assert lineNum >= 0
        assert optionName != ""

        errMsg = "Escape in a value of quoted option [{0}] is not completed. Line {1}.".format(
            optionName, lineNum
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
        optionName: str, lineNum: int, colNum: int, ch: str
    ):
        assert type(lineNum) == int
        assert type(optionName) == str
        assert type(ch) == str
        assert lineNum >= 0
        assert optionName != ""
        assert ch != ""

        errMsg = "Unknown escape symbol [{3}] in a value of quoted option [{0}]. Line {1}. Column {2}.".format(
            optionName, lineNum, colNum, ch
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def BadFormatOfCommaSeparatedList():
        errMsg = "Bad format of comma separated list."
        raise Exception(errMsg)


# //////////////////////////////////////////////////////////////////////////////
