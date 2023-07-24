import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = 'abhirami')
# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Mydb_python")
#
# mycursor.execute("show databases")
# for x in mycursor:
#     print(x)
mycursor.execute("use mydb_python")
# mycursor.execute("create table test (name varchar(250),department varchar(250),salary int);")

# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)

# sql = "insert into test values ('jack','python',12563)"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,'record inserted')


# sql = "insert into test (name,department,salary) values(%s,%s,%s)"
# sql = "delete  from test where name = 'kavya'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,'Records delete')
# val = [
#     ('anagha','python',52461),
#     ('abhi','java',85643),
#     ('anu','python',58453),
#     ('kavya','python',85476),
#     ('archana','java',85456)
# ]
# mycursor.executemany(sql,val)
# mydb.commit()
# print(mycursor.rowcount,"record inserted")

# mycursor.execute("select * from test")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor.execute("select * from test")
# myresult = mycursor.fetchone()
# print(myresult)

# sql = "update test set department = 'java' where name = 'anu'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,'record(s) affected')

# sql = "select * from test order by name"
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
#

# sql = "SELECT * FROM test ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# sql = "SELECT * FROM test ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mycursor.execute('use mydb_python')
# mycursor.execute('create table student (Id int,Name varchar(250),Course varchar(250),marks int);')
# mycursor.execute("show tables")
# for x in mycursor:
#     print(x)
# mycursor.execute(("use mydb_python"))
# sql1 = "insert into student (Id,Name,Course,marks) values(%s,%s,%s,%s) "
# val1 = [
#     (1,'anju','python',56),
#     (2,'archana','python',60),
#     (3,'arsha','java',55),
#     (4,'minu','.net',65),
# ]
# mycursor.executemany(sql1,val1)
# mydb.commit()
# print(mycursor.rowcount,'record inserted')

