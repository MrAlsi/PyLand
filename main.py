import tkinter as tk

window = tk.Tk()
window.geometry("700x700")
window.title("PYLAND")
window.resizable(False, False)
window.configure(background="black")

question_label = tk.Label(window, text="Cosa vuoi essere in questo mondo?")
ElfButton = tk.Button(text="Elfo")
question_label.pack()
ElfButton.pack()



#Run window
if __name__ == "__main__":
    window.mainloop()
