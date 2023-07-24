# # define parent class Company
# class Company:
#     # constructor
#     def __init__(self, name, proj):
#         self.name = name  # name(name of company) is public
#         self.proj = proj  # proj(current project) i
#
#     # public function to show the details
#     def show(self):
#         print("The code of the company is = ", self.proj)
#
# # define child class Emp
# class Emp(Company):
#     # constructor
#     def __init__(self, eName, sal, cName, proje):
#         # calling parent class constructor
#         Company.__init__(self, cName, proje)
#         self.name = eName  # public member variable
#         self.__sal = sal  # private member variable
#
#     # public function to show salary details
#     def show_sal(self):
#         print("The salary of ", self.name, " is ", self.__sal, )
#
#
# # creating instance of Company class
# c = Company("Stark Industries", "Mark 4")
# # creating instance of Employee class
# e = Emp("Steve", 9999999, c.name, c.proj)
#
# print("Welcome to ", c.name)
# print("Here ", e.name, " is working on ", e.proj)
#
# # only the instance itself can change the __sal variable
# # and to show the value we have created a public function show_sal()
# e.show_sal()
# e.show()
# c.show()
#




# define parent class Company
class Company:
    # constructor
    def __init__(self, name2, proj):
        self.name2 = name2  # name2(name2 of company) is public
        self._proj = proj  # proj(current project) is protected

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self._proj)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, ename, sal, cname, proj):
        # calling parent class constructor
        Company.__init__(self, cname, proj)
        self.name2 = ename  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name2, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name2, c.show())

print("Welcome to ", c.name2)
print("Here ", e.name2, " is working on ", c._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()
e.show()
c.show()