# CHAPTER 5 EXERCISES

#Exercise 1

#total = 0
#count = 0 

#while True:
 #   try:

  #      line = input('Enter a number: ')

   #     if line == 'done':
    #        break

     #   count = count + 1
      #  total = total + int(line)

        
    #except:
     #   print('Invalid input')

#average = total / count
#print(count, total, average)

#Exercise 2

total = 0
count = 0 
max = None
min = None

while True:
    try:

        line = input('Enter a number: ')

        if line == 'done':
            break

        num = int(line)

        total = total + num
        count = count + 1

        if max is None or num > max:
            max = num

        if min is None or num < min:
            min = num
        
        
    except:
        print('Invalid input')

print(count, total, max, min)