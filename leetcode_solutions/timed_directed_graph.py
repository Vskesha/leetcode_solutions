from collections import defaultdict


def network_delay_time(times, n, k):
    nodes = defaultdict(list)
    time = [-1] * n
    for fr, to, tim in times:
        nodes[fr].append((to, tim))

    def move_from(fr):
        for to, tim in nodes[fr]:
            if time[to-1] == -1 or time[to-1] > time[fr-1] + tim:
                time[to-1] = time[fr-1] + tim
                move_from(to)

    time[k - 1] = 0
    move_from(k)
    mx = time[0]
    for t in time:
        if t == -1:
            return -1
        if t > mx:
            mx = t
    return mx


if __name__ == '__main__':
    print('2 ===', network_delay_time(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
    print('1 ===', network_delay_time(times=[[1, 2, 1]], n=2, k=1))
    print('-1 ===', network_delay_time(times=[[1, 2, 1]], n=2, k=2))
