import tkinter, pathlib, tkinter.filedialog
root = tkinter.Tk()
path1 = pathlib.Path("..\\Documents")
root.withdraw()
fType = [("","")]
fd = tkinter.filedialog.askopenfilenames(filetype = fType, initialdir = path1)

print(fd, type(fd))

