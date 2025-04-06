import random

print('welcome to password generator')

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!()@#$%&*.,1234567890'

number = input('Amount of password to generate:')
number = int(number)

length = input('Input your passworld length:')
length = int(length)

print('\nhere is your password:')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(char)
    print(password)
        
       