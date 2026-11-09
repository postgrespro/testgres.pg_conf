from src.exceptions import PostgresConfigBugCheckException


class TestSet001_Constructor:
    def test_001_positional_args_001__description(self):
        e = PostgresConfigBugCheckException("abcdef\n12345")
        assert e.description == "abcdef\n12345"
        assert e.message == "[BUG CHECK] abcdef\n12345"
        assert e.source is None
        assert str(e) == "[BUG CHECK] abcdef\n12345"
        assert repr(e) == "PostgresConfigBugCheckException('abcdef\\n12345', None)"
        return

    def test_001_positional_args_002__description_source(self):
        e = PostgresConfigBugCheckException("abcdef\n54321", "mysource\n1")
        assert e.description == "abcdef\n54321"
        assert e.message == "[BUG CHECK] abcdef\n54321"
        assert e.source == "mysource\n1"
        assert str(e) == "[BUG CHECK] abcdef\n54321"
        assert (
            repr(e)
            == "PostgresConfigBugCheckException('abcdef\\n54321', 'mysource\\n1')"
        )
        return

    def test_002_named_args_001__source_description(self):
        e = PostgresConfigBugCheckException(source="s", description="m")
        assert e.description == "m"
        assert e.message == "[BUG CHECK] m"
        assert e.source == "s"
        assert str(e) == "[BUG CHECK] m"
        assert repr(e) == "PostgresConfigBugCheckException('m', 's')"
        return
