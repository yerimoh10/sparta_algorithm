input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        num = ord(char) - 97
        array[num] += 1
    max_index = 0
    for index in range(len(array)):
        max_num = array[0]
        if max_num < array[index]:
            max_num = array[index]
            max_index = index
    return chr(max_index + ord("a"))
    # 선생님 예제
    # alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    #                   "t", "u", "v", "x", "y", "z"]
    # max_occurrence = 0
    # max_alphabet = alphabet_array[0]
    # for alphabet in alphabet_array:
    #     occurrence = 0
    #     for char in string:
    #         if char == alphabet:
    #             occurrence += 1
    #     if occurrence > max_occurrence:
    #         max_occurrence = occurrence
    #         max_alphabet = alphabet
    # return max_alphabet


result = find_max_occurred_alphabet(input)
print(result)
