from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    # 구현해보세요!
    time = 0    # 항상 시간을 점검해야 하니 time 변수 필요
    queue = deque()
    queue.append((brown_loc, 0))    # 위치와 시간을 함께 queue 에 포함시켜 준다. [브라운위치][시간]

    # 성공조건을 위한 배열 (코니와 브라운의 위치와 시간이 동일해야 한다.)
    visited = [{} for _ in range(200001)]   # 방문한 시간와 위치를 저장하기 위해 배열을 만든다.
                                            # 위치마다 브라운이 방문한 시간을 적기 위해 배열 안에 딕셔너리를 넣는다.
    # 5 in visited[3] 는 5초에 위치 3을 방문했는지 여부를 저장하고,
    # 9 in visited[3] 는 9초에 위치 3을 방문했는지 여부를 저장한다.
    # visited[위치][시간]
    # visited[cony_loc][time]

    while cony_loc <= 200000:
        cony_loc += time    # +1 +2 +3 +4 +5 .... 시간만큼 가속도가 붙기 때문에
        if time in visited[cony_loc]:
            return time     # 코니와 브라운이 만나는 시점 return

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

            new_position = current_position - 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1

    return -1   # 코니 위치가 조건에 부합하지 않는다면 -1을 return 한다.


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))

