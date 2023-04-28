import tkinter as tk
import pyautogui

move_amount = 10

def left_click(event=None):
    pyautogui.click(button='left')

def right_click(event=None):
    pyautogui.click(button='right')

def move_up(event=None):
    pyautogui.moveRel(0, -move_amount)

def move_down(event=None):
    pyautogui.moveRel(0, move_amount)

def move_left(event=None):
    pyautogui.moveRel(-move_amount, 0)

def move_right(event=None):
    pyautogui.moveRel(move_amount, 0)

def change_move_amount():
    global move_amount
    move_amount = int(entry_move_amount.get())

def on_key(event):
    if event.keysym == "Up":
        move_up()
    elif event.keysym == "Down":
        move_down()
    elif event.keysym == "Left":
        move_left()
    elif event.keysym == "Right":
        move_right()
    elif event.keysym.lower() == "z":
        left_click()
    elif event.keysym.lower() == "x":
        right_click()

app = tk.Tk()
app.title("Mouse Controller")

# マウス移動量変更機能
label_move_amount = tk.Label(app, text="Move Amount:")
label_move_amount.grid(row=0, column=3)
entry_move_amount = tk.Entry(app)
entry_move_amount.grid(row=1, column=3)
button_move_amount = tk.Button(app, text="Change", command=change_move_amount)
button_move_amount.grid(row=2, column=3)

# クリックボタンを配置
button_left_click = tk.Button(app, text="Left Click", command=left_click)
button_left_click.grid(row=3, column=0)

button_right_click = tk.Button(app, text="Right Click", command=right_click)
button_right_click.grid(row=3, column=2)

# カーソル移動ボタンを配置
button_up = tk.Button(app, text="Up", command=move_up)
button_up.grid(row=0, column=1)

button_down = tk.Button(app, text="Down", command=move_down)
button_down.grid(row=2, column=1)

button_left = tk.Button(app, text="Left", command=move_left)
button_left.grid(row=1, column=0)

button_right = tk.Button(app, text="Right", command=move_right)
button_right.grid(row=1, column=2)

# キーボードイベントをバインド
app.bind("<Key>", on_key)

app.mainloop()
