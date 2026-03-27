# print("hello world")

# class student:
#     def __init__(self,name,grade):
#         self.name = name
# #         self.grade = grade

# # print("choose operation")
# # print("1, + addition")
# # print("2, - subtraction")
# # print("3, * multiply")
# # print("4, / divide")

# # a = input("choose operator(=+,-,*,/)")

# num1 = int(input("enter your first number: "))
# num2 = int(input("enter your second number: "))


# a = input("choose operator(=+,-,*,/)")

# if a == "+":
#     print("result =",num1+num2)

# # elif a == "-":
# #     print("result =",num1-num2)

# # elif a == "*":
# #     print("result =",num1*num2)

# # elif a == "/":
# #     print ("result =",num1/num2)

# # else:
# #     print("invalid operation chooses:")    

# # year = int(input("enter a year:"))

# # if year % 400 == 0:
# #     print("it is a leap year: ")

# # elif year % 4 == 0:
# #     print("it is a leap year: ")

# # elif year % 100 == 0:
# #     print("it is a leap year: ")    

# # else:
# #     print("it is not a leap year")    

# num = int(input("enter any 3 digit number: "))

# a = num % 10
# b = (num // 10) % 10
# c = (num // 10)

# sum = (a**3)+(b**3)+(c**3)
# if sum == num:
#     print("it is an armstrong number")

# else:
#     print("it is not armstrong number")    

# num = int(input("enter any number: "))   

# if num % 3 == 0:
#     print("odd number")

# # else:
# #     print("not a odd number ")    

# age = int(input("enter your age: "))

# if age < 18:
#     print("you are not too young for the marrige")

# elif age >= 18:
#     print("yoa are eligible for the marriage")  

# else:
#     ("you are not eligible")      

# num = int(input("enter any number: "))

# for number in range(1,11):
#     print(num * number)

# password = "abhinav bajpai"

# input_password = input("enter password: ")

# while password != input_password:
#     input_password = input("enter password: ")

# else:
#     ("unlocked !! ")    
# import keyword
# # print(keyword.kwlist)

# for num in range (1,11):
#     if num % 2 == 0:
#         break
#     else:
#         print(num)

# def calculator():
#     print("addition : ","a+b")
    
#     print("subtraction : ","a-b")
    
#     print("multiplication : ","a*b")
    
#     print("divison : ","a/b")

#     calculator(4,8)    

# # def greet(name):
# #     return("good evening",'abhingreet()
# # print(msg)

# # def greet(firstname,lastname):
# #     print("good evening",firstname,lastname)

# #     greet("ankit","kumar")


# class A:
#     "learn coding....!!"
    
#     age =10

#     print(age)
#     def fun(self):
# #         name="abhinav bajpai"  
# #         "kr mangalam university....!!" 
# #         print(name)

# # obj = A()
# # obj.fun()  
# # print(obj.fun.__doc__)

# # print(obj.age)
# # # print(A.age)
# # # print(obj.__doc__)

# # class A:

# #     def __init__(self,age,name,address):
# #         print(age,"",name,"",address,"")

# # obj=A(10,"abhianv","gurgaon haryana ")    
# # # obj=A(10,"aarvik","jaipur")   
# # # # obj=A(15,"bittu","mohammadi")

# # # class a:
# # #     def __init__(self):
# # #         name="abhinav bajpai"
# # #         print(name)

# # # #     def __init__(self):
# # # #         age =20  
# # # #         print(age)

# # # # obj = a()        

# # # class a:
# # #     name = "abhinav bajpai"
# # #     age =18
# # #     def __init__(self):
# # #         address = "mohammadi kheri"
# # #         print(self.name,"",address)
# # #     def show(self):
# # #         print(self.age)

# # # obj = a()  
# # # obj.show()          

# # # class a:
# # #     def __init__(self,name,age,school,address):
# # #         self.name = "abhinav"
# # #         print(self.name)
# # #         self.age = 18
# # #         print(self.age)

