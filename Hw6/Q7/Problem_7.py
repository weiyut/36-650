


class Node:
    def __init__(self, data):
        self.too_big = None
        self.big = None
        self.small = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif data - self.data < 10:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            else:
                if self.too_big is None:
                    self.too_big = Node(data)
                else:
                    self.too_big.insert(data)
        else:
            self.data = data
    
    def traversal(self):
        if self.small:
            self.small.traversal()
        if self.data:
            #skip the node if its empty#
            print(self.data)
        if self.big:
            self.big.traversal()
        if self.too_big:
            self.too_big.traversal()
    
    def delete(self, data):
        if data == self.data:
            self.data = None
                
        elif data < self.data:
            if self.small:
                self.small.delete(data)
        elif data - self.data < 10:
            if self.big:
                self.big.delete(data)
        else:
            if self.too_big: 
                self.too_big.delete(data)




root = Node(20)
root.insert(40)
root.insert(45)
root.insert(32)
print('Tree contents after insertion using the traversal():')
root.traversal()

root.delete(45)
print('Tree contents after deleting 45 using the traversal():')

root.traversal()

root.delete(20)
print('Tree contents after deleting 45 and 20 using the traversal():')
root.traversal()






