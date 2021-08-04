def binaryAddition(binaryNumber1,binaryNumber2):
    ''' Adds the two binary numbers and return the sum '''
    cin=0
    finalSumList=[]
    coutList=[]

    #simulating an 8-bit adder circuit by adding various logic gates and Carry in and Carry out concepts
    for i in range(len(binaryNumber1)-1,-1,-1):
        
        if coutList==[]:
            cout = (cin & (binaryNumber1[i] ^ binaryNumber2[i])) | (binaryNumber1[i] & binaryNumber2[i])
            coutList.append(cout)
            sum_ = cin ^ (binaryNumber1[i] ^ binaryNumber2[i])
            finalSumList.append(sum_)

        else:
            cout = ((coutList[-1]) & (binaryNumber1[i] ^ binaryNumber2[i])) | (binaryNumber1[i] & binaryNumber2[i])
            coutList.append(cout)

            sum_=coutList[-2] ^ (binaryNumber1[i] ^ binaryNumber2[i])
            finalSumList.append(sum_)

    return finalSumList
