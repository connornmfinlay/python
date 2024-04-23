import random
import string

def generate_password(length=8):
    char = string.ascii_letters + string.digits + string.punctuation
    chars = char.replace('i', '').replace('I','')
    password = ''.join(random.choice(chars)  for i in range(length))

    return password

if __name__ == '__main__':
    password = generate_password()
    print(password)