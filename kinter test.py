import tkinter as tk
import playsound

BACKDOOR = "Joshua"

window = tk.Tk()
window.title("W.O.P.R")
window.geometry("400x400")


# Functions
def on_click():
    password = str(user_password.get())
    while True:
        if password != BACKDOOR:
            return 'Access Denied'
        else:
            return playsound.playsound('Greetings.mp3')


def wrong_pass():
    access = on_click()
    access_display = tk.Text(master=window, height=10, width=30)
    access_display.grid(row=2, column=3)
    access_display.insert(tk.END, access)


# This is for users to enter their password
user_password = tk.Entry(window, width=50, border=10)
user_password.grid(row=0, column=3)

# Login in button
but1 = tk.Button(window, text="Login", command=wrong_pass(), padx=40)
but1.grid(row=1, column=3)


def banter():
    playsound.playsound('howareyou.mp3')
    # print('Hello, how are you doing today?')
    input('Response: ')
    playsound.playsound('deletion.mp3')
    input('Response: ')
    playsound.playsound('yes.mp3')
    playsound.playsound('shallwe.mp3')


window.mainloop()
