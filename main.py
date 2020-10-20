from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Denting Player')
root.geometry("800x500")

# initialize Pygame Mixer
pygame.mixer.init()
bgColor = "#999999"
fgColor = "#FF3333"

# Add Song Function
def addSong():
    song = filedialog.askopenfilename(initialdir='H:/DOWNLOAD/Music/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    
    # Strip out The Directory Info and .mp3 Extension from the Source
    song = song.replace("H:/DOWNLOAD/Music/", "")
    song = song.replace(".mp3", "")
    
    # Add song to listbox
    songBox.insert(END, song)
    # print(song)

def play():
    song = songBox.get(ACTIVE)
    song = F'H:/DOWNLOAD/Music/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    songBox.selection_clear(ACTIVE)

# Create Playlist Box
songBox = Listbox(root, bg=bgColor, fg="black", width=100, height=20, selectforeground="#00FFFF")
songBox.pack(pady=20)

# Define Player Control Button Image
backBtnImg = PhotoImage(file='assets/previous.png')
stopBtnImg = PhotoImage(file='assets/stop.png')
pauseBtnImg = PhotoImage(file='assets/pause.png')
playBtnImg = PhotoImage(file='assets/play.png')
nextBtnImg = PhotoImage(file='assets/next.png')

# Create Player Control Frame
controlsFrame = Frame(root)
controlsFrame.pack()

# Create Player Control Button
backBtn = Button(controlsFrame, image=backBtnImg, borderwidth=0)
stopBtn = Button(controlsFrame, image=stopBtnImg, borderwidth=0, command=stop)
pauseBtn = Button(controlsFrame, image=pauseBtnImg, borderwidth=0)
playBtn = Button(controlsFrame, image=playBtnImg, borderwidth=0, command=play)
nextBtn = Button(controlsFrame, image=nextBtnImg, borderwidth=0)

backBtn.grid(row=0, column=0, padx=10)
stopBtn.grid(row=0, column=1, padx=10)
pauseBtn.grid(row=0, column=2, padx=10)
playBtn.grid(row=0, column=3, padx=10)
nextBtn.grid(row=0, column=4, padx=10)

# Create Menu
myMenu = Menu(root)
root.config(menu=myMenu)

# Add Song Menu
addSongMenu = Menu(myMenu)
myMenu.add_cascade(label="Add Songs", menu=addSongMenu)
addSongMenu.add_command(label="Add One Song to Playlist", command=addSong)

root.mainloop()