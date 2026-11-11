# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations
import typing

# //////////////////////////////////////////////////////////////////////////////

T = typing.TypeVar("T")


# //////////////////////////////////////////////////////////////////////////////
# MultiIndex


class MultiIndexIterator(typing.Iterator[T]):
    m_DataIterator: typing.Iterator[typing.Union[T, typing.List[T]]]

    m_CurrentList: typing.Optional[typing.List[T]]
    m_CurrentIndex: int

    # --------------------------------------------------------------------
    def __init__(
        self,
        dataIterator: typing.Iterator[typing.Union[T, typing.List[T]]],
        currentList: typing.Optional[typing.List[T]] = None,
        currentIndex: int = 0,
    ):
        assert dataIterator is not None
        assert isinstance(dataIterator, typing.Iterator)
        assert currentList is None or type(currentList) is list
        assert type(currentIndex) is int
        assert currentList is None or currentIndex <= len(currentList)

        self.m_DataIterator = dataIterator
        self.m_CurrentList = currentList
        self.m_CurrentIndex = currentIndex
        return

    # interface ----------------------------------------------------------
    def __iter__(self) -> MultiIndexIterator[T]:
        assert self.m_DataIterator is not None
        assert isinstance(self.m_DataIterator, typing.Iterator)

        it = self.m_DataIterator.__iter__()
        assert it is not None
        assert isinstance(it, typing.Iterator)

        if it is self.m_DataIterator:
            return self

        return __class__(
            it,
            self.m_CurrentList,
            self.m_CurrentIndex,
        )

    # --------------------------------------------------------------------
    def __next__(self) -> T:
        assert self.m_DataIterator is not None
        assert isinstance(self.m_DataIterator, typing.Iterator)

        while True:
            if self.m_CurrentList is not None:
                assert self.m_CurrentIndex <= len(self.m_CurrentList)

                if self.m_CurrentIndex != len(self.m_CurrentList):
                    data = self.m_CurrentList[self.m_CurrentIndex]
                    self.m_CurrentIndex += 1
                    return data

                self.m_CurrentList = None
                self.m_CurrentIndex = 0

            assert self.m_CurrentList is None
            assert self.m_CurrentIndex == 0

            raw_data = self.m_DataIterator.__next__()

            if isinstance(raw_data, list):
                assert len(raw_data) > 1
                self.m_CurrentList = raw_data
                continue

            return raw_data


# //////////////////////////////////////////////////////////////////////////////
# MultiIndex


class MultiIndex(typing.Generic[T]):
    T_ITERATOR = MultiIndexIterator

    # --------------------------------------------------------------------
    m_dict: typing.Dict[str, typing.Union[T, typing.List[T]]]
    m_count: int

    # --------------------------------------------------------------------
    def __init__(self) -> None:
        self.m_dict = {}
        self.m_count = 0
        return

    # --------------------------------------------------------------------
    def add(self, key: str, value: T) -> None:
        """Add an entity to the index. Supports duplicates under the same key."""
        assert type(key) is str
        assert value is not None

        if key not in self.m_dict:
            self.m_dict[key] = value
        else:
            existing = self.m_dict[key]
            if isinstance(existing, list):
                existing.append(value)
            else:
                self.m_dict[key] = [existing, value]

        self.m_count += 1
        return

    # --------------------------------------------------------------------
    def remove_exact(self, key: str, value: T) -> bool:
        """Remove a specific entity instance from the index
           (e.g., when deleting a single line).

        Returns:
            bool: True if removed successfully, False if not found.
        """
        assert type(key) is str
        assert value is not None

        if key not in self.m_dict:
            return False

        data = self.m_dict[key]

        if isinstance(data, list):
            i = 0

            c = len(data)

            while i != c:
                assert i < c

                if data[i] is value:
                    break

                i += 1
                continue

            if i == c:
                return False

            assert self.m_count > 0

            data.pop(i)

            if len(data) == 1:
                self.m_dict[key] = data[0]
            elif len(data) == 0:
                self.m_dict.pop(key)

            self.m_count -= 1
            return True

        if data is value:
            assert self.m_count > 0
            del self.m_dict[key]
            self.m_count -= 1
            return True

        return False

    # --------------------------------------------------------------------
    def keys(self) -> typing.Iterable[str]:
        return self.m_dict.keys()

    # --------------------------------------------------------------------
    def elements(self) -> typing.Iterable[T]:
        return __class__.T_ITERATOR(
            self.m_dict.values().__iter__(),
        )

    # --------------------------------------------------------------------
    def get_elements_count(self) -> int:
        assert type(self.m_count) is int
        assert self.m_count >= 0
        assert len(self.m_dict) <= self.m_count
        return self.m_count

    # --------------------------------------------------------------------
    def __getitem__(self, key: str) -> typing.Union[T, typing.List[T]]:
        """Bracket syntax access: index[key].

        Returns the raw stored value (either a single entity or a list of duplicates).
        Raises KeyError if the key is not found, mirroring standard dict behavior.
        """
        assert type(key) is str
        return self.m_dict[key]


# //////////////////////////////////////////////////////////////////////////////
