def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for st in string:
        if not st.isalpha():
            continue    # 공백문자 걸러내기
        num = ord(st) - 97
        alphabet_occurrence_array[num] += 1
        # 이 부분을 채워보세요!

    return alphabet_occurrence_array
    # for char in string:
    #     if not char.isalphar():
    #         continue
    #     arr_index = ord(char) - ord("a")
    #     alphabet_occurrence_array[arr_index] += 1

print(find_alphabet_occurrence_array("hello my name is sparta"))