# # #         self.school = "tprs"
# # #         print(self.school)
# # #         self.address = "mohammadi kheri"
# # #         print(self.address)

# # # obj = a("abhinav",18,"tprs","mohammadi")        

# # class a:
# #     name2 = "aarvik dixit"
# #     def __init__(self,name,age,address):
# #         address = "mohammadi"
# #         print(name,age,address,self.name2)
# #     def show(self):
# #         print(self.name2)

# # obj = a("abhinav",18,None) 
# # obj.show()     

# class father:
#     def lands(self):
#         print("father have 50 acre of the land")

# class son(father):   
#     def money(self):
#         print("it have money propety of approximetly of the hundred crore")  

# S = son()
# S.lands()
# S.money()        


# class a:
#     num1 = int(input("enter first number: "))   
#     num2 = int(input("enter second number: "))

#     def add(self):
#         print("addition: ",self.num1+self.num2)

#     def subtraction(self):
#         print("subtraction: ",self.num1-self.num2)    
        
# class b(a):
#     def multiply(self):
#         print("multiply: ",self.num1*self.num2)

#     def divison(self):
#         print("divison: ",self.num1/self.num2)

# class c(b):
#     def land(self):
#         print("I habe a land of 100 acre")    

#     def money(self):
#         print("i ahve a property of 10 lakhs")


# s = b()        
# s.add()
# s.subtraction()
# s.multiply()
# s.divison()

# d = c()
# d.land()
# # d.money()

# class parent1:
#     def enginerring(self):
#         print("It have a 9 cgpa")

# class parent2:
#     def doctor(self):
#         print("i have got 182 marks in NEET")    

# class parent3:
#     def lawyer(self):
#         print("i have solve approximetly of 100 cases" )    

# class child(parent1,parent2,parent3):
#     def army(self):
#         print("i have got rank in indian army")         


# parent4 =child()
# parent4.enginerring()   
# # parent4.doctor()    
# # parent4.lawyer()       
# # parent4.army() 

# class parent:
#     def add(self):
#         print("i have learning machine language and artificial intelligence")

# class child1(parent):
#     def sub(self):
#         print("i have learning computer science")     

# class child2(parent):
#     def div(self):
#         print("i have b.tech computer science engineer ")     


# child3 = child1()
# child3.add()
# child3.sub()

# child4 = child2()
# child4.div()

# inheritence completed:::::

#class a:
#     _a=10
#     __b=20
#     def show(self):
# #         print("a= ",self._a)       
# #         print("b= ",self.__b)

# # obj = a()
# # obj.show()
# # print("outside the class ",obj._a) 

# class A:
#     def show(self):
#         print("wlecome")

#     def show(self,firstname=''):
#         print("welcome: ",firstname)

#     def show(self,firstname='',lastname=''):
#         print("welcome: ",firstname,lastname)

# obj =A()   
# obj.show() 
# # obj.show("abhinav")   
# # obj.show("abhinav","bajpai")     
           

# a = int(input("enter any radius: "))

# area = (22/7*a*a)

# print("area of the circe is: ",area)

# print("hello b.tech")

# name = str(input("enter your name: "))
# roll = int(input("emter your rool no: "))
# branch = input("enter your branch: ")

# a= 10
# b= 5
# a,b = b,a
# print(a,b)

# c = int(input("enter the temprature: "))

# farenheit = 9/5*c+32 

# print("the tempraure in farenheit is: ",farenheit)
# # a  = {"my name is abhinav:"","}
# print(type(a))

# a = 10
# b = str(a)
# print(b)

# var = [10,"abhianv bajpai", "aarvik","bulla","bittu",10.5]
# var1 = var.append("archika")
# print(var1)

# principal = int(input("enter the value of the principle: "))
# rate = int(input("enter the value of the rate: "))
# time = int(input("enter the value of the time:"))

