# Node class to represent each element in the queue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Queue class to manage queue operations
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.size = 0      # Keeps track of the queue size

    # Add an element to the rear of the queue
    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Add the new node after the rear
            self.rear = new_node       # Move the rear to the new node
        self.size += 1

    # Remove and return the front element
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        dequeued_node = self.front
        self.front = self.front.next  # Move the front pointer to the next node
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node.value

    # Return the front element without removing it
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.value

    # Check if the queue is empty
    def isEmpty(self):
        return self.size == 0

    # Get the current size of the queue
    def queueSize(self):
        return self.size

    # Display all elements in the queue from front to rear
    def displayQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Create a queue and test the methods with numbers
myQueue = Queue()

# Test enqueueing numbers into the queue
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)

# Display the queue
print("Queue: ", end="")
myQueue.displayQueue()

# Test dequeue operation
print("Dequeue: ", myQueue.dequeue())  # Dequeue and show front item

# Test peek operation
print("Peek: ", myQueue.peek())  # Show front item without removing it

# Check if the queue is empty
print("isEmpty: ", myQueue.isEmpty())  # Check if queue is empty

# Show the current size of the queue
print("Size: ", myQueue.queueSize())  # Show current queue size

# Display the queue again
print("Queue after dequeue: ", end="")
myQueue.displayQueue()

# Test dequeue the rest of the queue
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())
print("Dequeue: ", myQueue.dequeue())

# Check if the queue is empty again
print("isEmpty after dequeues: ", myQueue.isEmpty())  # Should be True now
