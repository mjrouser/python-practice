#CHAPTER 11 EXERCISES

#Exercise 1
def regExFunc():
    import re
    searchRE = input('Enter a regular experssion:')

    fhandle = open('mbox.txt')
    lineCount = 0
    for line in fhandle:
        line = line.strip()
        if re.search(searchRE, line):
            lineCount += 1
    print('mbox.txt had',lineCount, 'lines that matched "'+ str(searchRE)+'"')
#regExFunc()

#Exercise 2

def regSumFunc():
    import re
    fhandle = open('mbox.txt')
    sum = 0
    count = 0


    for line in fhandle:
        line.strip()
        if re.search('New Revision: ([0-9].*)', line):
            extractNumber = re.findall('New Revision: ([0-9].*)', line)
            #print(extractNumber)
            number = int(extractNumber[0])
            #print(number)
            count += 1
            sum = sum + number
    avg = sum/count
    print(sum, int(avg))
#regSumFunc()

#Autograder exercise 1

def regexAutoGrader():
    import re
    fhanndle = open('egex_sum_1422630.txt')

    sum = 0 

    for line in fhanndle:
        line.rstrip()
        if len(line) > 0:
            if re.search('([0-9]\d*)', line):
                #print('Debug: ',line)
                extractNumber = re.findall('([0-9]\d*)', line)
                #print('Debug extractNumber: ', extractNumber)
                for num in extractNumber:
                    num2 = num.strip()
                    #print('Debug num2: ',num2)
                    num3 = int(num2)
                    sum = sum + num3
    print(sum)

#regexAutoGrader()

def regexAutoGrader2():
    import re
    fhandle = open('regex_sum_42.txt')
    sum = 0 
    newList = [int(i) for i in re.findall('([0-9]\d*)',fhandle.read())]
    newList2 = newList
    sumNewList = sum(newList2)
    print(newList)
    print(sumNewList)

#    if re.search('([0-9]\d*)', line):
#           extractNumber = re.findall('([0-9]\d*)', line)
#           for num in extractNumber:
#                num2 = num.strip()
#                num3 = int(num2)
#               sum = sum + num3
    print(sum)

regexAutoGrader2()

#Bonus


import re
#print( sum( [ int[i] for i in re.findall('[0-9]+',open('regex_sum_42.txt').read()) ] ) )