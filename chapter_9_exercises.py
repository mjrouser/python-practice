#CHAPTER 9 EXERCISES

#Exercise 1

def exercise1 ():
    fileHandler = open('words.txt')
    myDict = dict()
    count = 0
    #print('Debug for myDict instantiation:',myDict, count)
    for line in fileHandler:
        splitLine = line.split()
        for word in splitLine:
            count += 1
            myDict.update({word: count})
            #print('Debug for myDict instantiation:',myDict)
    keyList = list(myDict.keys())
    #print('Debug for count', count)
    #print(keyList)
    print('Writing' in keyList)

#exercise1()

#Exercise 2

def dictFunc():
    import string
    try:
        fileInput = input('Enter the name of the file you want to open:')
        fhandle = open(fileInput)
    except:
        print('Cannot open file as input')
    
    daysCount = dict()

    for line in fhandle:
        words = line.split()
        #print(words)
        if words == [] or words[0] != 'From' : continue
        #print(words) #mbox-short.txt
        day = words[2]
        daysCount[day] = daysCount.get(day,0) + 1
    print(daysCount)

#dictFunc()

#Exercise 3

def addressFunc():
    import string
    try:
        fileInput = input('Enter the name of the file you want to open:')
        fhandle = open(fileInput)
    except:
        print('Cannot open file as input')
    
    daysCount = dict()

    for line in fhandle:
        words = line.split()
        #print(words)
        if words == [] or words[0] != 'From' : continue
        #print(words) #mbox-short.txt
        day = words[1]
        daysCount[day] = daysCount.get(day,0) + 1
    print(daysCount)

#addressFunc()

#Exercise 4

def maxMinFunc():
    import string
    try:
        fileInput = input('Enter the name of the file you want to open:')
        fhandle = open(fileInput)
    except:
        print('Cannot open file as input')
    
    senderCount = dict()

    for line in fhandle:
        words = line.split()
        #print(words)
        if words == [] or words[0] != 'From' : continue
        #print(words) #mbox-short.txt
        sender = words[1]
        senderCount[sender] = senderCount.get(sender,0) + 1
    print(senderCount)

    maxSentVal = None
    maxSentKey = None
    minSentVal = None
    minSentKey = None
    for key in senderCount:
        thing = int(senderCount[key])
        #print('Debug:',thing)
        if maxSentVal == None or maxSentVal < thing:
            maxSentKey = key
            maxSentVal = thing
            print('Debug:',maxSentKey, maxSentVal)
        if minSentVal == None or minSentVal > thing:
            minSentKey = key
            minSentVal = thing
            print('Debug:',minSentKey, minSentVal)

    print(maxSentKey, maxSentVal)
    print(minSentKey, minSentVal)

#maxMinFunc()

#mbox-short.txt

#Exercise 5

def domainFunc():
    import string
    try:
        fileInput = input('Enter the name of the file you want to open:')
        fhandle = open(fileInput)
    except:
        print('Cannot open file as entered')
    
    domainCount = dict()

    for line in fhandle:
        words = line.split()
        #print(words)
        if words == [] or words[0] != 'From' : continue
        #print(words) #mbox-short.txt
        address = words[1]
        domPos = address.find('@')
        domain = address[domPos+1:]
        domainCount[domain] = domainCount.get(domain,0) + 1
    print(domainCount)

domainFunc()