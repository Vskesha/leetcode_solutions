def merge(nums1, m, nums2, n):
    # i, j = m - 1, n - 1
    # for k in range(m + n - 1, -1, -1):
    #     if j < 0: break
    #     elif i < 0 or nums2[j] > nums1[i]: nums1[k] = nums2[j]; j -= 1
    #     else: nums1[k] = nums1[i]; i -= 1
    copy1 = nums1[:m]
    i = j = 0
    for k in range(m+n):
        if i < m and (j >= n or copy1[i] < nums2[j]):
            nums1[k] = copy1[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    merge(nums1, m, nums2, n)
    print(nums1)
