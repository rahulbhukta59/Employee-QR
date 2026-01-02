#most require installation:
#qrcode libary installation.(pip install qrcode)
#resize libary installation.(pip install python-resize-image)
#pillow libary installation(pip install pillow)
from tkinter import*
import qrcode 
import os
from PIL import Image,ImageTk
from resizeimage import resizeimage
class QrGenerator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator | Developed by RAHUL BHUKTA")
        self.root.resizable(False,False)

        title=Label(self.root,text="QR Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w').place(x=0,y=0,relwidth=1)

        # ====Employee Details Window=====
        #======variables==========
        self.var_emp_code=StringVar()
        self.var_Name=StringVar()
        self.var_Department=StringVar()
        self.var_Designation=StringVar()

        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        emp_title=Label(emp_Frame,text="Employee Details",font=("goudy old style",30),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        lbl_emp_code=Label(emp_Frame,text="Employee ID",font=("Times New Roman",15,'bold'),bg='white').place(x=20,y=60)
        lbl_Name=Label(emp_Frame,text="Name",font=("Times New Roman",15,'bold'),bg='white').place(x=20,y=100)
        lbl_Department=Label(emp_Frame,text="Department",font=("Times New Roman",15,'bold'),bg='white').place(x=20,y=140)
        lbl_Designation=Label(emp_Frame,text="Designation",font=("Times New Roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_emp_code=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=60)
        txt_Name=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_Name,bg='lightyellow').place(x=200,y=100)
        txt_Department=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_Department,bg='lightyellow').place(x=200,y=140)
        txt_Designation=Entry(emp_Frame,font=("Times New Roman",15),textvariable=self.var_Designation,bg='lightyellow').place(x=200,y=180)

        btn_generator=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=250,width=200,height=30)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=280,y=250,width=120,height=30)
        self.msg=' '
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("Times New Roman",20),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)

                # ====EmployeeQr code Window=====
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Frame,text="Employee QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text='QR code \n not Avalible',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear (self):
        self.var_emp_code.set(' ')
        self.var_Name.set(' ')
        self.var_Department.set(' ')
        self.var_Designation.set(' ')
        self.msg=' '
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate (self):
        if self.var_emp_code.get()=='' or self.var_Department.get()=='' or self.var_Name.get()=='' or self.var_Designation.get()=='':
            self.msg="All Fields are Required!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID:{self.var_emp_code.get()}\n Employee Name:{self.var_Name.get()}\n Depertment:{self.var_Department.get()}\n Designation:{self.var_Designation.get()}")
            if not os.path.exists('Employee_QR'):
                os.makedirs('Employee_QR')

            qr_code= qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save('Employee_QR/EMP_'+str(self.var_emp_code.get())+'.png')
            #======QR Code Image Update=========
            self.im=ImageTk.PhotoImage(file='Employee_QR/EMP_'+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)
            #=========Updating Notifaction============
            self.msg="QR Generated SuccessFully!!!"
            self.lbl_msg.config(text=self.msg,fg='green')

root=Tk()
obj=QrGenerator(root)        
root.mainloop()