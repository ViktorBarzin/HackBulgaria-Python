import re

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val

bin_size = 5

# print(twos_comp(int('01110', 2),  bin_size))


def twos(val_str):
    import sys
    val = int(val_str, 2)
    b = val.to_bytes(1, byteorder=sys.byteorder, signed=False)
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)

print(twos('11111100'))