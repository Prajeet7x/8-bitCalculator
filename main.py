from binaryAddition import binaryAddition        #Importing the methods from modules
from decimalToBinary import decimalToBinary
from listToString import finalResult
from reverseNumber import reverseNumber
from validation import validateNumber

print("\n\n=========================================")
print("Welcome to the Binary Addition program!")
print("=========================================\n\n")
continuation=True
while continuation==True:
    
    #Exception handling for the first number entered
    success=False
    while success==False:
        try:
            num1=int(input("Enter a decimal number: "))
            success=True
        except:
            print("Invalid entry! Enter a decimal number \n")

    #validating the number to ensure number lies within 0-255
    num1=validateNumber(num1)


    #Exception handling for the second number entered
    success=False
    while success==False:
        try:
            num2=int(input("Enter another decimal number: "))
            success=True
        except:
            print("Invalid entry! Enter a decimal number \n")

    #validating the number to ensure number lies within 0-255            
    num2=validateNumber(num2)


    #converting the decimal numbers into binary
    reverseBinaryNum1=decimalToBinary(num1)
    reverseBinaryNum2=decimalToBinary(num2)


    #reversing the binary numbers as to obtain the correct converted binary value
    FinalBinaryNum1=reverseNumber(reverseBinaryNum1)
    FinalBinaryNum2=reverseNumber(reverseBinaryNum2)


    #Obtaining the reverse sum of the two binary numbers entered
    binarySumReverse=binaryAddition(FinalBinaryNum1,FinalBinaryNum2)


    #Obtaining the binary sum of the two numbers by reversing the previous value
    finalBinarySum=reverseNumber(binarySumReverse)

    #Obtaining the binary sum by converting and displaying it into string
    finalAnswer=finalResult(finalBinarySum)
    
    print("\nThe binary sum of ",num1,"and ",num2," is: ",finalAnswer)    

    toContinue=input("\nDo you want to enter different numbers?(yes/no)").lower()
    
    if toContinue=="no":
        print("Thank you!")
        break
