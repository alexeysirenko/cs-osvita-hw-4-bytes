import sys

CONT_MIN = 0x80
TWO_BYTE = 0xC0
THREE_BYTE = 0xE0
FOUR_BYTE = 0xF0


def truncate(s: bytes, n: int) -> bytes:
    s, i = s[:n], len(s[:n])

    while i > 0 and CONT_MIN <= s[i - 1] < TWO_BYTE:
        i -= 1

    if i == 0:
        return b''

    if s[i - 1] >= TWO_BYTE and len(s) - i != (1 if s[i - 1] < THREE_BYTE else 2 if s[i - 1] < FOUR_BYTE else 3):
        return s[:i - 1]

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
