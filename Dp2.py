with open("ip_data_num", "r") as read_file:
    read_data = read_file.read()

nums = read_data.split(" ")
print("nums = ",nums)

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext

class ordered_list:
    def __init__(self):
        self.head = None

    def add(self, item):
        current  = self.head
        previous = None
        stop     = False
        while current != None and not stop:
            if current.getdata() > item:
                stop = True
            else:
                previous = current
                current  = current.getnext()

        temp = Node(item)
        if previous == None:
            temp.setnext(self.head)
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)

    def search(self, item):
        current = self.head
        found   = False
        stop    = False
        while current != None and not found and not stop:
            if current.getdata() == item:
                found = True
            else:
                if current.getdata() > item:
                    stop = True
                else:
                    current = current.getnext()
        return found
            
            
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getnext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found  =  False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
                
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())
            
    def display(self):
        current = self.head
        writefile = open("ip_data_num", 'w')
        while current != None:
            print("item = ",current.getdata())
            writefile.write("%s "%str(current.getdata()))
            current = current.getnext()

mylist = ordered_list()

for num in nums:
    mylist.add(int(num))    

item = int(input("Enter which element you want to add or search? = "))
ans = mylist.search(item)
print("ans = ",ans)
if ans == True:
    mylist.remove(item)
mylist.display()
