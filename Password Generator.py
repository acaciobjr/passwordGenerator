import random
print('welcome to your Password Generator')

chars= ('abcdefghijklmnopqrstuywx1234567890*#$+=.;')

number = input('How many passwords do you want?: ')
number = int(number)

length = input('What size password do you want?: ')
length = int(length)

print('here are your passwords: ')

for psw in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
