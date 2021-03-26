from avl_node import AVLNode


class AVLTree:

    def __init__(self):
        """Default constructor. Initializes the AVL tree.
        """
        self.root = None
        self.size = 0
        self.h = 0
        self.array = []

    def get_root(self):
        """@returns the root of the AVLTree
        """
        return self.root

    def get_height(self):
        """Retrieves tree height.
    	 @return -1 in case of empty tree, current tree height otherwise.
    	 """
        return self.h

    def get_size(self):
        """Yields number of key/element pairs in the tree.
        @return Number of key/element pairs.
        """
        return self.size

    def to_array(self):
        """Yields an array representation of the tree elements (pre-order).
    	@return Array representation of the tree elements.
        """
        self.array = []
        self.preorder(self.root)
        return self.array

    def preorder(self, node):

        if node:
            self.array.append(node.elem),

            self.preorder(node.left)

            self.preorder(node.right)

    def find(self, key):
        """Returns element of node with given key.
    	 @param key: Key to search.
    	 @return Corresponding element if key was found, None otherwise.
         @raises ValueError if the key is None
    	 """
        result = self.find_rec(self.root, key)
        if result == None:
            raise ValueError
        else:
            return result

    def find_rec(self, node, key):
        if node:

            if node.key == key:
                return node.elem
            else:
                self.find_rec(node.left, key)
                self.find_rec(node.right, key)

    def insert(self, key, elem):
        """Inserts a new node into AVL tree.
    	 @param key: Key of the new node.
    	 @param elem: Data of the new node. Elements with the same key
    	 are not allowed. In this case false is returned. None-Keys are
    	 not allowed. In this case an exception is thrown.
         @raises ValueError if the key or elem is None.
        """
        # e bine oare?
        if key is None:
            raise ValueError
        if elem is None:
            raise ValueError

        if not self.root:
            self.root = self.insert_node(self.root, key, elem)
            self.size = self.size + 1
            return self.root
        else:
            self.root = self.insert_node(self.root, key, elem)
            self.size = self.size + 1
            self.setHeight(self.root)
            return self.root

    def insert_node(self, root, key, elem):

        # Find the correct location and insert the node
        if not root:
            return AVLNode(key, elem)
        elif key < root.key:
            root.left = self.insert_node(root.left, key, elem)
            root.left.parent = root
        else:
            root.right = self.insert_node(root.right, key, elem)
            root.right.parent = root

        if root.left and root.right:
            root.height = 1 + max(root.left.height, root.right.height)
        elif root.right:
            root.height = 1 + root.right.height
        elif root.left:
            root.height = 1 + root.left.height
        else:
            root.height = 0

        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                root = self.rightRotate(root) #
                return root
            else:
                root.left.right.right = self.rightRotate(root.left.right.right)
                root.left.right = self.leftRotate(root.left.right)
                return self.root

        if balanceFactor < -1:
            if key > root.right.key:
                root = self.leftRotate(root)
                return root
            else:
                root.right.left = self.leftRotate(root.right.left)
                root.right = self.rightRotate(root.right)
                return self.root

        return root

    def getBalance(self, node):
        if not self.root:
            return 0
        if not node:
            return 0
        if not node.right and not node.left:
            return 0
        if not node.right:
            return node.left.height
        if not node.left:
            return -node.right.height

        return node.left.height - node.right.height

    def setHeight(self, node):
        if not node:
            return 0
        else:
            if not node.right and not node.left:
                return 0
            hL = self.setHeight(node.left)
            hR = self.setHeight(node.right)
            node.height = max(hL, hR) + 1
            return max(hL, hR) + 1

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        if T2:
            T2.parent = z
        y.left = z
        z.right = T2
        y.parent = z.parent
        z.parent = y

        if z.left and z.right:
            z.height = 1 + max(z.left.height, z.right.height)
        elif z.right:
            z.height = 1 + z.right.height
        elif z.left:
            z.height = 1 + z.left.height
        else:
            z.height = 0

        if y.left and y.right:
            y.height = 1 + max(y.left.height, y.right.height)
        elif y.right:
            y.height = 1 + y.right.height
        elif y.left:
            y.height = 1 + y.left.height
        else:
            y.height = 0

        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        if T3:
            T3.parent = z
        y.right = z
        z.left = T3
        y.parent = z.parent
        z.parent = y

        if z.left and z.right:
            z.height = 1 + max(z.left.height, z.right.height)
        elif z.right:
            z.height = 1 + z.right.height
        elif z.left:
            z.height = 1 + z.left.height
        else:
            z.height = 0

        if y.left and y.right:
            y.height = 1 + max(y.left.height, y.right.height)
        elif y.right:
            y.height = 1 + y.right.height
        elif y.left:
            y.height = 1 + y.left.height
        else:
            y.height = 0

        return y

    def remove(self, key):
        """Removes node with given key.
    	 @param key: Key of node to remove.
    	 @return true If element was found and deleted.
         @raises ValueError if the key is None
        """
        self.delete_node(self.root, key)
        return self.root

    def delete_node(self, root, key):

        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        if root.left and root.right:
            root.height = 1 + max(root.left.height, root.right.height)
        elif root.right:
            root.height = 1 + root.right.height
        elif root.left:
            root.height = 1 + root.left.height
        else:
            root.height = 0

        balanceFactor = self.getBalance(root)
        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                root = self.rightRotate(root)  #
                return root
            else:
                root.left.right.right = self.rightRotate(root.left.right.right)
                root.left.right = self.leftRotate(root.left.right)
                return self.root
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                root = self.leftRotate(root)
                return root
            else:
                root.right.left = self.leftRotate(root.right.left)
                root.right = self.rightRotate(root.right)
                return self.root
        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
