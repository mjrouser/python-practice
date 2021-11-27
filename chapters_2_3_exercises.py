
#CHAPTER 2 EXERCISES
#Exercise 2
#prompt = 'Enter your name:\n'
#name = input (prompt)
#reply = 'Hello ' + name + '!' 
#print(reply)

#Exercise 3
#HoursPrompt = 'Enter hours worked:\n'
#RatePrompt = 'Enter pay rate:\n'

#hours = input(HoursPrompt)
#rate = input(RatePrompt)

#calc = int(hours) * float(rate)

#print(calc)

#Exercise 4
#width = 17
#height = 12

#Exercise 5
#prompt = 'Enter your temperature in Centrigrade:\n'
#answer = 'Your temperature in Farenheit is: '

#ctemp = input(prompt)

#ftemp = answer + str(float(ctemp) * 1.8 + 32)

#print(ftemp)

#CHAPTER 3 EXERCISES
#Exercise 1

#HoursPrompt = 'Enter hours worked:\n'
#RatePrompt = 'Enter pay rate:\n'

#hours = int(input(HoursPrompt))
#rate = int(input(RatePrompt))

#calc = hours * rate
#overtimeCalc = ((hours - 40) * 1.5* rate) + (40*rate)

#if hours <= 40:
#    print(calc)
#elif hours > 40:
#    print(overtimeCalc)

#Exercise 2

#HoursPrompt = 'Enter hours worked:\n'
#RatePrompt = 'Enter pay rate:\n'

#try:

 #   hours = int(input(HoursPrompt))
 #  rate = int(input(RatePrompt))

 #  calc = hours * rate
#    overtimeCalc = ((hours - 40) * 1.5* rate) + (40*rate)

 #   if hours <= 40:
  #      print(calc)
  #  elif hours > 40:
  #      print(overtimeCalc)
    
#except:
 #   print('Please enter an integer')

#Exercise 3

prompt = 'Enter your score:\n'
reply = 'Your grade is '

try:
    score = float(input(prompt))

    if score >= 0.9:
        print(reply + 'an A')
    elif score >= 0.8:
        print(reply + 'a B')
    elif score >= 0.7:
        print(reply + 'a C')
    elif score >= 0.6:
        print(reply + 'a D')
    elif score < 0.6:
        print(reply + 'an F')

except:
    print('Bad scoee')