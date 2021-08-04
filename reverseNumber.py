def reverseNumber(originalNumber):
    ''' Converts the original number and returns the reversed number '''
    reverseNumber=[]

    #reversing the number obtained from the parameter
    for i in range(len(originalNumber)-1,-1,-1):
        reverseNumber.append(originalNumber[i])

    return reverseNumber