# intrest = (principal*rate*time/100)

# print(intrest)

# a  = int(input("enter any number: "))
# b=  int(input("enter any number: "))

# # c = a**b 
# # print(c)

# a  = int(input("enter any number: "))
# b = (input("+","-","0"))
# # b = int(input("enter any number: "))
# # c = int(input("entr any number:"))

# if a == +a:
#     print("it is a positive number: ")

# elif a == -a:
#     print("it is a negative number: ")    

# # elif a == 0:
# #     print("it is a zero number: ")  

# # else:
# #     print("it is not a any kind of number from the above value")      

# n= int(input("enter any number: "))

# if n > 0 :
#     print("it is positive number:")

# elif n<0 :
#     print("it is negative number: ")

# # elif n == 0:
# #     print("it is a zero number: ")        

# # else:
# #     print("the above number is incorrect")   


# # n= int(input("enter any number: "))
# # /
# #     print("it is not a true")    

# # if n >= 10:
# #     print("it is true number:")
# # elif n<=50:
# #     print("it is a wrong number:")    
# # else:
# #     print("it is a false number")    

# # n = int(input("enter any number:"))

# # if n % 2 == 0:
# #     print("it is even number")

# # else:
# #     print  ("it is odd number")  

# # n = int(input("enter any 3 digit number:"))

# # if n == 999:
# #     print("it is the largest of the three digit number")

# # else:
# #     print("it is the smallest number")    


# year = int(input("enter any number: "))

# if year % 400 == 0:
#     print("it is a leap year")

# elif year % 100 == 0:
#     print("it is a leap year")    

# # elif year % 4 == 0:
# #     print("it is a leap year")    

# # else:
# #     print("it is not a leap year")    

# marks = int(input("enter your marks: "))

# if marks >= 90:
#     print("grade is A")

# elif marks >=80:
#     print("grade is B")    

# elif marks >=70:
#     print("grade is C")    

# # elif marks >=60:
# #     print("grade is D")  

# # else:
# #     print("you are not clear the exam")   

# vow = str(input("enter the vow: "))   

# if vow == "a":
#     print("it is a vowel")
# elif vow == "e":
#     print("it is a vowel")   
# elif vow == "i":
#     print("it is a vowel")  
# elif vow == "o":
#         print("it is a vowel")  
# elif vow == "u":
# #          print("it is a vowel")          
# # else:
# #     print("it is the consonant")    

# num = int(input("enter any number:"))

# for num in range(1,101):
#     print(num)

# num = int(input("enter any number:"))
# for number in range(0,101):
#     print(num*number)
# num2 = int(input("entr any number: "))


# for num  in range(0,10):
#     if num1+num2 == "+":
#         print("it is the natural number: ")
# else:
#     print("it is not a natural number: ")


# n = int(input("enter any factorial number: "))

# for n in range(0,101):
#     break
# while  (n*n*n):
#     print(n)

# list1 = [1,2,3,4,5,6,"abhinav","aarvik",10.45,"biitu","bulla","vashu"]

# while list1 in range(-1):
#     print(list1)

# print(len(list1))
# print(list1::-1)



# factorial number::::
# n = int(input("enter any number: "))
# fact =1
# for i in range(1,n+1):
#     fact *=i
# print(fact)



# sum of first n natural number
# n =int(input("enter any number: "))

# s  =0
# for i in range(1,n+1):
#     s += i
#     print(s)


# print("hello world")

# num1= int(input("enter any number: "))
# num2 = int(input("enter any number: "))

# def add(self,num1,num2):
#         print("add two numbers: ",num1+num2)

# list1 = ["abhianv","aarav","ishanvi","archika","aarvik","sudhakar","prabhakar","aarav"]
# new_list1=set(list1)
# print(new_list1)


# print(len(list1))


# print("largest: ",max(list1))
# print("smallest: ",min(list1))


    


    
   



     
        







        