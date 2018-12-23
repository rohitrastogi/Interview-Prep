def convert_bases(value, from_base, to_base):
    return decimal_to(to_base, from_decimal(from_base, value))

def from_decimal(base, value):
    res = 0
    for i, digit in enumerate(value):
        res += base ** (len(value) - i - 1) * int(digit)
    return res

def decimal_to(base, value):
    remainders = []
    while value != 0:
        remainders.append(str(value % base))
        value = value // base
    return ''.join(reversed(remainders))

print(convert_bases('1123', 4, 7))