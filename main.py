def bin2dec(n):
    toreturn = 0
    nstr = str(n)
    nlenght = len(nstr)
    for i in range(0, nlenght):
        bit = int(nstr[nlenght - 1 - i])
        toreturn = toreturn + bit * (2 ** i)
    print(toreturn)


def dec2bin(num):
    """
    :param num: Enter any integer or float. It can be both positive or negative
    :return: Returns the binary representation of the decimal used as parameter
    """

    def float_to_binary(numb):
        exponent = 0
        shifted_num = numb
        while shifted_num != int(shifted_num):
            shifted_num *= 2
            exponent += 1
        if exponent == 0:
            return '{0:0b}'.format(int(shifted_num))
        binary = '{0:0{1}b}'.format(int(shifted_num), exponent + 1)
        integer_part = binary[:-exponent]
        fractional_part = binary[-exponent:].rstrip('0')
        return '{0}.{1}'.format(integer_part, fractional_part)

    def floathex_to_binary(floathex):
        number = float.fromhex(floathex)
        return float_to_binary(number)

    if 0 < num < 1:
        p = 0
        while ((2 ** p) * num) % 1 != 0:
            p += 1
        x = int(num * (2 ** p))
        result = ''
        if x == 0:
            result = '0'
        while x > 0:
            result = str(x % 2) + result
            x //= 2
        for i in range(p - len(result)):
            result = '0' + result
        result = result[0:-p] + '.' + result[-p:]

    elif num > 0 and type(num) is float:
        num_hex = float.hex(num)
        result = floathex_to_binary(num_hex)

    elif num < 0 and type(num) is float:
        num_hex = float.hex(num)
        result = floathex_to_binary(num_hex)

    else:

        if num < 0:
            isneg = True
            num = abs(num)
        else:
            isneg = False

        result = ''

        if num == 0:
            result = '0'

        while num > 0:
            result = str(num % 2) + result
            num //= 2

        if isneg:
            result = '-' + result

    return result


def hexa2dec(n):
    longueur = len(n)
    nombre = 0
    for i in range(0, longueur):
        if str.lower(n[i]) == "a":
            c = 10
        elif str.lower(n[i]) == "b":
            c = 11
        elif str.lower(n[i]) == "c":
            c = 12
        elif str.lower(n[i]) == "d":
            c = 13
        elif str.lower(n[i]) == "e":
            c = 14
        elif str.lower(n[i]) == "f":
            c = 15
        else:
            c = int(n[i])
        nombre = nombre + c * (16 ** (longueur - i - 1))
    print(nombre)


def addbinary(a, b):
    max_len = max(len(str(a)), len(str(b)))
    a = str(a).zfill(max_len)
    b = str(b).zfill(max_len)

    result = ''

    carry = 0

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    print(str(result).zfill(max_len))


def binaries_length(n):
    return len(str(dec2bin(n)))


bin2dec(10110)
print(dec2bin(22*4))
print(binaries_length(2205))
hexa2dec("")
addbinary(0, 0)
