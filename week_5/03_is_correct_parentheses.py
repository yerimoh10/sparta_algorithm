from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parentheses(string): # 올바른 괄호 문자열인지 확인해 주는 함수
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0      # stack에 아무것도 남아있지 않다면 올바른 괄호 문자열임을 알 수 있다.


# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = ''.join(list(queue))
    # print(u, v)
    return u, v


# 4번 - else에서 빼온 함수
def revers_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string


def change_to_correct_parentheses(string):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if string == "":
        return ""

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = separate_to_u_v(string)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    if is_correct_parentheses(u):
        return u + change_to_correct_parentheses(v)    # 재귀함수 사용

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    #  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #   4-3. ')'를 다시 붙입니다.
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    #   4-5. 생성된 문자열을 반환합니다.
    else:
        return "(" + change_to_correct_parentheses(v) + ')' + revers_parentheses(u[1:-1])  # 4-1 ~ 4-3


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)

    # ')' 가 나오면 queue 에다가 넣어놨다가, '(' 가 나오는 것을 확인하면, '('의 개수별로
    # queue 에 있던 얘들을 popleft() 시키면 된다.


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!