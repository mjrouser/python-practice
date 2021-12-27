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
 
    

#maxMinFunc()
#mbox-short.txt
#mbox.txt

#Exercise 2

def hourFunc():
    import string
    fhandle = open('mbox-short.txt')
    
    hourCount = dict()

    for line in fhandle:
        words = line.split()
        #print(words)
        if words == [] or words[0] != 'From' : continue
        #print(words) #mbox-short.txt
        time = words[5]
        hourPos = time.find(':')
        hour = time[:hourPos]
        hourCount[hour] = hourCount.get(hour,0) + 1
    #print(hourCount)

    newTupleList = list()
    for key, val in list(hourCount.items()):
        newTupleList.append((key, val))

    newTupleList.sort(reverse=True)

    for key, val in newTupleList:
        print(key, val)

#hourFunc()


#Exercise 3

def letterCountFunc():
    import string
    fhandle = open('mbox-short.txt')
    
    letterCount = dict()
    count = 0

    for line in fhandle:

        #print(type(line))
        stripped = line.strip()
        translated = stripped.translate(stripped.maketrans('', '', string.punctuation))
        lettersOnly = translated.translate(translated.maketrans('', '', string.digits))
        noWtSpc = lettersOnly.translate(lettersOnly.maketrans('','',string.whitespace))
        #print(count, translated)
        lowered = noWtSpc.lower()
        #print(count, lowered)
        for letter in lowered:
            letterCount[letter] = letterCount.get(letter,0) + 1

        #count +=  1
        #if count == 10: break

    #print(letterCount)

    letterCountList = list(letterCount.items())
    letterCountList2 = list()
    #print(letterCountList)
    for key, val in letterCountList:
        letterCountList2.append((val, key))
    letterCountList2.sort(reverse=True)
    for key, val in letterCountList2:
        print(val, key)
letterCountFunc()