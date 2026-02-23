# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from .raise_error import RaiseError

# //////////////////////////////////////////////////////////////////////////////
# class DataVerificator


class DataVerificator:
    def CheckOptionName(name: str):
        if name is None:
            RaiseError.OptionNameIsNone()

        if type(name) is not str:
            RaiseError.OptionNameHasBadType(type(name))

        if name == "":
            RaiseError.OptionNameIsEmpty()

        # TODO: Add an extended verification of an option name

    # --------------------------------------------------------------------
    sm_InvalidCommentSymbols: str = "\n\r\0"

    # --------------------------------------------------------------------
    def IsValidCommentText(text: str) -> bool:
        assert text is not None
        assert type(text) is str

        assert type(__class__.sm_InvalidCommentSymbols) is str

        for ch in text:
            if ch in __class__.sm_InvalidCommentSymbols:
                return False

        return True

    # --------------------------------------------------------------------
    def CheckCommentText(text: str):
        assert text is not None
        assert type(text) is str

        assert type(__class__.sm_InvalidCommentSymbols) is str

        if not __class__.IsValidCommentText(text):
            RaiseError.CommentTextContainsInvalidSymbols()

        # OK

    # --------------------------------------------------------------------
    def CheckStringOfFilePath(text: str):
        assert text is not None
        assert type(text) is str

        if text == "":
            RaiseError.FilePathIsEmpty()


# //////////////////////////////////////////////////////////////////////////////
