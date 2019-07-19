from tkinter import *

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.FtoCButton = tkinter.Button(self.main_window, text='Convert F to C', command=self.FtoC)
        self.quit_button = tkinter.Button(self.main_window,text='Quit', command=self.main_window.destory)

        self.FtoCButton.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def FtoC(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')

my_gui = MyGUI()
