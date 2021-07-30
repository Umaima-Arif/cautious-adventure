#import tkinter and its modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


id = 0
dllist = None
wcount = 0

class Node:   # creating node class
    def __init__(self, data):     # initialize node class
        self.data = data  
        self.next = None  # reference to next node in DLL
        self.prev = None  # reference to previous node in DLL

class doubly_linked_list:   # creating dll class
    def __init__(self):       #initialize dll class
        self.head = None
    
    # Fuction to add a new node at front of the list
    def push_front(self, newElement):       
        newNode = Node(newElement)    #Allocate the Node & Put in the data
       # Make next of new node as
    # head and previous as None 
        if(self.head == None):
            self.head = newNode
            return
        else:
            self.head.prev = newNode        #change prev of head node to new node 
            newNode.next = self.head
            self.head = newNode           #move the head to point to the new node
        
     # Fuction to add a new node at Last of the list
    def pushLast(self, newElement):  
        newNode = Node(newElement)
        if(self.head == None):         #check if the given prev_node is NULL
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode  
            newNode.prev = temp  # Change previous of new_node's next node
   
    # Function to delete value from front Of list           
    def pop_front(self, head):   
        # if head is not null, create a
    #   temp node pointing to head
        
        if(self.head != None):
            temp = self.head
            self.head = self.head.next  # move head to next of head
            temp = None       #delete temp node
            
          #  If the new head is not null, then
    #   make prev of the new head as null
            if(self.head != None):
                self.head.prev = None 
    
    # Function to delete value at end Of list 
    def pop_last(self,head):           
    # if head in not null and next of head
    #   is null, release the head 
        
        if(self.head != None):
            if(self.head.next == None):
                self.head = None
                
      # Else, traverse to the second last 
      #   element of the list
            else:
                temp = self.head
                while(temp.next.next != None):
                    temp = temp.next
      # Change the next of the second 
      #   last node to null and delete the
      #   last node
                lastNode = temp.next
                temp.next = None
                lastNode = None
                
    # Function to Delete an element at the given position           
    def pop_at(self, head, position):      
        print(self.head)         
        msg = ""
        if head is None:
            msg = "Node Wth ID Not Found"   #This will be printed if specific index does not exit 
            
        # check if the position is > 0
        elif(position < 1):
            msg = "position should be >= 1."
        elif self.head.data.id == position:   # check if id is matched with specific position
            self.head = self.head.next
        else:    
            temp = self.head
            
            while temp != None:
                print("In loop")
                if temp.data.id == position:  #check id is at position
                    print("ID matched")  
                    break
                prevtemp = temp
                temp = temp.next
            if temp != None:    
                if temp.data.id == position:
                    prevtemp.next = temp.next
            else:
                msg = "Node Wth ID Not Found"
        return msg
                
    def searchEmployee(self, head, name): # function to search node by value
        temp = self.head
        while  temp != None:
            if temp.data.name == name:
                return ("ID :"+str(temp.data.id)+" NAME : " + temp.data.name+" DEPARTMENT : " + temp.data.dep+" DESIGNATION: " + temp.data.des)
              
            temp = temp.next     
        else:
            return ("Name Not Found")
        
    def searchEmployeeBYID(self, head, id):  # function to search node by index
        msg = ""
        if head is None:
            msg = "Node Wth ID Not Found"
        temp = self.head
        while  temp != None:
            if temp.data.id == int(id):
                return (str(temp.data.id)+":" + temp.data.name+":" + temp.data.dep+":" + temp.data.des)
            temp = temp.next     
        else:
            return ("ID Not Found")
        
    def update_data(self, head , id, name, dept, desg): # function to chnage value of nodes in dll
       
        temp = self.head
        while  temp != None:
            if temp.data.id == int(id):
                print("matched")
                temp.data.name = name
                temp.data.dep = dept
                temp.data.des = desg
            temp = temp.next 
            
        
        
    def listprint(self, node, widget): # print function to display nodes
        global wcount
        while node is not None:
            widget.insert(parent='', index=wcount, iid=wcount, text='', values=(node.data.id,
                           node.data.name,node.data.dep,node.data.des))
            last = node
            node = node.next
            wcount += 1      
        
class employee:        
    def __init__(self, id,name, dep,des ):  # initialize employee class
            self.id=id
            self.name = name
            self.dep=dep
            self.des=des

