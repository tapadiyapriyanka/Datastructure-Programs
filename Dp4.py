class queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def enque(self, item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display_que(self):
        return self.items

ip = int(input("Enter How many people You want to enter in queue = "))
q = queue()
for i in range(ip):
    q.enque(i)

sum = 0
for i in range(ip):
    ans = input("Do you want to withdraw or deposite?? = ")
    if ans.startswith('d') == True:
        amount = int(input("Enter how many amount you want to deposite = "))
        sum = sum + amount
    else:
        amount = int(input("Enter how many amount you want to withdraw = "))
        sum = sum - amount
print("cash balence = ",sum)
