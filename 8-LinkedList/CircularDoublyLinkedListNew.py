class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def constructor2(self, value):
        new_node = Node(value)
        new_node.next = new_node
        new_node.prev = new_node
        
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        result = ''
        currentNode = self.head
        while currentNode:
            result += str(currentNode.value)
            currentNode = currentNode.next
            if currentNode == self.head: break
            result += ' <-> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
            if currentNode == self.head:
                break

    def reverse_traverse(self):
        currentNode = self.tail
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.prev
            if currentNode == self.tail:
                break

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            print("Error: Index out of bounds.")
            return

        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        tempNode = self.get(index - 1)

        new_node.next = tempNode.next
        new_node.prev = tempNode
        tempNode.next.prev = new_node
        tempNode.next = new_node

        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        currentNode = None
        if index < self.length // 2:
            currentNode = self.head
            for i in range(index):
                currentNode = currentNode.next
        else:
            currentNode = self.tail
            for i in range(self.length - 1, index, -1):
                currentNode = currentNode.prev

        return currentNode

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        if self.length == 0:
            return None

        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head

        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None

        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.prev = None
            popped_node.next = None
            self.tail.next = self.head
            self.head.prev = self.tail

        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        self.length -= 1
        return popped_node

    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0



new_ccll = CircularDoublyLinkedList()
new_ccll.append(10)
new_ccll.append(20)
new_ccll.append(30)
print(new_ccll)