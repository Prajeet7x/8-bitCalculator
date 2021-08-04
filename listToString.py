def finalResult(binarySumList):
    ''' returns the sum of the binary numbers in string '''
    digit=''

    #converting the sum from list type to String type
    for i in range(len(binarySumList)):            
        digit=digit+str(binarySumList[i])
    return digit
