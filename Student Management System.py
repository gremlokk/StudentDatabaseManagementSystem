#front end
from tkinter import *
import tkinter.messagebox
import sys
import StudentDB

class Student:
        def __init__(self, root):
            self.root = root
            self.root.resizable(False,False)

            StudentID = StringVar()
            FirstName = StringVar()
            SurName = StringVar()
            DoB = StringVar()
            Age = StringVar()
            Gender = StringVar()
            Address = StringVar()
            PhoneNumber = StringVar()
            
            #===================================================================================FUNCTIONS===========================================================================================================
            def Exit():#work
                Exit = tkinter.messagebox.askyesno("Student DBMS", "Would you like to exit? ")
                if Exit > 0:
                    root.destroy()
                    return

            def clearData():#work
                self.textStudentID.delete(0,END)
                self.textName.delete(0,END)
                self.textSurName.delete(0,END)
                self.textDoB.delete(0,END)
                self.textAge.delete(0,END)
                self.textGender.delete(0,END)
                self.textAddress.delete(0,END)
                self.textPhoneNumber.delete(0,END)
                print("Record cleared.")

            def addData():
                studentList.insert(END, "Data")
                stuff = StudentID.get()

                print ("Data: " + stuff)
                '''
                if (len(StudentID.get()) !=0):
                    StudentDB.addStudentRecord(StudentID.get(), FirstName.get(), SurName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), PhoneNumber.get())
                    studentList.delete(0,END)#make sure list is empty first
                    studentList.insert(END, StudentID.get(), FirstName.get(), SurName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), PhoneNumber.get())#insert data
                '''
            def displayData():
                studentList.delete(0,END)#make sure list is empty first
                for row in StudentDB.viewData():
                    studentList.insert(END, row, str(""))

            def deleteData():
                print ("Deleted record...")


            def searchDB():
                print ("Search DB...")

            
            def Update():
                print ("Update DB... ")
  
            #===================================================================================Frames===========================================================================================================
            MainFrame = Frame(self.root, bg ="gray")
            MainFrame.grid()

            #Frame -> Mainframe
            TitleFrame = Frame(MainFrame, bd=2, padx=54, pady=8,  bg ="ghost White", relief=RIDGE)
            TitleFrame.pack(side=TOP)
            
            self.labelTitle = Label(TitleFrame, font=('arial', 45, 'bold'), text="Student Database Management System", bg="Ghost White")
            self.labelTitle.grid()

            ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, relief=RIDGE, bg="Ghost White")
            ButtonFrame.pack(side=BOTTOM)
             
            DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="lightgray")
            DataFrame.pack(side=BOTTOM)
            
            DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White", font=('arial', 20, 'bold'), text="Student Membership Information\n")
            DataFrameLeft.pack(side=LEFT)

            DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White", font=('arial', 20, 'bold'), text="Student Details\n")
            DataFrameRight.pack(side=RIGHT)
            
            #===========================================================================Labels and Entry Wdigets==================================================================================================
            self.labelStudentID = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="    STUDENT ID: ", bg="Ghost White", padx=2, pady=2)
            self.labelStudentID.grid(row=0,column=0, sticky=W)
            self.textStudentID = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=StudentID, text="Student ID: ", width=39)
            self.textStudentID.grid(row=0,column=1)

            self.labelName = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="    FIRSTNAME: ", bg="Ghost White", padx=2, pady=2)
            self.labelName.grid(row=1,column=0, sticky=W)
            self.textName = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=FirstName, text="FIRSTNAME: ", width=39)
            self.textName.grid(row=1,column=1)

            self.labelSurname = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="SURNAME: ", bg="Ghost White", padx=2, pady=2)
            self.labelSurname.grid(row=2,column=0)
            self.textSurName = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=SurName, text="SURNAME: ", width=39)
            self.textSurName.grid(row=2,column=1)

            self.labelDoB = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="DATE OF BIRTH: ", bg="Ghost White", padx=2, pady=2)
            self.labelDoB.grid(row=3,column=0, sticky=W)
            self.textDoB = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=DoB, text="DATE OF BIRTH: ", width=39)
            self.textDoB.grid(row=3,column=1)

            self.labelAge = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="         AGE: ", bg="Ghost White", padx=2, pady=2)
            self.labelAge.grid(row=4,column=0, sticky=W)
            self.textAge = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=Age, text="AGE: ", width=39)
            self.textAge.grid(row=4,column=1)

            self.labelGender = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="GENDER: ", bg="Ghost White", padx=2, pady=2)
            self.labelGender.grid(row=5,column=0)
            self.textGender = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=Gender, text="GENDER: ", width=39)
            self.textGender.grid(row=5,column=1)

            self.labelAddress = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="ADDRESS: ", bg="Ghost White", padx=2, pady=2)
            self.labelAddress.grid(row=6,column=0)
            self.textAddress = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=Address, text="ADDRESS: ", width=39)
            self.textAddress.grid(row=6,column=1)

            self.labelPhoneNumber = Label(DataFrameLeft, font=('arial', 18, 'bold'), text="PHONENUMBER: ", bg="Ghost White", padx=2, pady=2)
            self.labelPhoneNumber.grid(row=7,column=0)
            self.textPhoneNumber = Entry(DataFrameLeft, font=('arial', 18, 'bold'), textvariable=PhoneNumber, text="PHONENUMBER: ", width=39)
            self.textPhoneNumber.grid(row=7,column=1)

            #===========================================================================ListBox and Scrollbar Widgets==================================================================================================
         
            scrollbar = Scrollbar(DataFrameRight)
            scrollbar.grid(row=0, column=1, sticky='ns')

            studentList = Listbox(DataFrameRight, width=41, height=16, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
            studentList.grid(row=0, column=0, padx=8)
            scrollbar.config(command = studentList.yview)
         
            #===========================================================================Button Widgets==================================================================================================

            self.ButtonAddData = Button(ButtonFrame, text="Add New", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=addData)
            self.ButtonAddData.grid(row=0, column=0)

            self.DisplayDataButton = Button(ButtonFrame, text="Display", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=displayData)
            self.DisplayDataButton.grid(row=0, column=1)

            self.ClearDataButton = Button(ButtonFrame, text="Clear", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=clearData)
            self.ClearDataButton.grid(row=0, column=2)

            self.DeleteDataButton = Button(ButtonFrame, text="Delete", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=deleteData)
            self.DeleteDataButton.grid(row=0, column=3)

            self.SearchDataButton = Button(ButtonFrame, text="Search", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=searchDB)
            self.SearchDataButton.grid(row=0, column=4)

            self.UpdateDataButton = Button(ButtonFrame, text="Update", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=Update)
            self.UpdateDataButton.grid(row=0, column=5)

            self.ExitButton = Button(ButtonFrame, text="Exit", font=('arial', 18, 'bold'), height=1, width=10, bd=4, command=Exit)
            self.ExitButton.grid(row=0, column=6)


def main():
    root = Tk()
    root.title("Student Database Management System")
    root.geometry("1280x720+0+0")
    root.config(bg="gray")
    app = Student(root)
    root.mainloop()

if __name__ == "__main__":
   main()
