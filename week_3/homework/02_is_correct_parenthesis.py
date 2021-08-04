s = "((())))"


def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    else:
        return True

    # first_small_letter_exist = 0
    # last_small_letter_exist = 0
    # for letter in string:
    #     if letter == '(':
    #         first_small_letter_exist += 1
    #     elif letter == ')':
    #         last_small_letter_exist += 1
    # if first_small_letter_exist == last_small_letter_exist:
    #     return True
    # else:
    #     return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))