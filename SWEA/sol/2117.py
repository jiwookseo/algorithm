# 2117. [모의 SW 역량테스트] 홈 방범 서비스
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V61LqAf8DFAWu&categoryId=AV5V61LqAf8DFAWu&categoryType=CODE

f = [0, 1]
g = [[]]
 
def fee(i):
    global f
    if len(f) > i:
        return f[i]
    else:
        f.append(fee(i - 1) + 4 * (i - 1))
        return f[i]
 
def grid(n):
    global g
    if len(g) > n:
        return g[n]
    else:
        g.append(grid(n - 1) + [(i, j) for i in range(-n + 1, n) for j in range(-n + 1, n) if abs(i) + abs(j) == n - 1])
        return g[n]
 
def check(n):
    global board, result, N
    d = grid(n)
    maxi = 0
    for r in range(N):
        for c in range(N):
            count = 0
            for dr, dc in d:
                tr, tc = r + dr, c + dc
                if 0 <= tr < N and 0 <= tc < N:
                    if board[tr][tc]:
                        count += 1
            if count > maxi:
                maxi = count
    return maxi
 
for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    hn = sum([sum(board[i]) for i in range(N)])
    max_fee = M * hn
    i = 1
    while fee(i) < max_fee:
        i += 1
    max_try = i
    for i in range(max_try - 1, 0, -1):
        temp = check(i)
        if M * temp - fee(i) >= 0:
            result = temp
            break
    print("#{} {}".format(TC, result))
