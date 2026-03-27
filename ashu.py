# # topic :: dynamic array::
# # import sys
# # l= []

# # for i in range(100):
# #     print(i,sys.getsizeof(l))
# #     l.append(i)

# # import ctypes

# # class meralist:
# #     def __init__(self):
# #         self.size = 1
# #         self.n = 0
# #         self.a = self.__make_array(self.size)
# #     def __make_array(self,capacity):
# #         return (capacity*ctypes.py_object)()   
# #     def __str__(self):
# #         result = ''
# #         for i in range(self.n):
# #             result = result + str(self.a(i)) + ','
# #         return '['+ result +']'     
    

# # l.append('hello')
# # l.append(3)
# # l.append(True)
# # l.append(100)
# # print(l)    

# # linked list:::--
# # It is the linear data structure of the array and it is the collection of the notes.

# # class node:
# #     def __init__(self,value):
# #         self.data = value
# #         self.next = None

# # a = node(1)
# # b = node(2)  
# # c = node(3)   
# # print(c.data)   
# # print(id(c))
# # print(id(b))
# # print(id(a))
        
# # class linkedlist:
# #     def __init__(self):
# #         self.head = None
# #         self.n = 0

# #     def __len__(self):
# #         return self.n
# # l  = linkedlist()
# # print(len(l))       

# # operation on the linkedlist:::
# # insert,traverse,delete,search

# # def transverse(self):
# #     curr = self.head

# #     while curr != None:
# #         print(curr.data)
# #         curr = curr.next

# # self.traverse()        

# def insert_after(self,after,value):

#    new_node = Node(value) 

#    curr = self.head

#    while curr != None:
#       if curr.data == after:
#          break
#       curr = curr.next
#       if curr != None:
#          new_node.next = curr.next
# #          curr.next = new_node
# #       else:
# #          return 'item not found'   

# # stack = []
# # stack.append(1)
# # stack.append(2)     
# # stack.append(3)
# # print("stack after push = ",stack)

# # popped_element = stack.pop()
# # print("popped element = ",popped_element)

# # # queue = []
# # # queue.append(1)
# # # queue.append(2)     
# # # queue.append(3)
# # # queue.append(4)
# # # print("queue after enqueue = ",queue)
# # # dequeued_element = queue.pop(0)
# # # print("dequeued element = ",dequeued_element)

# # class queue:
# #     def __init__(self):
# # #         self.values = []
# # #     def enqueue(self,x):
# # #         self.values.append(x)
# # #         def dequeue(self):
# # #             front = self.values[0]
# # #             self.values = self.values[1:]   
# # #             return front 
# # # q1 = queue()
# # # q1.enqueue(10)
# # # q1.enqueue(20)
# # # q1.enqueue(30)
# # # print(q1.values)    
# # # q1.enqueue(40)
# # # print(q1.values)
# # # print(q1.dequeue()) print(q1.values)

# # # class employee:
# # #     def set_data(self,name,age,salary):
# # #         self.n = name
# # #         self.a = age
# # #         self.s = salary

# # #     def display_data(self):
# # #         print(self.n,self.a,self.s)   

# # # e1 = employee()
# # # e1.set_data('ashu',23,50000)
# # # e1.display_data()

# # # e2 = employee()
# # # e2.set_data('ram',25,60000)
# # # e2.display_data()

# class employee:
#     def set_data(self,name,age,salary):
#         self.n = name
#         self.a = age
#         self.s = salary

#     def display_data(self):
#         print(self.n,self.a,self.s)   

# e1 = employee()
# e1.set_data("ashu",18,40000)         
# e1.display_data()

# e2= employee()
# e2.set_data("ram",20,50000)
# e2.display_data()


# class employee:
#     def set_data(self,n,a,s):
#         self.name = n
#         self.age = a
#         self.salary = s

#     def display_data(self):
#         print(self.name,self.age,self.salary) 


#     def __init__(self,n="",a="",s=""):
#         self.name = n
#         self.age = a
#         self.salary = s

#     def __del__(self):

#         print("deleting object" + str(self))

# e1 =employee() 
# e1.set_data("ashu",18,40000)         
# e1.display_data()

# e2= employee()
# e2.set_data("ram",20,50000)
# e2.display_data()

# e1 = None
# e2 = None

# queue = []

# def insertion():
#     item= int(input("enter any element: "))
#     queue.append(item)

# print(queue)

# def delete():
#     if len(queue) == 0:
#         print("queue is empty")

#     else:
#         removed_item = queue.pop()
#         print(removed_item)    
    
# def traversal():
#     if len(queue) == 0:
#         print("list is empty")
#     else:
#         print("queue elements are: ") 

#         while True:
#             print("1.insert")   
#             print("2.delete") 
#             print("3.traversal")  
#             print("4.exit")   
# choice =int(input("enter your choice: "))      

# if choice == 1:
#     insertion()
# elif choice == 2:
#     delete()
# elif choice == 3:
#     traversal()
# elif choice == 4:          



