class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit 

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            pass
            # raise ValueError("Stack is full")
        else:
            return self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        for i in range(len(self.items)-1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
