# -*- coding: utf-8 -*-
""" IS 210 final project, music player, luis hernandez """

from Tkinter import *
import tkFileDialog
import mp3play
import Tkinter as tk
import tkMessageBox


"""basic music player that will only reproduce one song per time """
""" this show the mp3 player box interface size and if its resizable or not, also color"""
root = Tk()
root.title("IS210, music player")
root.wm_minsize(width=330, height=140)
root.resizable(0, 0)
w = "white"

"""this is the information for the instructions read me first button"""


class clickmeinfo:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.myLabel = tk.Label(top, text='\n- This player will only play mp3 files. '
                                          '-\nPrior play any file make sure you have all audio codecs needed.'
                                          '-\nOtherwise you will get the error: '
                                          '\n"The specified device is not open or is not recognized by MCI."')
        self.myLabel.pack()


def clickme():
    inputDialog = clickmeinfo(root)
    root.wait_window(inputDialog.top)


"""this is the information size and color for the button read me first"""
infobutton = tk.Button(root, text='Read me first', width=20, height=1, fg="black", command=clickme, cursor="hand1")
infobutton.pack()
infobutton.place(x=160, y=144)

""" this is the function that will search the file, only mp3 files"""


def searchfile():
    try:
        file = tkFileDialog.askopenfilename(filetypes=(("Songs", "*.mp3"),))
        if file:
            return file
    except IOError:
        tkinter.messagebox.showerror('Error, please click on the read me first button on the main player')


""" this is the main class music player"""


class MusicPlayer:
    def __init__(self):
        self.Play = [None]


musicplayer = MusicPlayer()

""" this is the function that will open the selected file on the previous func search file"""


def open():
    filelocation = searchfile()
    if filelocation is not None:
        myaudio = mp3play.AudioClip(filelocation)
        musicplayer.Play[0] = myaudio
        """ the following play() will allow the player to start playing automatically"""
        myaudio.play()
        textplay = "Play: " + filelocation.split("/")[-1] + " " * 22
        textmusic = Label(root, text=textplay, fg="white").place(x=10, y=40)


nowplaying = Label(root, text=" Now Playing: : ", fg="blue")
nowplaying.place(x=10, y=20)

"""stop button function"""


def stop():
    if musicplayer.Play[0] is not None:
        musicplayer.Play[0].stop()


"""play button function"""


def playbutton():
    try:
        if musicplayer.Play[0] is not None:
            musicplayer.Play[0].play()
    except IOError:
        tkinter.messagebox.showerror('Error, please click on the read me first button on the main player')


"""pause button function"""


def pause():
    if musicplayer.Play[0] is not None:
        if musicplayer.Play[0].isplaying():
            musicplayer.Play[0].pause()
        elif musicplayer.Play[0].ispaused():
            musicplayer.Play[0].unpause()


"""Class for the volume controls, buttons"""


class Volume:
    def __init__(self):
        self.Vol = 20

    def update(self):
        if musicplayer.Play[0] is not None:
            musicplayer.Play[0].volume(self.Vol)

    def decrease(self):
        if self.Vol >= 0:
            self.Vol -= 8
            self.update()

    def increase(self):
        if self.Vol < 99:
            self.Vol += 10
            self.update()


vol = Volume()

""" this is where all the button used on the functions will get size, color configurations, and given functions names"""
button1 = Button(root, text="▲", width=6, height=4, fg=w, command=open, cursor="hand2")
button1.place(x=4, y=70)
button2 = Button(root, text="►", width=6, height=4, fg=w, command=playbutton, cursor="hand2")
button2.place(x=78, y=70)
button3 = Button(root, text="Vol +", width=6, height=1, fg=w, command=vol.increase, cursor="hand2")
button3.place(x=250, y=15)
button4 = Button(root, text="Vol - ", width=6, height=1, fg=w, command=vol.decrease, cursor="hand2")
button4.place(x=250, y=50)
button5 = Button(root, text="▐▐ ", width=6, height=1, fg=w, command=pause, cursor="hand2")
button5.place(x=175, y=94)
button6 = Button(root, text="██", width=6, height=1, fg=w, command=stop, cursor="hand2")
button6.place(x=250, y=94)
Myname = Label(root, text="by Luis Hernandez", fg="black")
Myname.place(x=20, y=170)

root.tk_setPalette("gray")
root.mainloop()
