# Read input string
s = input().strip()

# Convert to lower case for palindrome check
def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

if is_palindrome(s):
    print("palindrome")
else:
    print("not palindrome")
