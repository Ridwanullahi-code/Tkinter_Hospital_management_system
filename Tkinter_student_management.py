from tkinter import*
from tkinter import ttk

root = Tk()
root.geometry("1100x465")
root.resizable(width="no",height="no")
root.title("Treeview")
def Add_button():
	global count
	entry_values = [1+count, s_entry.get().capitalize() , f_entry.get().capitalize(), l_entry.get().capitalize(), d_entry.get().upper(),
	m_entry.get().upper(), level_entry.get(),g_entry.get(),p_entry.get()]	
	my_tree.insert(parent="",index="end",iid=count,values=entry_values)
	data.append(entry_values)
	print(data)
	delete_value = [s_entry, f_entry, l_entry, d_entry, m_entry, level_entry, g_entry, p_entry]	
	count +=1
	for n in range(0,8):
		delete_value[n].delete(0,END)

p_title = Label(root,text="Student Management System",fg="#0E4C92",bg="white",bd=3,relief=GROOVE,font=("times new roman",23,"bold"))
p_title.place(x=0,y=0,width=1100,height=48)
frame = Frame(root,bd=3,bg ="white")
frame.place(x=0,y=48,width=1100,height=405)
sub_frame1 = Frame(frame,bg="#BF0A30")
sub_frame1.place(x=0,y=0,width=380,height=400)
manage = Label(sub_frame1,text="Manage Students",fg="white",bg="#BF0A30",font=("Verdana",16,"bold"))
manage.place(x=100,y=10)

