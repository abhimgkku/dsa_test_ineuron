class q:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.insert(0, item)
    def pop(self):
        return self.items.pop
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items) == 0


q = q()
q.push("a")
q.push("b")
print(q.pop())
print(q.isEmpty())
print(q.pop())
print(q.isEmpty())
print(q.size()==0)