from __future__ import print_function


print (False == 0) 
print( True == 1 )
print (True + True + True)
print (True + False + False)
print (None == 0)
print (True or False)
print (False and True)
print (not True)

a = [1,2,3]
print ("THe list before deleting any value")
print (a)
del a[1]
print ("The list after deleting 2nd element")
print (a)
#assert 5 < 3, "5 is not smaller than 3"

count = 0
while (count < 3):
    count = count + 1
    print("Hello Python")

print("List Iteration")
l = ["I", "am","Python","expert"]
for i in l :
    print(i)

print("\nTuple Iteration")
t = ("I", "am","Python","expert")
for i in t :
    print(i)

print("\nString Iteration")
s = "Python"
for i in s :
    print(i) 

print("\nDictionary Iteration")
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s %d"%(i, d[i]))


for i in range(1,5):
    for j in range(i):
        print(i, end=' ')
    print()

for letter in "IamPythonExpert":
    if letter == 'e' or letter == 'm':
        continue
    print("Current Letter: ", letter)
    var = 10

for letter in "IamPythonExpert":
    if letter == 'p' or letter == 'r':
        break
print("Current letter: ", letter)

for letter in "IamPythonExport":
    pass
print("Last letter: ", letter)

class Test:
    def fun(self):
        print("Hello")
obj = Test()
obj.fun()


class Person:
    def __init__ (self, name):
        self.name = name
    def say_hi(self):
        print("Hello, my name is ", self.name)
p = Person ("Sejin")
p.say_hi()


class CSStudent :
    stream = "cse"
    def __init__(self,roll):
        self.roll = roll
a = CSStudent(101)
b = CSStudent(102)

print(a.stream)
print(b.stream)
print(a.roll)
print(CSStudent.stream)



a = 3
A = 4
print(a)
print(A)

a = 2
b = 3
c = a + b
print(c)
d = a * b
print(d)

a = 3
b = 9
if b % a == 0 :
    print("b is divisible by a")
elif b + 1 == 10 :
    print("Increment in b produces 10")
else :
    print("You are in else statement")

def checkDivisibility(a,b):
    if a % b == 0 :
        print("a is divisible by b")
    else :
        print("a is not divisible by b")
checkDivisibility(4,2)
