from tkinter import*

root = Tk()
root.title("User Login")
root.geometry("300x200")
#Name 
Name = Label(root, text="Name").place(x=20,y=40)
entry = Entry(root,width=30).place(x=70,y=40)
#Email   
email = Label(root, text="Email").place(x=20,y=70)
entry2 = Entry(root,width=30).place(x=70,y=70)
#Password 
password = Label(root, text="Password").place(x=15,y=100)
entry3 = Entry(root,width=30,show="*").place(x=70,y=100)
#Submit 
Button(root,text="Submit",padx=3,pady=4, fg="white", bg="red",activebackground="green").place(x=120,y=150)
root.mainloop()