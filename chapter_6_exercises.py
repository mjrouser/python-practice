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

word = 'banana'
def count ():
    increment = 0
    for letter in word:
        if letter == 'a':
            increment = increment +1
    print(increment)
count()