from dearpygui.core import *
from dearpygui.simple import *
import playsound
"""I can not claim any of the pictures or movies lines as my own. Everything shown in
this app is from the movie WarGames. The only thing that is mine is how I formed the
code to make it seem like the movie. This is a cheesy first program, but it is the 
first one I have ever written myself."""

# These are my Constants
PASSWORD = "Joshua"
GAMES = ["Falken's Maze", "Back Jack", "Checkers", "Chess",
         "Poker", "Global Thermonuclear War"]

"""This function is part of the redrawing process of the next screen. I can't take credit for this.
I found this on the internet"""

def recursively_show(container):
    for item in get_item_children(container):
        if get_item_children(item):
            show_item(item)
            recursively_show(item)
        else:
            show_item(item)


"""This function checks the users password and if it is correct it will send the user over to the next screen so they 
speak with the Joshua."""

def check_password(sender, data):
    input_value = get_value("User Input")
    print(input_value)
    if input_value != PASSWORD:
        add_text("Incorrect", before="Login")
        playsound.playsound("access_denied.mp3")
    else:
        add_text("Access Granted", before="Login")
        playsound.playsound("Greetings.mp3")
        delete_item("W.O.P.R")
        recursively_show('Access Window')
        playsound.playsound("howareyou.mp3")


"""I call this function banter, because in the movie David and the Joshua exchange conversation between each other"""

def banter(sender, data):
    chatter = get_value("Reply")
    if 'fine' in chatter:
        playsound.playsound("deletion.mp3")
    elif 'mistakes' in chatter:
        playsound.playsound("yes.mp3")
        playsound.playsound("shallwe.mp3")
    else:
        if 'List' in chatter:
            hide_item("Reply")
            hide_item("Submit")
            add_listbox(name="Games", items=GAMES, num_items=6, callback=play_games, width=400, before="Reply")


"""This function is so the user can select their game. Unforutnly they only have on choice,
because all the other game are under development :)"""

def play_games(sender):
    user_choice = (GAMES[get_value(sender)])
    if user_choice == GAMES[5]:
        hide_item("logo_2")
        add_drawing("logo_3", width=510, height=290, before="logo_2")
        draw_image("logo_3", 'map.png', [0], [520, 290])
        hide_item("Games")
        add_text("Please chose your side: \n  USA  or Russia", before="Games")
        color = ([232, 163, 33])
        add_input_text("Selection", width=100, before="Games")
        add_button('Enter', callback=self_annihilation, before="Games")

    else:
        if user_choice == GAMES[0] or [1] or [2] or [3] or [4]:
            playsound.playsound("development.mp3")

"This is the last (function) move of the movie.This is where Joshua learns that there is no side that will win."

def self_annihilation():
    choice = get_value("Selection")
    if choice == "Russia":
        hide_item("logo_3")
        add_drawing("logo_4", width=510, height=290, before="logo_3")
        draw_image("logo_4", 'Joshua.png', [0], [520, 290])
        playsound.playsound("ending.mp3")
        stop_dearpygui()
    else:
        playsound.playsound("ending.mp3")
        stop_dearpygui()
#setting main window settings

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
    set_primary_window("W.O.P.R", False)

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
    add_input_text("User Input", width=100, password=True, hint="My Son")
    add_spacing(count=12)
    add_button("Login", callback=check_password)

#This is the second window after the login
with window("Access Window"):
    add_drawing("logo_2", width=510, height=290)
    draw_image("logo_2", 'wopr.jpg', [0], [520, 290])
    add_separator()
    add_spacing(count=12)
    add_input_text("Reply", multiline=True, enabled=True, width=400)
    add_button('Submit', callback=banter)
    set_primary_window("Access Window", True)
    hide_item('Access Window', children_only=True)

start_dearpygui(primary_window="Access Window")
