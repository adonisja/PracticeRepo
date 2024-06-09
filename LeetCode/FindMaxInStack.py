class Block:
    def __init__(self, value, localMax):
        self.value = value
        self.localMax = localMax

class Stack():
    def __init__(self, size):
            self.size = size
            self.items = [None] * size
            self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print('Stack is full')
        else:
            self.top += 1
            if self.top == 0:
                self.stack[self.top] = Block(value, value)
            else:
                if self.stack[self.top - 1].localMax > value:
                    self.stack[self.top] = Block(value, self.stack[self.top - 1].localMax)
                else:
                    self.stack[self.top] = Block(value, value)
        print(value, "inserted in the stack")

        
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            self.top -= 1
            print("Element was removed")

    def max(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("The maximum value is the stack is: ", self.stack[self.top].localMax)

def main():
    stack = Stack(6)
    stack.push(2)
    stack.max()
    stack.push(6)
    stack.max()
    stack.pop()
    stack.max()  

if __name__ ==  '__main__':
    main()