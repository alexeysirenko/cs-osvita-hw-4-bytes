import struct


def encode(n: int) -> bytes:
    """
        Add your code here
    """
    pass


def decode(var_int: bytes) -> int:
    """
        Add your code here
    """
    pass


basic_tests = (
    ('1.uint64', b'\x01'),
    ('150.uint64', b'\x96\x01'),
    ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01'),
)

for file_name, expectation in basic_tests:
    with open(file_name, 'rb') as f:
        n = struct.unpack('>Q', f.read())[0]
        assert encode(n) == expectation
        assert decode(encode(n)) == n
print('sample tests passed')


print("stress test started...")
for n in range(1 << 30):
    assert decode(encode(n)) == n
    if n % 1000 == 0:
        print(f"{n} tests passed")
print('all tests passed')
