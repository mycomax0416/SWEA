import sys
sys.stdin = open('4828_min max_input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    print('#{} {}'.format(t+1, max(numbers)-min(numbers)))