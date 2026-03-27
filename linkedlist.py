
# # pattern solvning problem

# # for i in range(1,6):
# #     for j in range(i):
# #         print("*", end = " ")
# #     print()


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# a = Node(3)
# b = Node(5)
# c = Node(7)    

# a.next = b
# b.next = c

# head = a
# def printlist():

# # print(head.data)
# # print(head.next.data)
# # print(head.next.next.data)
#  curr = head
# # while curr != None:
    
# #     print(curr.data, end = " ")

# #     curr = curr.next
# # # adding value in linkedlist from starting
# # newNode = Node(4)    
# # newNode.next = head
# # head = newNode

# # curr = head
# # while curr != None:
# #     print(curr.data,end=" ")
# #     curr = curr.next
# # # adding value in linkedlist from last
# # newNode = Node(1)
# # curr = head
# # while curr.next != None:
# #    curr.next = newNode
# #    curr = curr.next

# # # at the mid of the linkedlist::

# # k= 2
# # newNode = Node(6)
# # curr = head
# # for i in range(k-1):
# #     curr = curr.next
# #     curr.next = newNode.next
# #     curr.next = newNode

    

# def precedence(operator):
#     if operator == "=" or operator == "-":
#         return 1
#     elif operator == "*" or operator == "/":
#         return 2
#     elif operator == "^":
#         return 3
#     else:
#         return 0
    
# def infix_to_postfix(expression):
#     stack = []
#     postfix = ""  

#     for char in expression:
#         if char. isalnum():
#             postfix += char
#         elif char == "(":
#             stack.append(char)
#         elif char == ")":
#             while stack and stack[-1] != "(":
#                 postfix += stack.pop()

#             stack.pop()
#         else:
# #             while stack and precedence(stack[-1]) >= precedence(char):
# #                 postfix += stack.pop()
# #             stack.append(char)

# #             while stack:
# #                 postfix += stack.pop()
# #             return postfix
        
# #         expr =input("enter the infix expression:")

# #         expr = expr.replace(" ", "")
# #         postfix_expr = infix_to_postfix(expr)       
# #         print("postfix expression",postfix_expr)

# # linkedlist of the prograame::

# class node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# a = node(1)
# b = node(2)
# c = node(3)
# a.next = b
# b.next = c
# head = a
# print(head.data)

# # traversing 
# def printlinkedlist(head):
#  curr = head   

#  while curr != None:
   
#     print(curr.data,end="")
#     curr = curr.next
# printlinkedlist(head)

# # insertion at the beginning::

# newnode = node(4)

# newnode.next = head

# newnode = head
# printlinkedlist(head)

# # insert at the end of the linkedlist::

# newnode = node(8)

# # curr = head

# # while curr.next != None:
# #    curr = curr.next
# #    curr.next = head

# #    printlinkedlist(head)

# # # insert at the middle of the linkedlist::

# # k= 2

# # newnode = node(6)
# # curr = head
# # for i in range(k-1):
# #    curr = curr.next
# #    newnode.next = curr.next
# #    curr.next = newnode

# # # deletion from start the linkedlist::

# # head = head.next
# # printlinkedlist(head)

# # # delete at the end of the linkedlist::
# # curr = head

# # while curr.next.next != None:
# #    curr = curr.next
# # curr = None
# # printlinkedlist(head)   


# class node:
#     def __init__(self,data):
#             self.data = data
#             self.next = None

# a = node(1) 
# b = node(2) 
# c = node(3) 

# a.next = b
# b.next = c
# head = a
# print(head.data)

# # traversing the linkedlist:: 

# def printlinkedlist(head):
#     curr = head
#     while curr != None:
#         print(curr.data,end="")
#         curr = curr.next
        

#    # insertion at the beginning of the linkedlist::

# newnode = node(4)

# newnode.next = head
# head = newnode


# # insertion at the end of the linkedlist::

# newnode = node(5)
# curr = head
# while curr.next != None:
#     curr = curr.next
# curr.next = newnode
# # printlinkedlist(head)

# # insertion at the mid of the linkedlist::

# k = 2
# newnode = node(6)
# curr = head
# for i in range(k-1):
#     curr = curr.next
# newnode.next = curr.next
# curr.next = newnode
# # printlinkedlist(head)


# # deletion from the start of the linkedlist::

# head= head.next
# # printlinkedlist(head)

# # deletion from the end of the linkedlist::

# curr = head
# while curr.next.next != None:
#     curr = curr.next
# curr.next = None
# printlinkedlist(head)

# binary search ::

# def binary_seacrh(arr,key):
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid = (low+high)//2

#         if arr[mid] == key:
#             return mid
#         elif arr[mid] < key:
#             high = mid-1
          

#         else:
#             low  = mid +1
#             return -1
        
# arr = [1,2,3,4,5,6,7,8,9]
# key = 5
# print(binary_seacrh(arr,key))      


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print("matrix:")
# print(matrix)

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j],end = "")
#         print()

# bubble sorting:

def bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                return arr
            arr = [64,34,25,12,22,11,90]
            bubble_Sort(arr)
            print("sorted arr",arr)








     























