import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation # This will take all type of charecters like letters,digits,special charecters.
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        length = int(input("Enter the password length you want to generate(More than 5 will be a good choice): ")) # Taking input of the length of the password by user.
        if length > 0:
            print(f"Generated strong password: {generate_password(length)}")
        else:
            print(" This is a invalid length. Please enter a positive integer.")
    except ValueError:
        print("This is a invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()

