import sqlite3

##Connect to sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to insert record, create ,table,retrieve

cursor=connection.cursor()

##create the table
table_info="""Create table Mydb(Name varchar(25),Class varchar(25),
Section varchar(25),Marks INT);"""


cursor.execute(table_info)

## Insert some more records

#cursor.execute(table_info)

cursor.execute('''Insert into Mydb values('Abdul','AI Engineer','A',90)''')
cursor.execute('''Insert into Mydb values('Qadir','Data Scientist','B',100)''')
cursor.execute('''Insert into Mydb values('Abhishek','ML Engineer','A',86)''')
cursor.execute('''Insert into Mydb values('Chanchal','Devops','A',50)''')
cursor.execute('''Insert into Mydb values('Anshika','Devops','A',35)''')

print("The inserted records are")

data=cursor.execute('''Select * From Mydb''')

for row in data:
    print(row)


connection.commit()
connection.close()