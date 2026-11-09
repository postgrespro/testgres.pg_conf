# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from src.core.raise_error import RaiseError
from src.core.raise_error import PostgresConfigException
from tests.ErrorMessageBuilder import ErrorMessageBuilder

import pytest
import datetime

# //////////////////////////////////////////////////////////////////////////////
# class TestFor_RaiseError


class TestFor_RaiseError:
    def test_MethodIsNotImplemented(self):
        with pytest.raises(expected_exception=NotImplementedError) as x:
            RaiseError.MethodIsNotImplemented(
                TestFor_RaiseError,
                "a",
            )
        assert str(x.value) == ErrorMessageBuilder.MethodIsNotImplemented(
            TestFor_RaiseError,
            "a",
        )
        return

    # --------------------------------------------------------------------
    def test_GetPropertyIsNotImplemented(self):
        with pytest.raises(expected_exception=NotImplementedError) as x:
            RaiseError.GetPropertyIsNotImplemented(
                TestFor_RaiseError,
                "a",
            )

        expectedMsg = ErrorMessageBuilder.GetPropertyIsNotImplemented(
            TestFor_RaiseError,
            "a",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_OptionNameIsNone(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionNameIsNone()

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsNone()
        return

    # --------------------------------------------------------------------
    def test_OptionNameHasBadType(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionNameHasBadType(int)

        assert str(x.value) == ErrorMessageBuilder.OptionNameHasBadType(int)
        return

    # --------------------------------------------------------------------
    def test_OptionNameIsEmpty(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionNameIsEmpty()

        assert str(x.value) == ErrorMessageBuilder.OptionNameIsEmpty()
        return

    # --------------------------------------------------------------------
    def test_NoneValueIsNotSupported(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.NoneValueIsNotSupported()

        assert str(x.value) == ErrorMessageBuilder.NoneValueIsNotSupported()
        return

    # --------------------------------------------------------------------
    def test_NoneOptionValueItemIsNotSupported(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.NoneOptionValueItemIsNotSupported(
                "a",
            )

        expectedMsg = ErrorMessageBuilder.NoneOptionValueItemIsNotSupported(
            "a",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CommentObjectWasDeleted(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CommentObjectWasDeleted()

        assert str(x.value) == ErrorMessageBuilder.CommentObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_OptionObjectWasDeleted(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionObjectWasDeleted()

        assert str(x.value) == ErrorMessageBuilder.OptionObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_IncludeObjectWasDeleted(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.IncludeObjectWasDeleted()

        assert str(x.value) == ErrorMessageBuilder.IncludeObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_FileLineObjectWasDeleted(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileLineObjectWasDeleted()

        assert str(x.value) == ErrorMessageBuilder.FileLineObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_FileObjectWasDeleted(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileObjectWasDeleted()

        assert str(x.value) == ErrorMessageBuilder.FileObjectWasDeleted()
        return

    # --------------------------------------------------------------------
    def test_BadOptionValueType(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.BadOptionValueType(
                "aa",
                int,
                str,
            )

        expectedMsg = ErrorMessageBuilder.BadOptionValueType(
            "aa",
            int,
            str,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CantConvertOptionValue(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CantConvertOptionValue(
                "aa",
                int,
                str,
            )

        expectedMsg = ErrorMessageBuilder.CantConvertOptionValue(
            "aa",
            int,
            str,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_BadOptionValueItemType(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.BadOptionValueItemType(
                "aa",
                int,
                str,
            )

        expectedMsg = ErrorMessageBuilder.BadOptionValueItemType(
            "aa",
            int,
            str,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CommentTextContainsInvalidSymbols(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CommentTextContainsInvalidSymbols()

        assert str(x.value) == ErrorMessageBuilder.CommentTextContainsInvalidSymbols()
        return

    # --------------------------------------------------------------------
    def test_FileIsAlreadyRegistered(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileIsAlreadyRegistered(
                "ppp",
            )

        expectedMsg = ErrorMessageBuilder.FileIsAlreadyRegistered(
            "ppp",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_OptionIsAlreadyExistInAnotherFile(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionIsAlreadyExistInAnotherFile(
                "fff",
                "ppp",
            )

        expectedMsg = ErrorMessageBuilder.OptionIsAlreadyExistInAnotherFile(
            "fff",
            "ppp",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_OptionIsAlreadyExistInFile(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionIsAlreadyExistInFile(
                "fff",
                "ppp",
            )

        expectedMsg = ErrorMessageBuilder.OptionIsAlreadyExistInFile(
            "fff",
            "ppp",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_OptionValueItemIsAlreadyDefined(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionValueItemIsAlreadyDefined(
                "fff",
                "ppp",
                "vvv",
            )

        expectedMsg = ErrorMessageBuilder.OptionValueItemIsAlreadyDefined(
            "fff",
            "ppp",
            "vvv",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_OptionValueItemIsAlreadyDefinedInAnotherFile(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.OptionValueItemIsAlreadyDefinedInAnotherFile(
                "fff",
                "ppp",
                "vvv",
            )

        expectedMsg = ErrorMessageBuilder.OptionValueItemIsAlreadyDefinedInAnotherFile(
            "fff",
            "ppp",
            "vvv",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_UnknownFileName(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.UnknownFileName(
                "fff",
            )

        expectedMsg = ErrorMessageBuilder.UnknownFileName(
            "fff",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_MultipleDefOfFileIsFound(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.MultipleDefOfFileIsFound(
                "fff",
                3,
            )

        expectedMsg = ErrorMessageBuilder.MultipleDefOfFileIsFound(
            "fff",
            3,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_FilePathIsEmpty(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FilePathIsEmpty()

        assert str(x.value) == ErrorMessageBuilder.FilePathIsEmpty()
        return

    # --------------------------------------------------------------------
    def test_FileWasModifiedExternally(self):
        ts1 = datetime.datetime.now()
        ts2 = datetime.datetime.today()

        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileWasModifiedExternally(
                "fff",
                ts1,
                ts2,
            )

        expectedMsg = ErrorMessageBuilder.FileWasModifiedExternally(
            "fff",
            ts1,
            ts2,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_FileLineAlreadyHasComment(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileLineAlreadyHasComment()

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasComment()
        return

    # --------------------------------------------------------------------
    def test_FileLineAlreadyHasOption(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileLineAlreadyHasOption(
                "pp1",
            )

        expectedMsg = ErrorMessageBuilder.FileLineAlreadyHasOption(
            "pp1",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_FileLineAlreadyHasIncludeDirective(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.FileLineAlreadyHasIncludeDirective()

        assert str(x.value) == ErrorMessageBuilder.FileLineAlreadyHasIncludeDirective()
        return

    # --------------------------------------------------------------------
    def test_CfgReader__UnexpectedSymbol(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__UnexpectedSymbol(
                1,
                2,
                "a",
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__UnexpectedSymbol(
            1,
            2,
            "a",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__IncludeWithoutPath(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__IncludeWithoutPath(
                123,
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__IncludeWithoutPath(
            123,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__EndOfIncludePathIsNotFound(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__EndOfIncludePathIsNotFound(
                1234,
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__EndOfIncludePathIsNotFound(
            1234,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__IncompletedEscapeInInclude(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__IncompletedEscapeInInclude(
                1234,
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__IncompletedEscapeInInclude(
            1234,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__UnknownEscapedSymbolInInclude(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__UnknownEscapedSymbolInInclude(
                1,
                2,
                "a",
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__UnknownEscapedSymbolInInclude(
            1,
            2,
            "a",
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__IncludeHasEmptyPath(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__IncludeHasEmptyPath(
                1234,
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__IncludeHasEmptyPath(
            1234,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__OptionWithoutValue(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__OptionWithoutValue(
                "pp1",
                1234,
            )

        assert str(x.value) == ErrorMessageBuilder.CfgReader__OptionWithoutValue(
            "pp1",
            1234,
        )
        return

    # --------------------------------------------------------------------
    def test_CfgReader__EndQuotedOptionValueIsNotFound(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__EndQuotedOptionValueIsNotFound(
                "pp1",
                1234,
            )

        expectedMsg = ErrorMessageBuilder.CfgReader__EndQuotedOptionValueIsNotFound(
            "pp1",
            1234,
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__IncompletedEscapeInQuotedOptionValue(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__IncompletedEscapeInQuotedOptionValue(
                "pp1",
                1234,
            )

        expectedMsg = (
            ErrorMessageBuilder.CfgReader__IncompletedEscapeInQuotedOptionValue(
                "pp1",
                1234,
            )
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_CfgReader__UnknownEscapedSymbolInQuotedOptionValue(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
                "pp1",
                1234,
                31,
                "v",
            )

        expectedMsg = (
            ErrorMessageBuilder.CfgReader__UnknownEscapedSymbolInQuotedOptionValue(
                "pp1",
                1234,
                31,
                "v",
            )
        )

        assert str(x.value) == expectedMsg
        return

    # --------------------------------------------------------------------
    def test_BadFormatOfCommaSeparatedList(self):
        with pytest.raises(expected_exception=PostgresConfigException) as x:
            RaiseError.BadFormatOfCommaSeparatedList()

        assert str(x.value) == ErrorMessageBuilder.BadFormatOfCommaSeparatedList()
        return


# //////////////////////////////////////////////////////////////////////////////
