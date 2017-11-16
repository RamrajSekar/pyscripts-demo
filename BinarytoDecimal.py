from collections import Counter,defaultdict
#To convert binary to decimal (ie. 0001 to 1)
##n = "1010"
##a = []
##
##for i in n:
##    a.append(int(i))
##b = len(a)-1
##c = 0
##for j in a:
##    #print(b)
##    c += (j * (2)**b)
##    b -= 1
##print(c)


##print(1%2)
#To convert decimal to binary(ie. 1 to 0001)
d = 6
rem = []
nmax = []
while(d > 0):
    e = d%2
    d = d//2
    #print(bal)
    rem.append(e)
#print(rem)
for i in range(len(rem)-1,-1,-1):
    nmax.append(rem[i])
print(nmax)

count = -1
for j in nmax:
   if(j == 1):
       count = count+1
print(count)
