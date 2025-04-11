import random
passlen = int(input("enter the length of password"))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)

# Variable creation and viewing them in return
name = "Muzain"
age = 4.4
print (f"My name is {name}" )

# Variable datatype viewer [$name is a String & $age is an Integer] in <class 'DATATYPE'> format
print (type(name), type(age))

# Delete the variable out of existence
del name

# Input datatype variable. This will give you a text field option. You can then print that out
outpost = input("You can write anything here to print it out! ")
print (outpost)

# Conditional logical inputs
while True:
    try:
        firstNum = int(input("Provide your 1st number"))
        break
    except ValueError:
        print ("Please enter an integer")
while True:
    try:
        secondNum = int(input("Provide your 2nd number"))
        break
    except ValueError:
        print ("Please enter an integer")


print (f"The boolean value below will tell the inequality-relation of the given numbers ({firstNum},{secondNum}) correctly & legitimately")
print(f"They are equal to each other: {firstNum == secondNum}")
print(f"Opposite -> They aren't equal to each other: {firstNum != secondNum}")
print(f"First Number is greater than the Second: {firstNum > secondNum}")
print(f"Second Number is greater than the First: {firstNum < secondNum}")

# These only prints out the given Strings & basic operations of given numbers
print(f"This is Addition of {firstNum} & {secondNum}:")
print(firstNum+secondNum)
print(f"This is Subtraction of {firstNum} & {secondNum}:")
print(firstNum-secondNum)
print(f"This is Multiplication of {firstNum} & {secondNum}:")
print(firstNum*secondNum)
if firstNum > secondNum:
    print(f"This is lesser Exponentiation of {firstNum} & {secondNum}:")
    print(firstNum**secondNum)
    print(f"This is improper fraction (x>1) of {firstNum} & {secondNum}:")
    print(firstNum/secondNum)
    print(f"This is Floor (Integer based Quotient) of {firstNum} & {secondNum}:")
    print(firstNum//secondNum)
    print(f"This is Modulus (Remainder) of {firstNum} & {secondNum}:")
    print(firstNum%secondNum)
elif firstNum < secondNum:
    print(f"This is greater Exponentiation of {secondNum} & {firstNum}:")
    print(firstNum**secondNum)
    print(f"This is proper fraction (0<x<1) of {secondNum} & {firstNum}:")
    print(firstNum/secondNum)
    print(f"This is Floor (Integer based Quotient) of {secondNum} & {firstNum} (which is logically Zero):")
    print(firstNum//secondNum)
    print(f"This is Modulus (Remainder) of {secondNum} & {firstNum} (which is the given 2nd Number = {secondNum}:")
    print(firstNum%secondNum)
elif secondNum == 1:
    print("No other operation is necessary in this case")
elif firstNum == secondNum:
    print(f"This is the Power tower of Second Order (^^2) for {firstNum} (Hence, 1st Number {firstNum} = 2nd Number {secondNum}):")
    print(firstNum**secondNum)
    print(f"This is unitary fraction (0<x<1) of {secondNum} & {firstNum} (which logically results in One):")
    print(f"Floor (Integer based Quotient) = 1; doesn't matter in this case")
    print(f"This is Modulus (Remainder) of {secondNum} & {firstNum} (which is logically Zero):")
    print(firstNum%secondNum)

# Series of integer-based Conditions
Req_Age = 18
while True:
    try:
        Your_Age = int(input("Provide your curent Age honestly"))
        if 0<= Your_Age <=120:
            break
        else:
            print ("Please enter a legitimate age")
    except ValueError:
        print ("Please enter an integer")

print (f"Your age is {Your_Age}. Read the conditional result below")

if Your_Age < Req_Age:
    print("You're not Mature yet")
elif Your_Age == Req_Age:
    print("You're newly Mature")
elif Your_Age <= (Req_Age+1) & Your_Age > Req_Age: 
    print("You already became Mature a year ago")
elif Your_Age <= (Req_Age+2) & Your_Age > (Req_Age+1): 
    print("You already became Mature two years ago")
elif Your_Age <= (Req_Age+3) & Your_Age > (Req_Age+2): 
    print("You already became Mature three years ago")
else:
    print("You had became Mature several years ago")

# How to refine multiple errors by defining an external (user-built) function

def pr_string_var():
    variable = "Repeated VAR(DataType==p0STRING) 4 times to fix spelling issue ALL AT ONCE!"
    print(variable)
    print(variable)
    print(variable)
    print(variable)

pr_string_var()
print("~~END of Repetitions~~")

# Alternate Method of the same definer function

def pr_string_var(text):
    print(text)
    print(text)
    print(text)
    print(text)

pr_string_var("Repeated VAR(DataType==p0STRING) 4 times to fix spelling issue ALL AT ONCE!")
print("~~END of Repetitions~~")

#This will return Name & Age by giving that pair of info
def Class(name, age):
    print(f"That means, your name is {name} & your age is {age}")

Class(int(input("Your name?")), 
    str(input("Your age?")))

#While Loop
print("~~Odd numbers below Ten~~")
x=1
while x<10:
    print(x)
    x=x+2

#For Loop
print("~~All numbers between Ten & Twenty~~")
for x in range(11, 20):
    print(x)

#Array Integration in Loop
WeekDays = ["Fri", "Satur", "Sun", "Mon", "Tues", "Wednes", "Thurs"]

for d in WeekDays:
    print(f"Today is {d}day")