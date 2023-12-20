def integer_to_binary(integerPart):
    if integerPart == 0: return '0'

    binary = ''
    while integerPart > 0:
        remainder = integerPart % 2
        binary = str(remainder) + binary
        integerPart //= 2
    return binary


def float_to_binary(floatPart):
    if floatPart == 0: return '0'

    binary = ''
    while floatPart > 0:
        floatPart *= 2
        remainder = int(floatPart)
        binary += str(remainder)
        floatPart -= remainder
    return binary


def float_to_ieee754(number):
    if number == 0: return '0' * 32
    sign = '0' if number >= 0 else '1'

    number = abs(number)
    integerPart = int(number)
    decimalPart = number - integerPart

    integerBinary = integer_to_binary(integerPart)
    decimalBinary = float_to_binary(decimalPart)

    counter = 0
    if len(integerBinary) > 1:
        while len(integerBinary) > 1:
            decimalBinary = integerBinary[-1] + decimalBinary
            integerBinary = integerBinary[:-1]
            counter += 1
    else:
        while '1' not in integerBinary:
            integerBinary = integerBinary + decimalBinary[0]
            decimalBinary = decimalBinary[1:]
            counter -= 1

    exponent = counter + 127
    exponentBinary = integer_to_binary(exponent)
    while len(exponentBinary) < 8: exponentBinary = "0" + exponentBinary
    mantissaBinary = decimalBinary

    if len(mantissaBinary) < 23:
        while len(mantissaBinary) < 23: mantissaBinary += "0"
    else: mantissaBinary = mantissaBinary[:23]

    ieee754Representation = sign + " " + exponentBinary + " " + mantissaBinary
    return ieee754Representation

number = -10.4
print(f"Liczba: {number}\nZapis IEEE 754: {float_to_ieee754(number)}")