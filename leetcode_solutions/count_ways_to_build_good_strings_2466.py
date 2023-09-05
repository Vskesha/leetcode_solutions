def count_good_strings(low, high, zero, one):
    ans, mod = 0, 1000000007
    for i1 in range(0, high // one + 1):
        rem_low = (low - i1 * one - 1) // zero + 1
        rem_high = (high - i1 * one) // zero + 1
        for i0 in range(rem_low, rem_high):
            # combs = factorial(i0 + i1) // factorial(i0) // factorial(i1)
            combs = 1
            bigger = max(i1, i0) + 1
            for big, small in zip(range(bigger, i1+i0+1), range(1, bigger+1)):
                combs = combs * big // small % mod
            # print(f'{combs=}, for {i1=}, {i0=}, total_length={i1*one+i0*zero}')
            ans += combs
            ans %= mod
    return ans


if __name__ == '__main__':
    print('8 ===', count_good_strings(low=3, high=3, zero=1, one=1))
    print('5 ===', count_good_strings(low=2, high=3, zero=1, one=2))
