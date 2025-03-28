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
        if self.out_stack.is_empty():  # jesli pusty przenosimy wszystko z drugiego stosu
            if self.in_stack.is_empty():
                raise IndexError("dequeue from empty queue")  # Kolejka jest pusta
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        else:
            return self.out_stack.pop()

    def peek(self):
        if self.out_stack.is_empty():
            if self.in_stack.is_empty():
                raise IndexError("peek from empty queue")
            while self.in_stack:
                self.out_stack.push(self.in_stack.pop())
        if self.out_stack:
            return self.out_stack.peek()

    def is_empty(self):
        return self.out_stack.is_empty() or self.in_stack.is_empty()

    def size(self):
        return self.out_stack.size() + self.in_stack.size()


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print(queue.dequeue())  # 10
    print(queue.dequeue())  # 20
    print(queue.dequeue())  # 20
    print(queue.is_empty())  # False