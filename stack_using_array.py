'''
Goal will be to implement a Stack class that has the following behaviors:

push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise

'''

class Stack:
    def __init__(self,intial_size = 10):
        self.arr = [0 for _ in range(intial_size)]
        self.next_index = 0
        self.num_element = 0

foo = Stack()
print(foo.arr)
print("Pass" if foo.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")

'''push method'''

class Stack:
    def __init__(self,initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_element = 0

    def push(self,data):
        self.arr[self.next_index] = data
        self.next_index +=1
        self.num_element +=1

foo = Stack()
foo.push("Test!")
print(foo.arr)
print("Pass" if foo.arr[0] == "Test!" else "Fail")

'''handle full capacity'''

class Stack:
    def __init__(self,intial_size = 10):
        self.arr = [0 for _ in range(intial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self,data):
        def push(self, data):
            if self.next_index == len(self.arr):
                print("Out of space! Increasing array capacity ...")
                self._handle_stack_capacity_full()

            self.arr[self.next_index] = data
            self.next_index += 1
            self.num_elements += 1


    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2*len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

'''Implementing Size and Is_empty methods'''

class Stack:
    def __init__(self,intial_size=10):
        self.arr = [0 for _ in range(intial_size)]
        self.next_index = 0
        self.num_element = 0

    def push(self,data):
        if self.next_index == len(self.arr):
            print('out of space, inc size')
            self._handle_stack_capacity_full()
        self.arr[self.next_index] = data
        self.next_index +=1
        self.num_element +=1

    def size(self):
        return self.num_element

    def isempty(self):
        return self.num_element ==0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2*len(old_arr))]
        for index,value in enumerate(old_arr):
            self.arr[index] = value

foo = Stack()
print(foo.size()) # Should return 0
print(foo.isempty()) # Should return True
foo.push("Test") # Let's push an item onto the stack and check again
print(foo.size()) # Should return 1
print(foo.isempty()) # Should return False

'''implementing pop method'''

class Stack:
    def __init__(self,intial_size =10):
        self.arr = [0 for _ in range(intial_size)]
        self.next_index = 0
        self.num_element = 0

    def push(self,data):
        if self.next_index == len(self.arr):
            print('out of space, inc space')
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index +=1
        self.num_element +=1

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -=1
        self.num_element -=1
        return self.arr[self.next_index]

    def size(self):
        return self.num_element

    def is_empty(self):

        return self.num_element ==0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2*len(old_arr))]
        for index,value in enumerate(old_arr):
            self.arr[index] = value

foo = Stack()
foo.push("Test") # We first have to push an item so that we'll have something to pop
print(foo.pop()) # Should return the popped item, which is "Test"
print(foo.pop()) # Should return None, since there's nothing left in the stack