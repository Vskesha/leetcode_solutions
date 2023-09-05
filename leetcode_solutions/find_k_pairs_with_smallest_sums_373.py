from heapq import heappush, heappop


class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]
        n1, n2 = len(nums1), len(nums2)
        res = []

        while heap and k:
            minimum = heappop(heap)
            _, i, j = minimum
            res.append([nums1[i], nums2[j]])
            if j < n2 - 1:
                heappush(heap, (nums1[i] + nums2[j+1], i, j + 1))
            if j == 0 and i < n1 - 1:
                heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
            k -= 1
        return res


def main():
    sol = Solution()
    print(' [[1, 2], [1, 4], [1, 6]]\n', sol.kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))
    print(' [[1, 1], [1, 1]]\n', sol.kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))
    print(' [[1, 3], [2, 3]]\n', sol.kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))


if __name__ == '__main__':
    main()