class MyGUI():        #Create GUI class
    
    global dllist           # making list global
    dllist = doubly_linked_list()   #calling doubly linked list function
    
    
    #creating gui main windows 
    def __init__(self):
        self.main_window = tkinter.Tk()          #create instance
        self.main_window.geometry("600x400")   # specifying size width height of main window
        self.main_window.minsize(520, 1)
        self.main_window.maxsize(1370, 749)
        self.main_window.resizable(1, 1)
        self.main_window.title("Employee Management System")   #Title 
        
      # creating widgets to be displayed on main windows
        self.label1=tkinter.Label(self.main_window, bg='white', text='Welcome To Employee Managment System')
        self.label1.config(font=("Arial Black",16))
        
        self.add_btn=tkinter.Button(self.main_window,bg='white', text='Add a Record',width=12 , command=self.add)
        
        self.delt_btn=tkinter.Button(self.main_window,  bg='white',    text='Delete a Record',width=12 , command=self.delete )
        self.update_btn=tkinter.Button(self.main_window,bg='white',  text='Update a Record',width=12 , command=self.update)
        
        self.search_btn=tkinter.Button(self.main_window,bg='white',  text='Search a Record',width=12 , command=self.search)
        
        self.display_btn=tkinter.Button(self.main_window,bg='white',  text='Display Records',width=12 , command=self.show)
        
        self.close_btn=tkinter.Button(self.main_window,bg='white',  text='Close',width=12 , command=self.close)
        
        
        # setting widgets places
        self.label1.place(relx=0.100, rely=0.033)
        self.add_btn.place(x=220, y=70)
        self.delt_btn.place(x=220, y=110)
        self.update_btn.place(x=220, y=150)
        self.search_btn.place(x=220, y=190)
        self.display_btn.place(x=220, y=230)
        self.close_btn.place(x=220, y=270)
        self.main_window.configure(bg='black')
        tkinter.mainloop()
        
        #This add function will be called when u press add button
    def add(self): 
        self.top = tkinter.Toplevel(self.main_window)   #this will be displayed on nother window
        self.top.geometry("600x800") 
        self.top.title("ADD RECORDS")
        
        self.top.configure(bg='black')
        
        #widgets to be displayed on this window
        self.label1=tkinter.Label(self.top, bg='white', text='ADD RECORDS')
        self.label1.config(font=("Arial Black",16))
    
        self.label1.config(anchor=CENTER)
        self.label1.place(x=100 ,y=5) 
        
        self.namelabel= tkinter.Label(self.top,  text='Employee name:')
        self.namelabel.place(x=120,y=65)  
        
        self.nameEntry=tkinter.Entry(self.top)
        self.nameEntry.place(x=240,y=65)  
        
        self.departmentlabel= tkinter.Label(self.top,  text='Department of Employee:')
        self.departmentlabel.place(x=100,y=100)
        
      
        self.options_list1 = ["IT Sector", "Finance Sector", "Sales Sector"]
  
        self.value_inside1 = tkinter.StringVar(self.top)
        self.value_inside1.set("Select Department")
  
        self.question_menu1 = tkinter.OptionMenu(self.top, self.value_inside1, *self.options_list1)
        self.question_menu1.place(x=260,y=90)
    
        self.designationlabel= tkinter.Label(self.top,  text='Designation of Employee')
        self.designationlabel.place(x=100,y=130)
        
        self.options_list2 = ["Manager","Asst Manager","Project Manager","Team Lead","Finance Head", 
                  "Sales Head","Senior Developer","Junior Developer","Intern"]

        self.value_inside2 = tkinter.StringVar(self.top)
        self.value_inside2.set("Select Designation")
  

        self.question_menu2 = tkinter.OptionMenu(self.top, self.value_inside2, *self.options_list2)
        self.question_menu2.place(x=260,y=130)
        
        self.save_button= tkinter.Button(self.top, bg="white" ,text='SAVE FRONT', width = 12 ,command=lambda:self.save_choice(self.nameEntry.get(),
                                                                       self.value_inside1.get(),self.value_inside2.get()))
        self.save_button.place(x=160,y=180)
        
        self.save_button2= tkinter.Button(self.top,text='SAVE LAST',bg="white", width = 12 ,command=lambda:self.save_choice_last(self.nameEntry.get(),
                                                     self.value_inside1.get(),self.value_inside2.get()))
        self.save_button2.place(x=260,y=180)
        
        self.showView(self.top)   # display entries in table
        self.top.mainloop()  
        
        # this will show all the entries in hierachical relation ship
    def showView(self, top):
        self.frame = tkinter.Frame(self.top, width = 845, height = 500)
        self.frame.place(x = 100, y = 240)
        self.t = ttk.Treeview(self.frame, height = 20, selectmode = "extended")
        # Name of columns
        self.t['columns']=('ID', 'Name', 'Department','Designation')
        self.t.column('#0', width=0 ,stretch=NO)
        self.t.column('ID', anchor=CENTER, width=80)
        self.t.column('Name', anchor=CENTER, width=80)
        self.t.column('Department', anchor=CENTER, width=90)
        self.t.column('Designation', anchor=CENTER, width=80)
        
        self.t.heading('#0', text='', anchor=CENTER)
        self.t.heading('ID', text='Id', anchor=CENTER)
        self.t.heading('Name', text='Name', anchor=CENTER)
        self.t.heading('Department', text='Department', anchor=CENTER)
        self.t.heading('Designation', text='Designation', anchor=CENTER) 
        
        dllist.listprint(dllist.head, self.t)
        self.t.grid()
        
        # After pressing button ADD FRONT Record will be created in front of list
    def save_choice(self,name,dep,des):      
        #if no entry entered show messagebox 
            if name == "" or dep == "Select Department" or des == " Select Designation":
                tkinter.messagebox.showinfo("showinfo", "Insert Data")
            else:
                self.nameEntry.delete(0, 'end')
                self.value_inside1.set("Select Department")
                self.value_inside2.set("Select Designation")
                print(name,dep ,des)
                global id  #Id is set global
                global dllist   #  list is set gloabl
                id+=1   # id will be assigned and incremented as we enter record
                emp=employee(id,name,dep,des)  # calling employee class
                dllist.push_front(emp)    #calling push_front function to insert record
                self.closeTreeView()
                self.showView(self.top)  #show entries in tree view
                self.top.mainloop()
                
        
      # After pressing button ADD LAST Record will be created at the end  of list
    def save_choice_last(self,name,dep,des):     
         #if no entry entered show messagebox
        if name == "" or dep == "Select Department" or des == " Select Designation":
                tkinter.messagebox.showinfo("showinfo", "Insert Data")
                
        else:
            self.nameEntry.delete(0, 'end')
            self.value_inside1.set("Select Department")
            self.value_inside2.set("Select Designation")
            print(name,dep ,des)
            global id             #Id is set global
            global dllist            #  list is set gloabl
            id+=1   # id will be assigned and incremented as we enter record
            emp=employee(id,name,dep,des)    # calling employee class
            dllist.pushLast(emp)     #calling pushLast function 
            self.closeTreeView()
            self.showView(self.top)
            self.top.mainloop()
          
    #This function wil be called as we click delete button
    def delete(self):
        self.dtop = Toplevel(self.main_window) #toplevel windows will poo
        self.dtop.geometry("500x500")
        
        self.dtop.title("DELETE RECORDS")
        
        self.dtop.configure(bg='black')
        
        #Widgets to be displayed on this window
        self.label1=tkinter.Label(self.dtop, bg='white', text='DELETE RECORDS')
        self.label1.config(font=("Arial Black",16))
    
        self.label1.config(anchor=CENTER)
        self.label1.place(x=100 ,y=5) 
        
        self.fdelt_bttn= tkinter.Button(self.dtop,width=12,text='Delete Front',command=self.delete_first)
        self.fdelt_bttn.place(x=400,y=65) 
        
        self.ldelt_bttn= tkinter.Button(self.dtop,width=12,text='Delete Last',command=self.delete_last)
        self.ldelt_bttn.place(x=400,y=105)
        
        self.sdelt_bttn= tkinter.Button(self.dtop ,width=12,text='Delete By ID',command=self.delete_at_index)
        self.sdelt_bttn.place(x=400,y=150)
        self.showTreeView(self.dtop)  # as u delete entries u can see them deleted from the table
        self.dtop.mainloop()
        
        # this the table shows hierarchical relation among the records
    def showTreeView(self, dtop):
        self.frame = tkinter.Frame(self.dtop, width = 845, height = 500)
        self.frame.place(x = 10, y=60)
        self.t = ttk.Treeview(self.frame, height = 20, selectmode = "extended")
        
        # Columns name
        self.t['columns']=('ID', 'Name', 'Department','Designation')
        self.t.column('#0', width=0 ,stretch=NO)
        self.t.column('ID', anchor=CENTER, width=80)
        self.t.column('Name', anchor=CENTER, width=80)
        self.t.column('Department', anchor=CENTER, width=90)
        self.t.column('Designation', anchor=CENTER, width=80)
        
        
        self.t.heading('#0', text='', anchor=CENTER)
        self.t.heading('ID', text='Id', anchor=CENTER)
        self.t.heading('Name', text='Name', anchor=CENTER)
        self.t.heading('Department', text='Department', anchor=CENTER)
        self.t.heading('Designation', text='Designation', anchor=CENTER) 
         
        dllist.listprint(dllist.head, self.t)
        
        self.t.grid()
     
    # as u click delete front this function will be called
    def delete_first(self):             
        global dllist     #list is made global
        dllist.pop_front(dllist.head)   # pop front function will be called to delete from front
        self.closeTreeView()
        self.showTreeView(self.dtop)          # to show table
        self.dtop.mainloop()
        
         # as u click deletelast this function will be called
    def delete_last(self):              
        
        global dllist  #list is made global
        dllist.pop_last(dllist.head)  # pop last function will be called to delete from last
        self.closeTreeView()
        self.showTreeView(self.dtop)
        self.dtop.mainloop()
        
        # as u click delete By ID this function will be called
    def delete_at_index(self):                  
        self.topp = tkinter.Toplevel(self.main_window)  #Another window will be popped
        self.topp.geometry("300x200")
        self.topp.title("DELETE RECORDS")
        self.topp.configure(bg='black')
        
        #Widgets to be displayed
        self.idlabel=tkinter.Label(self.topp, text="Employee ID:")
        self.idlabel.place(x=1, y=3)
        
        self.identry=tkinter.Entry(self.topp) #Ebter the id to be deleted
        self.identry.place(x=120, y=3)
        
        self.delte_btn=tkinter.Button(self.topp,text='Delete',width=12 ,command=lambda:self.delete_val(self.identry.get()))
        self.delte_btn.place(x=5, y=50)
        
        self.topp.mainloop()
        
        #This function will delete the record using id
    def delete_val(self,id):
        #if no id entered display message
        self.message = ""
        if id == "" :
                tkinter.messagebox.showinfo("showinfo", "Insert ID")
        else:
            global dllist #list is made global
            self.message = dllist.pop_at(dllist.head,int(id))  #Calling pop at function to delete at index
            #if id not present show error message
            if self.message != "":
                tkinter.messagebox.showinfo("showinfo", self.message)
            print("Message " + self.message)
            self.closeTreeView()
            self.showTreeView(self.dtop)    # deleting from table
            self.topp.destroy()
    
    #As u click update buton this will be executed and will ask to enter id to be 
    #updated then it will search the id and display its related info and then u can make changes in it 
    def update(self):
        self.ftop = Toplevel(self.main_window)   #New windows will be created
        self.ftop.geometry("600x600")
        self.ftop.title("UPDATE RECORDS")
        self.ftop.configure(bg='black')
        
        #Widgets to be displayed
        self.label1=tkinter.Label(self.ftop, bg='white', text='UPDATE RECORDS')
        self.label1.config(font=("Arial Black",16))
    
        self.label1.config(anchor=CENTER)
        self.label1.place(x=150 ,y=30) 
        
        self.idlabel=tkinter.Label(self.ftop, text="Employee ID:")
        self.idlabel.place(x=100 ,y=100) 
        
        self.identry=tkinter.Entry(self.ftop)
        self.identry.place(x=250 ,y=100)
        
        self.search_bttn= tkinter.Button(self.ftop,text='Search ' ,command=lambda:self.update_at_index(self.identry.get()))
        self.search_bttn.place(x=250 ,y=150)
        
        #As u click search buton this function will be executed 
        #in this function u can edit ur data
    def update_at_index(self,id):
            global dllist
            var = StringVar()
            self.label = tkinter.Label( self.ftop, textvariable=var, relief=RAISED )
            print(self.identry.get())  #this will get the id from entry and show output in label
            data = dllist.searchEmployeeBYID(dllist.head, self.identry.get()) #function to search by id wil be called
            if data == "ID Not Found":
                tkinter.messagebox.showinfo("showinfo", "Employee with "+data)
                
            else:    # id is found this will display the entries again to edit
                data = data.split(':') 
        
                self.namelabel= tkinter.Label(self.ftop,  text='Employee name:')
                self.namelabel.place(x=100,y=205)  
                value=StringVar(self.ftop, value=data[1])
        
                self.nameEntry=tkinter.Entry(self.ftop ,textvariable = value)
                self.nameEntry.place(x=210,y=205)
        
                self.departmentlabel= tkinter.Label(self.ftop,  text='Department of Employee:')
                self.departmentlabel.place(x=100,y=240)
        
      
                self.options_list1 = ["IT Sector", "Finance Sector", "Sales Sector"]

                self.value_inside1 = tkinter.StringVar(self.ftop)
                self.value_inside1.set(data[2])

                self.question_menu1 = tkinter.OptionMenu(self.ftop, self.value_inside1, *self.options_list1)
                self.question_menu1.place(x=260,y=230)

                self.designationlabel= tkinter.Label(self.ftop,  text='Designation of Employee')
                self.designationlabel.place(x=100,y=280)

                self.options_list2 = ["Manager","Asst Manager","Project Manager","Team Lead","Senior Tester", 
                      "Junior Tester","Senior Developer","Junior Developer","Intern"]

                self.value_inside2 = tkinter.StringVar(self.ftop)
                self.question_menu2 = tkinter.OptionMenu(self.ftop, self.value_inside2, *self.options_list2)
                self.value_inside2.set(data[3])

                self.question_menu2.place(x=260,y=270)

                self.btn=tkinter.Button(self.ftop,text="Update" ,command=lambda:self.Update_Record(self.identry.get(),self.nameEntry.get(),
                                          self.value_inside1.get(),self.value_inside2.get()))
                self.btn.place(x=300, y=320)

                self.label.grid()
        
        
            self.ftop.mainloop()
        
        # this fuction will update the record and save it in table
    def Update_Record(self,id,name,dep,des):
        
        global dllist
        self.message1 = dllist.update_data(dllist.head, id, name, dep, des)
        self.ftop.destroy()
        
        
        # This function will be displayed as u click search button
    def search(self):
        self.atop = tkinter.Toplevel(self.main_window) #new window displayed
        self.atop.geometry("500x300")        
        self.atop.title("Search a Record")        
        self.atop.configure(bg='black')
        #widgets will be displayed
        self.label1=tkinter.Label(self.atop, bg='white', text='SEARCH RECORDS')
        self.label1.config(font=("Arial Black",16))
    
        self.label1.config(anchor=CENTER)
        self.label1.place(x=150 ,y=30) 
        
        self.namelabel= tkinter.Label(self.atop, bg='white', text='Employee name:')
        self.namelabel.place(x=100 ,y=100) 
        
        self.nameEntry=tkinter.Entry(self.atop)
        self.nameEntry.place(x=250 ,y=100) 
        
        self.search_button= tkinter.Button(self.atop,text='Search ',width=12 ,bg='white' ,command=lambda:self.search_choice(self.nameEntry.get()))
        self.search_button.place(x=250 ,y=150) 
        self.atop.mainloop()
        
        #AS this function is executed the id u entered will be displayed
    def search_choice(self,name):
        #if empty entry is entered message will pop 
        if name == "" :
                tkinter.messagebox.showinfo("showinfo", "Insert Name")
        else:
            #else , id exits below code will be executed
            global dllist
            var = StringVar()
            self.label = tkinter.Label( self.atop, textvariable=var, relief=RAISED )
            print(self.nameEntry.get())
            var.set(dllist.searchEmployee(dllist.head, self.nameEntry.get())) #Search function will be called
            self.label.place(x=50, y= 200)
            self.nameEntry.delete(0, 'end')
            self.atop.mainloop()
        
    def closeTreeView(self):  #to close the table
        self.t.destroy() 
        
    def close(self):    # to end the tkinter window
        self.main_window.destroy()
     #As u click display button a table will be displayed
    def show(self):  #This will display table , which contains all the entries 
        global dllist
        
        self.top = tkinter.Toplevel(self.main_window)   # A new window
        self.top.geometry("500x600")
        self.top.title('Records')
        self.top.configure(bg='black')
        
        #DATA BASE LABEL DISPLAYED
        self.label1=tkinter.Label(self.top, bg='white', text='DATA BASE')
        self.label1.config(font=("Arial Black",16))
    
        self.label1.config(anchor=CENTER)
        self.label1.place(x=150 ,y=30) 
        
        #table will be displayed in a frame
        self.frame = tkinter.Frame(self.top, width = 300, height = 300)
        self.frame.place(x = 50, y = 100)
        self.t = ttk.Treeview(self.frame, height = 20, selectmode = "extended")
        
        self.t['columns']=('ID', 'Name', 'Department','Designation')  # columns in table
        self.t.column('#0', width=0 ,stretch=NO)
        self.t.column('ID', anchor=CENTER, width=80)
        self.t.column('Name', anchor=CENTER, width=80)
        self.t.column('Department', anchor=CENTER, width=90)
        self.t.column('Designation', anchor=CENTER, width=80)        
        
        self.t.heading('#0', text='', anchor=CENTER)  #headings in table
        self.t.heading('ID', text='Id', anchor=CENTER)
        self.t.heading('Name', text='Name', anchor=CENTER)
        self.t.heading('Department', text='Department', anchor=CENTER)
        self.t.heading('Designation', text='Designation', anchor=CENTER) 
         
        dllist.listprint(dllist.head, self.t)  #print the record
        
        self.t.pack()   # pack the table 
        self.top.mainloop()
        
my_gui=MyGUI() # call gui class