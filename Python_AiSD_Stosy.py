class Stack:
    #variable
    __stack = []

    #methods
    def __init__(self):
        self.__stack= []

    def push(self, object):
        self.__stack.append(object)

    def pop(self):
        return self.__stack.pop()

    def peek(self):
        return self.__stack[-1]

    def isEmpty(self):
        if not self.__stack:
            return True
        else:
            return False

    def size(self):
        return len(self.__stack)

stos = Stack()
stos.push(4)
stos.push(3)
stos.push(2)
stos.push(1)
print(stos.pop())
print(stos.peek())
print(stos.peek())
print(stos.isEmpty())
print(stos.size())