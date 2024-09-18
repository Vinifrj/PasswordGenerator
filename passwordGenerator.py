import random
import string

class ShortPasswordException(Exception):
    pass

def generatePassword(size):

    try:
        if size < 16:
            raise ShortPasswordException
        else:
            passGen = string.printable
            passGen = passGen.strip()
            passGen = list(passGen)
            random.shuffle(passGen)

            password = ''

            for i in range(size):
                password += random.choice(passGen)

            return password 
    except ShortPasswordException:
        print('Password is too short! Password must be at least 16 characters long!')

size = int(input('How long do you want your password? '))
password = generatePassword(size)

while password is None:
    size = int(input('How long do you want your password? '))
    password = generatePassword(size)

print(password)