#     print("exit the programme")   

# else:
#     print("invalid choice try again later") 

# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)

# print("stack the element",stack)

# popped_element = stack.pop()

# print("the element which are popped",popped_element)

# queue = []

# queue.append(1)
# # queue.append(2)
# # queue.append(3)

# # print("queue elements are the",queue)

# # dequeue_element=queue.pop()

# # print("the dequeue elements are the ",dequeue_element)

# class stack:
#     def __init__(self):
#         self.data = []
#     def push(self,x):
#         self.data.append(x)
#     def pop(self):
#         if len (self.data) == 0:
#             return -1
#         x = self.data[-1]

#         self.data.pop()
#         return x
    
#     def top(self):
#         if len (self.data) == 0:
#             print("stack is empty")

#         else:
#             return self.data[-1]    
        
   
        
   

# stack = stack()
# stack.push(1)           
# stack.push(2)   
# stack.push(3)          
# stack.push(4)    
# print(stack.pop())
# print(stack.top())                 


# class stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,x):
#         self.stack.append(x)
#         print(x,"item append in the stack")

#     def pop(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             print(self.stack.pop(),"item should br popoed from the stack")

#     def peek(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             print("top element is",self.stack[-1])

#     def is_empty(self):
#         return len(self.stack) == 0
    
#     print("stack is empty")

#     def display(self):
#         print("stack element",self.stack)

                                
# s = stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)

# s.display()
# s.pop()
# s.peek()
# s.display()

# def factorial(fact):
#     if fact == 0 or fact == 1:
#         return 1
#     else:
#         return fact*factorial(fact-1)
# num = int(input("enter any number"))
# result= factorial(num)    

# print(result,num)

# def fibonacci(n):
#     if n <=1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# num = int(input("enter any number: "))

# result = fibonacci(num)
# print(result,num)

# def sum(n):
#     if n == 0:
#         return n
    
#     else:
#         return n+1
# num = int(input("enter any number"))    
# result = sum(num)
# print("the result of the sum is",result ,"if input is entered as")


# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class linkedlist:
#     def __init__(self):

#         self.head = None


# def insert (self,data):
#     new = node(data)

#     if self.haed == None:
# #         self.head = new
# #     else:
# #         temp = self.head
# #         while temp.next != None:
# #             temp = temp.next
# #         temp.next = new

# # def delete(self,value):
# #     temp =self.head

# #     if temp != None and temp.data == value:
# #         self.head = temp.next
# #         return
# #     prev = None
# #     while temp != None and temp.data != value:
# #         prev = temp
# #         temp = temp.next
# #     if temp == None:
# #         print("not found")
# #         return
# #     prev.next = temp.next

# # def traverse(self):
# #     temp = self.head

# #     while temp != None:
# #         print(temp.data, end='->')
# #         temp = temp.next

# #         print("None")

# # l = linkedlist()

# # l.insert(1)
# # l.insert(2)
# # l.insert(3)
# # l.insert(4)

# # l.display()

# # l.delete(2)

# # l.display()

# def precedence(operator):
# #     if operator == "+" or operator == "-":
# #         return 1
# #     elif operator == "*" or operator == "%":
# #         return 2
# #     elif operator == "^":
# #         return 3
    
# #     else:
# #         return 0

# # def infix_to_postfix(expression):
# #     stack = []
# #     postfix = ""
# #     for char in expression:
# #         if char.isalnum():
# #             postfix += char
# #         elif char == "(":
# #          stack.append(char)  
# #         elif char == ")":
# #             while stack and stack [-1] != "(":
# #                 postfix += stack.pop()
# #         else:
# #             while stack  and precedence (stack[-1]) >= precedence (char):
# #                 postfix += stack.pop()
# # expr = input("enter your expression: ")

# # postfix_expr = infix_to_postfix(expr)

# # print("post expression",postfix_expr)

# # def precednece(operator):
# #     if operator == "+" or operator == "-":
# #         return 1
# #     elif operator == "*" or operator == "%":
# #         return 2
    
# #     elif operator == "^":
# #         return 3
# #     else:
# #         return 0

# # def infix_to_postfix(expression):
# #     stack = []
# #     postfix = ""
# #     for char in expression():
# #         if char. isalnum():
# #             postfix += char

# #         elif char == "(":
# #             stack.append(char)

# #         elif char == ")":
# #             while stack and stack [-1] != "(":

# #                 postfix += stack.pop()
# #         else:
# #             while stack and precednece(stack[-1]) >= precednece(char):
# #                 postfix += stack.pop()
# # expr = input("enter any expression")

# # postfix = infix_to_postfix(expr)
# # print(postfix)


# class stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,x):
#         self.stack.append(x)
#         print(x,"item should be appended")

#     def pop(self):
#         if self.is_empty():
#             print("stack is empty")

#         else:
#             print(self.stack.pop(),"item should be popped")

