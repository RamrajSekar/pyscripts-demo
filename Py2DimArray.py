import os
a,b = 6,5

##matrix = [[0 for x in range(a)] for y in range(b)]
##print(matrix)


##c = [1 for x in range(a)]
##print(c)

while b > 0:
    for y in range(a):
        if y >= 3 or y >=6:
            print(y,end=' ')
        else:
            print(y,end=' ')
        print('\n')
    b=b-1
    #file.write("\n")
