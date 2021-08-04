def validateNumber(decimalNumber):
    ''' Checks whether the number lies between 0 to 255 '''
    continuation=True
    
    #repeateadly asking the input from the user within the range 0-255
    while continuation==True:
        if(decimalNumber < 0 or decimalNumber > 255):
            print("Number receeds 0 or exceeds 255!")
            decimalNumber=int(input("Enter the number within the range (0-255): "))
        else:
            continuation=False
    return decimalNumber
            
