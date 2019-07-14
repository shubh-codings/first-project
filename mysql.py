import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="shubh", passwd="1234", database="shubh")
    mycursor = mydb.cursor()
    mycursor.execute("select * from student")
    result = mycursor.fetchall()
    for i in result:
        print(i)

    mycursor.execute('insert into student values(\"rahul\",15885,\"electrical\")')
    mycursor.execute('delete from student where name= "mrinal"')
    mycursor.execute("select * from student")
    result = mycursor.fetchall()
    for i in result:
        print(i)
except Exception as e:
    print(e)
