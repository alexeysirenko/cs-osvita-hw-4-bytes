import re
import sys


def hex_to_rgb(r):
    """
    return r.group(1)
    Add your code here
    """


sys.stdout.write(
    re.sub(
        r'\#([0-9a-fA-F]+)',
        hex_to_rgb,
        sys.stdin.read()
    )
)
