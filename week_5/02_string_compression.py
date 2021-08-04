input = "abcabcabcabcdededededede"
# 모든 경우의 수를 파악하여 가장 짧은 문자열의 길이를 넘겨주어야 한다.
# 소문자가 들어왔는지 체크하기
# 1로 자른 문자열의 길이
# 첫 문자와 바로 다음 문자가 동일한 경우
    # 그 다음 문자 (3번째 문자)와도 동일한지 체크
    # 다른 문자가 나올 때까지 체크하고 동일한 문자의 수의 길이로 문자열 자르기 (1)
# 첫 문자가 바로 다음 문자와 이어지지 않는 경우
    # 그 다음 문자 확인하여 첫 문자와 이어붙이기
    # 이어 붙인 다음 세번째 네번쨰 문자와 동일한지 비교 (2)
    # 다른 문자가 나올 때까지 체크하고 동일한 문자의 수의 길이로 문자열 자르기 (1)
        # 세번째 문자까지 한 문자열로 보고 4,5,6 번째 문자열과 비교해서 동일하다면 문자 수대로 문자열 자르기
# 2, 3, 4, 5 ... 로 잘랐을때 동일한 문자열이 있는지 체크
# 그 중 문자열이 가장 짧은 것 return


def string_compression(string):
    n = len(string)
    compression_length_array = []

    for split_size in range(1, n // 2):     # 문자열을 나누는 기준을 구하는 반복문, 1 ~ n // 2(반까지만 구하면 됨)
        splited = [string[i:i+split_size] for i in range(0, n, split_size)]
        # 0부터 n까지 split_size 만큼
        # print(splited)
        compressed = ""     # 압축할 수 있는 문자열인지 비겨하기 위해 저장해두는 변수
        count = 1   # splited 에서 자른 문자열을 비교하기 위해 사용
        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]  # 첫 문자열과 다음 문자열 비교
            if prev == cur:     # 0번째와 1번쨰
                count += 1
            else:       # 이전 문자와 다르다면
                if count > 1:
                    compressed += (str(count) + prev)
                else:       # 문자가 반복되지 않을 때
                    compressed += prev
                count = 1       # 초기화
        if count > 1:       # splited 배열의 마지막 문자까지 앞 문자와 동일하다면
            compressed += (str(count) + splited[-1])
        else:               # 동일하지 않다면 그냥 문자열 추가
            compressed += prev
        compression_length_array.append(len(compressed))
    return min(compression_length_array)


print(string_compression(input))  # 14 가 출력되어야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))
