import sys
sys.stdin = open('1259_금속막대_input.txt', 'r')

T = int(input())
for t in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    screws = []
    for _ in range(n):
        screws.append((arr.pop(0), arr.pop(0)))
    left, right = screws.pop()
    link = [left, right]
    while screws:
        for idx in range(len(screws)):
            if screws[idx][0] == right:
                screw_left, screw_right = screws.pop(idx)
                right = screw_right
                link.append(screw_left)
                link.append(screw_right)
                break
            elif screws[idx][1] == left:
                screw_left, screw_right = screws.pop(idx)
                left = screw_left
                link.insert(0, screw_right)
                link.insert(0, screw_left)
                break
            
    print('#{} {}'.format(t+1, ' '.join(map(str, link))))