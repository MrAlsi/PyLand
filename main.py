import tkinter as tk

# SET WINDOWS CONFIG
window = tk.Tk()
window.geometry("1000x1000")
window.title("PYLAND")
window.resizable(False, False)
window.configure(background="black")


container = tk.Frame(self)
container.pack()

frames = {}
current_frame = None
