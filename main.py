from logging import exception
from db import Db
database = Db()

def main():
    while True:
        print("Press 1 for insert the student :")
        print("Press 2 for show all the students :")
        print("Press 3 for update the student :")
        print("Press 4 for delete the student :")
        print("Press 5 for exit :")
        try:
            choice = int(input())
            if choice==1:
                userid = input("Enter UserId : ")
                username = input("Enter Name : ")
                email = input("Enter Email : ")
                phone = input("Enter Phone :")
                year = int(input("Enter Year : "))
                department = input("Enter Department : ")
                database.insert_user(userid,username,email,phone,year,department)

            elif choice==2:
                database.fetch_all()

            elif choice==3:
                userid = input("Enter UserId : ")
                username = input("Enter Name : ")
                email = input("Enter Email : ")
                phone = input("Enter Phone :")
                year = int(input("Enter Year : "))
                department = input("Enter Department : ")
                database.update_user(userid,username,email,phone,year,department)

            elif choice==4:
                userid = input("Enter UserId : ")
                database.delete_user(userid)

            elif choice==5:
                break
            else:
                print("Invalid key ! please try again....")
        except exception as e:
            print(e)
            print("Invalid user ! please try again....")

if __name__ == "__main__":
    main()