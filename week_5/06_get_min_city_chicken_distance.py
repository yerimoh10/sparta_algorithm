import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]
# 여러 개 중에서 M 개를 고른뒤, 모든 치킨거리의 합이 가장 작게 되는 경우 반환
# -> 여러 개 중에서 특정 개수를 뽑는 경우의 수 + 모든 경우의 수를 다 구해야 함
# ==> "조합" 사용


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:     # 집
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:   # 치킨 집
                chicken_location_list.append([i, j])
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combinations in chicken_location_m_combinations:
        city_chicken_distance = 0    # 현재 도시의 치킨 거리
        for home_r, home_c in home_location_list:       # 각 거리의 치킨 거리를 구할 수 있다.
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combinations:
                min_home_chicken_distance = min(min_home_chicken_distance,
                                                abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1]))
            city_chicken_distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)
    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
print("hihi")