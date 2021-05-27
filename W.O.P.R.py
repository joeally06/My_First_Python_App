import playsound
from tkinter import Tk

BACKDOOR = "Joshua"
games= ["Falken's Maze","Back Jack","Checkers","Chess",
        "Poker","Global Thermonuclear War"]



def main():
    wopr_login()
    print('')
    banter()
    print('')
    list_game()




def wopr_login():
    user_password = (input("Login: "))
    while True:
        if user_password == BACKDOOR:
            playsound.playsound('Greetings.mp3')
            break
        else:
            print('Access Denied')
        user_password = input("Login: ")

def banter():
    playsound.playsound('howareyou.mp3')
    #print('Hello, how are you doing today?')
    input('Response: ')
    playsound.playsound('deletion.mp3')
    input('Response: ')
    playsound.playsound('yes.mp3')
    playsound.playsound('shallwe.mp3')


def list_game():
    user_request = input("Response: ")
    if user_request != "List games":
        print("That wasn't found in our database")
    else:
        print("\n".join(map(str, games)))

    while True:
        user_choice = input('Response: ')
        if user_choice in games:
            playsound.playsound('game_chess.mp3')
            break

        else:
            print("Sorry, That game is not in the list. Choose again.")

    while True:
        user_choice_two = input("Response: ")
        if user_choice_two in games:
            playsound.playsound('fine.mp3')
            break
        else:
            print("Sorry, That game is not in the list. Choose again.")
            user_choice = input('Response: ')



if __name__ == '__main__':
    main()