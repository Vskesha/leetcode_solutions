from queue import Queue


def predict_party_victory(senate: str) -> str:
    radiants = 0
    sen = Queue()
    for c in senate:
        sen.put(c)
        if c == 'R':
            radiants += 1
    dires = len(senate) - radiants

    ban = 0  # positive if banned dires and negative when banned radiants
    while radiants and dires:
        c = sen.get()
        if c == 'R':
            if ban >= 0:
                sen.put(c)
                dires -= 1
            ban += 1
        else:
            if ban <= 0:
                sen.put(c)
                radiants -= 1
            ban -= 1

    return 'Radiant' if radiants else 'Dire'


def predict_party_victory5(senate: str) -> str:
    ls = len(senate)
    r_que = Queue()
    d_que = Queue()

    for i, c in enumerate(senate):
        if c == 'R':
            r_que.put(i)
        else:
            d_que.put(i)

    while True:
        r = r_que.get()
        d = d_que.get()
        if r < d:
            if d_que.empty():
                return 'Radiant'
            r_que.put(r+ls)
        else:
            if r_que.empty():
                return 'Dire'
            d_que.put(d+ls)


def predict_party_victory4(senate: str) -> str:
    ls = len(senate)
    banned = [False] * ls
    r_count = senate.count('R')
    d_count = ls - r_count

    def ban(to_ban, start_at):
        pointer = start_at
        while banned[pointer] or senate[pointer] != to_ban:
            pointer = (pointer + 1) % ls
        banned[pointer] = True

    turn = 0
    while r_count and d_count:
        if not banned[turn]:
            senator = senate[turn]
            if senator == 'R':
                ban('D', (turn + 1) % ls)
                d_count -= 1
            else:
                ban('R', (turn + 1) % ls)
                r_count -= 1
        turn = (turn + 1) % ls

    return 'Radiant' if r_count else 'Dire'


def predict_party_victory3(senate: str) -> str:
    ls = len(senate)
    radiants = senate.count('R')
    dires = ls - radiants
    if radiants >= 2 * dires:
        return 'Radiant'
    elif dires >= 2 * radiants:
        return 'Dire'

    banned = [False] * ls
    turn = 0

    def ban_opponent(senator: str, idx: int):
        while banned[idx] or senate[idx] == senator:
            idx = (idx + 1) % ls
        banned[idx] = True

    while radiants and dires:
        if not banned[turn]:
            ban_opponent(senate[turn], turn)
            if senate[turn] == 'R':
                dires -= 1
            else:
                radiants -= 1
        turn = (turn + 1) % ls
    return 'Radiant' if radiants else 'Dire'


def predict_party_victory2(senate: str) -> str:
    def find_next_opponent(opp: str, start: int) -> int:
        ls = len(senate)
        j = (start + 1) % ls
        while j != start:
            if senate[j] == opp:
                return j
            else:
                j = (j + 1) % ls
        return start

    radiants = senate.count('R')
    dires = len(senate) - radiants
    if radiants >= 2 * dires:
        return 'Radiant'
    elif dires >= 2 * radiants:
        return 'Dire'

    senate = list(senate)
    i = 0
    while True:
        if senate[i] == 'R':
            idx = find_next_opponent('D', i)
            if idx == i:
                return 'Radiant'
            else:
                senate.pop(idx)
                if idx > i:
                    i += 1
        else:
            idx = find_next_opponent('R', i)
            if idx == i:
                return 'Dire'
            else:
                senate.pop(idx)
                if idx > i:
                    i += 1
        i %= len(senate)


if __name__ == '__main__':
    print('Radiant ===', predict_party_victory('RD'))
    print('Dire ===', predict_party_victory('RDD'))
    print('Dire ===', predict_party_victory('DDRRR'))
