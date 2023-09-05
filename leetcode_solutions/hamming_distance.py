def hamming_distance(x: int, y: int) -> int:
    xs = f'{x:b}'
    ys = f'{y:b}'
    if x > y:
        ys = ys.zfill(len(xs))
    else:
        xs = xs.zfill(len(ys))
    res = 0
    for i in range(len(xs)):
        if xs[i] != ys[i]:
            res += 1
    return res



if __name__ == '__main__':
    print(hamming_distance(1, 4))
    print(hamming_distance(1, 3))
