# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

import typing

# //////////////////////////////////////////////////////////////////////////////
# BugCheckError


class BugCheckError:
    @staticmethod
    def UnkObjectDataType(
        objectType: type,
    ) -> typing.NoReturn:
        assert objectType is not None
        assert type(objectType) is type

        errMsg = "[BUG CHECK] Unknown object data type [{0}].".format(objectType)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfOptionIsFound(
        optName: str,
        count: int,
    ) -> typing.NoReturn:
        assert type(optName) is str
        assert type(count) is int

        errMsg = (
            "[BUG CHECK] Multiple definitition of option [{0}] is found - {1}.".format(
                optName, count
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnkOptObjectDataType(
        optName: str,
        optDataType: type,
    ) -> typing.NoReturn:
        assert type(optName) is str
        assert type(optDataType) is type

        errMsg = (
            "[BUG CHECK] Unknown type of the option object data [{0}] - {1}.".format(
                optName, optDataType.__name__
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfFileIsFound(
        fileName: str,
        count: int,
    ) -> typing.NoReturn:
        assert type(fileName) is str
        assert type(count) is int

        errMsg = (
            "[BUG CHECK] Multiple definitition of file [{0}] is found - {1}.".format(
                fileName, count
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnkFileObjectDataType(
        fileName: str,
        fileDataType: type,
    ) -> typing.NoReturn:
        assert type(fileName) is str
        assert type(fileDataType) is type

        errMsg = "[BUG CHECK] Unknown type of the file object data [{0}] - {1}.".format(
            fileName, fileDataType.__name__
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnkFileDataStatus(
        filePath: str,
        fileStatus: typing.Any,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert fileStatus is not None

        errMsg = "[BUG CHECK] Unknown file data status [{0}] - {1}.".format(
            filePath, fileStatus
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def FileIsNotFoundInIndex(
        fileKey: str,
        filePath: str,
    ) -> typing.NoReturn:
        assert type(fileKey) is str
        assert type(filePath) is str

        errMsg = "[BUG CHECK] File [{0}][{1}] is not found in index.".format(
            fileKey, filePath
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsNotFoundInIndex(
        optName: str,
    ) -> typing.NoReturn:
        assert type(optName) is str

        errMsg = "[BUG CHECK] Option [{0}] is not found in index.".format(optName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsNotFoundInFileLine(
        optName: str,
    ) -> typing.NoReturn:
        assert type(optName) is str

        errMsg = "[BUG CHECK] Option [{0}] is not found in file line.".format(optName)
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def CommentIsNotFoundInFileLine() -> typing.NoReturn:
        errMsg = "[BUG CHECK] Comment is not found in file line."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def IncludeIsNotFoundInFileLine() -> typing.NoReturn:
        errMsg = "[BUG CHECK] Include is not found in file line."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineIsNotFoundInFile() -> typing.NoReturn:
        errMsg = "[BUG CHECK] FileLine is not found in file."
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToPrepareSetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "[BUG CHECK] OptionHandlerToPrepareSetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToPrepareGetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "[BUG CHECK] OptionHandlerToPrepareGetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToPrepareSetValueItemIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "[BUG CHECK] OptionHandlerToPrepareSetValueItem for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToSetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "[BUG CHECK] OptionHandlerToSetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToGetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "[BUG CHECK] OptionHandlerToGetValue for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToAddOptionIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = (
            "[BUG CHECK] OptionHandlerToAddOption for [{0}] is not defined.".format(
                name
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToSetValueItemIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = (
            "[BUG CHECK] OptionHandlerToSetValueItem for [{0}] is not defined.".format(
                name
            )
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToWriteIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "[BUG CHECK] OptionHandlerToWrite for [{0}] is not defined.".format(
            name
        )
        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnexpectedSituation(
        bugcheckSrc: str,
        bugcheckPoint: str,
        explain: str,
    ) -> typing.NoReturn:
        assert type(bugcheckSrc) is str
        assert type(bugcheckPoint) is str
        assert explain is None or type(explain) is str

        errMsg = "[BUG CHECK] Unexpected situation in [{0}][{1}].".format(
            bugcheckSrc, bugcheckPoint
        )

        if explain is not None and explain != "":
            errMsg += " "
            errMsg += explain

        assert errMsg[-1] == "."

        raise Exception(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnknownOptionValueType(
        optionName: str,
        typeOfOptionValue: type,
    ) -> typing.NoReturn:
        assert type(optionName) is str
        assert optionName != ""
        assert type(typeOfOptionValue) is type

        errMsg = "[BUG CHECK] Unknown value type [{1}] of option [{0}].".format(
            optionName, typeOfOptionValue.__name__
        )

        raise Exception(errMsg)


# //////////////////////////////////////////////////////////////////////////////
