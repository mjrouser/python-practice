#CHAPTER 4 EXERCISES
#Exercise 1

import random

#for i in range (10):
#    x = random.random()
#   print(x)

#print(random.randint(5,10))

#t =  [1,2,3,4,5]
#print(random.choice(t))


#Exercise 2&3

#def print_lyrics():
#    print("I'm a lumberjack, and I'm OK.")
#    print('I sleep all night and I work all day.')

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()

#repeat_lyrics()

#def addTwo(a,b):
#    added = a + b
#    return added

#x = addTwo(3,5)
#print(x)

#Exercise 6

#HoursPrompt = 'Enter hours worked:\n'
#RatePrompt = 'Enter pay rate:\n'

#try:

#    hours = int(input(HoursPrompt))
#    rate = int(input(RatePrompt))

#    def computePay(hours, rate):
#        calc = hours * rate
#        overtimeCalc = ((hours - 40) * 1.5* rate) + (40*rate)
#        if hours <= 40:
#            x = calc
#        elif hours > 40:
#            x = overtimeCalc
#        return x

#    y = computePay(hours, rate)
#    print(y)
    

#except:
#    print('Please enter an integer')

#Exercise 7 

prompt = 'Enter your score:\n'
reply = 'Your grade is '

try:
    score = float(input(prompt))

    def computeGrade(score):
        if score < 1.1 and score >= 0.9:
            grade =  'an A'
        elif score >= 0.8 and score <0.9:
            grade = 'a B'
        elif score >= 0.7 and score <0.8:
            grade = 'a C'
        elif score >= 0.6 and score <0.7:
            grade = 'a D'
        elif score < 0.6:
            grade = 'an F'
        return grade

    Y = computeGrade(score)
    print(reply + Y)

except:
    print('Bad score')