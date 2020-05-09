# 6 Feet Adventure by AfreAustin and SkyKnuckles 
# Created for Hacklarios 09-10/5/2020
# Adventure Game set during the pandemic

from tkinter import *
import os
from sys import exit

def main():
    root = Tk()
    root.geometry("800x600")
    
    app = Window(root)
    app.configure(bg = '#beb5b5')
    
    root.mainloop()

# GUI
class Window(Frame):

    # main window / master widget
    def __init__(self, master = None):              # master = None is default
        Frame.__init__(self, master)

        self.master = master
        
        self.pack()
        self.init_window()
        self.init_labels()
        self.init_events()
        self.init_invent()
        
    # window frame
    def init_window(self):

        self.master.title("6 Feet Adventure")
        self.pack(fill = BOTH, expand = 1)

       # Menu Bar
        dropdown = Menu(self.master)
        self.master.config(menu = dropdown)

       # File Menu
        file = Menu(dropdown)
        file.add_command(label   = "Exit",
                         command = self.master.destroy)
        dropdown.add_cascade(label = 'File', menu = file)

    # window labels
    def init_labels(self):
        
        # Title
        title = Label(self, bg = 'white',
                      text = "6 Feet Adventure",
                      relief = RAISED)
        title.config( font = ('CopperplateGothicLight', '25', 'bold') )
        title.place(relx = 0.30, rely = 0.01)

        # Exit Button
        exitButton = Button(self, bg = '#f44040', fg = 'black',
                            text = " EXIT ", 
                            command = self.master.destroy )
        exitButton.place(relx = 0.90, rely = 0.015)

        # Credits
        credits = Label(self, bg = '#beb5b5',
                        text = ("_" * 153) + "\n created by AfreAustin and SkyKnuckes")
        credits.place(relx = 0.015, rely = 0.90)

    # events window
    def init_events(self):

        events = Label(self, bg = 'white',
                       text = "EVENTS",
                       height = 30, width = 70)
        events.place(relx = 0.05, rely = 0.10)
    
    # inventory window
    def init_invent(self):

        item1, item2 = 1, 2;

        InventL = Label(self, bg = 'yellow',
                        text = " Shopping List  " + "\n\n" +
                                "\n" + str(item1) + 
                                "\n" + str(item2),
                        height = 15, width = 30)
        InventL.place(relx = 0.70, rely = 0.10)


main()