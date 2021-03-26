import unittest

from avl_tree import AVLTree
tree = None

class TestAssignment02Student(unittest.TestCase):
    def reset(self):
        global tree
        tree = AVLTree()

    def insert_kv(self, key, value):
        global tree
        return tree.insert(key, value)

    def insert(self, key):
        global tree
        return tree.insert(key, float(key))

    def remove(self, key):
        global tree
        return tree.remove(key)

    def test_structure1_rotation_hardcoded(self):
        global tree

        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        root = tree.get_root()

        self.assertEqual(root.key, 5)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.left.key, 2)
        self.assertEqual(root.left.height, 0)
        self.assertEqual(root.right.key, 14)
        self.assertEqual(root.right.height, 1)
        self.assertEqual(root.left.left, None)
        self.assertEqual(root.left.right, None)
        self.assertEqual(root.right.left.key, 8)
        self.assertEqual(root.right.left.height, 0)
        self.assertEqual(root.right.left.left, None)
        self.assertEqual(root.right.left.right, None)
        self.assertEqual(root.right.right.key, 18)
        self.assertEqual(root.right.right.height, 0)
        self.assertEqual(root.right.right.left, None)
        self.assertEqual(root.right.right.right, None)

    def test_to_array(self):
        global tree

        self.reset()
        self.insert(5)
        self.insert(18)
        self.insert(2)
        self.insert(8)
        self.insert(14)
        self.insert(16)
        self.insert(13)
        self.insert(3)
        self.insert(12)
        self.insert(21)
        self.insert(1)
        self.insert(0)

        array = tree.to_array()

        self.assertEqual(array[0], 5)
        self.assertEqual(array[1], 2)
        self.assertEqual(array[2], 1)
        self.assertEqual(array[3], 0)
        self.assertEqual(array[4], 3)
        self.assertEqual(array[5], 14)
        self.assertEqual(array[6], 12)
        self.assertEqual(array[7], 8)
        self.assertEqual(array[8], 13)
        self.assertEqual(array[9], 18)
        self.assertEqual(array[10], 16)
        self.assertEqual(array[11], 21)

        print("-------------------------------------------------------")
        print("testToArray\n Ordered (Pre):   5.0 2.0 1.0 0.0 3.0 14.0 12.0 8.0 13.0 18.0 16.0 21.0")
        print("Your order:      ", end=" ")
        i = 0
        while i < len(array):
            print(str(array[i]) + " ", end=" ")
            i += 1
        print(" ")
        self.assertTrue(self.check_AVL_integrity())
        print("testToArray: AVL integrity check successfull")

    def check_AVL_integrity(self):
        global tree
        return self.check_AVL_integrity_n(tree.get_root())

    def check_AVL_integrity_n(self, n):
        is_AVL = True
        if n is None:
            return True
        if not self.is_AVL_tree(n):
            is_AVL = False

        if not is_AVL:
            lh = -1 if n.left is None else n.left.height
            rh = -1 if n.right is None else n.right.height
            print("node: " + str(n.elem) + " " + str(n.height) + ";" + str(lh) + ";" + str(rh))

        if not self.check_AVL_integrity_n(n.left):
            is_AVL = False
        if not self.check_AVL_integrity_n(n.right):
            is_AVL = False

        return is_AVL

    def is_AVL_tree(self, n):
        diff = (-1 if n.left is None else n.left.height) - (-1 if n.right is None else n.right.height)
        return -1 <= diff <= 1


if __name__ == '__main__':
    unittest.main()
