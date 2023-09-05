import bisect


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs.sort(key = lambda x: x[1], reverse=True)
        
        my_heap = []
        for i in range(k):
            bisect.insort(my_heap, pairs[i][0])
        
        heap_sum = sum(my_heap)
        max_score = heap_sum * pairs[k-1][1]
        for i in range(k, len(pairs)):
            curr_val = pairs[i][0]
            curr_min = pairs[i][1]
            bisect.insort(my_heap, curr_val)
            heap_sum += curr_val - my_heap.pop(0)
            max_score = max(max_score, heap_sum * curr_min)
        
        return max_score
    
    
if __name__ == '__main__':
    sol = Solution()
    print('12 ===', sol.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3))
    print('30 ===', sol.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1))
    