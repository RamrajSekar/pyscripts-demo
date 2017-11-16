import os

print('Current working directory is: ',os.getcwd())
mypath = 'C:\\CignitiProjects\\ATD\\AspireIntegration'
os.chdir(mypath)


print('New working directory is: ',os.getcwd())
##try:
##    if(os.getcwd() == mypath):
##        os.makedirs('C:\\CignitiProjects\\ATD\\AspireIntegration\\B')
##        print('Folder is created')
##    else:
##        print('Folder is not created')
##except FileExistsError:
##    print('Folder already exists')

print('---Finding file size---')
print(os.path.getsize(mypath))

print(os.listdir(mypath))
fsize=0
for filename in os.listdir(mypath):
    fsize = fsize + os.path.getsize(os.path.join(mypath, filename))
print(fsize)

print('---Finding a specific file in folder and read the same---')
for filenames in os.listdir(mypath):
    if filenames == 'ImpQueries.txt':
        ofile = open('C:\\CignitiProjects\\ATD\\AspireIntegration\\ImpQueries.txt')
        fileCont = ofile.read()
        print(fileCont)
        print('Pass')
    else:
        pass

print('---Finding a specific file in folder and write in the same---')
nfile = open('ImpQueries.txt','w')
nfile.write('Hello World..!!\n')
nfile.close()
nfile = open('ImpQueries.txt')
content = nfile.read()
print(content)
nfile.close()
