class stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

s = stack()
paran = "(5+6)(7+8)/(4+3)(5+6)(7+8)/(4+3)"
balenced = True
index = 0

for p in paran:
    if p == '(':
        s.push(p)
    elif p == ')':
        if s.size() != 0:
            s.pop()
        else:
            print("Your Expression is incorrect")
            break
    
if s.size() == 0:
    print("Your expression is correctly Balenced.. ")
else:
    print("Your Expression is incorrect..")





