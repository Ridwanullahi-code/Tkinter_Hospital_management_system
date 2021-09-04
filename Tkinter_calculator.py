from tkinter import*
import math

root = Tk()
root.geometry("400x390")
root.resizable(width=NO,height=NO)
root.title("Calculator")
root.configure(bg="black")

def button_click(number):
	current = entry.get()
	entry.delete(0,END)
	entry.insert(0,str(current) + str(number))

def clear_button():
	current = entry.get()
	entry.delete(0,END)

def equal_button():
	second_num = entry.get()
	entry.delete(0,END)
	if  sign== "addition":
		entry.insert(0, f_num + int(second_num))
	elif sign == "multiply":
		entry.insert(0, f_num *int(second_num))
	elif sign == "division":
		entry.insert(0, f_num / int(second_num))
	elif sign == "substraction":
		entry.insert(0, f_num - int(second_num))
	elif sign == "modulus":
		entry.insert(0, f_num % int(second_num))
 
def Addition_button():
	first_num = entry.get()
	global sign,f_num
	sign = "addition"
	f_num = int(first_num)
	entry.delete(0,END)

def multiply_button():
	first_num = entry.get()
	global sign,f_num
	sign = "multiply"
	f_num = int(first_num)
	entry.delete(0,END)

def division_button():
	first_num = entry.get()
	global sign,f_num
	math = "division"
	f_num = int(first_num)
	entry.delete(0,END)

def sub_button():
	first_num = entry.get()
	global sign,f_num
	sign = "substraction"
	f_num = int(first_num)
	entry.delete(0,END)

def mod_button():
	first_num = entry.get()
	global sign,f_num
	sign = "modulus"
	f_num = int(first_num)
	entry.delete(0,END)
	
entry = Entry(root, bd=5, relief=GROOVE, width="30",font="Roboto 14")
entry.place(x=30, y=30)

clear = Button(root, text="Clear", bg="orange", padx=3, pady=3,activebackground="purple",width=8, font="Roboto 14", command=lambda:clear_button())
clear.place(x=30,y=80)

addition = Button(root,text="+",bg="gray",padx=3,pady=3,font="Roboto 14",width=5, command= lambda: Addition_button()).place(x=145,y=80)
multiply = Button(root,text="X",bg="gray",padx=3,pady=3,font="Roboto 14",width=5,command =lambda:multiply_button()).place(x=225,y=80)
substract = Button(root,text="-",bg="gray",padx=3,pady=3,font="Roboto 14",width=5, command=lambda:sub_button()).place(x=305,y=80)

button7 = Button(root,text="7",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5, command= lambda:button_click(7)).place(x=30,y=140)
button8 = Button(root,text="8",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(8)).place(x=120,y=140)
button9 = Button(root,text="9",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(9)).place(x=210,y=140)
division = Button(root,text="/",bg="gray",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:division_button()).place(x=305,y=140)

button4 = Button(root,text="4",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(4)).place(x=30,y=200)
button5 = Button(root,text="5",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(5)).place(x=120,y=200)
button6 = Button(root,text="6",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(6)).place(x=210,y=200)
modulos = Button(root,text="%",bg="gray",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:mod_button()).place(x=305,y=200)

button1 = Button(root,text="1",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(1)).place(x=30,y=260)
button2 = Button(root,text="2",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(2)).place(x=120,y=260)
button3 = Button(root,text="3",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5,command= lambda:button_click(3)).place(x=210,y=260)
equal = Button(root,text="=",bg="#98FB98",padx=3,pady=3,font="Roboto 14",width=5,height=4,command=lambda:equal_button()).place(x=305,y=260)

zero = Button(root,text="0",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=13,command= lambda:button_click(0)).place(x=30,y=320)
point = Button(root,text=".",bg="#57A0D2",padx=3,pady=3,font="Roboto 14",width=5).place(x=210,y=320)

root.mainloop()