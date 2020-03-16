import sys
sys.stdin = open('4869_종이붙이기_input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())

    arr = [(10, 1), (20, 3)]
    while arr[-1][0] != N:
        arr.append((arr[-1][0]+10, arr[-1][1]+arr[-2][1]*2))
    
    print('#{} {}'.format(t+1, arr[-1][1]))


# def func(n):
#     if n < 1:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 3
#     else:
#         return func(n-1) + func(n-2)*2
    
# T = int(input())
# for t in range(T):
#     N = int(input())
    
#     print('#{} {}'.format(t+1, function(N//10)))