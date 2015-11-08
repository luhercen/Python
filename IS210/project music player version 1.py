# -*- coding: utf-8 -*-


from Tkinter import *
import tkFileDialog
import mp3play

"""basic music player that will only reproduce one song per time """

window = Tk()
window.wm_minsize(width=450,height=100)
window.resizable(0,0)
w = "white"
def SearchFile():
    File = tkFileDialog.askopenfilename(filetypes = (("Songs", "*.mp3"),))
    if File:
        return File

class MusicPlayer:
    def __init__(self):
        self.Play = [None]
        
musicplayer = MusicPlayer()

def Open():
    filelocation = SearchFile()
    if filelocation != None:
        myAudio = mp3play.AudioClip(filelocation)
        musicplayer.Play[0] = myAudio
        textplay = "Play: "+filelocation.split("/")[-1]+" "*30
        TextMusic = Label(window,text=textplay,fg="white").place(x=10,y=270)

def stop():
    if musicplayer.Play[0] != None:
        musicplayer.Play[0].stop()
        
def playbutton():
    if musicplayer.Play[0] != None:
        musicplayer.Play[0].play()
def pause():
    if musicplayer.Play[0] != None:
        if musicplayer.Play[0].isplaying():
            musicplayer.Play[0].pause()
        elif musicplayer.Play[0].ispaused():
            musicplayer.Play[0].unpause()
class Volume:
    def __init__(self):
        self.Vol = 20
    def update(self):
        if musicplayer.Play[0] != None:
            musicplayer.Play[0].volume(self.Vol)
    def decrease(self):
        if self.Vol >= 0:
            self.Vol -= 2
            self.update()
    def increase(self):
        if self.Vol < 99:
            self.Vol += 2
            self.update()
            
vol = Volume()
button1 = Button(window,text="▲",width=6,height=4,fg=w,command=Open,cursor="hand2")
button1.place(x=4,y=4)
button2 = Button(window,text="██",width=6,height=4,fg=w,command=stop,cursor="hand2")
button2.place(x=78,y=4)
button3 = Button(window,text="Vol +",width=6,height=4,fg=w,command=vol.increase,cursor="hand2")
button3.place(x=152,y=4)
button4 = Button(window,text="Vol - ",width=6,height=4,fg=w,command=vol.decrease,cursor="hand2")
button4.place(x=226,y=4)
button5 = Button(window,text="►",width=6,height=4,fg=w,command=playbutton,cursor="hand2")
button5.place(x=300,y=4)
button6 = Button(window,text="▐▐",width=6,height=4,fg=w,command=pause,cursor="hand2")
button6.place(x=374,y=4)
Myname = Label(window,text = "by Luis Hernandez",fg="black")
Myname.place(x=20,y=150)
window.tk_setPalette("gray")
window.title("Music Player")
window.mainloop()
