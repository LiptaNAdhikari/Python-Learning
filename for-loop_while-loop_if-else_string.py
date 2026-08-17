#for loop with range

for i in range(5):
  print(i)


print("----------------")
#for loop with list

list_1 = ["apple",10,"banana",10.5]

for i in list_1:
  print(i)


print("----------------")
#for loop with range and start,stop

for i in range (5, 10, 2):
  print(i)

"""**while loop in Python**"""

cnt = 1
while cnt <= 10:
  print(cnt)
  cnt=cnt+1

"""**Basic if-else statement**"""

flag = 7

if flag==1:
  print("Apple")
elif flag==2:
  print("Mango")
else:
  print("Banana")


print("-------------------")

age = 18

if age<18:
  print("Minor")
elif age == 18:
  print("Just Adult")
else:
  print("Adult")

"""**Nested if else**"""

x = 2

if x>5:
  if x<=10:
    print("The number is in a perfect range")
  else:
    print("The number is out of perfect range")
else:
  print("The number is not applicable")


print("---------------")


x = 16
if x > 0:
    if x % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")

"""**shorthand if else**"""

x = 56

if x>0:print("The Number is Positive")

print("--------------")

x = -47

print("Number is Positive") if x>0 else print("Number is Negative")

"""**Strings in Python**"""

#accessing string element
str_1 = "Hello_1"
str_2 = "Hello_2"
str_3 = "Hello_3"

print(str_1[0])
print(str_1[-7])
print(str_1[-1])

print("-------------------")

#string slicing

##positive indexing
print(str_2[0:4])
print(str_2[2:6])
print(str_3[:5])
print(str_3[3:])

print("------")

##negative indexing
print(str_2[-7:-3])
print(str_2[-5:-1])
print(str_3[:-2])
print(str_3[-4:])

print("-------------------")

#string operation

a = "Hello"
b = "World"
print(a+" "+b) #concatenation
print((a+" ")*3)
print("L" in a)


print("-------------------")

#string methods
s = "python programming"
print(s.upper())
s = s.upper()
print(s.lower())
s = s.lower()

s_1 = " python programming "
print(s_1)
print(s_1.strip())

print(s.replace("python", "Java"))
print(s)
print(s.split())
print(s.find("gram"))
print(s_1.find("gram"))

