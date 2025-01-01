import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length.

    Parameters:
        length (int): The desired length of the password.

    Returns:
        str: The generated password.
    """
    if length < 4:  # Ensure the password is long enough for complexity
        return "Password length must be at least 4 characters."

    # Define character sets for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one of each type of character
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt the user to specify the password length
        length = int(input("Enter the desired length of the password: "))
        # Generate the password
        password = generate_password(length)
        # Display the password
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
