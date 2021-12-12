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

chop(values)

print(middle(other_values))

def chop2(u):
    listLength = len(u)
    del u[0]
    del u[listLength-2]
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
    

middle2(newList)
middle2(newList2)

chop2(newList)
chop2(newList2)