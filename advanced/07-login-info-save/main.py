import re

EMAIL_REGEX = r'^\w[\w\.\-]*@\w+\.\w+$'

def get_valid_email():
    while True:
        email = input("Enter your email: ")
        if re.match(EMAIL_REGEX, email):
            return email
        else:
            print("Invalid email format. Example: expression@string.string")

def get_valid_password():
    while True:
        password = input("Enter your password (must contain letters and numbers): ")
        has_digit = any(c.isdigit() for c in password)
        has_alpha = any(c.isalpha() for c in password)
        if has_digit and has_alpha:
            return password
        else:
            print("Password must include both letters and digits.")

def save_to_file(email, password, filename="login_db.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{email},{password}\n")

if __name__ == "__main__":
    email = get_valid_email()
    password = get_valid_password()
    save_to_file(email, password)
    print("Your information has been saved.")
