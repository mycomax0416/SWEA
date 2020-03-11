import sys
sys.stdin = open('4834_숫자 카드_input.txt', 'r')

# T = int(input())
# for t in range(T):
#     N = int(input())
#     nums = list(input())
#     cnts = dict()
#     for num in nums:
#         if num not in cnts:
#             cnts[num] = 1
#         else:
#             cnts[num] += 1
#     max_num, max_cnt = 0, 0
#     for key, val in cnts.items():
#         key = int(key)
#         if max_num < key and max_cnt <= val:
#             max_num, max_cnt = key, val
#     print('#{} {} {}'.format(t+1, max_num, max_cnt))

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(input())

    max_num = 0
    max_cnt = 0
    cnts = [0 for _ in range(10)]
    for num in nums:
        cnts[int(num)] += 1
    for idx in range(10):
        if max_cnt <= cnts[idx]:
            max_num = idx
            max_cnt = cnts[idx]
    print('#{} {} {}'.format(t+1, max_num, max_cnt))