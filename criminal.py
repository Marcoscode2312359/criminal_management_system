from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1450x900+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #variables

        self.var_case_id=StringVar()
        self.var_criminal_no=StringVar()
        self.var_name=StringVar()
        self.var_nickname=StringVar()
        self.var_arrest_date=StringVar()
        self.var_date_of_crime=StringVar()
        self.var_address=StringVar()
        self.var_age=StringVar()
        self.var_occupation=StringVar()
        self.var_birthMark=StringVar()
        self.var_crime_type=StringVar()
        self.var_father_name=StringVar()
        self.var_gender=StringVar()
        self.var_wanted=StringVar()

        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE', font=('times new roman', 33, 'bold'), bg='black', fg='gold')
        lbl_title.place(x=0, y=0, width=1350, height=70)

        # NCR logo
        img_logo = Image.open('images/ncr.jpg')
        img_logo = img_logo.resize((60, 60), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=100, y=5, width=60, height=60)
        
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=75, width=1350, height=160)

        # First image
        img1 = Image.open('images/p1.jpg')
        img1 = img1.resize((500, 160), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=500, height=160)

        # Second image
        img2 = Image.open('images/p4.jpg')
        img2 = img2.resize((500, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=500, y=0, width=470, height=160)

        # Third image
        img3 = Image.open('images/p2.jpg')
        img3 = img3.resize((480, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=970, y=0, width=480, height=160)
        
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=0, y=205, width=1350, height=700)

        upper_frame = Frame(Main_frame, bd=2, relief=RIDGE, bg='white')
        upper_frame.place(x=0, y=0, width=1350, height=270)  # Increased height for form and button frame

        # Adding a label for the title inside the upper_frame
        title_label = Label(upper_frame, text='Criminal Information', font=('times new roman', 15, 'bold'), fg='red', bg='white')
        title_label.place(x=0, y=0)

        # Labels and Entry Fields
        # Case ID
        caseid = Label(upper_frame, text='Case ID:', font=('arial', 12, 'bold'), bg='white')
        caseid.place(x=10,y=30)

        caseentry = ttk.Entry(upper_frame,textvariable=self.var_case_id, width=22, font=('arial', 11, 'bold'))
        caseentry.place(x=150,y=30)

        # Criminal No
        lbl_criminal_no = Label(upper_frame, font=("arial", 12, "bold"), text="Criminal No:", bg="white")
        lbl_criminal_no.place(x=10,y=60)

        txt_criminal_no = ttk.Entry(upper_frame,textvariable=self.var_criminal_no, width=22, font=("arial", 11, "bold"))
        txt_criminal_no.place(x=150,y=60)

        # Criminal Name
        lbl_Name = Label(upper_frame, font=("arial", 12, "bold"), text="Criminal Name:", bg="white")
        lbl_Name.place(x=10,y=90)

        txt_Name = ttk.Entry(upper_frame,textvariable=self.var_name, width=22, font=("arial", 11, "bold"))
        txt_Name.place(x=150,y=90)

        # Nickname
        lbl_nickname = Label(upper_frame, font=("arial", 12, "bold"), text="Nickname:", bg="white")
        lbl_nickname.place(x=10,y=120)

        txt_nickname = ttk.Entry(upper_frame,textvariable=self.var_nickname, width=22, font=("arial", 11, "bold"))
        txt_nickname.place(x=150,y=120)

        # Arrest Date
        lbl_arrestDate = Label(upper_frame, font=("arial", 12, "bold"), text="Arrest Date:", bg="white")
        lbl_arrestDate.place(x=10,y=150)

        txt_arrestDate = ttk.Entry(upper_frame,textvariable=self.var_arrest_date, width=22, font=("arial", 11, "bold"))
        txt_arrestDate.place(x=150,y=150)
        # Date of Crime
        lbl_dateofCrime = Label(upper_frame, font=("arial", 12, "bold"), text="Date of Crime:", bg="white")
        lbl_dateofCrime.place(x=10,y=180)

        txt_dateofCrime = ttk.Entry(upper_frame,textvariable=self.var_date_of_crime, width=22, font=("arial", 11, "bold"))
        txt_dateofCrime.place(x=150,y=180)

        # Address
        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="Address:", bg="white")
        lbl_address.place(x=350,y=30)

        txt_address = ttk.Entry(upper_frame,textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.place(x=460,y=30)

        # Age
        lbl_age = Label(upper_frame, font=("arial", 12, "bold"), text="Age:", bg="white")
        lbl_age.place(x=350,y=60)
        txt_age = ttk.Entry(upper_frame,textvariable=self.var_age, width=22, font=("arial", 11, "bold"))
        txt_age.place(x=460,y=60)

        # Occupation
        lbl_occupation = Label(upper_frame, font=("arial", 12, "bold"), text="Occupation:", bg="white")
        lbl_occupation.place(x=350,y=90)
        txt_occupation = ttk.Entry(upper_frame,textvariable=self.var_occupation, width=22, font=("arial", 11, "bold"))
        txt_occupation.place(x=460,y=90)


        # Birthmark
        lbl_birthMark = Label(upper_frame, font=("arial", 12, "bold"), text="Birth Mark:", bg="white")
        lbl_birthMark.place(x=350,y=120)
        txt_birthMark = ttk.Entry(upper_frame,textvariable=self.var_birthMark, width=22, font=("arial", 11, "bold"))
        txt_birthMark.place(x=460,y=120)

        # Crime Type
        lbl_crimeType = Label(upper_frame, font=("arial", 12, "bold"), text="Crime Type:", bg="white")
        lbl_crimeType.place(x=350,y=150)
        txt_crimeType = ttk.Entry(upper_frame,textvariable=self.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crimeType.place(x=460,y=150)

        # Father Name
        lbl_fatherName = Label(upper_frame, font=("arial", 12, "bold"), text="Father Name:", bg="white")
        lbl_fatherName.place(x=350,y=180)

        txt_fatherName = ttk.Entry(upper_frame,textvariable=self.var_father_name, width=22, font=("arial", 11, "bold"))
        txt_fatherName.place(x=460,y=180)

        # Gender
        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="Gender:", bg="white")
        lbl_gender.place(x=670,y=30)

        gender_combo = ttk.Combobox(upper_frame,textvariable=self.var_gender, font=("arial", 11, "bold"), state='readonly', width=20)
        gender_combo['values'] = ('Select Gender', 'Male', 'Female', 'Other')
        gender_combo.place(x=800,y=30)
        
        # Most Wanted
        lbl_wanted = Label(upper_frame, font=("arial", 12, "bold"), text="Most Wanted:", bg="white")
        lbl_wanted.place(x=670,y=60)

        wanted_combo = ttk.Combobox(upper_frame,textvariable=self.var_wanted, font=("arial", 11, "bold"), state='readonly', width=20)
        wanted_combo['values'] = ('Select Option', 'Yes', 'No')
        wanted_combo.place(x=800,y=60)

        # Button Frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg="white")
        button_frame.place(x=10, y=210, width=350, height=50)  # Positioned below the upper frame's content

        btn_add = Button(button_frame,command=self.add_data, text='Add', font=('arial', 12, 'bold'), bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=10, pady=10)

        btn_update = Button(button_frame,command=self.update_data, text='Update', font=('arial', 12, 'bold'), bg='green', fg='white')
        btn_update.grid(row=0, column=1, padx=10, pady=10)

        btn_delete = Button(button_frame,command=self.delete_data, text='Delete', font=('arial', 12, 'bold'), bg='red', fg='white')
        btn_delete.grid(row=0, column=2, padx=10, pady=10)

        btn_clear = Button(button_frame,command=self.clear_data, text='Clear', font=('arial', 12, 'bold'), bg='grey', fg='white')
        btn_clear.grid(row=0, column=3, padx=10, pady=10)

        #background right side image

        img7 = Image.open('images/7.jpg')
        img7 = img1.resize((400, 255), Image.LANCZOS)
        self.photo7 = ImageTk.PhotoImage(img7)

        self.img_7 = Label(upper_frame, image=self.photo7)
        self.img_7.place(x=990, y=0, width=400, height=255)



        # Down Frame
        down_frame = Frame(Main_frame, bd=2, relief=RIDGE, bg='white')
        down_frame.place(x=0, y=270, width=1350, height=700)  # Positioned below the upper_frame and button_frame

        # Adding a label for the title inside the down_frame
        down_title_label = Label(down_frame, text='Criminal Information Table', font=('times new roman', 15, 'bold'), fg='red', bg='white')
        down_title_label.place(x=0, y=0)

        # Search frame
        # Create the search frame inside down_frame
        search_frame = Frame(down_frame, bd=2, relief=RIDGE, bg='white')
        search_frame.place(x=0, y=30, width=1350, height=60)

        # Add a label for the search frame
        search_label = Label(search_frame, text='Search Criminal Record', font=('times new roman', 15, 'bold'), fg='red', bg='white')
        search_label.place(x=0, y=0)

        # Add a label for the "Search By" text
        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By:", bg="red")
        search_by.place(x=0, y=28)

        # Combo box for search options
        self.var_com_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_com_search, font=("arial", 11, "bold"), width=18, state='readonly')
        combo_search_box['values'] = ('Select Option', 'case_id', 'criminal_no')
        combo_search_box.current(0)
        combo_search_box.place(x=100, y=28)

        # Entry field for search text
        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=("arial", 11, "bold"))
        search_txt.place(x=280, y=28)

        # Search button to trigger search_data function
        btn_search = Button(search_frame, command=self.search_data, text='Search', font=("arial", 13, "bold"), width=14, bg="blue", fg="white")
        btn_search.place(x=440, y=22)

        # Show All button to trigger fetch_data function
        btn_all = Button(search_frame, command=self.fetch_data, text='Show All', font=("arial", 13, "bold"), width=14, bg="blue", fg="white")
        btn_all.place(x=600, y=22)


        crimeagency=Label(search_frame,font=("times new roman",28,"bold"),text="NATIONAL CRIME AGENCY",fg="red")
        crimeagency.place(x=790,y=5)

        #table frame

        table_frame = Frame(down_frame, bd=2, relief=RIDGE)
        table_frame.place(x=0, y=90, width=1350, height=120)



        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # Treeview (table)
        self.criminal_table = ttk.Treeview(
        table_frame,
        columns=("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"),
        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # Packing scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configuring the scrollbars to work with the Treeview
        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",text="CaseId")
        self.criminal_table.heading("2",text="CrimeNo")
        self.criminal_table.heading("3",text="Criminal Name")
        self.criminal_table.heading("4",text="NickName")
        self.criminal_table.heading("5",text="ArrestDate")
        self.criminal_table.heading("6",text="CrimeOfDate")
        self.criminal_table.heading("7",text="Address")
        self.criminal_table.heading("8",text="Age")
        self.criminal_table.heading("9",text="Occupation")
        self.criminal_table.heading("10",text="Birth Mark")
        self.criminal_table.heading("11",text="Crime Type")
        self.criminal_table.heading("12",text="Father Name")
        self.criminal_table.heading("13",text="Gender")
        self.criminal_table.heading("14",text="Wanted")

        self.criminal_table['show']='headings'
        self.criminal_table.column('1',width=80)
        self.criminal_table.column('2',width=80)
        self.criminal_table.column('3',width=80)
        self.criminal_table.column('4',width=80)
        self.criminal_table.column('5',width=80)
        self.criminal_table.column('6',width=80)
        self.criminal_table.column('7',width=80)
        self.criminal_table.column('8',width=80)
        self.criminal_table.column('9',width=80)
        self.criminal_table.column('10',width=80)
        self.criminal_table.column('11',width=80)
        self.criminal_table.column('12',width=80)
        self.criminal_table.column('13',width=80)
        self.criminal_table.column('14',width=80)


        self.criminal_table.pack(fill=BOTH,expand=1)

        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # Add Function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Aman@9389',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_case_id.get(),
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthMark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get(),        
                                                                                                                     ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    #fetch data   
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Aman@9389',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']
        
        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])


    #update

    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Aman@9389',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set criminal_no=%s,criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where case_id=%s',(
                    
                    
                                                                                                                                                                                                                                                    
                    self.var_criminal_no.get(),
                    self.var_name.get(),
                    self.var_nickname.get(),
                    self.var_arrest_date.get(),
                    self.var_date_of_crime.get(),
                    self.var_address.get(),
                    self.var_age.get(),
                    self.var_occupation.get(),
                    self.var_birthMark.get(),
                    self.var_crime_type.get(),
                    self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get(),
                    self.var_case_id.get(),
                                                                                                                                                                                                                                                 ))


                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    #delete
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure Delete this criminal record')
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Aman@9389',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record successfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due To{str(es)}')


    #clear
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    #search
    def search_data(self):
    # Check if the search combo box is empty
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror('Error', 'All Fields are required')
        else:
            try:
                # Establish connection to the MySQL database
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    password='Aman@9389',
                    database='management'
                )
                my_cursor = conn.cursor()

                # Execute the query based on selected search criteria
                query = f"SELECT * FROM criminal WHERE {self.var_com_search.get()} LIKE '%{self.var_search.get()}%'"
                my_cursor.execute(query)
                rows = my_cursor.fetchall()

                # Clear the current data in the table
                if len(rows) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())

                    # Insert new data fetched from the database
                    for row in rows:
                        self.criminal_table.insert("", END, values=row)

                # Commit the transaction and close the connection
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}')

       
if __name__ == '__main__':
    root = Tk()
    app = Criminal(root)
    root.mainloop()
