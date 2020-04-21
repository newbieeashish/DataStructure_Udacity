'''

 push is when you add an element to the top of the stack and
 a pop is when you remove an element from the top of the stack.
 Python 3.x conviently allows us to demonstate this functionality with a list.
 When you have a list such as [2,4,5,6] you can decide which end of the list is
 the bottom and the top of the stack respectivley.
'''

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.size() ==0:
            return None
        else:
            return self.items.pop()


MyStack = Stack()

MyStack.push("Web Page 1")
MyStack.push("Web Page 2")
MyStack.push("Web Page 3")

print (MyStack.items)

MyStack.pop()
MyStack.pop()

print ("Pass" if (MyStack.items[0] == 'Web Page 1') else "Fail")

MyStack.pop()

print ("Pass" if (MyStack.pop() == None) else "Fail")
