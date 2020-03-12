import sys
sys.stdin = open('1208_Flatten_input.txt', 'r')

for t in range(10):
    cnt = int(input())
    heights = list(map(int, input().split()))
    heights.sort()
    
    while cnt != 0:
        heights[0] += 1
        heights[-1] -= 1
        heights.sort()
        cnt -= 1

    print('#{} {}'.format(t+1, heights[-1]-heights[0]))