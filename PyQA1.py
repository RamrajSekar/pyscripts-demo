print('Split string and int from a variable')
a = "0Ram123"
b=[]
c =[]
##print(len(a))
##print(a[1])
##print(re.split('(\d+)',a))

for i in range(0,len(a)):
    if (a[i].isdigit())== True:
        b.append(a[i])
    else:
        c.append(a[i])
print("The integer values are: ",''.join(b))
print("The string values are: ",''.join(c))
