class Stack:
  def __init__(self):
    self.items = []
  def push(self,item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()

stack = Stack()

stack.push(3)
stack.push(10)
stack.push(2)
stack.pop()
stack.pop()

print(stack.items)

class Queue:
  def __init__(self):
    self.items = []
  def enqueue(self, value):
    self.items.insert(0, value)
  def dequeue(self):
    return self.items.pop()
  def isEmpty(self):
    return self.items == []

queue = Queue()

queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(45)  
queue.dequeue()
queue.dequeue()



print(queue.items)