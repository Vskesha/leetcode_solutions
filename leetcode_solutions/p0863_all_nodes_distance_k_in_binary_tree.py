from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        graph = defaultdict(list)

        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                stack.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                stack.append(node.right)

        # Another way to fill all the edges of a graph
        # def traverse(node, parent):
        #     v = node.val
        #     if parent:
        #         graph[v].append(parent.val)
        #     if node.left:
        #         graph[v].append(node.left.val)
        #         traverse(node.left, node)
        #     if node.right:
        #         graph[v].append(node.right.val)
        #         traverse(node.right, node)

        # traverse(root, None)

        result = []

        bfs = deque([(target.val, 0)])
        visited = {target.val}

        while bfs:
            node, dist = bfs.popleft()
            if dist == k:
                result.append(node)
                continue
            for neib in graph[node]:
                if neib not in visited:
                    bfs.append((neib, dist + 1))
                    visited.add(neib)

        return result


def list_to_binary_tree(lst: list) -> TreeNode:
    if not lst:
        return None
    if len(lst) % 2 == 0:
        lst.append(None)
    root = TreeNode(lst[0])
    i = 1
    dq = deque([root])
    while i < len(lst):
        curr = dq.popleft()
        if lst[i] is not None:
            curr.left = TreeNode(lst[i])
            dq.append(curr.left)
        i += 1
        if lst[i] is not None:
            curr.right = TreeNode(lst[i])
            dq.append(curr.right)
        i += 1
    return root


def main():
    null = None
    sol = Solution()
    root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]  # target=5, k=2
    tree_root = list_to_binary_tree(root)
    print(
        " [7, 4, 1]\n",
        sol.distanceK(root=tree_root, target=tree_root.left, k=2),
    )
    root = [0, null, 1, null, 2, null, 3]  # target = 1, k = 2
    tree_root = list_to_binary_tree(root)
    print(" [3]\n", sol.distanceK(tree_root, tree_root.right, 2))


if __name__ == "__main__":
    main()
