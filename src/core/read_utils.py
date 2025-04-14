# //////////////////////////////////////////////////////////////////////////////
# Postgres Pro. PostgreSQL Configuration Python Library.

from __future__ import annotations

from .raise_error import RaiseError

import typing

# //////////////////////////////////////////////////////////////////////////////
# class LineReader


class LineReader:
    C_DEFAULT_TAB_SIZE = 4

    m_TabSize: int

    m_LineNum: int
    m_ColNum: int
    m_Next: int
    m_Data: str

    # --------------------------------------------------------------------
    def __init__(self, tabSize=C_DEFAULT_TAB_SIZE):
        assert type(tabSize) == int
        assert tabSize > 0

        self.m_TabSize = tabSize

        self.m_LineNum = 0
        self.m_ColNum = 0
        self.m_Next = 0
        self.m_Data = 0

    # --------------------------------------------------------------------
    def SetData(self, lineData: str):
        assert type(lineData) == str
        assert type(self.m_LineNum) == int
        assert self.m_LineNum >= 0

        self.m_Data = lineData
        self.m_LineNum += 1
        self.m_ColNum = 0
        self.m_Next = 0

    # --------------------------------------------------------------------
    def GetLineNum(self) -> int:
        assert type(self.m_LineNum) == int
        assert self.m_LineNum >= 0
        return self.m_LineNum

    # --------------------------------------------------------------------
    def GetColNum(self) -> int:
        assert type(self.m_ColNum) == int
        assert self.m_ColNum >= 0
        return self.m_ColNum

    # --------------------------------------------------------------------
    def GetColOffset(self) -> int:
        assert type(self.m_ColNum) == int
        assert self.m_ColNum > 0
        return self.m_ColNum - 1

    # --------------------------------------------------------------------
    def StepBack(self):
        assert type(self.m_Next) == int
        assert type(self.m_ColNum) == int
        assert type(self.m_Data) == str
        assert self.m_Next > 0
        assert self.m_Next <= len(self.m_Data)
        assert self.m_ColNum > 0

        self.m_Next -= 1

        if self.m_Next == 0:
            assert self.m_ColNum == 1
            self.m_ColNum = 0
        else:
            assert self.m_Next > 0
            stepSize = self.Helper__GetStepSize(self.m_Data[self.m_Next - 1])
            assert self.m_ColNum > stepSize
            self.m_ColNum -= stepSize
            assert self.m_ColNum > 0

    # --------------------------------------------------------------------
    def ReadSymbol(self) -> typing.Optional[str]:
        assert type(self.m_Next) == int
        assert type(self.m_ColNum) == int
        assert type(self.m_Data) == str
        assert self.m_Next >= 0
        assert self.m_Next <= len(self.m_Data)

        if self.m_Next == len(self.m_Data):
            return None

        result = self.m_Data[self.m_Next]

        if self.m_Next == 0:
            self.m_ColNum = 1
        else:
            self.m_ColNum += self.Helper__GetStepSize(self.m_Data[self.m_Next - 1])

        self.m_Next += 1

        return result

    # --------------------------------------------------------------------
    def Helper__GetStepSize(self, ch: str) -> int:
        assert type(ch) == str
        assert ch != ""
        assert type(self.m_TabSize) == int
        assert self.m_TabSize > 0

        if ch == "\t":
            return self.m_TabSize

        return 1


# //////////////////////////////////////////////////////////////////////////////
# class ReadUtils


