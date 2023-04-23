"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""

# ask the user for a number 
number = int(input("Please enter a number: "))
print(number)

# calculate the list of divisors
divisor_list = []
for n in range(1,number+1):
    if number % n == 0:
        divisor_list.append(n)

print(divisor_list)
