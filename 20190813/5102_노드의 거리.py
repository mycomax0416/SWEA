import sys
sys.stdin = open('5102_노드의 거리_input.txt', 'r')


def func(start):
    queue = [(start, 1)]
    visit = [False for _ in range(V+1)]
    visit[start] = True
    while queue:
        node, cnt = queue.pop(0)
        for n in graph[node]:
            if n == G:
                return cnt
            elif not visit[n]:
                queue.append((n, cnt+1))
                visit[n] = True
    return 0


T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())

    ans = func(S)

    print('#{} {}'.format(t+1, ans))