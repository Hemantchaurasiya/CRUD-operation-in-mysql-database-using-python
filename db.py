import mysql.connector as connector

class Db:
    def __init__(self):
        self.con = connector.connect(host='localhost',user='root',password='jarvis',port='3306',database='student')
        query = "create table if not exists user(userId varchar(12) primary key,userName varchar(30),email varchar(30),phone varchar(12),year int,department varchar(20))"
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    #insert the new user
    def insert_user(self,userid,username,email,phone,year,department):
        query = "insert into user(userId,userName,email,phone,year,department)values('{}','{}','{}','{}',{},'{}')".format(userid,username,email,phone,year,department)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user add successfully....")
    
    #fetch all the information from the database
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Enroll No. : ",row[0])
            print("Name : ",row[1])
            print("email : ",row[2])
            print("Phone : ",row[3])
            print("year : ",row[4])
            print("department : ",row[5])
            print()
            print()
    
    #delete the record by userid 
    def delete_user(self,userid):
        query = "delete from user where userId = '{}'".format(userid)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User deleted successfully...")
    
    #update the record by userid
    def update_user(self,userId,username,email,phone,year,department):
        query = "update user set userName='{}',email='{}',phone='{}',year={},department='{}'where userId='{}'".format(username,email,phone,year,department,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user updated seccessfully....")

