#Database for Student DBMS
import sqlite3

def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StudentID text, FirstName text, SurName text, \
    DoB text, Age text, Gender text, Address text, PhoneNumber text)")
    print("Database executed...")
    con.commit()
    con.close()

def addStudentRecord(StudentID, FirstName, SurName, DoB, Age, Gender, Address, PhoneNumber):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?, ?, ?, ?)", StudentID, FirstName, SurName, DoB, Age, Gender, Address, PhoneNumber)
    print("Record added!")
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    print("Viewing records...")
    con.close()
    return rows

def deleteRecord(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id))
    print("Record Deleted!")
    con.commit()
    con.close()

#troubleshoot
def searchData(id, StudentID, FirstName, SurName, DoB, Age, Gender, Address, PhoneNumber):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StudentID=? OR, FirstName=? OR, SurName=? OR, DoB=? OR, Age=? OR, Gender=? OR, Address=? OR, PhoneNumber=?",\
        (StudentID, FirstName, SurName, DoB, Age, Gender, Address, PhoneNumber, id))
    rows=cur.fetchall()
    print("Searching Data...")
    con.commit()
    con.close()
    return rows

#troubleshoot
def updateData(id, StudentID, FirstName, SurName, DoB, Age, Gender, Address, PhoneNumber):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StudentID=?, FirstName=?, SurName=?, DoB=?, Age=?, Gender=?, Address=?, PhoneNumber=? WHERE id=?", \
        (StudentID, FirstName, SurName, DoB, Age, Gender, Address, PhoneNumber, id))
    print("Database updated successfully! :)")
    con.commit()
    con.close()

if __name__ == "__main__":    
    studentData()

