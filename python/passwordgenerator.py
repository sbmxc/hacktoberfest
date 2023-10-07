import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    password = generate_password(password_length)
    print("Generated Password:", password)
