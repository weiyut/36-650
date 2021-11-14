

class Queue:
    inner_list = []
    counter = 0
    
    def enqueue(self, value):
        self.inner_list.insert(0, value)
        self.counter = self.counter + 1
        
        
    def dequeue(self):
        if self.counter == 0:
            return 'Needs implementation'
        else :
            self.counter = self.counter - 1
            result = self.inner_list.pop(self.counter)
            return result
        
### delete function starts from this line         
    def delete(self, value):
        pos_count = 0
        limit = len(self.inner_list)
        while pos_count < limit:
            temp = self.dequeue()
            if value != temp:
                self.enqueue(temp)
            pos_count = pos_count + 1
        




obj = Queue()
obj.enqueue(5)
obj.enqueue(7)
obj.enqueue(13)
obj.enqueue(4)
obj.enqueue(7)
obj.delete(7)

print(obj.dequeue())







