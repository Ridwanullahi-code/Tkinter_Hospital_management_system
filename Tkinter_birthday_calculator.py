from tkinter import*
from PIL import ImageTk, Image
from datetime import datetime, date

root = Tk()
root.geometry("380x470")
root.title("Birthday Calculation")
root.resizable(width=NO, height=NO)

y_value = IntVar(value ="")
m_value = IntVar(value ="")
d_value = IntVar(value ="")
age_value = IntVar(value ="")

date_now = date.today()
year = date_now.year
month = date_now.month
day = date_now.day


path = "image/birthday3.jpg"
my_image = ImageTk.PhotoImage(Image.open(path))


def calc_button():
	e1 = y_value.get()
	e2 = m_value.get()
	e3 = d_value.get()

	cal_date = date(e1, e2, e3)
	y = cal_date.year
	m = cal_date.month
	d = cal_date.day

	result = str((y - year) * 365) + " Days"
	entry4.insert(0,result + "  " + str(d) + "  " + "  " + str(m) + "  " + str(y))

def clear_button():
	entry1.delete(0,END)
	entry2.delete(0,END)
	entry3.delete(0,END)
	entry4.delete(0,END)


image_label = Label(root, image=my_image,width=380, height=200).place(x=0,y=0)

birth_year = Label(root, text="Which Year",font="Roboto 10 bold").place(x=40,y=240)
birth_month = Label(root, text="Month",font="Roboto 10 bold").place(x=40,y=280)
birth_day = Label(root, text="Day",font="Roboto 10 bold").place(x=40,y=320)
birthday =  Label(root, text="Birthday",font="Roboto 10 bold").place(x=40,y=360)

entry1 = Entry(root,font="Roboto 10 bold",width=27,bd=3,relief=GROOVE, textvariable= y_value, justify=CENTER)
entry1.place(x=130,y=240)

entry2 = Entry(root,font="Roboto 10 bold",width=27,bd=3,relief=GROOVE,textvariable= m_value, justify=CENTER)
entry2.place(x=130,y=280)

entry3 = Entry(root,font="Roboto 10 bold",width=27,bd=3,relief=GROOVE,textvariable= d_value, justify=CENTER)
entry3.place(x=130,y=320)


entry4= Entry(root,font="Roboto 10 bold",width=27,bd=3,relief=GROOVE)
entry4.place(x=130,y=360)

button1 = Button(root, text="Calculate",padx=3,pady=3,width=9,
				activebackground="#B22222", bg="#FC0FC0", 
				fg="white", font="Roboto 14 bold",command=calc_button)

button1.place(x=40,y=400)

button2 = Button(root, text="Clear",padx=3,pady=3,width=9,
				activebackground="#FC0FC0", bg="#B22222", fg="white",
				font="Roboto 14 bold",command=clear_button)

button2.place(x=220,y=400)

root.mainloop()

