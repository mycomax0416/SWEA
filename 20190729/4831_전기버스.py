import sys
sys.stdin = open('4831_전기버스_input.txt', 'r')

T = int(input())
for t in range(T):
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))
    charge_stations.append(300)

    count = 0
    point = 0
    while point + K < N:
        if charge_stations[0] - point > K:
            count = 0
            break
        else:
            idx = 0
            while charge_stations[idx] - point <= K:
                idx += 1
            point = charge_stations[idx-1]
            charge_stations = charge_stations[idx:]
            count += 1

    print('#{} {}'.format(t+1, count))