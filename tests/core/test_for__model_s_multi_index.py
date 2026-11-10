# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library. Tests.

from src.core.model_s_multi_index import MultiIndex

import typing

# //////////////////////////////////////////////////////////////////////////////
# TestFor_MultiIndex


class TestFor_MultiIndex:
    def test_000__constructor(self):
        x: MultiIndex[int] = MultiIndex()

        assert x.get_values_count() == 0
        assert "x" not in x.keys()

        assert list(x.values()) == []
        return

    # --------------------------------------------------------------------
    def test_001__add(self):
        x: MultiIndex[int] = MultiIndex()

        assert x.get_values_count() == 0
        assert "x" not in x.keys()
        assert list(x.values()) == []

        x.add("a", 1)
        assert x.get_values_count() == 1
        assert "a" in x.keys()
        assert "a1" not in x.keys()
        assert list(x.values()) == [1]

        x.add("a", 2)
        assert x.get_values_count() == 2
        assert "a" in x.keys()
        assert "a1" not in x.keys()
        assert list(x.values()) == [1, 2]

        x.add("b", 2)
        assert x.get_values_count() == 3
        assert "a" in x.keys()
        assert "b" in x.keys()
        assert "a1" not in x.keys()
        assert list(x.values()) == [1, 2, 2]
        return

    # --------------------------------------------------------------------
    def test_002__remove_exact(self):
        x: MultiIndex[int] = MultiIndex()

        assert x.get_values_count() == 0
        assert "x" not in x.keys()
        assert list(x.values()) == []

        assert not x.remove_exact("a", 1)

        assert x.get_values_count() == 0
        assert "x" not in x.keys()
        assert list(x.values()) == []
        return

    # --------------------------------------------------------------------
    def test_003__remove_exact(self):
        x: MultiIndex[int] = MultiIndex()

        assert x.get_values_count() == 0
        assert "x" not in x.keys()
        assert list(x.values()) == []

        x.add("a", 1)
        assert x.get_values_count() == 1
        assert "a" in x.keys()
        assert "a1" not in x.keys()
        assert list(x.values()) == [1]

        assert x.remove_exact("a", 1)

        assert x.get_values_count() == 0
        assert "x" not in x.keys()
        assert list(x.values()) == []
        return

    # --------------------------------------------------------------------
    T_STR_INT = typing.Tuple[str, int]

    # --------------------------------------------------------------------
    T_DICT_STR_INT = typing.Dict[str, typing.Union[int, typing.List[int]]]

    # --------------------------------------------------------------------
    @staticmethod
    def helper__add_to_dict(
        d: T_DICT_STR_INT,
        v: T_STR_INT,
    ) -> None:
        if v[0] not in d:
            d[v[0]] = v[1]
            return

        item = d[v[0]]

        if type(item) is list:
            item.append(v[1])
            return

        assert type(item) is int

        d[v[0]] = [item, v[1]]
        return

    # --------------------------------------------------------------------
    @staticmethod
    def helper__del_from_dict(
        d: T_DICT_STR_INT,
        v: T_STR_INT,
    ) -> None:
        assert v[0] in d

        item = d[v[0]]

        if type(item) is list:
            i = 0

            while True:
                assert i < len(item)

                if v[1] is item[i]:
                    break

                i += 1
                continue

            item.pop(i)

            if len(item) == 0:
                d.pop(v[0])
                return

            if len(item) == 1:
                d[v[0]] = item[0]
                return

            return

        assert item is v[1]

        d.pop(v[0])
        return

    # --------------------------------------------------------------------
    @staticmethod
    def helper__dict_to_all(
        d: T_DICT_STR_INT,
    ) -> typing.List[int]:
        assert type(d) is dict

        r: typing.List[int] = []

        for v in d.values():
            if type(v) is list:
                r.extend(v)
                continue

            assert type(v) is int
            r.append(v)
            continue

        return r

    # --------------------------------------------------------------------
    def test_004__remove_exact(self):
        x: MultiIndex[int] = MultiIndex()

        source: typing.List[__class__.T_STR_INT] = [
            ("a", 1),
            ("b", 2),
            ("a", 3),
            ("b", 4),
            ("a", 5),
            ("b", 6),
            ("a", 7),
            ("b", 8),
        ]

        expected: __class__.T_DICT_STR_INT = dict()

        i = 0
        while i < len(source):
            s = source[i]
            i += 1

            x.add(s[0], s[1])
            __class__.helper__add_to_dict(expected, s)
            assert len(list(x.values())) == i
            assert x.m_dict == expected

            assert list(x.values()) == __class__.helper__dict_to_all(expected)
            continue

        assert x.get_values_count() == len(source)

        i = len(source)
        while i != 0:
            i -= 1
            s = source[i]

            x.remove_exact(s[0], s[1])
            assert x.get_values_count() == i
            assert len(list(x.values())) == i

            __class__.helper__del_from_dict(expected, s)

            assert x.m_dict == expected

            assert list(x.values()) == __class__.helper__dict_to_all(expected)
            continue

        assert x.get_values_count() == 0
        assert list(x.values()) == []
        return


# //////////////////////////////////////////////////////////////////////////////
