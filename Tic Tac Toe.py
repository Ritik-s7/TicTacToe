from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox as tmsg

root = Tk()

GUI_width = 350
GUI_Height = 380

Screen_width = root.winfo_screenwidth()
Screen_height = root.winfo_screenheight()

x = (Screen_width / 2) - (GUI_width / 2)
y = (Screen_height / 2) - (GUI_Height / 2)

root.geometry(f"{GUI_width}x{GUI_Height}+{int(x)}+{int(y)}")
root.title("Tic Tac Toe")

player1 = simpledialog.askstring("Input", "Enter Player 1's name", parent=root)
player2 = simpledialog.askstring("Input", "Enter Player 2's name", parent=root)

print(player1, player2)

button = []

for i in range(0, 9):
    button.append(i)
    button[i] = f"button{i}"
count = 4


def CheckWin():
    if button[0]['text'] == button[3]['text'] == button[6]['text'] \
            or button[1]['text'] == button[4]['text'] == button[7]['text'] \
            or button[2]['text'] == button[5]['text'] == button[8]['text'] \
            or button[0]['text'] == button[4]['text'] == button[8]['text'] \
            or button[2]['text'] == button[4]['text'] == button[6]['text'] \
            or button[0]['text'] == button[1]['text'] == button[2]['text'] \
            or button[3]['text'] == button[4]['text'] == button[5]['text'] \
            or button[6]['text'] == button[7]['text'] == button[8]['text']:
        if count % 2 == 0:
            tmsg.showinfo("Game Over", f"{player1} Won")

        elif count % 2 != 0:
            tmsg.showinfo("Game Over", f"{player2} Won")


def pressed(event):
    global count
    global player

    global XOValue
    text = event.widget.cget("text")
    if count % 2 == 0:
        player = X
        try:
            button[int(text)]['text'] = "X"
            button[int(text)]['bg'] = 'red'
            button[int(text)]['fg'] = 'white'
            button[int(text)].config(state="disabled")
            CheckWin()
            count += 1
            if count >= 13:
                print("game over")
                tmsg.showinfo("Game Over", "Game Ended in a draw.")
                quit()
            print(count)
        except Exception as e:
            print(e)

    elif count % 2 != 0:
        player = "O"
        try:
            button[int(text)]['text'] = "O"
            button[int(text)]['bg'] = 'blue'
            button[int(text)]['fg'] = 'white'
            button[int(text)].config(state="disabled")
            CheckWin()
            count += 1
            if count >= 13:
                print("game over")
                tmsg.showinfo("Game Over", "Game Ended in a draw.")
                quit()
            print(count)
        except Exception as e:
            print(e)


# Status bar - Scoring
statusVar = StringVar()
statusVar.set("Scores")

# Buttons - Play Area
XOValue = StringVar()
XOValue.set("")
frame0 = Frame(root, bg="white", relief=RIDGE, )
frame0.pack(side=TOP)
l = Label(frame0, text=f"{player1}", font="Times 14 bold italic", fg="red")
l.pack(side=LEFT, padx=10)
l = Label(frame0, text=f"Tic Tac Toe", font="Times 14 bold italic")
l.pack(side=LEFT)
l = Label(frame0, text=f"{player2}", font="Times 14 bold italic", fg="blue")
l.pack(side=LEFT, padx=10)

frame1 = Frame(root, bg="white", relief=RIDGE, )
frame1.pack(side=TOP)
frame2 = Frame(root, bg="white", relief=RIDGE, )
frame2.pack(side=TOP)
frame3 = Frame(root, bg="white", relief=RIDGE, )
frame3.pack(side=TOP)

for i in range(0, 9):
    if 0 <= i < 3:
        button[i] = Button(frame1, width=9, height=5, text=f"{i}", bg="light grey", fg="light grey", padx=10,
                           font="Times 10 bold italic")
        button[i].pack(side=LEFT, padx=5, pady=10)
        button[i].bind("<Button-1>", pressed)
    if 3 <= i < 6:
        button[i] = Button(frame2, width=9, height=5, text=f"{i}", bg="light grey", fg="light grey", padx=10,
                           font="Times 10 bold italic")
        button[i].pack(side=LEFT, padx=5, pady=10)
        button[i].bind("<Button-1>", pressed)
    if 6 <= i < 9:
        button[i] = Button(frame3, width=9, height=5, text=f"{i}", bg="light grey", fg="light grey", padx=10,
                           font="Times 10 bold italic")
        button[i].pack(side=LEFT, padx=5, pady=10)
        button[i].bind("<Button-1>", pressed)

root.mainloop()
