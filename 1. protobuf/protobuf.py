import struct


def encode(n: int) -> bytes:
    if n == 0:
        return b'\x00'

    result = bytearray()
    while n > 0:
        byte = n & 0x7F
        n >>= 7
        if n > 0:
            byte |= 0x80
        result.append(byte)
    return bytes(result)


def decode(var_int: bytes) -> int:
    result = 0
    shift = 0
    for byte in var_int:
        result |= (byte & 0x7F) << shift
        if not (byte & 0x80):
            break
        shift += 7
    return result


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
