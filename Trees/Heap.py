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
        super().__init__()
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
            Heap._insert(self.root, value)


    @staticmethod
    def _insert(node, value):
        '''
        FIXME:
        Implement this function.
        '''
        if node.left and node.right:
            node.left = Heap._insert(node.left,value)
            if node.value > node.left.value:
                return Heap._upHeapBubble(node,value)

        if node.left is None:
            node.left = Node(value)
            if node.value > node.left.value:
                return Heap._upHeapBubble(node,value)
        elif node.right is None:
            node.right = Node(value)
            if node.value > node.right.value:
                return Heap._upHeapBubble(node,value)
        
        return node
    
               
    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for elem in xs:
            self.insert(elem)

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
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            rightMost = Heap._findRight(self.root)
            self.root = Heap._remove(self.root)
            if rightMost == self.root.value:
                return
            else:
                self.root.value = rightMost

            if Heap._is_heap_satisfied(self.root) == False:
                return Heap._downHeapBubble(self.root)
    
    @staticmethod
    def _remove(node):
        if node is None:
            return
        elif node.right:
            node.right = Heap._remove(node.right)
        elif node.left:
            node.left = Heap._remove(node.left)
        else:
            if node.right is None and node.left is None:
                return None
        return node
    

    @staticmethod
    def _downHeapBubble(node):
        if node.left is None and node.right is None:
            return node
        if node.left and (node.right is None or node.left.value <= node.right.value):
            if node.left.value < node.value:
                temp1 = node.value
                temp2 = node.left.value
                node.value = temp2
                node.left.value = temp1
            node.left = Heap._downHeapBubble(node.left)
        elif node.right and (node.left is None or node.right.value <= node.left.value):
            if node.right.value < node.value:
                temp1 = node.value
                temp2 = node.right.value
                node.value = temp2
                node.right.value = temp1
            node.right = Heap._downHeapBubble(node.right)
            
        return node
            
                          
    @staticmethod
    def _upHeapBubble(node,value):
        if Heap._is_heap_satisfied(node) == True:
            return node
        
        if node.left and node.left.value > node.value:
            node.left = Heap._upHeapBubble(node.left,value)
        if  node.right and node.right.value > node.value:
            node.right = Heap._upHeapBubble(node.right, value)
        if node.left:
            if node.left.value == value:
                temp1 = node.value
                temp2 = node.left.value
                node.value = temp2
                node.left.value = temp1
        if node.right:
            if node.right == value:
                temp1 = node.value
                temp2 = node.right.value
                node.value = temp2
                node.right.value = temp1
                
        return node
    @staticmethod
    def _findRight(node):
        if node.left is None and node.right is None:
            return node.value
        elif node.right:
            return Heap._findRight(node.right)
        elif node.left:
            return Heap._findRight(node.left)
