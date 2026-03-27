# import abc

# class employee():
#     _a = 2501010159
#     _b = "abhinav bajpai"
#     _C = 50000
#     def __init__(self,_a,_b,_c):
#         print("the user have id of",_a,"and its name is",_b,"and its salary is about ",_c)

#     def calculate_salary(self):
#         pass


# class permanent_employee(employee):

#     def calculate_salary(self):
#         hra = self._C*0.20
#         da = self._C*0.10

     
#         total_Salary = self._C+hra+da
         
#         return total_Salary
    
# class contract_employee(employee):
#     def __init__(self,_a,_b_,hours_worked):

       

#         self._hours_worked = hours_worked

#     def calculate_salary(self):
#         return self._C*self._hours_worked   
     
# class payrollsystem:
#     def __init__(self):
#         self.employee_list = []

#     def add_employee(self,employee):
#         self.employee_list.append(employee)  

#     def show_payroll(self):
#         for emp in self.employee_list:
#             print("the user have id about 102 qnd its anme is abhinav bajpai and its salary is about of 50000")
#             print("-----------------------")

# payroll = payrollsystem()           

# emp1 = permanent_employee(101,"rahul",30000)
# emp2 = contract_employee(102,"amrit",50000)

# payroll.add_employee(emp1)
# payroll.add_employee(emp2)

# payroll.show_payroll()


        

    





