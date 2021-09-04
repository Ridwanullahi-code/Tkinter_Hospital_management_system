from tkinter import*
import random
from time import sleep


items = ["ROCK","PAPER","SCISSORS"]

computer = None
root = Tk()
root.geometry("450x400")
root.title("ROCK PAPER SCISSORS")
root.resizable(width=NO,height=NO)


def button_click(word):
	global computer_score, player_score,entry1_val,entry2_val
	game_running = True
	computer_score = 0
	player_score = 0
	computer = random.choice(items)
	entry1.delete(0,END)
	entry2.delete(0,END)

	entry2.insert(0,word)
	entry1.insert(0,computer)
	entry1_val = entry1.get()
	entry2_val = entry2.get()

	if entry1_val == "ROCK" and entry2_val == "SCISSORS":
		computer_score += 1
		winner.delete(0,END)
		winner.insert(0,"COMPUTER WIN")
		
			
	elif entry1_val == "PAPER" and entry2_val == "ROCK":
		computer_score += 1
		winner.delete(0,END)
		winner.insert(0,"COMPUTER WIN")
			
		
	elif entry1_val == "SCISSORS" and entry2_val == "PAPER":
		print(f"COMPUTER PLAY: {entry1_val} PLAYER PLAY : {entry2_val} ")
		computer_score += 1
		winner.delete(0,END)
		winner.insert(0,"COMPUTER WIN")
		

	elif entry1_val == "SCISSORS" and entry2_val == "ROCK":
		player_score += 1
		winner.delete(0,END)
		winner.insert(0,"PLAYER WIN")
		
			

	elif entry1_val == "ROCK" and entry2_val == "PAPER":
		player_score = +1
		winner.delete(0,END)
		winner.insert(0,"PLAYER WIN")
		
	elif entry1_val == "PAPER" and entry2_val == "SCISSORS":
		player_score += 1
		winner.delete(0,END)
		winner.insert(0,"PLAYER WIN")		

	elif entry1_val == entry2_val:
		winner.delete(0,END)
		winner.insert(0,"IT IS A TIE")		

def clear_button():
	entry2.delete(0,END)
	entry1.delete(0,END)
	winner.delete(0,END)
	
label = Label(root,text="ROCK PAPER SCISSORS", font="Roboto 15 bold")
label.place(x=110,y=10)
entry1 = Entry(root,bd=4,bg="white",width=14, font="Roboto 15 bold",relief=GROOVE)
entry1.place(x=12,y=100)
button1 = Button(root, text="ROCK",bg="#B200ED",padx=6,pady=10,width=7, font="Roboto 16 bold",fg="white",command= lambda: button_click("ROCK"))
button1.place(x=20,y=240)


labe2= Label(root,text="COMPUTER PLAY", font="Roboto 15 bold")
labe2.place(x=5,y=60)
entry2 = Entry(root,bd=4,bg="white",width=14, font="Roboto 15 bold",relief=GROOVE)
entry2.place(x=280,y=100)
button2 = Button(root,text="PAPER",bg="#0018F9",padx=6,pady=10,width=7,font="Roboto 16 bold",fg="white",command=lambda: button_click("PAPER"))
button2.place(x=170,y=240)


labe3 = Label(root,text="PLAYER PLAY", font="Roboto 15 bold")
labe3.place(x=300,y=60)
button3 = Button(root,text="SCISSORS",bg="#BD011F",padx=6,pady=10,width=7,font="Roboto 16 bold",fg="white",command= lambda:button_click("SCISSORS"))
button3.place(x=320,y=240)

button4 = Button(root,text="RESET",bg="#F9A602",padx=6,pady=10,width=12,font="Roboto 16 bold",fg="white",command=clear_button)
button4.place(x=137,y=320)
winner = Entry(root,bd=4,bg="white",width=20,font="Roboto 15 bold",relief=GROOVE,justify=CENTER)
winner.place(x=110,y=180)

root.mainloop()