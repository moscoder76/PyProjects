import random

name = str(input("Name: "))
while True:
    try:
        age = float(input("Age: "))
        break
    except ValueError:
        print("You need to enter any decimal number")

print(f"So, your name is {name} & your age is {age}")

# Variable datatype viewer [$name is a String & $age is an Integer] in <class 'DATATYPE'> format
print(f"{name} is a {type(name)} datatype & {age} is a {type(age)} datatype")

# Series of integer-based Conditions
Req_Age = 18

print("Read the conditional result of your age below")

if age < Req_Age:
    print("You're not Mature yet")
elif age == Req_Age:
    print("You're newly Mature")
elif age == Req_Age + 1:
    print("You already became Mature in the last year")
else:
    y_num = ["two", "three", "four", "five"]
    for i in range(0, 4):
        if age == Req_Age + i + 2:
            print(f"You already became Mature {y_num[i]} years ago")
            break
    else:
        print("You had became Mature several years ago")

# Delete the variable out of existence
del name

# Input datatype variable. This will give you a text field option. You can then print that out
outpost = input("Write anything here & print it out: ")
print(f'you have written, "{outpost}"\n\n')

# Conditional logical inputs
print("Let's do some basic maths!")

while True:
    try:
        firstNum = int(input("1st number: "))
        break
    except ValueError:
        print("Please enter an integer")
while True:
    try:
        secondNum = int(input("2nd number: "))
        break
    except ValueError:
        print("Please enter an integer")


print(
f"""\n\nThe boolean values given below
will tell you the inequality-relation of
the given numbers ({firstNum}, {secondNum})
correctly & legitimately\n"""
)

if firstNum > secondNum:
    print(f"First Number is greater than the Second one\n")
elif firstNum < secondNum:
    print(f"Second Number is greater than the First one\n")
else:
    print(f"The pair of numbers are equal to each other\n")

sent_part = ["This is the ", f" of {firstNum} & {secondNum}: "]
op_names = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "lesser Exponentiation",
    "improper fraction (x>1)",
    "Floor (Integer based Quotient)",
    "greater Exponentiation",
    "proper fraction (0<x<1)",
]
op_calc = [
    firstNum + secondNum,
    firstNum - secondNum,
    firstNum * secondNum,
    firstNum ** secondNum,
    firstNum / secondNum,
    firstNum // secondNum,
]
S = [sent_part, op_names, op_calc]
r = [S[0][0], S[0][1]]
# These prints out the given Strings & basic operations of given numbers
# by interpolating array elements as a list of strings (through multiple interpolatory layers)
for i in range(0, 3):
    print(f"{r[0]+S[1][i]+r[1]}({S[2][i]}).\n")
    continue

if firstNum > secondNum:
    for i in range(3, 6):
        print(f"{r[0]+S[1][i]+r[1]}({S[2][i]}).\n")
        continue

elif firstNum < secondNum:
    print(f"{r[0]+S[1][5]+r[1]}(0).\n")
    print(f"{r[0]+S[1][6]+r[1]}({S[2][3]}).\n")
    print(f"{r[0]+S[1][7]+r[1]}({S[2][4]}).\n")

elif secondNum == 1:
    print("No other operation is necessary in this case")

elif firstNum == secondNum:
    print(
        f"This is the Power tower of Second Order (^^2) for {firstNum} (Hence, 1st Number {firstNum} = 2nd Number {secondNum}):"
    )
    print(firstNum ** secondNum)
    print(
        f"The fraction (0<x<1) of {secondNum} & {firstNum} = 1 logically, which is unitary\n\n"
    )


# How to refine multiple errors by defining an external (user-built) function

defined_string = (
    "Repeated VAR(DataType==p0STRING) 4 times to fix spelling issue ALL AT ONCE!"
)


def pr_string_var():
    variable = defined_string
    print(f"{variable}\n" * 4)


pr_string_var()
print("~~END of Repetitions~~")

# Alternate Method of the same definer function


def pr_string_var(text):
    print(f"{text}\n" * 4)


pr_string_var(defined_string)
print("~~END of Repetitions~~")

# While Loop
print("~~Odd numbers below Ten~~")
x = 1
while x < 10:
    print(x)
    x = x + 2
    continue
del x
# For Loop
print("~~Odd numbers between Ten & Twenty~~")
for i in range(11, 20, 2):
        print(i)
        continue

# Array Integration in the for-Loop
WeekDays = ["Fri", "Satur", "Sun", "Mon", "Tues", "Wednes", "Thurs"]

for d in WeekDays:
    print(f"Today is {d}day")


print("This is a basic password generator")
passlen = int(input("Length of password? (should be <75):"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s, passlen))
print(p)
