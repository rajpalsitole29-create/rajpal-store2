import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Simple Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill="both", ipadx=8, pady=10)

# Buttons Frame
frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "0", "C", "=", "/"
]

i = 0
for btn in buttons:
    b = tk.Button(frame, text=btn, font="lucida 15 bold", padx=20, pady=20)
    b.grid(row=i//4, column=i%4)
    b.bind("<Button-1>", click)
    i += 1

root.mainloop()

