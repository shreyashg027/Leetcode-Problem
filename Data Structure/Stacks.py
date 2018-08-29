class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if data not in self.stack:
            self.stack.append(data)

    def peek(self):
        return self.stack[len(self.stack)-1]

    def remove(self):
        if len(self.stack) <= 0:
            return 'No element in the stack'
        else:
            return self.stack.pop()

test = Stack()
test.push('Mon')
test.push('Tue')
test.push('wed')
print(test.peek())
print(test.remove())
print(test.peek())


