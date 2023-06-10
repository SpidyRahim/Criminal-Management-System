from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox


class Criminal:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Criminal Monitoring Software')

        # variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        lbl_title = Label(self.root, text='Criminal Monitoring Software', font=(
            'times new roman', 40, 'bold'), bg='black', fg='white')
        lbl_title.place(x=0, y=0, width=1530, height=70)

        # mujib logo
        mujib_logo = Image.open('images/mujib.png')
        mujib_logo = mujib_logo.resize((100, 60), Image.LANCZOS)
        self.mujib_shoto_logo = ImageTk.PhotoImage(mujib_logo)

        self.Mlogo = Label(self.root, image=self.mujib_shoto_logo)
        self.Mlogo.place(x=1370, y=5, width=150, height=60,)

        # police logo

        img_logo = Image.open('images/policelogo.png')
        img_logo = img_logo.resize((60, 60), Image.LANCZOS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root, image=self.photo_logo)
        self.logo.place(x=350, y=5, width=60, height=60)

        # Img_Frame
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='red')
        img_frame.place(x=0, y=70, width=1530, height=130)

        # ist image
        img1 = Image.open('images/first.jpg')
        img1 = img1.resize((540, 160), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0, y=0, width=540, height=160)

        # 2nd image

        img2 = Image.open('images/second.jpg')
        img2 = img2.resize((540, 160), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=541, y=0, width=540, height=160)

        # 3rd image

        img3 = Image.open('images/third.jpg')
        img3 = img3.resize((540, 160), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1082, y=0, width=540, height=160)

        # main frame
        Main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='gray')
        Main_frame.place(x=10, y=210, width=1500, height=560)

        # upper frame
        upper_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information', font=(
            'times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1480,
                          height=270)  # 1480 cilo width

        # right side police frame and entry
        #police_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Police Information', font=(
         #   'times new roman', 11, 'bold'), fg='red', bg='white')
        #police_frame.place(x=945, y=10, width=540, height=270)

        # Label and Entries

        # case id
        caseid = Label(upper_frame, text='Case Id:',
                       font=('arial', 12, 'bold'), bg='white')
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=22,
                              font=('arial', 11, 'bold'))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)

        # criminal no
        lbl_criminal_no = Label(upper_frame, text='Criminal No:',
                                font=('arial', 12, 'bold'), bg='white')
        lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_criminal_no = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=22,
                                    font=('arial', 11, 'bold'))
        txt_criminal_no.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # criminal name
        lbl_name = Label(upper_frame, text='Criminal Name:',
                         font=('arial', 12, 'bold'), bg='white')
        lbl_name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22,
                             font=('arial', 11, 'bold'))
        txt_name .grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # nickname
        lbl_nickname = Label(upper_frame, text='Nickname:',
                             font=('arial', 12, 'bold'), bg='white')
        lbl_nickname.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_nickname = ttk.Entry(upper_frame, textvariable=self.var_nickname, width=22,
                                 font=('arial', 11, 'bold'))
        txt_nickname.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        # arrest date
        lbl_arrestDate = Label(upper_frame, text='Arrest Date:',
                               font=('arial', 12, 'bold'), bg='white')
        lbl_arrestDate.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_arrestDate = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=22,
                                   font=('arial', 11, 'bold'))
        txt_arrestDate .grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # date of crime
        lbl_dateOfCrime = Label(upper_frame, text='Date Of Crime:',
                                font=('arial', 12, 'bold'), bg='white')
        lbl_dateOfCrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dateOfCrime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=22,
                                    font=('arial', 11, 'bold'))
        txt_dateOfCrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # address
        lbl_address = Label(upper_frame, text='Address:',
                            font=('arial', 12, 'bold'), bg='white')
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22,
                                font=('arial', 11, 'bold'))
        txt_address .grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # age
        lbl_age = Label(upper_frame, text='Age:',
                        font=('arial', 12, 'bold'), bg='white')
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age, width=22,
                            font=('arial', 11, 'bold'))
        txt_age.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # occupation
        lbl_occupation = Label(upper_frame, text='Occupation:',
                               font=('arial', 12, 'bold'), bg='white')
        lbl_occupation.grid(row=4, column=0, sticky=W, padx=2, pady=7)

        txt_occupation = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=22,
                                   font=('arial', 11, 'bold'))
        txt_occupation .grid(row=4, column=1, sticky=W, padx=2, pady=7)

        # birthmark
        lbl_birthMark = Label(upper_frame, text='Birth Mark:',
                              font=('arial', 12, 'bold'), bg='white')
        lbl_birthMark.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_birthMark = ttk.Entry(upper_frame, textvariable=self.var_birthMark, width=22,
                                  font=('arial', 11, 'bold'))
        txt_birthMark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Crime Type
        lbl_crimeType = Label(upper_frame, text='Crime Type:',
                              font=('arial', 12, 'bold'), bg='white')
        lbl_crimeType.grid(row=0, column=4, sticky=W, padx=2, pady=7)

        txt_crimeType = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=22,
                                  font=('arial', 11, 'bold'))
        txt_crimeType.grid(row=0, column=5, sticky=W, padx=2, pady=7)

        # Father Name
        lbl_fatherName = Label(upper_frame, text='Father Name:',
                               font=('arial', 12, 'bold'), bg='white')
        lbl_fatherName.grid(row=1, column=4, sticky=W, padx=2, pady=7)

        txt_fatherName = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=22,
                                   font=('arial', 11, 'bold'))
        txt_fatherName.grid(row=1, column=5, sticky=W, padx=2, pady=7)

        # Gender
        lbl_gender = Label(upper_frame, text='Gender:',
                           font=('arial', 12, 'bold'), bg='white')
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)

        # wanted
        lbl_wanted = Label(upper_frame, text='Most Wanted:',
                           font=('arial', 12, 'bold'), bg='white')
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # radio button gender
        radio_frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_gender.place(x=730, y=90, width=190, height=30)

        male = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Male',
                           value='Male', font=('arial', 9, 'bold'), bg='white')
        male.grid(row=0, column=0, padx=5, pady=2, sticky=W)
        self.var_gender.set('Male')

        female = Radiobutton(radio_frame_gender, variable=self.var_gender, text='Female',
                             value='Female', font=('arial', 9, 'bold'), bg='white')
        female.grid(row=0, column=1, padx=5, pady=2, sticky=W)
        self.var_gender, set('Female')

        # radio button wanted
        radio_frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        radio_frame_wanted.place(x=730, y=130, width=190, height=30)

        yes = Radiobutton(radio_frame_wanted, variable=self.var_wanted, text='Yes',
                          value='Yes', font=('arial', 9, 'bold'), bg='white')
        yes.grid(row=0, column=0, padx=5, pady=2, sticky=W)
        self.var_wanted.set('Yes')

        no = Radiobutton(radio_frame_wanted, variable=self.var_wanted, text='No',
                         value='No', font=('arial', 9, 'bold'), bg='white')
        no.grid(row=0, column=1, padx=5, pady=2, sticky=W)
        self.var_wanted.set('No')

        # Buttons
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)

        # add button
        btn_add = Button(button_frame, command=self.add_data, text='Save', font=(
            'arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)

        # update button
        btn_add = Button(button_frame, text='Update', font=(
            'arial', 13, 'bold'), width=14, bg='green', fg='white')
        btn_add.grid(row=0, column=1, padx=3, pady=5)

        # delete button
        btn_add = Button(button_frame, text='Delete', font=(
            'arial', 13, 'bold'), width=14, bg='red', fg='white')
        btn_add.grid(row=0, column=2, padx=3, pady=5)

        # clear button
        btn_add = Button(button_frame, text='Clear', font=(
            'arial', 13, 'bold'), width=14, bg='dark red', fg='white')
        btn_add.grid(row=0, column=3, padx=3, pady=5)

        # right side photo

        img_crime = Image.open('images/PoliceRightSidePhoto.png')
        img_crime = img_crime.resize((470, 245), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img_crime)

        self.img__crime = Label(upper_frame, image=self.photo)
        self.img__crime.place(x=1000, y=0, width=470, height=245)

        # lower frame
        lower_frame = LabelFrame(Main_frame, bd=2, relief=RIDGE, text='Criminal Information Table', font=(
            'times new roman', 11, 'bold'), fg='red', bg='white')
        lower_frame.place(x=10, y=280, width=1480, height=270)

        # search frame overlapping the lower frame
        search_frame = LabelFrame(lower_frame, bd=2, relief=RIDGE, text='Search Criminal Record', font=(
            'times new roman', 11, 'bold'), fg='red', bg='white')
        search_frame.place(x=0, y=0, width=1470, height=60)

        search_by = Label(search_frame, text='Search By: ',
                          font=('arial', 11, 'bold'), bg='dark green', fg='white')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # combo box
        combo_search_box = ttk.Combobox(search_frame, font=(
            'arial', 11, 'bold'), width=18, state='readonly')
        combo_search_box['value'] = ('Select Option', 'Case_id', 'Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        search_txt = ttk.Entry(search_frame, width=18,
                               font=('arial', 11, 'bold'))
        search_txt.grid(row=0, column=2, sticky=W, padx=5)

        # search button
        btn_search = Button(search_frame, text='Search', font=(
            'arial', 13, 'bold'), width=14, bg='cyan', fg='black')
        btn_search.grid(row=0, column=3, padx=3, pady=0)

        # all button
        btn_all = Button(search_frame, text='Show All', font=(
            'arial', 13, 'bold'), width=14, bg='cyan', fg='black')
        btn_all.grid(row=0, column=4, padx=3, pady=0)

        # table
        table_frame = Frame(lower_frame, bd=2, relief=RIDGE, bg='gray')
        table_frame.place(x=0, y=60, width=1470, height=170)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, columns=(
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1', text='Case ID')
        self.criminal_table.heading('2', text='Criminal No')
        self.criminal_table.heading('3', text='Criminal Name')
        self.criminal_table.heading('4', text='Nickname')
        self.criminal_table.heading('5', text='Arrest Date')
        self.criminal_table.heading('6', text='Crime Of Date')
        self.criminal_table.heading('7', text='Address')
        self.criminal_table.heading('8', text='Age')
        self.criminal_table.heading('9', text='Occupation')
        self.criminal_table.heading('10', text='Birth Mark')
        self.criminal_table.heading('11', text='Crime Type')
        self.criminal_table.heading('12', text='Father Name')
        self.criminal_table.heading('13', text='Gender')
        self.criminal_table.heading('14', text='Wanted')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column('1', width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)
        self.criminal_table.column('14', width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)

    # add function
    def add_data(self):
        if self.var_case_id.get() == "":
            messagebox.showerror('Error', 'All Fields Must Be Required')
        else:
            try:
                conn = mysql.connector.connect(
                    host='127.0.0.1', port='3306', user='root', password='password', database='monitoring_software')
                # requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"
                my_cursor = conn.cursor()
                my_cursor.execute(
                    'insert into monitoring_software.criminal values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (self.var_case_id.get(),
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
                conn.close()
                messagebox.showinfo(
                    'Success', 'Criminal Record Has Been Added')
            except Exception as es:
                messagebox.showerror('Error', f'Due To {str(es)}')


if __name__ == "__main__":
    root = Tk()
    obj = Criminal(root)
    root.mainloop()
