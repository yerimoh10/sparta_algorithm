import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]  # dates
supply_supplies = [20, 5, 10]   # supplies
supply_recover_k = 30       # k


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    heap = []
    answer = 0          # 최소한 해외 공장으로부터 몇번 공급 받아야 하는지
    last_added_data_index = 0   # 공장이 멈추지 않는 한 가장 마지막에 넣은 날짜의 인덱스 값
    while stock <= k:       # 남은 물량이 원래 공장에서 공급받을 수 있을 때까지 반복
        # last_added_data_index 가 dates 배열의 길이를 넘어가면서 조회하지 않도록 탈출 조건 작성
        # 날짜 배열의 값이 stock 의 값보다 작거나 같아야 공장을 돌리 수 있기 때문에 조건을 담
        while last_added_data_index < len(dates) and dates[last_added_data_index] <= stock:
            heapq.heappush(heap, -supplies[last_added_data_index])
            # 현재 stock 보다 적거나 같은 날짜에 공급 받을 수 있는 supplies 의 값을 heap 에 push 한다.
            last_added_data_index += 1  # 최소한으로 공급을 받아야 하니 날짜를 올려 dates 배열에 가능한 날짜가 있는지 확인해본다.

        answer += 1     # 위에 while 문을 돌고 나왔으면 일단 공급을 받았단 이야기이기 때문에 answer에 1을 더해준다.
        heappop = heapq.heappop(heap)
        stock += -heappop   # 공급을 받았기 때문에 stock에 heap의 최상위에 있는 supplies의 값을 더해준다.
    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))
