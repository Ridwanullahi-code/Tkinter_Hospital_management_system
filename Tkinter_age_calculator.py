from tkinter import*
from PIL import ImageTk,Image
import datetime

date_now = datetime.date.today()
year_now = int(date_now.year)

root = Tk()
root.geometry("400x550")
root.resizable(width=NO, height=NO)
root.title("Age Calculation")
y_value = IntVar(value="")
m_value = IntVar(value="")
d_value = IntVar(value="")
textvar = StringVar()
fn_value = StringVar()
other_value = StringVar()

def calculate_now():
	y = y_value.get()
	m = m_value.get()
	d = d_value.get()
	birth = datetime.date(y ,m ,d).year
	age = year_now - birth
	textvar.set(age)

def clear_button():
	entry1.get()
		
path = "image/birthday.png"
my_image = ImageTk.PhotoImage(Image.open(path))

label = Label(root, image=my_image, width=200, height=170)
label.place(x=100,y=10)

firsrName = Label(root,text="First Name: ",font="Roboto 10 bold",fg="black").place(x=0,y=220)
OtherName = Label(root,text="Other Name: ",font="Roboto 10 bold",fg="black").place(x=0,y=260)

year = Label(root,text="Year : ",font="Roboto 10 bold",fg="black").place(x=0,y=300)
month = Label(root,text="Month : ",font="Roboto 10 bold",fg="black").place(x=0,y=340)
date = Label(root,text="Date : ",font="Roboto 10 bold",fg="black").place(x=0,y=380)
Age = Label(root,text="Age : ",font="Roboto 10 bold",fg="black").place(x=0,y=420)

entry1 = Entry(root, bd=3, relief=GROOVE,width=18,font="Roboto 14 bold")
entry1.place(x=100,y=220)

entry2 = Entry(root, bd=3, relief=GROOVE,width=18,font="Roboto 14 bold")
entry2.place(x=100,y=260)

entry3 = Entry(root, bd=3, relief=GROOVE,width=18,font="Roboto 14 bold", textvariable= y_value)
entry3.place(x=100,y=300)

entry4 = Entry(root, bd=3, relief=GROOVE,width=18,font="Roboto 14 bold", textvariable= m_value)
entry4.place(x=100,y=340)

entry5 = Entry(root, bd=3, relief=GROOVE,width=18,font="Roboto 14 bold", textvariable= d_value)
entry5.place(x=100,y=380)

entry6 = Entry(root, bd=3, relief=GROOVE,width=18,font="Roboto 14 bold",textvariable=textvar,justify=CENTER)
entry6.place(x=100,y=420)

button1 = Button(root,text="Calculate", bg="#6F2DA8",
				activebackground="#D30000",width=10,padx=4,pady=4,
				fg="white", font="Roboto 10 bold",command=calculate_now)
button1.place(x=80,y=480)

button2= Button(root,text="Clear", bg="#D30000",
				activebackground="#6F2DA8",width=10,padx=4,pady=4,
				fg="white", font="Roboto 10 bold",command=clear_button)
button2.place(x=223,y=480)

root.mainloop()