import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
characters = ['.',',','?','!',';']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def password():
    new_password = ""
    for x in range(3):
        new_password += random.choice(alphabet)
        new_password += random.choice(characters)
        new_password += random.choice(characters).upper()
        new_password += random.choice(numbers)
    print(new_password)

password()