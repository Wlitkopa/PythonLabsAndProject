
# for n in range(255):
#     print(n.to_bytes(1, byteorder='big'))


def xor_bytes(by1, by2):
    return bytes([_a ^ _b for _a, _b in zip(by1, by2)])


ct = b'\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e'
pt = b'jowlsjowlsjowlsjowlsjowlsjowlsjowlsjowlsjowlsjowlsjowlsjowls'


print(xor_bytes(ct, pt))


