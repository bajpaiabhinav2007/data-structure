# class stack:
#     def __init__(self):
#         self.items = []
#         def isEmpty(self):
#             return len( self.items) == 0
        

#         def push (self, items):
#             self.items.append(items) 

#         def pop(self):
#                 if self.isEmpty():
# #                     return "stack is empty"
                
# #                 else:
# #                     return self.items.pop()

# #         def peek(self):
# #             if not self.isEmpty():
# #                 return self.items[-1]    
# #             else:
# #                 return "stack is empty"     
            

# #         def size(self):
# #             return len(self.items)   

# #         def display(self):
# #             return self.items   
        
# #         def menu():
# #             print("1.push")
# #             print("2.pop")
# #             print("3.peek")     
# #             print("4.size")
# #             print("5.display")
# #             print("6.exit")

                
# #         choice  = int(input("enter your choicr:"))

# #         if choice == 1:
# #                     item = int(input("enter the item to push:"))
# #                     self.push(item)
                
# #         elif choice == 2:
# #                     print("popped item:",self.pop())

# #         elif choice == 3:
# #                     print("top item is:",self.peek())

# #         elif choice == 4:
# #                     print("size of stack is:",self.size())  

# #         elif choice == 5:
# #                     print("stack items are:",self.dispaly())

# #         else:
# #                     print("it is a invalid choice")  
# # s=stack()

# class father:
#     def land(self):
#         print("father have a land of 50 acre" )

# class son(father):
#     def money(self):
#         print("son have a money of 5 lakhs")

# obj = son()        
# obj.land()
# obj.money()

# class a:
#     def __init__(self,name):

#         self.name = name
#         print("name is:",self.name) 

# obj = a("abhinav bajpai") 

# single level inheritence


# class A:

#     num1 = int(input("enter the num1:"))
#     num2 = int(input("enter the num2: "))
#     choose = input("enter the operation you want to perform:")

#     print("+",1)
#     print("-",2)
#     print("*",3)
#     print("/",4)
#     print("%",5)
    



#     def __init__(self):
#         print("welcome to calculator")

# #     def add(self):
# #         print("the addition od two number is :",self.num1+self.num2)

# #     def subtraction(self):
# #         print("the subtraction of two number is :",self.num1 - self.num2)    

# #     def multiply(self)    :
# #         print("the multiplication of two number is = ",self.num1*self.num2)

# #     def divide(self):
# #         print("the division of two number is ",self.num1/self.num2)    

# # class B(A):
# #     def modulus(self):
# #         print("the modulus of two number is :",self.num1 % self.num2)   

# # class C(B):

# #     def __land(self):
# #         print("this is private method")

# #     def __money(self):
# #         print("this is private method of money")        
             

# # # obj = B()     
# # obj= C()

# # obj.add()
# # obj.subtraction()
# # obj.multiply()
# # obj.divide()
# # obj.modulus()

# # obj._C__land()
# # obj._C__money()



# multilevel Inheritance


# class father:
#     surname = "bajpai"
  
# class son(father):
#     def money(self,surname):
#         print("son have a money of 5 lakhs sunil kumar",self.surname)

# class grandson(son):
#     def bike(self,surname):
#         print("grandson have a bike of 1 lakh ra ",self.surname)

# name = son()     
# name.money("bajpai")

# name1 = grandson()
# name1.bike("bajpai")


# multilevel Inheritance

# class abhinav:
#     back = "python and java"

#     def backend(self):
#         print("i am a backend developer and i know ",self.back)

# class himanshu:
#     front = "html and css"

#     def frontend(self):
#         print("i am a frontend developer and i know ",self.front)  

# class teamlead(abhinav,himanshu):
#     def show(self):
#         print("i am a team lead")        

# obj = teamlead()              

# obj.backend()
# obj.frontend()      
# obj.show()

# Multiple Inheritance

# class pranay:
#     back = "django and flask"
#     def backend(self):
#         print("i am a backend developer and i know ",self.back)

# class rohit:
#     front = "react and angular"
#     def frontend(self):
#         print("i am a frontend developer and i know ",self.front)

# class team_manager(pranay,rohit):
#     def show(self):
#         print("dynamic website is created by me")


# obj = team_manager()  
# obj.backend()
# obj.frontend()      
# obj.show()      



        



        
        