class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, elem):
        self.in_stack.push(elem)

    def dequeue(self):
        # uzupelnij

        return self.out_stack.pop()

    def peek(self):
    #     uzupelnij

    def is_empty(self):
        return self.in_stack.is_empty() and self.out_stack.is_empty()

    def size(self):
        return self.in_stack.size() + self.out_stack.size()


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.dequeue())  # 10
    print(queue.dequeue())  # 20
    print(queue.dequeue())  # 30
    print(queue.is_empty())  # True
