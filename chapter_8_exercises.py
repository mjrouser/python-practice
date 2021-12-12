#CHAPTER 8 EXERCISES

#Exercise 1

values = ['Bob', 'Sally', 'Frank']
other_values = ['books', 'computers', 'people']
newList = ['books', 'computers', 'people', 'legos', 'friends']
newList2 = ['books', 'computers', 'people', 'legos', 'friends', 'music', 'love', 'salad']

def chop(x):
    del x[2]
    del x[0]
    print(x)

def middle(y):
    return y[1]

#chop(values)

#print(middle(other_values))

def chop2(u):    
    del u[0]
    listLength = len(u)
    del u[listLength-1]
    print(u)


def middle2(z):
    length = len(z)
    lengthDiv2 = length/2
    if type(lengthDiv2) == float:
        lengthInt = int(lengthDiv2)
        middle_word = z[lengthInt]
    else:
        middle_word = z[lengthDiv2-1:lengthDiv2]
    print(middle_word)
    

#middle2(newList)
#middle2(newList2)

#chop2(newList)
#chop2(newList2)



def fromFunc():
    fhand = open('mbox-test.txt')
    for line in fhand:
        words = line.split()
        #print('Debug: ', words, len(words))
        if len(words) < 3 or words[0] != 'From' : continue
        print(words[2])
#fromFunc()


def romeo():
    finalWords = []
    rfhand = open('romeo.txt')
    for line in rfhand:
        rWords = line.split()
        for word in rWords:
            if word in finalWords : continue
            else:
                finalWords.append(word)
    finalWords.sort()
    print(finalWords)

#romeo()

def mboxFunc():
    mboxFhand = open('mbox-short.txt')
    count = 0
    for line in mboxFhand:
        splitLine = line.split()
        if splitLine == [] or splitLine[0] != 'From' : continue
        #print('Debug', splitLine)
        count = count +1
        print(splitLine[1])
    print('There were', count, 'lines in the file that started with From as the first word')
        
#mboxFunc()

def maxMin():
    numberList = []
    while True:

        try:
            number = input('Enter a number:')
            
            if number == 'done':
                try:
                    #print('Debug: not the logic if')
                    maxNumber = max(numberList)
                    #print(maxNumber)
                    minNumber = min(numberList)
                    print('Maximum: ', maxNumber)
                    print('Minimum: ', minNumber)
                    break
                except:
                    print('Please enter at least one number')
                    continue

            intNumber = int(number)
            
            
            numberList.append(intNumber)
            #print('debug', numberList)


        except:
            print('Please enter numbers only')

#maxMin()