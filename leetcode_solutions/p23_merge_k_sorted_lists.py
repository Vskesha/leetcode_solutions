import unittest
from functools import reduce
from heapq import heapify, heappop, heappush
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i) for i, node in enumerate(lists) if node]
        heapify(heap)
        dummy = curr = ListNode()

        while heap:
            _, i = heappop(heap)
            curr.next = lists[i]
            curr = curr.next
            if curr.next:
                heappush(heap, (curr.next.val, i))
                lists[i] = curr.next

        return dummy.next


class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(
            list1: Optional[ListNode], list2: Optional[ListNode]
        ) -> Optional[ListNode]:
            dummy = curr = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
            curr.next = list1 if list1 else list2
            return dummy.next

        return reduce(merge_two_lists, lists, None)


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lts = []
        for i in lists:
            while i:
                lts.append(i.val)
                i = i.next
        next_node = None
        for i in sorted(lts, reverse=True):
            node = ListNode(i, next_node)
            next_node = node
        return next_node


class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list1, list2):
            result = current = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 or list2
            return result.next

        res = None
        for l in lists:
            res = merge_two_lists(res, l)
        return res


class Solution4:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = curr = ListNode()
        lists = [l for l in lists if l]
        while lists:
            min_val = lists[0].val
            min_index = 0
            for i in range(1, len(lists)):
                curr_val = lists[i].val
                if min_val > curr_val:
                    min_val = curr_val
                    min_index = i
            curr.next = lists[min_index]
            curr = curr.next
            lists[min_index] = lists[min_index].next
            if not lists[min_index]:
                lists.pop(min_index)
        return result.next


class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sol = Solution()

    @staticmethod
    def arr_to_linked_list(arr: List[int]) -> Optional[ListNode]:
        head = None
        for val in reversed(arr):
            head = ListNode(val=val, next=head)
        return head

    def assertIsSorted(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        curr = head.val
        head = head.next
        while head:
            self.assertLessEqual(curr, head.val)
            curr = head.val
            head = head.next

    def test_merge_k_lists(self):
        print("Test mergeKLists 1 ... ", end="")
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        lists = list(map(self.arr_to_linked_list, lists))
        self.assertIsSorted(self.sol.mergeKLists(lists))
        print("OK")

    def test_merge_k_lists_2(self):
        print("Test mergeKLists 2 ... ", end="")
        lists = []
        lists = list(map(self.arr_to_linked_list, lists))
        self.assertIsSorted(self.sol.mergeKLists(lists))
        print("OK")

    def test_merge_k_lists_3(self):
        print("Test mergeKLists 3 ... ", end="")
        lists = [[]]
        lists = list(map(self.arr_to_linked_list, lists))
        self.assertIsSorted(self.sol.mergeKLists(lists))
        print("OK")


if __name__ == "__main__":
    unittest.main()
