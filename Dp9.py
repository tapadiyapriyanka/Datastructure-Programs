class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_node):
        self.next_node = new_node
        
class Queue:
    def __init__(self,head=None):
        self.head = head
    
    def enqueue(self,data):
        new_item = Node(data)
        current = self.head
        if current is None:
            self.head = new_item
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(new_item)

    def dequeue(self):
        current = self.head
        if current != None:
            self.head = current.get_next()
        else:
            print("Queue is empty.")

    def __len__(self):
        return len(self.temp)

    def is_empty(self):
        if self.head == None:
            print("Queue is empty")

    def print_queue(self):
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        return self.temp
    
q = Queue()
week_days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
q.enqueue(week_days)
sublist = []
mainlist = []
k = 0
count = 0
for i in range(1,36):
    if count<7:
        count = count + 1
        k = k+1
        sublist.append(k)
    else :
        q.enqueue(sublist)
        sublist = []
        count = 0
            
q.enqueue(sublist)
series = q.print_queue()

for i in series:
    print("  ".join(str(k) for k in i))
