"""
https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
"""
import json

if __name__ == '__main__':

    with open("birthdays.json", "r") as f:
        birthdays = json.load(f)

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
