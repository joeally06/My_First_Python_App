from dearpygui.core import *
from dearpygui.simple import *
import playsound
import random

PASSWORD = "Joshua"
games = ["Falken's Maze", "Back Jack", "Checkers", "Chess",
         "Poker", "Global Thermonuclear War"]

def recursively_show(container):
    for item in get_item_children(container):
        if get_item_children(item):
            show_item(item)
            recursively_show(item)
        else:
            show_item(item)


def check_password(sender, data):
    input_value = get_value("User Input")
    print(input_value)
    if input_value != PASSWORD:
        add_text("Incorrect", before="Login")

    else:
        add_text("Access Granted", before="Login")
        playsound.playsound("Greetings.mp3")
        delete_item("W.O.P.R")
        recursively_show('Main Window')


def banter(sender, data):
    playsound.playsound('howareyou.mp3')
    # print('Hello, how are you doing today?')
    input('Response: ')
    playsound.playsound('deletion.mp3')
    input('Response: ')
    playsound.playsound('yes.mp3')
    playsound.playsound('shallwe.mp3')


# setting main window settings
set_main_window_size(600, 677)
set_global_font_scale(1.25)
set_theme("Black")
set_style_window_padding(40, 40)
set_main_window_resizable(True)
set_main_window_title("WarGames")

# Start main window
with window("W.O.P.R", width=587, height=677):
    print("W.O.P.R is running....")
    set_window_pos("W.O.P.R", 0, 0)
    set_primary_window("W.O.P.R", True)

    # Adds image to window
    add_drawing("logo", width=510, height=290)
    draw_image("logo", 'wopr.jpg', [0], [520, 290])
    add_separator()
    add_spacing(count=12)

    # Instructions
    add_text("Please enter your password.")
    color = ([232, 163, 33])
    add_spacing(count=12)

    # User Input
    add_input_text("User Input", width=100, )
    add_spacing(count=12)
    add_button("Login", callback=check_password)

with window("Main Window"):
    with menu_bar('menu bar'):
        with menu('menu 1'):
            add_menu_item('menu item')
        with menu('menu 2'):
            add_menu_item('menu item 2')

    add_text('Congrats!, you may now use the app')
    add_button('Button 1')
    hide_item('Main Window', children_only=True)

start_dearpygui(primary_window="Main Window")
