import sys
sys.stdin = open('5105_미로의 거리_input.txt', 'r')


def find_start():
    for y in range(N):
        for x in range(N):
            if maze[y][x] == '2':
                return x, y

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def go_maze(start_x, start_y, start_cnt):
    queue = [(start_x, start_y, start_cnt)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_y][start_x] = True
    while queue:
        x, y, cnt = queue.pop(0)
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and maze[ny][nx] != '1' and visit[ny][nx] == False:
                queue.append((nx, ny, cnt+1))
                visit[ny][nx] = True
                if maze[ny][nx] == '3':
                    return cnt
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    x, y = find_start()
    ans = go_maze(x, y, 0)

    print("#{} {}".format(t+1, ans))