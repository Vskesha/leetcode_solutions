import functools


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(us_list: list) -> ListNode:
    next_val = None
    for x in reversed(us_list):
        node = ListNode(x, next_val)
        next_val = node
    return next_val


def from_linked_list(linked_list: ListNode) -> list:
    result = []
    while linked_list:
        result.append(linked_list.val)
        linked_list = linked_list.next
    return result


def list_of_linked_lists(lists):
    result = []
    for l in lists:
        result.append(to_linked_list(l))
    return result


class Solution:
    def mergeKLists(self, lists):
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


    def mergeKLists2(self, lists):

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

    def mergeKLists3(self, lists):
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


if __name__ == '__main__':
    sol = Solution()
    print(from_linked_list(sol.mergeKLists2(list_of_linked_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))))
    print(from_linked_list(sol.mergeKLists2(list_of_linked_lists([]))))
    print(from_linked_list(sol.mergeKLists2(list_of_linked_lists([[]]))))

    print(from_linked_list(sol.mergeKLists(list_of_linked_lists([[1, 4, 5], [1, 3, 4], [2, 6]]))))
    print(from_linked_list(sol.mergeKLists(list_of_linked_lists([]))))
    print(from_linked_list(sol.mergeKLists(list_of_linked_lists([[]]))))
