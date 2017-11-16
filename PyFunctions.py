#Basic function without parameters
def hello():
    print('Hello!')
    print('Howdy!!')
    print('Hello There!!!')
hello()


#def Statements with Parameters
def hello(name):
    print('Hello ',name)

hello('Ramraj')

#Return Values and return Statements
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decided so'
    elif answerNumber == 3:
        return 'Yes'

r = random.randint(1,3)
f = getAnswer(r)
print(f)

#Or
print(getAnswer(random.randint(1,3)))
