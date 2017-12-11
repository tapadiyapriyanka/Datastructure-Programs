class deque:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.itmes == []

    def addfront(self,item):
        self.items.append(item)

    def addrear(self, item):
        self.items.insert(0,item)

    def removefront(self):
        return self.items.pop()

    def removerear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

ip = input("Enter a string which you want to check pallindrome or not = ")
dq = deque()
for i in ip:
    dq.addfront(i)

first_str = []
for i in ip:
    first_str.append(dq.removefront())

pl1 = ''.join(first_str)
if pl1 == ip:
    print("strings are Pallendrome.. ")
else:
    print("strings are not pallendrome")
