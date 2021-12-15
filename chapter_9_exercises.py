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
            myDict.update({count: word})
            #print('Debug for myDict instantiation:',myDict)
    vals = list(myDict.values())
    #print('Debug for count', count)
    #print(vals)
    print('Writing' in vals)

exercise1()