class ReadUtils:
    def IsSpace(ch: str) -> bool:
        assert type(ch) == str

        if ch == " ":
            return True

        if ch == "\t":
            return True

        return False

    # --------------------------------------------------------------------
    def IsEOL(ch: str) -> bool:
        assert type(ch) == str

        if ch == "\n":
            return True

        return False

    # --------------------------------------------------------------------
    def IsValidSeqCh1(ch: str) -> bool:
        assert type(ch) == str

        if ch.isalpha():
            return True

        if ch in "_":
            return True

        return False

    # --------------------------------------------------------------------
    def IsValidSeqCh2(ch: str) -> bool:
        assert type(ch) == str

        if ch.isdigit():
            return True

        return __class__.IsValidSeqCh1(ch)

    # --------------------------------------------------------------------
    def Unpack_StrList2(source: str) -> list[str]:
        assert source is not None
        assert type(source) == str

        C_MODE__NONE = 0
        C_MODE__QSTART = 1
        C_MODE__QEND = 2

        class tagCtx:
            mode: int
            curValueItem: typing.Optional[str]
            dataLength: int
            result: list[str]
            index: set[str]

        ctx = tagCtx()
        ctx.mode = C_MODE__NONE
        ctx.curValueItem = None
        ctx.dataLength = 0
        ctx.result = list[str]()
        ctx.index = set[str]()

        i = 0
        length = len(source)

        # ----------------------------------------------
        def LOCAL__append_to_curValueItem(ctx: tagCtx, ch: str, isData: bool):
            assert type(ctx) == tagCtx
            assert type(ch) == str
            assert len(ch) == 1
            assert type(isData) == bool

            if ctx.curValueItem is None:
                ctx.curValueItem = ch
            else:
                assert type(ctx.curValueItem) == str
                ctx.curValueItem += ch

            if isData:
                ctx.dataLength = len(ctx.curValueItem)

            return

        # ----------------------------------------------
        def LOCAL__append_curValueItem_to_result(ctx: tagCtx, isLast: bool):
            assert type(ctx) == tagCtx

            if ctx.mode == C_MODE__QSTART:
                # quoted item is not completed
                RaiseError.BadFormatOfCommaSeparatedList()

            if ctx.curValueItem is None:
                if isLast and ctx.mode == C_MODE__NONE:
                    return
                s = ""
            elif ctx.mode == C_MODE__QEND:
                s = ctx.curValueItem
            else:
                assert ctx.mode == C_MODE__NONE
                s = ctx.curValueItem[: ctx.dataLength]

            if s not in ctx.index:
                ctx.index.add(s)
                ctx.result.append(s)

            ctx.mode = C_MODE__NONE
            ctx.curValueItem = ""
            ctx.dataLength = 0
            return

        # ----------------------------------------------
        while True:
            assert i >= 0
            assert i <= length

            if i == length:
                LOCAL__append_curValueItem_to_result(ctx, True)
                return ctx.result  # GO HOME!

            assert i >= 0
            assert i < length

            ch = source[i]

            if ch == "," and ctx.mode != C_MODE__QSTART:
                LOCAL__append_curValueItem_to_result(ctx, False)
                i += 1
                continue

            # space
            if not __class__.IsSpace(ch):
                pass
            else:
                if ctx.mode == C_MODE__QEND:
                    i += 1
                    continue

                if ctx.mode == C_MODE__QSTART:
                    pass
                elif ctx.curValueItem is None or ctx.curValueItem == "":
                    i += 1
                    continue

                # append this RAW space to result
                LOCAL__append_to_curValueItem(ctx, ch, False)
                i += 1
                continue

            assert not __class__.IsSpace(ch)

            if ch == '"':
                # quoted item
                if ctx.mode == C_MODE__NONE:
                    ctx.mode = C_MODE__QSTART
                    i += 1
                    continue

                if ctx.mode == C_MODE__QSTART:
                    i += 1

                    if i != length and source[i] == '"':
                        LOCAL__append_to_curValueItem(ctx, '"', True)
                        i += 1
                        continue

                    ctx.mode = C_MODE__QEND
                    continue

                assert ctx.mode == C_MODE__QEND
                RaiseError.BadFormatOfCommaSeparatedList()

            if ctx.mode == C_MODE__QEND:
                # Data after quoted text
                RaiseError.BadFormatOfCommaSeparatedList()

            LOCAL__append_to_curValueItem(ctx, ch, True)
            i += 1
            continue


# //////////////////////////////////////////////////////////////////////////////
