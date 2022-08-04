class stack():
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,item):                                        # >>>> to append the element ot the stack 
        self.stack.append(item)
        self.top+=1
    def check_empty(self):                                      # >>>> to check if the stack empty or not 
        return  (True if self.top==-1 else False)  
    def pop(self):                                              # >>>> to pop the last item in the stack[top]
        if (stack.check_empty(self)):                           # <<<<>>>>  Hint: use it with list()
            print(" this list is empty ")
        else:
            yield self.stack.pop()
            self.top-=1
    def pop_without_delete(self):                              # >>>> to pop but without deleting the element 
        if (stack.check_empty(self)):
            print(" this list is empty ")
        else:
            return self.stack[self.top]
    def print_the_stack(self):                                 # >>>> print the stack 
        return self.stack[::-1]

r=stack()
r.push('name1')
r.push(1)
r.push('name2')
r.push('name3')
r.push(13)
r.push(4444)
print(list(r.pop()))



