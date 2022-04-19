class BinarySearchTree:

    def __init__(self):
        self._size = 0
        self.root = None    

    class Node:
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def size(self):
        return self._size
    
    def add(self,key,value):
        if self.root == None:
            self.root = self.Node(key, value)
            self._size += 1
        else:
            self.add_recursion(self.root,key,value)
                 
    def add_recursion(self,subtree:Node,key,value):

        if subtree.key > key:
            if subtree.left == None:
                subtree.left = self.Node(key,value)
                self._size += 1
            else:
                self.add_recursion(subtree.left,key,value)
        else:
            if subtree.right == None:
                subtree.right = self.Node(key,value)
                self._size += 1
            else:
                self.add_recursion(subtree.right,key,value)
        
    
    def search(self, key):
        return self.search_recursion(self.root,key)

    def search_recursion(self, subtree:Node, key):
        if subtree == None:
            return False
        elif subtree.key == key:
            return subtree.value
        elif subtree.key < key:
            return self.search_recursion(subtree.right,key)
        else:
            return self.search_recursion(subtree.left,key)

    def inorder_walk(self):
        visited_node = []
        self.inorder_walk_recursion(self.root, visited_node)
        return visited_node

    def inorder_walk_recursion(self,subtree:Node,visited_node):
        if subtree:
            self.inorder_walk_recursion(subtree.left,visited_node)
            visited_node.append(subtree.key)
            self.inorder_walk_recursion(subtree.right,visited_node)
    
    def preorder_walk(self):
        visited_node = []
        self.preorder_walk_recursion(self.root, visited_node)
        return visited_node

    def preorder_walk_recursion(self,subtree:Node,visited_node):
        if subtree:
            visited_node.append(subtree.key)
            self.preorder_walk_recursion(subtree.left,visited_node)
            self.preorder_walk_recursion(subtree.right,visited_node)

    def postorder_walk(self):
        visited_node = []
        self.postorder_walk_recursion(self.root, visited_node)
        return visited_node

    def postorder_walk_recursion(self,subtree:Node,visited_node):
        if subtree:
            self.postorder_walk_recursion(subtree.left,visited_node)
            self.postorder_walk_recursion(subtree.right,visited_node)
            visited_node.append(subtree.key)

    def smallest(self):
        return self.smallest_recursion(self.root)

    def smallest_recursion(self,subtree:Node):
        if subtree.left == None:
            return (subtree.key, subtree.value)
        else:
            return self.smallest_recursion(subtree.left)

    def largest(self):
        return self.largest_recursion(self.root)

    def largest_recursion(self,subtree:Node):
        if subtree.right == None:
            return (subtree.key, subtree.value)
        else:
            return self.largest_recursion(subtree.right)

    def remove(self, key):
        if self.search(key):
            self.root = self.remove_recursion(self.root, key)
            self._size -= 1
        else:
            return self.search(key)

    def remove_recursion(self, subtree, key):
        if subtree is None:
            return subtree
        elif key < subtree.key:
            subtree.left = self.remove_recursion(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self.remove_recursion(subtree.right, key)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                successor = self.largest_recursion(subtree.left)
                subtree.key = successor[0]
                subtree.value = successor[1]
                subtree.left = self.remove_recursion(subtree.left, successor[0])
                return subtree


# bst = BinarySearchTree()
# bst.add(100,"this is 100")
# bst.add(20,"this is 20")
# bst.add(30,"this is 30")
# bst.add(10,"this is 10")
# bst.add(200,"this is 200")
# bst.add(300,"this is 300")
# bst.add(150,"this is 150")


# print(bst.size())
# print(bst.inorder_walk())
# print(bst.preorder_walk())
# print(bst.postorder_walk())
# print(bst.smallest())
# print(bst.largest())
# # print(bst.search(9))
# print('a')
# print(bst.search(10))
# print(bst.inorder_walk())
# print(bst.remove(22))
            