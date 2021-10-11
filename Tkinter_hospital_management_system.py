from tkinter import*
from tkinter import ttk 

root = Tk()
root.geometry("1090x510+100+120")
root.title("Hospital management system")
root.configure(bg="#B5E0E6")

def prescrib_button():
	global lab1
	entry_val = [e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get()
					,e11.get(),e12.get(),e13.get(),e14.get(),e15.get(),e16.get(),e17.get(),e18.get()]

	for t in range(len(entry_val)):
		lab1 = Label(sub_frame,text= entry_val[t],bg="white",font=("Verdana",8,"bold"))
		lab1.grid(column=1,row=t)

	
def Clear_button():
	clear_all = [e2.delete(0,END),e3.delete(0,END),e4.delete(0,END),e5.delete(0,END),
				e6.delete(0,END),e7.delete(0,END),e8.delete(0,END),e9.delete(0,END),e10.delete(0,END),
				e11.delete(0,END),e12.delete(0,END),e13.delete(0,END),e14.delete(0,END),e15.delete(0,END),
				e16.delete(0,END),e17.delete(0,END),e18.delete(0,END)]

	for d in range(len(clear_all)):
		clear_all[d]

pro_title = Label(root,text="+ HOSPITAL MANAGEMENT SYSTEM",bg="white",fg="#FE0203",bd=9,font=("times new roman",22,"bold"),relief=GROOVE)
pro_title.place(x=0,y=0,width=1090)

frame1 = Frame(root,bg='white',bd=5,relief= RIDGE)
frame1.place(x=0,y=50,width=1100,height=280)

patient_info = Label(root,text="Patient Information",bg="white",font=("Verdana",8,"bold"))
patient_info.place(x=5,y=55)

sub_frame1 = Frame(frame1,bg='white',bd=5,relief= RIDGE)
sub_frame1.place(x=0,y=10,width=750,height=255)

# <----------------------  patients informations labels ------------------------>
texts = ["Name Of Tablets","Reference No: ","Dose","No Of Tablets","Lot","Issue Date","Exp Date:","Daily Dose:","Side Effect:"]

l1 = Label(sub_frame1,text=texts[0],bg="white",font="Roboto 10 bold")
l1.place(x=10,y=10)
l2 = Label(sub_frame1,text=texts[1],bg="white",font="Roboto 10 bold")
l2.place(x=10,y=39)
l3 = Label(sub_frame1,text=texts[2],bg="white",font="Roboto 10 bold")
l3.place(x=10,y=64)
l4 = Label(sub_frame1,text=texts[3],bg="white",font="Roboto 10 bold")
l4.place(x=10,y=89)
l5 = Label(sub_frame1,text=texts[4],bg="white",font="Roboto 10 bold")
l5.place(x=10,y=114)
l6 = Label(sub_frame1,text=texts[5],bg="white",font="Roboto 10 bold")
l6.place(x=10,y=139)
l7 = Label(sub_frame1,text=texts[6],bg="white",font="Roboto 10 bold")
l7.place(x=10,y=164)
l8 = Label(sub_frame1,text=texts[7],bg="white",font="Roboto 10 bold")
l8.place(x=10,y=189)
l9 = Label(sub_frame1,text=texts[8],bg="white",font="Roboto 10 bold")
l9.place(x=7,y=215)

#<-------------------------- patients information entries ------------------------>

drug_list = ("alendronate tablet","acyclovir capsule","albuterol sulfate","alitretinoin","alprazolam")
e1 = ttk.Combobox(sub_frame1,values=drug_list,font="Roboto 12 bold",state="r",width=24)
e1.place(x=130,y=12)
e1.set("altretamine")

e2 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e2.place(x=130,y=39)
e3 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e3.place(x=130,y=64)
e4 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e4.place(x=130,y=89)
e5 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e5.place(x=130,y=114)
e6 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e6.place(x=130,y=139)
e7 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e7.place(x=130,y=164)
e8 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e8.place(x=130,y=189)
e9 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e9.place(x=130,y=215)

#<----------------------------- other information labels -------------------->
texts2 = ["Further Information",'Blood Pressure',"Storage Advice:","Medication","Patient id","NHS Number","Patient Name","Date Of Birth","Patient Address"]

