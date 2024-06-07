from typing import Optional, List


class TreeNode:
    def __init__(self, key=0, value=None, left=None, right=None, height=0):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.height = height

    def __copy__(self):
        return TreeNode(
            key=self.key,
            value=self.value,
            left=self.left.__copy__() if self.left else None,
            right=self.right.__copy__() if self.right else None,
            height=self.height,
        )

    def __repr__(self):
        return f"TreeNode(key={self.key}, value={self.value}, height={self.height})"

    def __str__(self):
        return self.__repr__()

    def ascending(self) -> List:
        result = []
        if self.left:
            result.extend(self.left.ascending())
        result.append(self.key)
        if self.right:
            result.extend(self.right.ascending())
        return result

    def balance(self):
        balance_ = self.get_balance()
        if balance_ == -2:
            if self.left.get_balance() == 1:
                self.left.rotate_left()
            self.rotate_right()
        elif balance_ == 2:
            if self.right.get_balance() == -1:
                self.right.rotate_right()
            self.rotate_left()

    def copy(self):
        return self.__copy__()

    def delete(self, key):
        if key == self.key:
            if self.left and self.right:
                min_in_right = self.right.get_min()
                self.key = min_in_right.key
                self.value = min_in_right.value
                self.right = self.right.delete(min_in_right.key)
            else:
                return self.left or self.right
        elif key > self.key and self.right:
            self.right = self.right.delete(key)
        elif key < self.key and self.left:
            self.left = self.left.delete(key)
        self.balance()
        self.update_height()
        return self

    def delete_tree(self) -> None:
        if self.left:
            self.left = self.left.delete_tree()
        if self.right:
            self.right = self.right.delete_tree()
        del self

    def descending(self) -> List:
        return self.ascending()[::-1]

    def get_max(self):
        return self.right.get_max() if self.right else self

    def get_min(self):
        return self.left.get_min() if self.left else self

    @staticmethod
    def get_height(node):
        return node.height if node else -1

    def get_balance(self):
        return self.get_height(self.right) - self.get_height(self.left)

    def insert(self, key, value=None):
        if key < self.key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = TreeNode(key, value)
        else:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = TreeNode(key, value)
        self.balance()
        self.update_height()

    def rotate_right(self):
        self.swap(self.left)
        buffer = self.right
        self.right = self.left
        self.left = self.left.left
        self.right.left = self.right.right
        self.right.right = buffer
        self.right.update_height()
        self.update_height()

    def rotate_left(self):
        self.swap(self.right)
        buffer = self.left
        self.left = self.right
        self.right = self.right.right
        self.left.right = self.left.left
        self.left.left = buffer
        self.left.update_height()
        self.update_height()

    def search(self, key):
        if self.key == key:
            return self
        elif key < self.key:
            return self.left.search(key) if self.left else None
        else:
            return self.right.search(key) if self.right else None

    def swap(self, other):
        self.key, other.key = other.key, self.key
        self.value, other.value = other.value, self.value
        self.height, other.height = other.height, self.height

    def update_height(self) -> None:
        self.height = max(self.get_height(self.left), self.get_height(self.right)) + 1


class Tree:
    def __init__(self):
        self.root = None

    def __copy__(self):
        new_tree = Tree()
        new_tree.root = self.root.copy() if self.root else None
        return new_tree

    def ascending(self) -> List:
        return self.root.ascending() if self.root else []

    def copy(self):
        return self.__copy__()

    def delete(self, key) -> None:
        if self.root:
            self.root.delete(key)

    def delete_tree(self) -> None:
        if self.root:
            self.root = self.root.delete_tree()

    def descending(self) -> List:
        return self.ascending()[::-1]

    def get_height(self):
        return TreeNode.get_height(self.root)

    def get_max(self) -> Optional[TreeNode]:
        return self.root.get_max() if self.root else None

    def get_min(self) -> Optional[TreeNode]:
        return self.root.get_min() if self.root else None

    def insert(self, key, value=None):
        if self.root:
            self.root.insert(key, value)
        else:
            self.root = TreeNode(key, value)

    def search(self, key) -> Optional[TreeNode]:
        return self.root.search(key) if self.root else None
