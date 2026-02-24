import sys


def truncate(s: bytes, n: int) -> bytes:
    if n >= len(s):
        return s
    while n > 0 and (s[n] & 0xC0) == 0x80:
        n -= 1
    return s[:n]


with open('cases', 'rb') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        n = line[0]
        s = line[1:-1]
        res = truncate(s, n)
        sys.stdout.buffer.write(res + b'\n')
