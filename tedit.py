import sys

# Determine Python version
v = sys.version

if "2.7" in v:
    from Tkinter import *
    import tkFileDialog as filedialog
elif "3.3" in v or "3.4" in v or v.startswith("3."):  # covers any 3.x version
    from tkinter import *
    from tkinter import filedialog

# GUI Setup
root = Tk()
root.title("Tedit")

text = Text(root)
text.grid()

def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt")
    if savelocation:
        with open(savelocation, "w", encoding="utf-8") as file1:
            file1.write(t)

button = Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    text.config(font="Helvetica")

def FontCourier():
    text.config(font="Courier")

font = Menubutton(root, text="Font")
font.grid()

font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

helvetica = IntVar()
courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)

root.mainloop()
