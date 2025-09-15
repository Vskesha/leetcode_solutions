import unittest
from itertools import pairwise

from _binary_search_tree import Tree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = Tree()
        for key in [7, 5, 8, 6, 3]:
            self.tree.insert(key)

    def tearDown(self) -> None:
        pass

    def test_insertion(self) -> None:
        print("Test insertion ... ", end="")
        self.assertEqual(self.tree.root.key, 7, "Bad root key")
        self.assertEqual(self.tree.root.left.key, 5)
        self.assertEqual(self.tree.root.left.left.key, 3)
        self.assertEqual(self.tree.root.left.right.key, 6)
        self.assertEqual(self.tree.root.right.key, 8)
        print("OK")

    def test_search(self) -> None:
        print("Test search ... ", end="")
        self.assertEqual(self.tree.search(7).key, 7)
        self.assertEqual(self.tree.search(6).key, 6)
        self.assertIsNone(self.tree.search(4))
        self.assertIsNone(self.tree.search(9))
        print("OK")

    def test_get_min(self) -> None:
        print("Test get_min method ... ", end="")
        self.assertEqual(self.tree.get_min().key, 3)
        print("OK")

    def test_get_max(self) -> None:
        print("Test get_max method ... ", end="")
        self.assertEqual(self.tree.get_max().key, 8)
        print("OK")

    def test_delete(self) -> None:
        print("Test deleting ... ", end="")
        self.assertEqual(self.tree.search(5).key, 5)
        self.tree.delete(5)
        self.assertIsNone(self.tree.search(5))
        self.tree.delete(10)
        self.assertIsNone(self.tree.search(10))
        print("OK")

    def test_ascending(self) -> None:
        print("Test ascending ... ", end="")
        for a, b in pairwise(self.tree.ascending()):
            self.assertLessEqual(a, b)
        print("OK")

    def test_descending(self) -> None:
        print("Test descending ... ", end="")
        for a, b in pairwise(self.tree.descending()):
            self.assertGreaterEqual(a, b)
        print("OK")

    def test_delete_tree(self) -> None:
        print("Test deleting the whole tree ... ", end="")
        self.tree.delete_tree()
        self.assertIsNone(self.tree.root)
        print("OK")

    def test_copy(self) -> None:
        print("Test copy ... ", end="")
        new_tree = self.tree.copy()
        self.assertIsNot(self.tree, new_tree)
        self.assertListEqual(self.tree.ascending(), new_tree.ascending())
        self.assertEqual(new_tree.root.key, 7, "Bad root key")
        self.assertEqual(new_tree.root.left.key, 5)
        self.assertEqual(new_tree.root.left.left.key, 3)
        self.assertEqual(new_tree.root.left.right.key, 6)
        self.assertEqual(new_tree.root.right.key, 8)
        print("OK")

    def test_get_height(self) -> None:
        print("Test get_height ... ", end="")
        self.assertEqual(self.tree.get_height(), 2)
        self.tree.delete(3)
        self.assertEqual(self.tree.get_height(), 2)
        self.tree.delete(6)
        self.assertEqual(self.tree.get_height(), 1)
        self.tree.delete_tree()
        self.assertEqual(self.tree.get_height(), -1)
        print("OK")

    def test_rotate_right(self) -> None:
        print("Test rotate right ... ", end="")
        root = self.tree.root
        lf = root.left.left
        lf.insert(2)
        lf.insert(4)

        self.assertEqual(root.left.left.left.key, 2)
        self.assertEqual(root.left.left.key, 3)
        self.assertEqual(root.left.left.right.key, 4)
        self.assertEqual(root.left.key, 5)
        self.assertEqual(root.left.right.key, 6)
        self.assertEqual(root.key, 7)
        self.assertEqual(root.right.key, 8)

        root.left.rotate_right()

        self.assertEqual(root.left.left.key, 2)
        self.assertEqual(root.left.key, 3)
        self.assertEqual(root.left.right.left.key, 4)
        self.assertEqual(root.left.right.key, 5)
        self.assertEqual(root.left.right.right.key, 6)
        self.assertEqual(root.key, 7)
        self.assertEqual(root.right.key, 8)

        print("OK")

    def test_rotate_left(self) -> None:
        print("Test rotate left ... ", end="")
        root = self.tree.root
        rn = root.right
        rn.insert(7)
        rn.insert(9)

        self.assertEqual(root.left.left.key, 3)
        self.assertEqual(root.left.key, 5)
        self.assertEqual(root.left.right.key, 6)
        self.assertEqual(root.key, 7)
        self.assertEqual(root.right.left.key, 7)
        self.assertEqual(root.right.key, 8)
        self.assertEqual(root.right.right.key, 9)

        root.rotate_left()

        self.assertEqual(root.left.left.left.key, 3)
        self.assertEqual(root.left.left.key, 5)
        self.assertEqual(root.left.left.right.key, 6)
        self.assertEqual(root.left.key, 7)
        self.assertEqual(root.left.right.key, 7)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.right.key, 9)

        print("OK")

    def test_balance_inserting(self) -> None:
        print("Test balance while insert ... ", end="")
        self.assertEqual(self.tree.get_height(), 2)
        self.tree.insert(2)
        self.assertEqual(self.tree.get_height(), 2)
        root = self.tree.root
        self.assertEqual(root.left.left.key, 2)
        self.assertEqual(root.left.key, 3)
        self.assertEqual(root.key, 5)
        self.assertEqual(root.right.left.key, 6)
        self.assertEqual(root.right.key, 7)
        self.assertEqual(root.right.right.key, 8)

        print("OK")

    def test_balance_deleting(self) -> None:
        print("Test balance while delete ... ", end="")
        self.assertEqual(self.tree.get_height(), 2)
        self.tree.insert(2)
        self.tree.insert(5)
        self.assertEqual(self.tree.get_height(), 3)
        self.tree.delete(3)
        self.assertEqual(self.tree.get_height(), 2)

        print("OK")

    def test_balance_insert_many(self) -> None:
        print("Test balance while insert many ... ", end="")

        tree = Tree()
        for i in range(1, 2000):
            tree.insert(i)
        self.assertEqual(tree.get_height(), 10)

        print("OK")


if __name__ == "__main__":
    unittest.main()
