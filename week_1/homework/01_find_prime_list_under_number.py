input = 20


def find_prime_list_under_number(number):
    prime_array = []
    if number < 2:
        return 0 #소수는 없다.
    for num in range(2, number+1):
        for n in prime_array:
            if num % n == 0 and n * n <= num:
                break
        else:
            prime_array.append(num)

    return prime_array


result = find_prime_list_under_number(input)
print(result)