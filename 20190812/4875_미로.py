import sys
sys.stdin = open('4875_미로_input.txt', 'r')


def find_start():
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                return x, y


# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def go_maze(start_x, start_y):
    stack = [(start_x, start_y)]
    visit = [[False for _ in range(N)] for _ in range(N)]
    visit[start_y][start_x] = True
    while stack:
        x, y = stack[-1]
        pre_x, pre_y = x, y
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visit[ny][nx] == False:
                if maze[ny][nx] == 0: 
                    stack.append((nx, ny))
                    visit[ny][nx] = True
                    x, y = stack[-1]
                    break
                elif maze[ny][nx] == 3:
                    return 1
        if pre_x == x and pre_y == y:
            stack.pop()
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]

    x, y = find_start()
    
    print('#{} {}'.format(t+1, go_maze(x, y)))