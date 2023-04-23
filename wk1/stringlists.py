"""
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

# Ask the user for a string and reverse it
user_string = input("Please enter a string: ")
reversed_string = user_string[::-1]

# work out if palindrome and print out whether this string is a palindrome or not
if reversed_string == user_string:
    print('This is a Palindrome!')
else:
    print('This is a not Palindrome!')