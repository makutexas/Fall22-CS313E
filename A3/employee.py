#  File: employee.py
#  Description: Employee.py provides a framework to create different employee objects with names, id, etc. 
#  Student Name: Mark Chao 
#  Student UT EID: mc72239
#  Partner Name: Benjamin Ton-That
#  Partner UT EID: bbt426
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 9/15/2022
#  Date Last Modified: 9/15/2022

import sys

class Employee:

    def __init__(self, **kwargs):
        """Employee has an name, id, and salary"""
        self.name = kwargs.get("name", None)
        self.id = kwargs.get("id", None)
        self.salary = kwargs.get("salary", None)

    def __str__(self):
        """Prints out Employee string"""
        print("Employee")
        return str(self.name) + " , " + str(self.id) + " , " + str(self.salary)
    

############################################################
############################################################
############################################################

class Permanent_Employee (Employee) :

    def __init__(self, **kwargs):
        """Permanant Employee has attributes of Employee and benefits"""
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits", None)
        pass

    def cal_salary(self):
        """Calculates the salary for a Permanent Employee"""
        if (self.benefits == ["health_insurance"]):
            return self.salary * 0.9   
        elif (self.benefits == ["retirement"]):
            return self.salary * 0.8
        elif (self.benefits == ["retirement","health_insurance"]):
            return self.salary * 0.7
        else:
            return self.salary
        

    def __str__(self):
        """Prints out Permanent Employee string"""
        print("Permanent_Employee")
        return str(self.name) + " , " + str(self.id) + " , " + str(self.salary) + " , " + str(self.benefits)

############################################################
############################################################
############################################################

class Manager (Employee):
    def __init__(self, **kwargs):
        """Manager has attributes of Employee and bonus"""
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus", None)

    def cal_salary(self):
        """Calculates salary for a Manager"""
        return self.salary + self.bonus
        pass

    def __str__(self):
        """Prints out Manager String"""
        print("Manager")
        return str(self.name) + " , " + str(self.id) + " , " + str(self.salary) + " , " + str(self.bonus)
        pass


############################################################
############################################################
############################################################
class Temporary_Employee (Employee) :
    def __init__(self, **kwargs): 
        """Temporary Employee has attributes of Employee and hours"""
        super().__init__(**kwargs) 
        self.hours = kwargs.get("hours", None) 
    def cal_salary(self): 
        """Calculates the salary of a Temporary Employee"""
        return self.salary * self.hours 
    def __str__(self):
        """Print out Temporary Employee string"""
        print("Temporary_Employee")
        return str(self.name) + " , " + str(self.id) + " , " + str(self.salary) +  " , " + str(self.hours)


############################################################
############################################################
############################################################


class Consultant (Temporary_Employee) :
    def __init__(self, **kwargs): 
        """Consultant has attributes of Temporary Employee and travel"""
        super().__init__(**kwargs) 
        self.travel = kwargs.get("travel", None) 
        pass
    def cal_salary(self): 
        """Calculates the salary for a Consultant"""
        return Temporary_Employee.cal_salary(self) + (self.travel * 1000)
    def __str__(self):
        """Print out Consultant string"""
        print("Consultant")
        return str(self.name) + " , " + str(self.id) + " , " + str(self.salary) + " , " + str(self.hours) + " , " + str(self.travel)
############################################################
############################################################
############################################################


class Consultant_Manager (Manager, Consultant):
    def __init__(self,  **kwargs):
        """Consultant Manager has attributes of Manager and Consultant"""
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)

    def cal_salary(self):
        """Calculates the salary for a Consultant Manager"""
        return (self.salary * self.hours) + (self.travel * 1000) + self.bonus
    def __str__(self):
        """Prints out Consultant Manager string"""
        print("Consultant_Manager")
        return str(self.name) + " , " + str(self.id) + " , " + str(self.salary) + " , " + str(self.hours) + " , " + str(self.travel) + " , " + "Consultant_Manager\n" +  str(self.name) + " , " + str(self.id) + " , " + str(self.salary) + " , " + str(self.bonus)
        pass


############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()
