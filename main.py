from gtts import gTTS
import os



def main():
    mytext = 'Greetings Professor Falken. A strange game. The only winning move is not to play. How about a nice game of chess?'
    language = 'en'

    output = gTTS(text=mytext, lang = language , slow =True)

    output.save("ending.mp3")

    os.system("ending.mp3")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
