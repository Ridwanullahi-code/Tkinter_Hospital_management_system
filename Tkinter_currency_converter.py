from tkinter import* 
from tkinter import ttk
from currencies import Currency
from currency_converter import CurrencyConverter 


root = Tk()

convert = CurrencyConverter()
currencies = tuple(convert.currencies)

root.geometry("500x250")
root.resizable(width=NO,height=NO)
root.title("Currency Converter")


def Label_change():
	c1 = combo1.get()
	c2 = combo2.get()
	labe1.configure(text=c1)
	
	labe2.configure(text=c2)
	root.after(1000,Label_change)

def button_click():
	labe1_val = labe1["text"]
	labe2_val = labe2["text"]
	e1 = entry1.get()
	conv = round(convert.convert(e1,labe1_val,labe2_val))
	entry2.insert(0,conv)

def clear_button():
	entry1.delete(0,END)
	entry2.delete(0,END)



combo1 = ttk.Combobox(root,font="Roboto 10 bold",values=currencies)
combo1.place(x=30,y=20)
combo1.set("USD")

labe1 = Label(root,font="Roboto 15 bold", bd=5,relief=GROOVE,width=15,bg="grey")
labe1.place(x=15,y=60)
button1 = Button(root,text="CONVERT", padx=4,pady=8,bg="purple",fg="white",activebackground="orange",width=10,font="Roboto 10 bold",command=button_click)
button1.place(x=90,y=180)
entry1 = Entry(root, font="Roboto 15 bold", width=20,bd=5,relief=GROOVE)
entry1.place(x=0,y=120)

labe3 = Label(root, text="TO",font="Roboto 20 bold")
labe3.place(x=223,y=60)

combo2= ttk.Combobox(root,font="Roboto 10 bold",values=currencies)
combo2.place(x=310,y=20)
combo2.set("AFN")
labe2 = Label(root,font="Roboto 15 bold", bd=5,relief=GROOVE,width=15,bg="grey")
labe2.place(x=290,y=60)
entry2= Entry(root, font="Roboto 15 bold", width=20,bd=5,relief=GROOVE)
entry2.place(x=268,y=120)
button2 = Button(root,text="CLEAR", padx=4,pady=8,bg="purple",fg="white",activebackground="orange",width=10,font="Roboto 10 bold",command=clear_button)
button2.place(x =300,y=180)

Label_change()

root.mainloop()