#     def peek(self):
#         if self.is_empty():
#             print("stack is empty")            
#         else:
#             print(self.stack[-1],"item should be on top")

#     def is_empty(self):
#         return len(self.stack) == 0
#     def display(self):
#         print("item should be displayed",self.stack)

# s = stack()

# s.display()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)

# s.pop()
# s.peek()
# s.display()


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n* factorial(n-1)
# num = int(input("enter any number: "))    
# result = factorial(num)

# print(result)

# def fibonacci (n):
#     if n <=1 :
#         return n
#     else:
#         return fibonacci (n-1) + fibonacci (n-2)
# num = int(input("enter any number: "))    
# result = fibonacci (num)
# print(result)

# def precedence(operator):
#     if operator == "+" or operator == "-":
#         return 1
#     elif operator == "*" or operator == "%":
#         return 2
#     elif operator == "^":
#         return 3
#     else:
#         return 0
# def infix_to_postfix(expression):
#     stack = []
#     postfix = ""

#     for char in expression:
#         if char .isalnum():
#             postfix += char

#         elif char == "(":
#             stack.append(char)

#         elif char == ")":
# #             while stack and stack [-1] != "(":
# #                 postfix += stack.pop()

# #         else:
# #             while stack and precedence (stack[-1]) >= precedence(char):
# #                 postfix += stack.pop()

# # expr = input("enter your expression: ")         

# # postfix  = infix_to_postfix(expr)
# # print(postfix)

# # queue = []

# # def enqueue(value):
# #     queue.append(value)
# #     print(value,"inserted")

# # def dequeue():
# #     if len(queue) == 0:
# #         print("queue is empty")

# #     else:
# #         removed = queue.pop(0)
# #         print(removed,"deleted")

# # def display():
# #     if len (queue) == 0:
# #         print("queue is empty")

# #     else:
# #         print(queue,"queue is always displayed")

# # enqueue = (10)   
# # enqueue = (20)      
# # enqueue = (30)      
# # enqueue = (40)       

# # display()
# # dequeue()
# # display()

# #  binary search::
# # arr = [10,20,30,40,50]

# # key = 30

# # low = 0
# # high = len(arr) -1

# # while low <= high:
# #     mid = (low+high) // 2

# #     if arr[mid] == key:
# #         print("found at index",mid)
# #         break

# #     elif arr[mid] < key:
# #         low = mid +1

# #     else:
# #         high = mid - 1
# # else:
# #     print("not found")    
# # 



# class stack:
#     def __init__(self):
#         self.stack= []
    

#     def push(self,x):
#         self.stack.append(x)
#         print(x,"item should be appended")

#     def pop(self):
#         if self.is_empty():
#             print("stack is empty")

#         else:
#             print(self.stack.pop(),"item shold be popped")

#     def peek(self):
#         if self.is_empty():
#             print("stack is empty")
#         else:
#             print(self.stack[-1],"items should be on top")

#     def is_empty(Self):
#         return len(Self.stack) == 0
    
#     def display(self):
#         print("item should be displayed",self.stack)
# s = stack()

# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.display()
# s.pop()
# s.peek()
# s.display()


# queue = []

# def enqueue(value):
#     queue.append(value)
#     print(value,"item should be inserted")

# def dequeue():
#     if len(queue) == 0:
#         print("queue is empty")

#     else:
#         removed = queue.pop(0)
#         print(removed,"item should be popped")

# def display():
# #     if len(queue) == 0:
# #         print("queue is empty")

# #     else:
# #         print(queue,"queue should be displayed")

# # enqueue(10)
# # enqueue(20)
# # enqueue(30)     
# # enqueue(40)
# # display()
# # dequeue()
# # display()            

# def precedence(operator):
#     if operator == "=" or operator == "-":
#         return 1
    
#     elif operator == "*" or operator == "%":
#         return 2

#     elif operator == "^":    
#         return 3
    
#     else:
#         return 0
    
# def infix_to_postfix(expression):
#     stack = []
#     postfix = ""

#     for char in expression:
#         if char.isalnum():
#             postfix += char

#         elif char == "(":
#             stack.append(char)

#         elif char == ")":
#             while stack and stack[-1] != "(":
#                 postfix += stack.pop()
#                 stack.pop()  

#         else:
#             while stack and precedence(char) <= precedence(stack[-1]):
#                 postfix += stack.pop()
#                 stack.append(char)

#             while stack:
#                 postfix += stack.pop()
#                 return postfix    

# expr = input("enter your expression:")
# expr = expr.replace(" ","")
# postfix = infix_to_postfix(expr)
# print(postfix)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# num = int(input("enter any number: "))  
# result = factorial(num)
# print(result)   

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# num = int(input("enter any number:"))  
# result = fibonacci(num)
# print(result)  

# bubble sort code: 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                return arr
            
            arr = [64,34,25,12,22,11,90]
            bubble_sort(arr)
            print("sorted array",arr)    

     

                













            




        














    



 






    
