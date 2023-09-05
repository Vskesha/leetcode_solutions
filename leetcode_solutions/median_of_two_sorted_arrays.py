import test


def median_of_two_sorted_arrays(nums1: list, nums2: list) -> float:
    i = j = counter = 0
    l1, l2 = len(nums1), len(nums2)
    middle_even = (l1 + l2) % 2
    middle = (l1 + l2 - 1) // 2
    nums1.append(10**8)
    nums2.append(10**8)
    while counter < middle:
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
        counter += 1
    res = sorted(nums1[i:i+2] + nums2[j:j+2])
    return float(res[0]) if middle_even else (res[0] + res[1]) / 2


if __name__ == '__main__':
    nums1 = [1, 3]; nums2 = [2]
    test.assert_equals(median_of_two_sorted_arrays(nums1, nums2), 2.0)
    nums1 = [1, 2]; nums2 = [3, 4]
    test.assert_equals(median_of_two_sorted_arrays(nums1, nums2), 2.5)
