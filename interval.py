### 비결정적 알고리즘 구현 연습
### N개의 블록으로 구성된 초콜릿을 Z개의 조각으로 나누는 모든 경우의 수 출력


N = int(input("Number of chocolate blocks : "))
Z = int(input("Number of pieces to split : "))


# 초콜릿 = [0, 1, 2, ..., N-1]
cho = []
for i in range(0, N) :
    cho.append(i)


# 각 조각의 끝부분 인덱스
# [0], [1], [2], ..., [Z-3], [Z-2], [N-1]
ends = []
for i in range(0, Z-1) :
    ends.append(i)
ends.append(N-1)


while (True) :

    # 현재 경우 출력
    start = 0
    for i in range(0, Z) :
        print(cho[start:ends[i]+1], end = " ")
        start = ends[i] + 1
    print()

    # 다음 경우 만들기
    X = Z - 2                               # (Z-2)번째 조각의 구간부터 늘려보기  시작
    while (X >= 0) :
        # X번째 조각의 구간을 늘릴 수 있다면
        if (ends[X] < N+X-Z) :
            ends[X] = ends[X] + 1           # X번째 조각의 구간을 늘리고
            for k in range(X+1, Z-1) :      # (X+1)번째 ~ (Z-2)번째 조각의 구간은
                ends[k] = ends[k-1] + 1     # 다시 길이 1로 돌려놓음
            break                           # 새로운 경우를 만들었으니 while문 탈출
        # X번째 조각의 구간을 더 이상 늘릴 수 없다면
        else :
            X = X - 1                       # 이제는 (X-1)번째 조각의 구간을 늘려봐야 함

    # 0번째 조각의 구간도 더 이상 늘릴 수 없다면 모든 경우의 수 계산이 끝난 것
    if (X < 0) :
        break

