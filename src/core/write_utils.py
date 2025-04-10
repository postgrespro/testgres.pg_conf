# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.


# //////////////////////////////////////////////////////////////////////////////
# class WriteUtils


class WriteUtils:
    def Pack_StrList2(strList: list) -> str:
        assert strList is not None
        assert type(strList) == list

        result = ""
        sep = ""

        index = set[str]()

        for x in strList:
            assert x is not None
            assert type(x) == str

            v = str(x)

            if v in index:
                continue

            index.add(v)

            result += sep
            result += __class__.Helper__PackStrListItem2(str(x))
            sep = ","

        return result

    # --------------------------------------------------------------------
    def Pack_Str(text: str) -> str:
        assert text is not None
        assert type(text) == str

        result = "'"

        for ch in text:
            if ch == "\0":
                result += "\\000"
            elif ch == "'":  # SINGLE QUOTE
                result += "\\'"
            elif ch == "\b":
                result += "\\b"
            elif ch == "\f":
                result += "\\f"
            elif ch == "\n":
                result += "\\n"
            elif ch == "\r":
                result += "\\r"
            elif ch == "\t":
                result += "\\t"
            elif ch == "\\":
                result += "\\\\"
            else:
                result += ch

        result += "'"

        return result

    # Helper Methods -----------------------------------------------------
    def Helper__PackStrListItem2(itemText: str) -> str:
        assert itemText is not None
        assert type(itemText) == str

        needQuote = __class__.Helper__StrList__DoesItemNeedToQuote(itemText)

        result = ""

        if needQuote:
            result += '"'

        for ch in itemText:
            if ch == '"':  # DOUBLE QUOTE
                assert needQuote
                result += '""'
            else:
                result += ch

        if needQuote:
            result += '"'

        return result

    # --------------------------------------------------------------------
    def Helper__StrList__DoesItemNeedToQuote(itemText: str) -> bool:
        assert itemText is not None
        assert type(itemText) == str

        if itemText == "":
            return True

        for ch in itemText:
            if ch == '"':
                return True
            if ch == " ":
                return True
            if ch == "\t":
                return True
            if ch == ",":
                return True


# //////////////////////////////////////////////////////////////////////////////
