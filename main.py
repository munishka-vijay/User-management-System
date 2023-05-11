from dbhelper import DBHelper

def main():
    db= DBHelper()
    while True:
        print("************************WELCOME TO PYTHON WITH SQL MENU*******************")
        print()
        print("Press 1 to inser new user")
        print("Press 2 to update user")
        print("Press 3 to delete user")
        print("Press 4 to display all users")
        print("Press 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice == 1):
                uid = int(input("Enter userid: "))
                uname = input("Enter user name: ")
                uphone = input("Enter user phone: ")
                db.insert_user(uid, uname, uphone)
                pass

            elif(choice == 2):
                uid = int(input("Enter userid: "))
                uname = input("Enter user name: ")
                uphone = input("Enter user phone: ")
                db.update_user(uid, uname, uphone)
                pass

            elif(choice == 3):
                uid = int(input("Enter userid: "))
                db.delete_user(uid)
                pass


            elif(choice == 4):
                db.fetch_all()

            elif(choice == 5):
                break

        except Exception as e:
            print(e)
            print("Invalid choice! Try again")


if __name__ == "__main__":
    main()

            

            



        




