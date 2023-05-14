import math
from functools import cache


def max_score(nums): # best dp solution
        n = len(nums)//2
        @cache
        def dp(i, mask):
            if i == 2*n: return ([])
            if not (mask >> i)&1: return dp(i+1, mask)
            ans, tot = [], 0
            mask -= (1 << i)
            for j in range(i+1, 2*n):
                if (mask >> j)&1:
                    gcds = sorted(dp(i+1, mask-(1<<j))+[math.gcd(nums[i], nums[j])])
                    score = sum(((i+1)*gcds[i]) for i in range(len(gcds)))
                    if score > tot:
                        ans = gcds
                        tot = score
            return ans
        gcds = sorted(dp(0, (1<<(2*n))-1))
        return sum(((i+1)*gcds[i]) for i in range(n))
    

def max_score1(nums): # dp iterative solution
    n = len(nums)
    max_states = 2 ** n
    final_mask = max_states - 1
    dp = [-1] * max_states
    dp[final_mask] = 0
    for state in range(final_mask - 1, -1, -1):
        numbers_taken = bin(state).count('1')
        if numbers_taken % 2:
            continue
        pairs_formed = numbers_taken // 2
        for i in range(n):
            if (state >> i) & 1:
                continue
            for j in range(i+1, n):
                if (state >> j) & 1:
                    continue
                state_after = state | (1 << i) | (1 << j)
                current_score = (pairs_formed + 1) * math.gcd(nums[i], nums[j])
                remaining_score = dp[state_after]
                dp[state] = max(dp[state], current_score + remaining_score)
    return dp[0]
                    


def max_score2(nums): # recursive solution
    
    def backtrack(state, pairs_picked) -> int:
        
        if pairs_picked == max_pairs:
            return 0
        
        if memo[state] != -1:
            return memo[state]

        max_score = 0
        for i in range(n-1):
            if (state >> i) & 1:
                continue
            for j in range(i+1, n):
                if (state >> j) & 1:
                    continue
                new_state = state | (1 << i) | (1 << j)
                curr_score = (pairs_picked + 1) * math.gcd(nums[i], nums[j])
                rem_score = backtrack(new_state, pairs_picked + 1)
                max_score = max(max_score, curr_score + rem_score)
        memo[state] = max_score
        return max_score
        
    n = len(nums)
    max_pairs = n // 2
    memo = [-1] * (2 ** n)
    return backtrack(0, 0)



if __name__ == '__main__':
    print('1 ===', max_score([1, 2]))
    print('11 ===', max_score([3, 4, 6, 8]))
    print('14 ===', max_score([1, 2, 3, 4, 5, 6]))
    print('527 ===', max_score([109497, 983516, 698308, 409009, 310455, 528595, 524079, 18036, 341150, 641864, 913962, 421869, 943382, 295019]))
    