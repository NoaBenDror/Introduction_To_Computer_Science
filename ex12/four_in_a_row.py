from ex12.gui import Gui
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("4 IN A ROW")
    root.resizable(0, 0)
    my_gui = Gui(root)
    root.mainloop()