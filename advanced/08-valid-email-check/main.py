import re

EMAIL_REGEX = r'^\w[\w\.\-]*@\w+\.\w+$'

def is_valid_email(email):
    return re.match(EMAIL_REGEX, email) is not None

if __name__ == "__main__":
    email = input()
    if is_valid_email(email):
        print("OK")
    else:
        print("WRONG")
