# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head

        while curr:
            if curr.child:
                child = curr.child
                end = child
                while end.next:
                    end = end.next
                nxt = curr.next
                curr.child = None
                curr.next = child
                child.prev = curr
                if nxt:
                    end.next = nxt
                    nxt.prev = end
            curr = curr.next

        return head


def test():
    sol = Solution()


if __name__ == '__main__':
    test()
