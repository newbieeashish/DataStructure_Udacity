''''
Reverse a stack. If your stack initially has 1, 2, 3, 4
(4 at the top and 1 at the bottom),
 after reversing the order must be 4, 3, 2, 1
 (4 at the bottom and 1 at the top).

'''

class LinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def reverse_stack(stack):
    stack_holder = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        stack_holder.push(popped_element)

    _reverse_stack_recussion(stack,stack_holder)

def _reverse_stack_recussion(stack,stack_holder):
    if stack_holder.is_empty():
        return
    popped_element = stack_holder.pop()
    _reverse_stack_recussion(stack,stack_holder)
    stack.push(popped_element)


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)