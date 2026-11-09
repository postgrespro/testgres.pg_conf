from src.exceptions import PostgresConfigExceptionBase


class TestSet002__usage:
    def test_001__str_and_repr(self):
        class EEE(PostgresConfigExceptionBase):
            @property
            def message(self) -> str:
                return "EEE!\neee?"

        e = EEE("abc321\n123cba")
        assert isinstance(e, PostgresConfigExceptionBase)
        assert e.message == "EEE!\neee?"
        assert e.source is None
        assert str(e) == "EEE!\neee?"
        # It a default implementation
        assert repr(e) == "EEE('abc321\\n123cba')"
        return

    def test_002__str_and_repr(self):
        class EEE(PostgresConfigExceptionBase):
            def __init__(self):
                super().__init__("zxc", "321")
                return

            @property
            def message(self) -> str:
                return "EEE!\neee?"

        e = EEE()
        assert isinstance(e, PostgresConfigExceptionBase)
        assert e.message == "EEE!\neee?"
        assert e.source is None
        assert str(e) == "EEE!\neee?"
        # It a default implementation
        assert repr(e) == "EEE('zxc', '321')"
        return
