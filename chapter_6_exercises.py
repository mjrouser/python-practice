#CHAPTER 6 EXERCISES

#Exercise 1

#fruit = 'banana'
#index = len(fruit) - 1

#while index < len(fruit) and index > -1:
#    letter = fruit[index]
#    print(letter)
#    index = index - 1 

#Exercise 2
#print(fruit[:])

#Exercise 3

#word = 'banana'
#letter = 'a'
#def count ():
#    increment = 0
#    for x in word:
#        if x == letter:
#            increment = increment +1
#    print(increment)
#count()

#Exercise 4

#string = 'banana'
#print(string.count('a'))

#Exercise 5

str = 'X-DSPAM-Confidence:0.8475'
digstart = str.find(':')
digits = str[digstart+1:]
print(float(digits))