t = ["Surname","First Name","Last Name","Department","Matric No","Level","Gender","Phone No"]
s_label = Label(sub_frame1,text=t[0],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
s_label.place(x=20,y=80)
f_label = Label(sub_frame1,text=t[1],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
f_label.place(x=20,y=110)
l_label = Label(sub_frame1,text=t[2],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
l_label.place(x=20,y=140)
d_label = Label(sub_frame1,text=t[3],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
d_label.place(x=20,y=170)
m_label = Label(sub_frame1,text=t[4],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
m_label.place(x=20,y=200)
leve_label = Label(sub_frame1,text=t[5],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
leve_label.place(x=20,y=230)
g_label = Label(sub_frame1,text=t[6],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
g_label.place(x=20,y=260)
p_label = Label(sub_frame1,text=t[7],fg="white",bg="#BF0A30",font=("Verdana",12,"bold"))
p_label.place(x=20,y=290)

s_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
s_entry.place(x=140,y=85)
f_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
f_entry.place(x=140,y=115)
l_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
l_entry.place(x=140,y=145)
d_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
d_entry.place(x=140,y=175)
m_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
m_entry.place(x=140,y=205)
level_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
level_entry.place(x=140,y=235)
g_entry = ttk.Combobox(sub_frame1,value=("Male","Female"),width=26,font=("times new roman",12,"bold"))
g_entry.place(x=140,y=267)
p_entry = Entry(sub_frame1,width=20,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
p_entry.place(x=140,y=295)

button_frame =Frame(sub_frame1,bd=3,bg ="white")
button_frame.place(x=25,y=345,width=345,height=40)

add_button = Button(button_frame,text="Add",width=10,pady=5,bg="#003151",fg="white",font=("times new roman",10),command=Add_button)
add_button.place(x=0,y=0)
update_button = Button(button_frame,text="Update",width=10,pady=5,bg="#003151",fg="white",font=("times new roman",10))
update_button.place(x=86,y=0)
delete_button = Button(button_frame,text="Delete",width=10,pady=5,bg="#003151",fg="white",font=("times new roman",10) )
delete_button.place(x=172,y=0)
clear_button = Button(button_frame,text="Clear",width=10,pady=5,bg="#003151",fg="white",font=("times new roman",10))
clear_button.place(x=258,y=0)

sub_frame2 = Frame(frame,bd=3,bg ="#BF0A30")
sub_frame2.place(x=385,y=0,width=708,height=405)
search_lab = Label(sub_frame2,text="Search By",fg="white",bg="#BF0A30",font=("times new roman",14,"bold"))
search_lab.place(x=9,y=8)
option = ttk.Combobox(sub_frame2,value=("Name","Matric No","Email"),width=15,font=("times new roman",12,"bold"))
option.place(x=110,y=8)
entry = Entry(sub_frame2,width=13,bd=4,relief=GROOVE,font=("Verdana",12,"bold"))
entry.place(x=260,y=6)
search_b = Button(sub_frame2,text="Search",width=11,pady=1,bg="white",fg="black",font=("Verdana",10,"bold"))
search_b.place(x=420,y=6)
show_b = Button(sub_frame2,text="Show All",width=11,pady=1,bg="white",fg="black",font=("Verdana",10,"bold"))
show_b.place(x=535,y=6)


column = (1,2,3,4,5,6,7,8,9)
head = ("SN","Surname","First Name","Last Name","Department","Matric No","Level","Gender","Phone No")
tree_frame = Frame(sub_frame2,bd=3,bg ="white")
tree_frame.place(x=5,y=45,width=692,height=348)
yscrollbar = Scrollbar(tree_frame,orient = VERTICAL)
xscrollbar = Scrollbar(tree_frame, orient = HORIZONTAL)

style = ttk.Style()
style.configure("Treeview.Heading",font=("Verdana",10,"bold"))
my_tree = ttk.Treeview(tree_frame,columns=column,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set,show="headings",height=2)
yscrollbar.pack(side=RIGHT,fill="y")
xscrollbar.pack(side=BOTTOM,fill="x")
yscrollbar.config(command=my_tree.yview)
xscrollbar.config(command=my_tree.xview)

my_tree.column(1,width=50,anchor=CENTER,stretch=NO)
my_tree.column(2,width=130,anchor=CENTER,stretch=NO)
my_tree.column(3,width=130,anchor=CENTER,stretch=NO)
my_tree.column(4,width=100,anchor=CENTER,stretch=NO)
my_tree.column(5,width=120,anchor=CENTER,stretch=NO)
my_tree.column(6,width=120,anchor=CENTER,stretch=NO)
my_tree.column(7,width=90,anchor=CENTER,stretch=NO)
my_tree.column(8,width=100,anchor=CENTER,stretch=NO)
my_tree.column(9,width=130,anchor=CENTER,stretch=NO)

my_tree.heading(1,text="SN")
my_tree.heading(2,text="Surname")
my_tree.heading(3,text="First Name")
my_tree.heading(4,text="Last Name")
my_tree.heading(5,text="Department")
my_tree.heading(6,text="Matric No")
my_tree.heading(7,text="Level")
my_tree.heading(8,text="Gender")
my_tree.heading(9,text="Phone No")

data = [[1,"Ajayi","Ridwan","Olalekan","IFT","IFT/19/0649","100","Male","08144580946"],
		[2,"Oladimeji","Ismail","Abiodun","IFT","IFT/19/0650","100","Male","09144580996"]
]
print(data)
count= 0
for record in data:
	my_tree.insert(parent="",index="end",iid= count,values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
	count +=1

my_tree.pack(fill=BOTH,expand=1)
root.mainloop()


#for i in range(0,7):
	#my_tree.heading(i+1,text=head[i])
	#my_tree.column(i+1,width=70)

#my_tree.insert(parent="",index="end",iid=0,text="Parent",values=("Ajayi","Ridwan","Olalekan","IFT","IFT/19/0649	","100","Male","08144580946"))
#my_tree.pack(fill=BOTH,expand=1)

"""
column = (1,2,3,4,5,6,7)
head = ("Roll No","Name","Email","Gender","Contact","DOB","Adress")


yscrollbar = Scrollbar(frame,orient = VERTICAL)
xscrollbar = Scrollbar(frame, orient = HORIZONTAL)

my_tree = ttk.Treeview(frame,columns=column,yscrollcommand=yscrollbar.set,xscrollcommand=xscrollbar.set,show="headings",height=3)
yscrollbar.pack(side=RIGHT,fill="y")
xscrollbar.pack(side=BOTTOM,fill="x")
yscrollbar.config(command=my_tree.yview)
xscrollbar.config(command=my_tree.xview)

for i in range(0,7):
	my_tree.heading(i+1,text=head[i])
	my_tree.column(i+1,width=70)

my_tree.insert(parent="",index="end",iid=0,text="Parent",values=("Parent","John","example@gmail.com","Male","08144580946","BBB","55555"))

data = [[1,"Ajayi","Ridwan","Olalekan","IFT","IFT/19/0649","100","Male","08144580946"],
		[2,"Oladimeji","Ismail","Abiodun","IFT","IFT/19/0650","100","Male","09144580996"]
]
count= 0
for record in data:
	my_tree.insert(parent="",index="end",iid= count,values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8]))
	count +=1


"""