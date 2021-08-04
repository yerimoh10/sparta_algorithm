seat_count = 9
vip_seat_array = [4, 7]     # 고정되어 있는 좌석
# 최대 한 좌석만 이동할 수 있다

memo = {
    1: 1,
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1        # 곱의 연산을 사용할 것이기에 1로 두기도 하고, 아무 자리도 옮기지 않았을 경우의 수도 1이기 때문에 1로 시작한다.
    current_index = 0
    for fixed_seat in fixed_seat_array:  # fixed_seat_array = [4, 7] -> index 가 아니라 번호이다.
        fixed_seat_index = fixed_seat - 1   # 그래서 1을 빼줌으로써 배열의 index 값을 구할 수 있다.
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        # fixed_seat_index - current_index = 사이 사이에 있는 변경할 수 있는 좌석들의 개수가 나온다. [(123) 4 (56) 7 (89)
        # count_of_ways = 고정된 좌석 사이 사이마다 있는 좌석들에서 나올 수 있는 경우의 수
        all_ways *= count_of_ways   # 곱 연산
        current_index = fixed_seat_index + 1    # 0 1 2 3 을 해 주었기 때문에 4 부터 진행하라고
    # 위 for 문은 7까지 진행되고 끝난다. 그래서 7 뒤에 있는 좌석들도 경우의 수를 구해야 하기 떄문에
    # total_count 에서 current_index 를 뺀 수를 다시 피보나치 함수에 돌려 경우의 수를 구한다.
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))