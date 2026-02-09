import sys

ASCII_MAX = 0x7F
CONT_MIN = 0x80
CONT_MAX = 0xBF
TWO_BYTE_MIN = 0xC0
TWO_BYTE_MAX = 0xDF
THREE_BYTE_MIN = 0xE0
THREE_BYTE_MAX = 0xEF
FOUR_BYTE_MIN = 0xF0
FOUR_BYTE_MAX = 0xF7


def truncate(s: bytes, n: int) -> bytes:
    s = s[:n]

    while len(s) > 0:
        last = s[-1]

        if last <= ASCII_MAX:
            return s

        if CONT_MIN <= last <= CONT_MAX:
            i = len(s) - 1
            while i >= 0 and CONT_MIN <= s[i] <= CONT_MAX:
                i -= 1

            if i < 0:
                return b''

            start = s[i]
            continuation_count = len(s) - 1 - i

            if TWO_BYTE_MIN <= start <= TWO_BYTE_MAX:
                expected = 1
            elif THREE_BYTE_MIN <= start <= THREE_BYTE_MAX:
                expected = 2
            elif FOUR_BYTE_MIN <= start <= FOUR_BYTE_MAX:
                expected = 3
            else:
                s = s[:i]
                continue

            if continuation_count == expected:
                return s
            else:
                s = s[:i]

        else:
            s = s[:-1]

    return s


with open('cases', 'rb') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        n = line[0]
        s = line[1:-1]
        res = truncate(s, n)
        sys.stdout.buffer.write(res + b'\n')
