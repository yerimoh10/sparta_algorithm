current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 0 은 청소하지 않은 장소,
# 1은 청소하지 못하는 장소,
# 2는 청소한 장소


# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방향 전환
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4
# 북 (왼쪽으로 회전) -> 서 : 0 -> 3    =>  (0 + 3) % 4 = 3
# 동 (왼쪽으로 회전) -> 북 : 1 -> 0    =>  (1 + 3) % 4 = 0
# 남 (왼쪽으로 회전) -> 동 : 2 -> 1    =>  (2 + 3) % 4 = 1
# 서 (왼쪽으로 회전) -> 님 : 3 -> 2    =>  (3 + 3) % 4 = 2
# ==> rotate -> index 가 (+ 3 % 4)


# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4
# 북 (후진) -> 남 : 0 -> 2    =>  (0 + 2) % 4 = 2
# 동 (후진) -> 서 : 1 -> 3    =>  (1 + 2) % 4 = 3
# 남 (후진) -> 븍 : 2 -> 0    =>  (2 + 2) % 4 = 0
# 서 (후진) -> 동 : 3 -> 1    =>  (3 + 2) % 4 = 1


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    count = 1               # 청소하는 칸의 개수
    n = len(room_map)       # row
    m = len(room_map[0])    # column
    room_map[r][c] = 2      # 청소가 된 칸은 2로 업데이트 시킨다
    queue = list([[r, c, d]])   #

    while queue:        # queue 가 끝날 때 까지 반복한다
        r, c, d = queue.pop(0)      # queue에 들어 있는 첫번째 칸을 꺼낸다
        temp_d = d      # 방향이 계속 돌아가기 때문에 임시 방향을 변수로 설정해준다
        for i in range(4):      # 모든 방향에 대해서 갈 수 있는 방향을 구한다
            temp_d = get_d_index_when_rotate_to_left(temp_d)    # 왼쪽으로 회전
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]       # 왼쪽으로 회전시 새로운 row 와 column 의 위치 변동

            # 새로운 row와 새로운 column의 칸이 len() 을 넘어가지 않고, 또 0으로 청소되지 않았다면
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][new_c] == 0:
                count += 1      # 그 칸을 청소를 하는 칸이기 때문에 청소한 칸의 변수에 1을 더하고
                room_map[new_r][new_c] = 2      # 이 칸은 청소 되었다는 의미로 2를 2차원 배열에 작성해 준다.
                # 새로운 칸을 queue 에 추가해 주는데, 이동한 칸에서 다시 한 번 탐색을 해 주어야 하기 때문이다.
                queue.append([new_r, new_c, temp_d])
                break   # 탐색해서 올바른 방향이 나왔다면 break 로 for 문을 빠져나간다.
            elif i == 3:    # 네 방향이 모두 청소가 되어 있거나, 벽일 경우, 후진한다.
                # get_d_index_when_go_back -> 뒤로 가는 함수를 사용해 row 와 column 을 변경한다.
                new_r, new_c = r + dr[get_d_index_when_go_back(temp_d)], c + dc[get_d_index_when_go_back(temp_d)]
                queue.append([new_r, new_c, temp_d])
                # 후진하여 새로운 장소로 옮겼는데 1 = 벽인 경우,
                if room_map[new_r][new_c] == 1:
                    return count    # 다 청소 했다고 생각하고 청소한 칸의 값을 반환해준다.


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,3,1,current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7,4,1,current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6,2,0,current_room_map4))