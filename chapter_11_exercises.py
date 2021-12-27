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
regSumFunc()