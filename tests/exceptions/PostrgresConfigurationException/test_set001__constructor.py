from src.exceptions import PostgresConfigException


class TestSet001_Constructor:
    def test_001_positional_args_000(self):
        e = PostgresConfigException()
        assert e.message == ""
        assert e.source is None
        assert str(e) == ""
        return

    def test_001_positional_args_001__arg1(self):
        e = PostgresConfigException("abcdef")
        assert e.message == "abcdef"
        assert e.source is None
        assert str(e) == "abcdef"
        assert repr(e) == "PostgresConfigException('abcdef')"
        return

    def test_001_positional_args_002__arg1_arg2(self):
        e = PostgresConfigException("abc123", "mysource")
        assert e.message == "('abc123', 'mysource')"
        assert e.source is None
        assert str(e) == "('abc123', 'mysource')"
        assert repr(e) == "PostgresConfigException('abc123', 'mysource')"
        return
