# password Validation using python program

#Its import regular expression to manipulate string and integer
import re

#Get input from user
Password=input("enter a password")

#This pattern is used to identify the integer
pattern=re.findall(r"\d",Password)

#It checks Given input contain integer or not if integer it return true else it return false
check=(bool(pattern))

# It is a state for checking integers
digit=0

#It change the state
if check:
    digit=1

#It is a state for checking Upper
upper=0

#It is check for the given input is contain atleast uppercase by iteration
for i in Password:
    k=i.isupper()
    if k:
        upper=1

#It is a state for final output for checking all the three condition
result=0

if upper>0 :
    result=result+1
else:
    print("password must have one upper case ")

if  len(Password)>=6 :
    result=result+1
else:
    print("Password must contain atleast 6 characters")

if digit>0:
   result=result+1
else:
    print("password atleast have one digit")

if result==3:
    print("password validate successfully")

