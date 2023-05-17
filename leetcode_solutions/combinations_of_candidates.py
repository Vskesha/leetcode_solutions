def combination_sum(candidates, target):
    ans = []
    
    def cmb(comb, sm):
        if sm > target:
            return
        if sm == target:
            ans.append(comb)
            return
        for c in candidates:
            cmb(comb + [c], sm + c)
            
    return ans


if __name__ == '__main__':
    print('[[2,2,3],[7]] ===', combination_sum(candidates = [2,3,6,7], target = 7))
    print('[[2,2,2,2],[2,3,3],[3,5]] ===', combination_sum(candidates = [2,3,5], target = 8))
    print('[] ===', combination_sum(candidates = [2], target = 1))