#   This is a UI test!
#   Never used tkinter before.
#   Here goes nothin.

from tkinter import Tk, BOTH, RIGHT, LEFT
from tkinter.ttk import Frame, Button, Style

class Example(Frame):   #   The class which uses the Frame method
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):   #   Initializes UI as called in constructor above.
                        #   This is where all the stuff gets defined and drawn initially.

        self.master.title("Simple")
        self.pack(fill=BOTH, expand=1)

        self.style = Style()    #   Adds a "theme" to the widgets
        self.style.theme_use("default")

        quitButton = Button(self, text="Quit",
        #   Instance of Button widget, child of the Frame container we made up there ^
            command=self.quit)
        quitButton.pack(side = RIGHT, padx=5, pady=5)

        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)

    
    def centerWindow(self): #   Allows you to center the window based on the size of the screen.
        w = 290
        h = 150

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2

        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main(): #   The "main" function
    root = Tk()
    root.geometry("250x150+300+300")
    ex = Example()
    root.mainloop() #   Handles all input and stuff once the window's all set up and passes info to the widgets.


if __name__ == '__main__':
    main()