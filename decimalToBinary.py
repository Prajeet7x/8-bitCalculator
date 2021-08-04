def decimalToBinary(decimalNumber):
    ''' Converts a decimal number into binary(8-bits) '''
    bit=[]
    count=0

    #obtaining the binary number of the decimal value by binary division
    while count!=8:
        remainder=decimalNumber%2
        bit.append(remainder)
        decimalNumber=decimalNumber//2
        count=count+1

    return bit
