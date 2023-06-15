string = "kayak"


def reversing_string(string):
    if (string == ""):
        return ""
    return reversing_string(string[1:]) + string[0]


reversed_string = reversing_string(string)
print(str)


def is_palindrome(string, reversed_string):
    if (string == reversed_string):
        return True
    else:
        return False


print(is_palindrome(string, reversed_string))
