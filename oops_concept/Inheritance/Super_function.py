class Company:
    def company_name(self):
        return 'Google'

class Employee(Company):
    def info(self):
         #calling the superclass methods using super() function.
        c_name =super().company_name()
        print("chithra works at",c_name)

emp = Employee()
emp.info()

