input = "abcba"


# 회문 검사

def is_palindrome(string):
    length = len(string)
    for i in range(length):
        print(string[length - 1 - i])
        if string[i] is not string[length - 1 - i]:
            return False
    return True


print(is_palindrome(input))
