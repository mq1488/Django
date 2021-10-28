import tkinter as tk
import firstWindow


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.geometry("400x400")
    firstWindow.onStart(root)
    root.mainloop()