l10 = Label(sub_frame1,text=texts2[0],bg="white",font="Roboto 10 bold")
l10.place(x=378,y=10)
l11 = Label(sub_frame1,text=texts2[1],bg="white",font="Roboto 10 bold")
l11.place(x=380,y=39)
l12 = Label(sub_frame1,text=texts2[2],bg="white",font="Roboto 10 bold")
l12.place(x=380,y=64)
l13 = Label(sub_frame1,text=texts2[3],bg="white",font="Roboto 10 bold")
l13.place(x=380,y=89)
l14 = Label(sub_frame1,text=texts2[4],bg="white",font="Roboto 10 bold")
l14.place(x=380,y=114)
l15 = Label(sub_frame1,text=texts2[5],bg="white",font="Roboto 10 bold")
l15.place(x=380,y=139)
l16 = Label(sub_frame1,text=texts2[6],bg="white",font="Roboto 10 bold")
l16.place(x=380,y=164)
l17 = Label(sub_frame1,text=texts2[7],bg="white",font="Roboto 10 bold")
l17.place(x=380,y=189)
l18 = Label(sub_frame1,text=texts2[8],bg="white",font="Roboto 10 bold")
l18.place(x=380,y=215)

#<---------------------- other information entries ---------------------->
e10 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e10.place(x=505,y=13)
e11 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e11.place(x=505,y=39)
e12 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e12.place(x=505,y=64)
e13 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e13.place(x=505,y=89)
e14 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e14.place(x=505,y=114)
e15 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e15.place(x=505,y=139)
e16 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e16.place(x=505,y=164)
e17 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e17.place(x=505,y=189)
e18 = Entry(sub_frame1,bd=3,bg='white',font= ("Verdana",11,"bold"),relief=GROOVE,width=21)
e18.place(x=505,y=215)

sub_frame2 = Frame(frame1,bg='white',bd=5,relief= RIDGE)
sub_frame2.place(x=760,y=10,width=327,height=255)
canvas = Canvas(sub_frame2,width=327,bg="white")
sub_frame = Frame(canvas,bg="white")

sub_scrollbar = Scrollbar(sub_frame2,orient=VERTICAL,command = canvas.yview)
canvas.configure(yscrollcommand=sub_scrollbar.set)
sub_scrollbar.pack(side=RIGHT,fill="y")
canvas.pack(side=LEFT)
canvas.create_window((0,0),window=sub_frame,anchor="nw")
sub_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


list1 = texts + texts2
for i in range(len(list1)):
	label1 = Label(sub_frame,text=list1[i],bg="white",font="Roboto 8 bold")
	label1.grid(column=0,row=i,sticky=W)

sub_frame3 = Frame(root,bg='white',bd=3,relief=GROOVE)
sub_frame3.place(x=0,y=327,width=1090,height=30)

button1 = Button(sub_frame3,text="Prescription",width=22,bg="green",fg="white",font=("Verdana",9,"bold"),command=prescrib_button)
button1.place(x=0,y=0)

button2 = Button(sub_frame3,text="Prescription Data",width=22,bg="green",fg="white",font=("Verdana",9,"bold"))
button2.place(x=186,y=0)

button3 = Button(sub_frame3,text="Update",width=22,bg="green",fg="white",font=("Verdana",9,"bold"))
button3.place(x=372,y=0)

button4 = Button(sub_frame3,text="Delete",width=22,bg="green",fg="white",font=("Verdana",9,"bold"))
button4.place(x=558,y=0)

button5= Button(sub_frame3,text="Clear",width=22,bg="green",fg="white",font=("Verdana",9,"bold"),command=Clear_button)
button5.place(x=744,y=0)

button6 = Button(sub_frame3,text="Exit",width=18,bg="green",fg="white",font=("Verdana",9,"bold"),command=root.quit)
button6.place(x=930,y=0)

sub_frame4 = Frame(root,bg='white',bd=4,relief=GROOVE)
sub_frame4.place(x=0,y=360,width=1092,height=152)

#<------------------------ scrollbars ---------------->

data = ["Name Of Table","Reference No","Dose","No Of Tables","Lot","Issue Date",
		"Exp Date","Daily Date","Storage","NHS Number","Patient Name","Date Of Birth","Address"]
column_no = [0,1,2,3,4,5,6,7,8,9,10,11,12]

y_scrollbar = Scrollbar(sub_frame4,orient=VERTICAL)
xscrollbar = Scrollbar(sub_frame4,orient= HORIZONTAL)
y_scrollbar.pack(side=RIGHT,fill="y")
xscrollbar.pack(side=BOTTOM,fill="x")

style = ttk.Style()
style.configure("Treeview.Heading",font=("Verdana",10,"bold"))
my_tree = ttk.Treeview(sub_frame4,columns=column_no,yscrollcommand = y_scrollbar.set, xscrollcommand = xscrollbar.set,show = "headings")
y_scrollbar.configure(command=my_tree.yview)
xscrollbar.configure(command=my_tree.xview)

for col in range(0,13):
	my_tree.column(column_no[col],width=125,anchor=CENTER)
	my_tree.heading(column_no[col],text=data[col])

my_tree.pack(fill=BOTH)

root.mainloop()

