def fraction_to_decimal(numerator: int, denominator: int) -> str:
    if not numerator:
        return '0'

    res = ''
    if (numerator < 0) ^ (denominator < 0):
        res +='-'

    num = abs(numerator)
    den = abs(denominator)

    res += str(num // den)

    if not num % den:
        return res

    res += '.'
    rem = num % den
    mp = {}
    
    while rem and rem not in mp:
        mp[rem] = len(res)
        res += str(rem * 10 // den)
        rem = rem * 10 % den

    if rem in mp:
        res = f'{res[:mp[rem]]}({res[mp[rem]:]})'
    
    return res
    
    
def fraction_to_decimal2(numerator: int, denominator: int) -> str:
    if not numerator:
        return '0'

    res = []
    if (numerator < 0) ^ (denominator < 0):
        res.append('-')

    num = abs(numerator)
    den = abs(denominator)

    z = num // den
    res.append(str(z))

    rem = num % den
    if rem:
        res.append('.')
    else:
        return ''.join(res)

    mp = {}
    brackets_idx = 0
    
    while rem:
        if rem in mp:
            brackets_idx = mp[rem]
            break
        else:
            mp[rem] = len(res)
            rem *= 10
            res.append(str(rem // den))
            rem %= den
    
    if brackets_idx:
        res.insert(brackets_idx, '(')
        res.append(')')
    
    return ''.join(res)         
            

if __name__ == '__main__':
    print('0.5 ===', fraction_to_decimal(1, 2))
    print('2 ===', fraction_to_decimal(2, 1))
    print('0.(012) ===', fraction_to_decimal(4, 333))
