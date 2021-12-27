#CHAPTER 10 EXERCISES

#Exercise 1

def maxMinFunc():
    import string

    #fileInput = input('Enter the name of the file you want to open:')
    fhandle = open('mbox-short.txt')
    
    senderCount = dict()

    for line in fhandle:
        words = line.split()
        if words == [] or words[0] != 'From' : continue
        sender = words[1]
        senderCount[sender] = senderCount.get(sender,0) + 1

    #tupleList = list(senderCount.items())

    newTupleList = list()

    for key, val in list(senderCount.items()):
        newTupleList.append((val, key))

    testTupleList = max(newTupleList)
    newTupleList.sort(reverse=True)

 

    test = ' '.join(str(e) for e in newTupleList[0])
    test2 = ' '.join(str(e) for e in testTupleList)

    keyVal = list(newTupleList[0])
    printKey =''
    for i in keyVal:
        printKey += ' ' + str(i) 

    print(test)
    print(test2)
    print(printKey.strip())
    print(keyVal[0], keyVal[1])
    

maxMinFunc()
#mbox-short.txt
#mbox.txt