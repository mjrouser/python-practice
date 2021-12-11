#CHAPTER 7 EXERCISES

#Exercise 1

#fhand = open('mbox-short.txt')
#for line in fhand:
#    line = line.upper()
#    print(line)

fname = input('Enter a file to open:')
try:
    fhand = open(fname)
except:
    if fname == 'na na na boo boo':
        print('Yeah, well na na na boo boo to you too!')
    elif fname == 'meh':
        print("Yeah, that's how I feel about it too")
    else:
        print('Could not locate file: ' + fname)
    exit()

count = 0
total = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        spampos = line.find(':')
        spam = line[spampos +1:]
        count = count + 1
        total = total + float(spam)
spamavg = total / count
print(spamavg)