numbers = [1, 1, 1, 1, 1]
target_number = 3
target_count = 0


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array):
        if current_sum == target_number:
            global target_count
            target_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - array[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)  # 5를 반환해야 합니다! target_number
print(target_count)