with open("ip_data.csv", 'r') as csvfile:
    read_data = csvfile.read()

words = read_data.split(" ")
print("words = ",words)
data_items = []

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self,newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.next = newnext

class Unordered_list:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        found   = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found  = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous  = current
                current = current.getnext()

        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())

    def display(self):
        current = self.head
        while current != None:
            data_items.append(current.getdata())
            current = current.getnext()
            
mylist = Unordered_list()
    
for word in words:
    mylist.add(word)

search_word = input("Enter the word which you want to search = ") 
ans = mylist.search(search_word)

if ans == False:
    mylist.add(search_word)
else:
    mylist.remove(search_word)
    
mylist.display()
with open("ip_data.csv", 'w') as csvfile:
    for item in data_items[::-1]:
        csvfile.write("%s "%item)
