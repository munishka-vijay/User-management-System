import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost', 
                                     port = '3306', 
                                     user='root', 
                                     password='sql@123', 
                                     database='pythontest')
        query = 'create table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'

        #Connection ki help se cursor nikalenge and curson ki help se queries ko fire karenge

        #Sabse pehle con variable se cursor banayenge

        cur=self.con.cursor()
        cur.execute(query)
        print("user table Created!")

    #Insert method/function
    def insert_user(self, userid, username, phone):
        query = "insert into user(userId, userName, phone) values({}, '{}', '{}')".format(userid, username, phone)
        print(query)

        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")



    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name : ", row[1])
            print("User Phone : ", row[2])
            print()
            print()


    #To fetch a record which matches the given userid
    def fetch_one(self, userid):
        query = "select * from user where userId={}".format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name : ", row[1])
            print("User Phone : ", row[2])
            print()
            print()

    
    #To delete a record which matches the given userid
    def delete_user(self, userid):
        query = "delete from user where userId = {}".format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user deleted")


    #To update the name of a user
    def update_username(self, userid, newname):
        query="update user set userName = '{}' where userId = '{}' ".format(newname, userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("username updated")

    
    #To update the phone of a user
    def update_userphone(self, userid, newphone):
        query = "update user set phone = '{}' where userId = '{}' ".format(newphone, userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("userphone updated") 


    #To update all the fields of user
    def update_user(self, userid, newname, newphone):
        query = "update user set userName = '{}', phone = '{}' where userId = {}".format(newname, newphone, userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user updated")

