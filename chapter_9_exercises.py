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

dictFunc()