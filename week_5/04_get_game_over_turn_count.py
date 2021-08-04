k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

# 동 → 서 : 0 → 1
# 서 → 동 : 1 → 0
# 북 → 남 : 2 → 3
# 남 → 북 : 3 → 2
# ==> 홀 수 = -1 / 짝수 = + 1


def get_d_index_when_go_back(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

# 말은 순서대로 이동한다. -> 말의 순서에 따라 반복문
# 말이 쌓일 수 있다. -> 맵에 말이 쌓이는 걸 저장해놔야 한다.
# 쌓인 순서대로 이동한다. -> stack 사용
# 현재 맵에 어떻게 말이 쌓일지 저장하기 위해서 리스트를 만들어 준다.


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    current_stacked_horse_map = [       # 3차원 배열
        [
            [] for _ in range(n)
        ] for _ in range(n)
    ]
    for i in range(horse_count):
        r, c, d = horse_location_and_directions[i]      # row, column, direction
        current_stacked_horse_map[r][c].append(i)
    turn_count = 1

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index]
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 파란색이거나 맵을 나갔을 때
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 가기로 한 곳이 막혀 있으면 안감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue

            # 2가 이동한다고 하면 2랑 3만 이동한다.
            # 즉, 자기자신의 인덱스보다 큰 애들만 데리고 간다.
            moving_horse_index_array = []   # 이동할 말만 넣어주는 변수
            for i in range(len(current_stacked_horse_map[r][c])):
               current_stacked_horse_index = current_stacked_horse_map[r][c][i]

               if horse_index == current_stacked_horse_index:  # 현재 이동하고 있는 말과 위치에 저장되어 있는 말의 index가 같은지 확인한다.
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]  # 위로 쌓여 있는 index 애들을 업고 함께 움직이기 때문
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]   # 현재 위치에는 남은 애들 (첫 인덱스와 i번째 까지의 말)을 다시 저장해준다.
                    break   # 현재 이동하려고 하는 말을 알았으면 반복문을 중단한다.
            if game_map[new_r][new_c] == 1:     # 이동하려는 칸의 위치가 1이면 방향(direction)을 변경해야 한다.
                moving_horse_index_array = reversed(moving_horse_index_array)
            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c
            # 턴이 진행되는 중 말이 4개 이상 쌓이는 순간 게임이 종료된다.
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count
        turn_count += 1

    # print(current_stacked_horse_map)    # 현재 각 체스 말들이 어떻게 쌓여져 있는지 저장해 놓는 공간이 된다.

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다