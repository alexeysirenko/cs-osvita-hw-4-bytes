import re
import sys


def hex_char_to_int(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    elif 'a' <= c <= 'f':
        return ord(c) - ord('a') + 10
    elif 'A' <= c <= 'F':
        return ord(c) - ord('A') + 10


def hex_byte_to_int(s):
    return hex_char_to_int(s[0]) * 16 + hex_char_to_int(s[1])


def hex_to_rgb(match):
    hex_str = match.group(1)

    if len(hex_str) == 3:
        r = hex_char_to_int(hex_str[0]) * 17
        g = hex_char_to_int(hex_str[1]) * 17
        b = hex_char_to_int(hex_str[2]) * 17
        return f'rgb({r} {g} {b})'

    elif len(hex_str) == 4:
        r = hex_char_to_int(hex_str[0]) * 17
        g = hex_char_to_int(hex_str[1]) * 17
        b = hex_char_to_int(hex_str[2]) * 17
        a = hex_char_to_int(hex_str[3]) * 17 / 255
        return f'rgba({r} {g} {b} / {a:.5f})'

    elif len(hex_str) == 6:
        r = hex_byte_to_int(hex_str[0:2])
        g = hex_byte_to_int(hex_str[2:4])
        b = hex_byte_to_int(hex_str[4:6])
        return f'rgb({r} {g} {b})'

    elif len(hex_str) == 8:
        r = hex_byte_to_int(hex_str[0:2])
        g = hex_byte_to_int(hex_str[2:4])
        b = hex_byte_to_int(hex_str[4:6])
        a = hex_byte_to_int(hex_str[6:8]) / 255
        return f'rgba({r} {g} {b} / {a:.5f})'

    return match.group(0)


sys.stdout.write(
    re.sub(
        r'\#([0-9a-fA-F]+)',
        hex_to_rgb,
        sys.stdin.read()
    )
)
