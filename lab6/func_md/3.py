def is_palindrome(string):
    return string == string[::-1]
string = "racecar"
if is_palindrome(string):
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
