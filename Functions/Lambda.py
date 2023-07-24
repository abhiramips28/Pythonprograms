""" The power of lambda is better shown when you use them as an anonymous function inside another function. """











#Q. Program to sort a list of dictionaries using lambda.

# employees = [{'id': 101 , 'name':'Adam', 'department':'Electronics'}, {'id': 102, 'name':'Ricky', 'department':'IT'},
#              {'id': 103, 'name': 'Shane', 'department':'Auto'}]
# print("List of employees : ")
# print(employees)
# sorted_employees = sorted(employees, key = lambda x: x['department'])
# print(" Sorted List of employees :")
# print(sorted_employees)



#Q. To extract year,month,date & time using lambda (2022-07-05 09:03:32).

# import datetime
# now = datetime (key = lambda x:x['%y-%m-%d %H:%H'])
# print(datetime(now))


# import datetime
# now = datetime.datetime.now()
# print(now)

# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# time = lambda x: x.time()
#
# print(year(now))
# print(month(now))
# print(day(now))
# print(time(now))








