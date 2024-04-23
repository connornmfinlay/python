import random
import string
import pyperclip

def generate_password(length=10):
    # Ensure at least 3 lowercase letters, 3 uppercase letters, 3 numbers, and 1 symbol
    num_lower = 3
    num_upper = 3
    num_digits = 3
    num_symbols = 1

    if length < num_lower + num_upper + num_digits + num_symbols:
        raise ValueError("Password length is too short to meet the requirements.")

    # Generate characters for each category
    lower_chars = ''.join(random.choice(string.ascii_lowercase.replace('l', '')) for _ in range(num_lower))
    upper_chars = ''.join(random.choice(string.ascii_uppercase.replace('I', '').replace('O','')) for _ in range(num_upper))
    digit_chars = ''.join(random.choice(string.digits.replace('1', '')) for _ in range(num_digits))
    symbol_chars = ''.join(random.choice(string.punctuation.replace('|','')) for _ in range(num_symbols))

    # Combine characters from all categories
    chars = lower_chars + upper_chars + digit_chars + symbol_chars

    # Fill the remaining length with random characters
    remaining_length = length - (num_lower + num_upper + num_digits + num_symbols)
    random_chars = ''.join(random.choice(string.ascii_letters.replace('lI', '') + string.digits.replace('1', '') + string.punctuation) for _ in range(remaining_length))

    # Shuffle the password to randomize the order
    password_list = list(chars + random_chars)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    password = generate_password()
    print(password)
    pyperclip.copy(password)
