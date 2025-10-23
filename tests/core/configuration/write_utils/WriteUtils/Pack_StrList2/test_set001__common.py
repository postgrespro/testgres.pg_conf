# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from src.core.write_utils import WriteUtils

import pytest

# //////////////////////////////////////////////////////////////////////////////
# TestSet001__Common


class TestSet001__Common:
    def test_001__empty(self):
        assert WriteUtils.Pack_StrList2(list[str]()) == ""

    # --------------------------------------------------------------------
    class tagData002:
        descr: str
        source: list[str]
        result: str

        def __init__(self, d: str, s: list[str], r: str):
            assert type(d) == str
            assert type(s) == list
            assert type(r) == str

            self.descr = d
            self.source = s
            self.result = r

    # --------------------------------------------------------------------
    sm_Data002 = [
        # fmt: off
        tagData002(
            "empty",
            [],
            ""
        ),
        tagData002(
            "empty_str",
            [""],
            "\"\""
        ),
        tagData002(
            "quoted_space",
            [" "],
            "\" \""
        ),
        tagData002(
            "new_line",
            ["\n"],
            "\n"
        ),
        tagData002(
            "return_caret",
            ["\r"],
            "\r"
        ),
        tagData002(
            "quoted_tab",
            ["\t"],
            "\"\t\""
        ),
        tagData002(
            "quote",
            ["\'"],
            "\'"
        ),
        tagData002(
            "double_quote",
            ["\""],
            "\"\"\"\""
        ),
        tagData002(
            "comma",
            [","],
            "\",\""
        ),
        tagData002(
            "zero",
            ["\0"],
            "\0"
        ),
        tagData002(
            "abc_and_zero",
            ["abc\0"],
            "abc\0"
        ),
        tagData002(
            "quote_abc_and_zero",
            ["'abc\0"],
            "'abc\0"
        ),
        tagData002(
            "double_quote_abc_and_zero",
            ["\"abc\0"],
            "\"\"\"abc\0\""
        ),
        tagData002(
            "space_aaa_space",
            [" aaa "],
            "\" aaa \""
        ),
        tagData002(
            "two_items",
            ["biha", "proxima"],
            "biha,proxima"
        ),
        tagData002(
            "mix001",
            ["biha,", " p\nroxima"],
            "\"biha,\",\" p\nroxima\""
        ),
        tagData002(
            "mix002",
            ["\"biha,\"", "\" p\nroxima", "", "   "],
            "\"\"\"biha,\"\"\",\"\"\" p\nroxima\",\"\",\"   \""
        ),
        tagData002(
            "check_unique",
            ["a", "a", "a", "b", "a", "c", "d", "a"],
            "a,b,c,d"
        ),
        # fmt: on
    ]

    # --------------------------------------------------------------------
    @pytest.fixture(params=sm_Data002, ids=[x.descr for x in sm_Data002])
    def data002(self, request: pytest.FixtureRequest) -> tagData002:
        assert isinstance(request, pytest.FixtureRequest)
        assert type(request.param) == __class__.tagData002
        return request.param

    # --------------------------------------------------------------------
    def test_002__generic(self, data002: tagData002):
        assert type(data002) == __class__.tagData002

        assert WriteUtils.Pack_StrList2(data002.source) == data002.result


# //////////////////////////////////////////////////////////////////////////////
