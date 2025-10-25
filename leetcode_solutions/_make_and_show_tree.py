from collections import deque
from typing import List, Optional

import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class TreeCreator:
    def get_text_for_graph_editor(self, root: TreeNode) -> str:
        relations = []

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                relations.append(f"{node.val} {node.left.val}")
            if node.right:
                queue.append(node.right)
                relations.append(f"{node.val} {node.right.val}")

        return "\n".join(relations)

    def list_to_tree(self, arr: List[int]) -> Optional[TreeNode]:
        if not arr:
            return None

        values = iter(arr)
        root = TreeNode(next(values))
        que = deque([root])

        while que:
            node = que.popleft()
            value = next(values, None)
            if value is not None:
                node.left = TreeNode(value)
                que.append(node.left)

            value = next(values, None)
            if value is not None:
                node.right = TreeNode(value)
                que.append(node.right)

        return root

    def plot_tree(
        self,
        node: TreeNode,
        x: float = 0.0,
        y: float = 0.0,
        branch_length: float = 2.0,
    ) -> None:
        if node is not None:
            plt.text(
                x, y, str(node.val), fontsize=20, ha="center", va="center"
            )
            # plt.text(x, y, "◯", fontsize=50, ha='center', va='center')
            # ax = plt.gca()
            # circle = plt.Circle((x, y), 0.05, color="g")
            # ax.add_patch(circle)
            if node.left is not None:
                plt.plot(
                    [x, x - branch_length],
                    [y, y - 1],
                    "k-",
                    marker="o",
                    markersize=50,
                    markerfacecolor="w",
                )
                self.plot_tree(
                    node.left, x - branch_length, y - 1, branch_length / 2
                )
            if node.right is not None:
                plt.plot(
                    [x, x + branch_length],
                    [y, y - 1],
                    "k-",
                    marker="o",
                    markersize=50,
                    markerfacecolor="w",
                )
                self.plot_tree(
                    node.right, x + branch_length, y - 1, branch_length / 2
                )

    def show_tree(self, arr: List[int]) -> None:
        root = self.list_to_tree(arr)
        plt.figure(figsize=(15, 10))
        self.plot_tree(root)
        plt.axis("off")
        plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
        plt.ylim(-6.5, 0.5)
        plt.show()


if __name__ == "__main__":
    null = None
    arr = [
        1,
        null,
        15,
        14,
        17,
        7,
        null,
        null,
        null,
        2,
        12,
        null,
        3,
        9,
        null,
        null,
        null,
        null,
        11,
    ]
    tc = TreeCreator()
    tc.show_tree(arr)
    # print(tc.get_text_for_graph_editor(root))
