import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=708
        height=539
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_815=tk.Button(root)
        GButton_815["anchor"] = "center"
        GButton_815["bg"] = "#f0f0f0"
        GButton_815["cursor"] = "fleur"
        ft = tkFont.Font(family='Times',size=10)
        GButton_815["font"] = ft
        GButton_815["fg"] = "#000000"
        GButton_815["justify"] = "center"
        GButton_815["text"] = "Button"
        GButton_815.place(x=230,y=440,width=258,height=52)
        GButton_815["command"] = self.GButton_815_command

    def GButton_815_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
