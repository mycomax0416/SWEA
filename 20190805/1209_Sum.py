import sys
sys.stdin = open('1209_Sum_input.txt', 'r')

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    sums = []
    for y in range(100):
        sums.append(sum(arr[y]))
    cro1 = []
    cro2 = []
    for idx in range(100):
        cro1.append(arr[idx][idx])
        cro2.append(arr[99-idx][99-idx])
    sums.append(sum(cro1))
    sums.append(sum(cro2))
    for y in range(100):
        for x in range(y, 100):
            arr[y][x], arr[x][y] = arr[x][y], arr[y][x]
    for y in range(100):
        sums.append(sum(arr[y]))
    
    print('#{} {}'.format(t, max(sums)))