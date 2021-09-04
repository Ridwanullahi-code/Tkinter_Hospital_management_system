from tkinter import*
import sys
#<---------- window to place all widget to --------->
root = Tk()
root.geometry("300x480")
root.resizable(width=NO,height=NO)
root.title("Whatsapp Boot")

# <------------ send button function ---------->
def button():
	import pywhatkit as kit
	p = phone_entry.get()
	h = hour_entry.get()
	m = minute_entry.get()
	t = text.get(1.0,END)
	s = kit.sendwhatmsg(f"+234{int(p)}", t, int(h), int(m))

# <------------ exit button function ---------->
def exit_button():
	sys.exit()

lblist = ["Phone No","Hour","Minute"]
title = Label(root,text="Whatsapp Message Sender",bg="#351E10",fg="white",font="Roboto 15 bold",relief=GROOVE,bd=3).place(x=0,y=0,width=300)
# <------------ parent frame ------------->
my_frame = Frame(root,width=300,height=480,bd=6,bg="white",relief=GROOVE)
my_frame.place(x=0,y=37)

# <-------------  children frame ---------------->
sub_frame1 =  Frame(my_frame,bg="#351E10",relief=GROOVE)
sub_frame1.place(x=0,y=0,width=289,height=380)

# <---------------- all label widget ------------>
for num in range(0,3):
	label = Label(sub_frame1,text=lblist[num],bg="#351E10",fg="white",font="Roboto 10 bold")
	label.grid(row=num,column=1,pady=4,padx=17)

# <--------------- all Entry widgets-------------->
phone_entry = Entry(sub_frame1,bg="white",font="Roboto 14 bold",bd=4,relief=GROOVE,width=13)
phone_entry.grid(row=0,column=2,pady=4,padx=12)
hour_entry = Entry(sub_frame1,bg="white",font="Roboto 14 bold",bd=4,relief=GROOVE,width=13)
hour_entry.grid(row=1,column=2,pady=4,padx=12)
minute_entry = Entry(sub_frame1,bg="white",font="Roboto 14 bold",bd=4,relief=GROOVE,width=13)
minute_entry.grid(row=2,column=2,pady=4,padx=12)
text_frame = Frame(my_frame,bg="white",bd=8,relief=GROOVE)
text_frame.place(x=0,y=160,width=302,height=220)
message = Label(sub_frame1,text="Message",bg="#351E10",fg="white",font="Roboto 16 bold")
message.place(x=80,y=130)
text = Text(text_frame,bg="white",font="Roboto 12 bold",relief=GROOVE,undo=True)
text.place(x=0,y=0,width=270,height=200)

# <--------------  scrollbar widget --------------->
my_scrollbar = Scrollbar(text_frame)
my_scrollbar.pack(side=RIGHT,fill="y")

# <--------------- this code make text scrollable ------->
my_scrollbar.configure(command=text.yview)
text.configure(yscrollcommand=my_scrollbar.set)

# <---------------- button frame widget ---------------->
button_frame = Frame(my_frame,bd=6,bg="#351E10")
button_frame.place(x=0,y=375,width=290,height=60)

# <------------------ buttons creation ----------------->
send = Button(button_frame,text="Send",width=10,bg="white",pady=5,font="Roboto 16 bold",command=button)
send.place(x=10,y=0)
exit = Button(button_frame,text="Exit",width=5,bg="white",pady=5,font="Roboto 16 bold",command=exit_button)
exit.place(x=190,y=0)

root.mainloop()

