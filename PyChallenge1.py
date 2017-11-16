from random import randint,randrange,uniform
##Challenge1:
##Write a program which will find all such numbers which are divisible by 7 but
##are not a multiple of 5,between 2000 and 3200 (both included).The numbers
##obtained should be printed in a comma-separated sequence on a single line.

##a = []
##for i in range(7,40):
##    if (i%7==0) and (i*5 !=0):
##        a.append(str(i))
##    else:
##        pass
##print(','.join(a))

##Challenge 2:
##Write a program which can compute the factorial of a given numbers.
##The results should be printed in a comma-separated sequence on a single line.

##def fact(b):
##    if b == 0:
##        return 1
##    return b * fact(b - 1)
##
##b = int(input("Enter a number: "))
##print(fact(b))

##Challenge 3:
##With a given integral number n, write a program to generate a dictionary that
##contains (i, i*i) such that is an integral number between 1 and n (both
##included) and then the program should print the dictionary.

##c ={}
##d = int(input("Enter a number: "))
##for i in range(1,d+1):
##    c[i] = i*i
##print(c)


##Challenge 4:
##Write a program which accepts a sequence of comma-separated numbers from
##console and generate a list and a tuple which contains every number.
##Example: If input is 34,67,55,33,12,98
##Then, the output should be:
##['34', '67', '55', '33', '12', '98']
##('34', '67', '55', '33', '12', '98')

##print("----Solution 1----")
##to_list = []
##e = 0
##while e is not None :
##    e = str(input("Enter a number: "))
##    to_list.append(e)
##    if len(to_list) == 6:
##        break
##print(to_list)
##print(tuple(to_list))

##print("----Solution 2----")
##values = input()
##l = values.split(",")
##print(l)
##t = tuple(l)
##print(t)

##Challenge 5: Write a script to generate random numbers bt 0 to 100
##and arrange in order.
f = []
for i in range(10):
    e = randint(0,100)
    f.append(e)
print("Values in Ascending Order: ",sorted(f, reverse=False))
print("Values in Descending Order: ",sorted(f, reverse=True))


##Challenge 5: Write a script to generate random numbers bt 0 to 100 and
##arrange in order.

for i in range(10):
    e = randint(0,10)
    if(e%2 == 0):
        print(e)
