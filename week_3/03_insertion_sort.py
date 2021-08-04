input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):      # print(i-j)
            if array[i-j-1] > array[i-j]:
                array[i-j-1], array[i-j] = array[i-j], array[i-j-1]
            else:
                break   # 비교할 필요가 없을 때 break 를 한다. 즉, 더 효율적임
    return


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!