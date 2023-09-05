class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = j = 0
        result = []
        
        while i < len(firstList) and j < len(secondList):
            st1, en1 = firstList[i]
            st2, en2 = secondList[j]
            st = max(st1, st2)
            en = min(en1, en2)
            if st <= en:
                result.append([st, en])
            if en1 > en2:
                j += 1
            else:
                i += 1
        return result


if __name__ == '__main__':
    sol = Solution()
    print('[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]] ===', sol.intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
    print('[] ===', sol.intervalIntersection(firstList = [[1,3],[5,9]], secondList = []))
    