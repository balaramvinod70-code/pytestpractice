#11.	Write a program using if statement to check whether a number is positive, negative or zero.
from math import factorial
from unittest import case

n=int(input("Enter the no:"))
if n>0:
    print("this is positive")
elif n<0:
    print("this is negative")
else:
    print("this is zero")

#12.	Write a program to print factorial of a number using a for loop (no math module).
#14.14Given a list:
 #nums = [10, 20, 30, 40, 50]
#Print using slicing:
#	a) First three
#	b) Last two
#	c) Reverse list"""
nums = [10, 20, 30, 40, 50]
print(nums[0:3])
print(nums[-1])
print(nums[::-1])

#13.	Write a match-case program:
weekdays=int(input("Enter the weekday from 1 to 2:"))
match weekdays:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Invalid Day")
#12.	Write a program to print factorial of a number using a for loop (no math module).

num=int(input("Enter the no:"))
factorial=1
for i in range(1,num+1):
    factorial*=i
print(factorial)

#15.15.	Write a program to count vowels in a string using a loop.

t=str(input("Enter any name:"))
t=t.lower()
count=0
for i in range(10):
    if 'aeiou' in t:
        count+=1
print("number of vowels are:",count)

#16.16.	Write a program to print keys & values from a dictionary using items()

a={"name":"vinoth","age":36}
print(a.items())