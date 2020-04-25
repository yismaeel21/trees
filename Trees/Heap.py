'''
'''

from Trees.BinaryTree import BinaryTree, Node

class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above 
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        self.root = None
        if xs:
            self.insert_list(xs)
    
    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"
        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        if node is None or (node.left is None and node.right is None):
            return True
        if node.right is None:
            return node.value <= node.left.value
        if node.value <= node.left.value and node.value <= node.right.value:
            return Heap._is_heap_satisfied(node.left) and Heap._is_heap_satisfied(node.right)
        
    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            Heap._insert(value, self.root)


    @staticmethod
    def _insert(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if node.left is None:
            node1 = Node(value)
            node.left = node1
        elif node.right is None:
            node1 = Node(value)
            node.right = node1
        else:
            leftSize = Heap.size(node.left)
            rightSize = Heap.size(node.right)
            if leftSize <= rightSize: 
                node1 = node.left  
            else: 
                node1 = node.right
            node1 = Heap._insert(value,node1)

        if node.value > node1.value:
            arg = node1.value
            node.value = arg
        return node

    
    @staticmethod
    def size(node):
        if node is None:
            return 0
        ourStack = []
        ourStack.append(node)
        size = 1
        while ourStack:
            node = ourStack.pop()
            if node.left:
                size +=1
                ourStack.append(node.left)
            if node.right:
                size += 1
                ourStack.append(node.right)
        return size

               
    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for elem in xs:
            self.insert(xs)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        but if you understand the structure of a Heap it should be easy to implement.
        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if Heap.is_heap_satisfied(self):
            return self.root.value
        

    def remove_min(self):
        '''
        Removes the minimum value from the Heap. 
        If the heap is empty, it does nothing.
        FIXME:
        Implement this function.
        '''
    
    @staticmethod
    def _flip(node1,node2):
        arg = node2.value
        node2.value = node1.value
        node1.value = arg
    
    
    @staticmethod
    def _downHeapBubble(node,value):
        if Heap._is_heap_satisfied(node):
            return
        else:
            if node.left is None and node.right is None:
                return node
            elif node.left is None:
                if node.right.value >= node.value:
                    return node
                else:
                    Heap._flip(node.right.value, node.value)
            else:
                if node.right.value < node.left.value:
                    Heap._flip(node.value, node.right.value)
                    return Heap._downHeapBubble(node, node.right.value)
                else:
                    Heap._flip(node.value, node.left.value)
                    return Heap._downHeapBubble(node, node.left.value)
