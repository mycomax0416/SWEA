import sys
sys.stdin = open('4871_그래프 경로_input.txt', 'r')

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    path = [[] for _ in range(V+1)]
    visit = [False for _ in range(V+1)]
    for e in range(E):
        A, B = map(int, input().split())
        path[A].append(B)
    S, G = map(int, input().split())
    
    ans = 0
    stack = [S]
    visit[S] = True
    while stack:
        pre = S
        if S == G:
            ans = 1
            break
        for n in path[S]:
            if visit[n] == False:
                stack.append(n)
                S = n
                visit[n] = True
                break
        if pre == S:
            S = stack.pop()

    print('#{} {}'.format(t+1, ans))