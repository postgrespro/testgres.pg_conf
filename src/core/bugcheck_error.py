# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from ..exceptions import PostgresConfigBugCheckException

import typing

# //////////////////////////////////////////////////////////////////////////////
# BugCheckError


class BugCheckError:
    @staticmethod
    def UnkObjectDataType(
        objectType: type,
    ) -> typing.NoReturn:
        assert objectType is not None
        assert isinstance(objectType, type)

        errMsg = "Unknown object data type [{0}].".format(
            objectType,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfOptionIsFound(
        optName: str,
        count: int,
    ) -> typing.NoReturn:
        assert type(optName) is str
        assert type(count) is int

        errMsg = "Multiple definitition of option [{0}] is found - {1}.".format(
            optName,
            count,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnkOptObjectDataType(
        optName: str,
        optDataType: type,
    ) -> typing.NoReturn:
        assert type(optName) is str
        assert isinstance(optDataType, type)

        errMsg = "Unknown type of the option object data [{0}] - {1}.".format(
            optName,
            optDataType.__name__,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def MultipleDefOfFileIsFound(
        fileName: str,
        count: int,
    ) -> typing.NoReturn:
        assert type(fileName) is str
        assert type(count) is int

        errMsg = "Multiple definitition of file [{0}] is found - {1}.".format(
            fileName,
            count,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnkFileObjectDataType(
        fileName: str,
        fileDataType: type,
    ) -> typing.NoReturn:
        assert type(fileName) is str
        assert isinstance(fileDataType, type)

        errMsg = "Unknown type of the file object data [{0}] - {1}.".format(
            fileName,
            fileDataType.__name__,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnkFileDataStatus(
        filePath: str,
        fileStatus: typing.Any,
    ) -> typing.NoReturn:
        assert type(filePath) is str
        assert fileStatus is not None

        errMsg = "Unknown file data status [{0}] - {1}.".format(
            filePath,
            fileStatus,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def FileIsNotFoundInIndex(
        fileKey: str,
        filePath: str,
    ) -> typing.NoReturn:
        assert type(fileKey) is str
        assert type(filePath) is str

        errMsg = "File [{0}][{1}] is not found in index.".format(
            fileKey,
            filePath,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def FileIsAlreadyRegistered(
        file_path: str,
    ) -> typing.NoReturn:
        errMsg = "File [{}] is already registered.".format(file_path)

        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsNotFoundInIndex(
        optName: str,
    ) -> typing.NoReturn:
        assert type(optName) is str

        errMsg = "Option [{0}] is not found in index.".format(optName)
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionIsNotFoundInFileLine(
        optName: str,
    ) -> typing.NoReturn:
        assert type(optName) is str

        errMsg = "Option [{0}] is not found in file line.".format(optName)
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def CommentIsNotFoundInFileLine() -> typing.NoReturn:
        errMsg = "Comment is not found in file line."
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def IncludeIsNotFoundInFileLine() -> typing.NoReturn:
        errMsg = "Include is not found in file line."
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def FileLineIsNotFoundInFile() -> typing.NoReturn:
        errMsg = "FileLine is not found in file."
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToPrepareSetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToPrepareSetValue for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToPrepareGetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToPrepareGetValue for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToPrepareSetValueItemIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToPrepareSetValueItem for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToSetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToSetValue for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToGetValueIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToGetValue for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToAddOptionIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToAddOption for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToSetValueItemIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToSetValueItem for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def OptionHandlerToWriteIsNotDefined(
        name: str,
    ) -> typing.NoReturn:
        assert type(name) is str

        errMsg = "OptionHandlerToWrite for [{0}] is not defined.".format(
            name,
        )
        __class__.Helper__Raise(errMsg)

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

        errMsg = "Unexpected situation in [{0}][{1}].".format(
            bugcheckSrc,
            bugcheckPoint,
        )

        if explain is not None and explain != "":
            errMsg += " "
            errMsg += explain

        assert errMsg[-1] == "."

        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnknownOptionValueType(
        optionName: str,
        typeOfOptionValue: type,
    ) -> typing.NoReturn:
        assert type(optionName) is str
        assert optionName != ""
        assert isinstance(typeOfOptionValue, type)

        errMsg = "Unknown value type [{1}] of option [{0}].".format(
            optionName,
            typeOfOptionValue.__name__,
        )

        __class__.Helper__Raise(errMsg)

    # --------------------------------------------------------------------
    @staticmethod
    def UnsupportedPgConfStrategy(
        strategy: typing.Any,
    ) -> typing.NoReturn:

        errMsg = "Unsupported data strategy {!r}.".format(
            strategy,
        )

        __class__.Helper__Raise(errMsg)

    # Helper methods -----------------------------------------------------
    @staticmethod
    def Helper__Raise(msg: str) -> typing.NoReturn:
        assert type(msg) is str
        assert msg != ""
        raise PostgresConfigBugCheckException(msg)


# //////////////////////////////////////////////////////////////////////////////
