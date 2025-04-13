# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.


# //////////////////////////////////////////////////////////////////////////////
# BugCheckError


class BugCheckError:
    def UnkObjectDataType(objectType: type):
        assert objectType is not None
        assert type(objectType) == type

        errMsg = "[BUG CHECK] Unknown object data type [{0}].".format(objectType)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def MultipleDefOfOptionIsFound(optName: str, count: int):
        assert type(optName) == str
        assert type(count) == int

        errMsg = (
            "[BUG CHECK] Multiple definitition of option [{0}] is found - {1}.".format(
                optName, count
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def UnkOptObjectDataType(optName: str, optDataType: type):
        assert type(optName) == str
        assert type(optDataType) == type

        errMsg = (
            "[BUG CHECK] Unknown type of the option object data [{0}] - {1}.".format(
                optName, optDataType.__name__
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def MultipleDefOfFileIsFound(fileName: str, count: int):
        assert type(fileName) == str
        assert type(count) == int

        errMsg = (
            "[BUG CHECK] Multiple definitition of file [{0}] is found - {1}.".format(
                fileName, count
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def UnkFileObjectDataType(fileName: str, fileDataType: type):
        assert type(fileName) == str
        assert type(fileDataType) == type

        errMsg = "[BUG CHECK] Unknown type of the file object data [{0}] - {1}.".format(
            fileName, fileDataType.__name__
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def UnkFileDataStatus(filePath: str, fileStatus: any):
        assert type(filePath) == str
        assert fileStatus is not None

        errMsg = "[BUG CHECK] Unknown file data status [{0}] - {1}.".format(
            filePath, fileStatus
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileIsNotFoundInIndex(fileKey: str, filePath: str):
        assert type(fileKey) == str
        assert type(filePath) == str

        errMsg = "[BUG CHECK] File [{0}][{1}] is not found in index.".format(
            fileKey, filePath
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionIsNotFoundInIndex(optName: str):
        assert type(optName) == str

        errMsg = "[BUG CHECK] Option [{0}] is not found in index.".format(optName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionIsNotFoundInFileLine(optName: str):
        assert type(optName) == str

        errMsg = "[BUG CHECK] Option [{0}] is not found in file line.".format(optName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def CommentIsNotFoundInFileLine():
        errMsg = "[BUG CHECK] Comment is not found in file line."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def IncludeIsNotFoundInFileLine():
        errMsg = "[BUG CHECK] Include is not found in file line."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def FileLineIsNotFoundInFile():
        errMsg = "[BUG CHECK] FileLine is not found in file."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToPrepareSetValueIsNotDefined(name: str):
        assert type(name) == str

        errMsg = "[BUG CHECK] OptionHandlerToPrepareSetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToPrepareGetValueIsNotDefined(name: str):
        assert type(name) == str

        errMsg = "[BUG CHECK] OptionHandlerToPrepareGetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToPrepareSetValueItemIsNotDefined(name: str):
        assert type(name) == str

        errMsg = "[BUG CHECK] OptionHandlerToPrepareSetValueItem for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToSetValueIsNotDefined(name: str):
        assert type(name) == str

        errMsg = "[BUG CHECK] OptionHandlerToSetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToGetValueIsNotDefined(name: str):
        assert type(name) == str

        errMsg = "[BUG CHECK] OptionHandlerToGetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToAddOptionIsNotDefined(name: str):
        assert type(name) == str

        errMsg = (
            "[BUG CHECK] OptionHandlerToAddOption for [{0}] is not defined.".format(
                name
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToSetValueItemIsNotDefined(name: str):
        assert type(name) == str

        errMsg = (
            "[BUG CHECK] OptionHandlerToSetValueItem for [{0}] is not defined.".format(
                name
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def OptionHandlerToWriteIsNotDefined(name: str):
        assert type(name) == str

        errMsg = "[BUG CHECK] OptionHandlerToWrite for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def UnexpectedSituation(bugcheckSrc: str, bugcheckPoint: str, explain: str):
        assert type(bugcheckSrc) == str
        assert type(bugcheckPoint) == str
        assert explain is None or type(explain) == str

        errMsg = "[BUG CHECK] Unexpected situation in [{0}][{1}].".format(
            bugcheckSrc, bugcheckPoint
        )

        if not (explain is None) and explain != "":
            errMsg += " "
            errMsg += explain

        assert errMsg[-1] == "."

        raise Exception(errMsg)

    # --------------------------------------------------------------------
    def UnknownOptionValueType(optionName: str, typeOfOptionValue: type):
        assert type(optionName) == str
        assert optionName != ""
        assert type(typeOfOptionValue) == type

        errMsg = "[BUG CHECK] Unknown value type [{1}] of option [{0}].".format(
            optionName, typeOfOptionValue.__name__
        )

        raise Exception(errMsg)


# //////////////////////////////////////////////////////////////////////////////
