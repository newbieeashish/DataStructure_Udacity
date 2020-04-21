'''

We will be using stacks to make sure the
parentheses are balanced in mathematical expressions such as:
((32+8)∗(5/2))/(2+6).  In real life you can see this extend to
 many things such as text editor plugins and interactive development
 environments for all sorts of bracket completion checks.

Take a string as an input and return True
if it's parentheses are balanced or False if it is not.

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

def equation_checker(equation):
    stack = Stack()

    for char in equation:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() == None:
                return False
    if stack.size() == 0:
        return True
    else:
        return False

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")
