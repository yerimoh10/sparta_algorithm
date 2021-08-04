input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_0_to_1 = 0
    count_1_to_0 = 0
    for index in string:
        if index == '0':
            count_0_to_1 += 1
        else:
            count_1_to_0 += 1
    if len(string) > 0 and (count_1_to_0 == 0 or count_0_to_1 == 0):
        return len(string)
    return min(count_1_to_0, count_0_to_1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)