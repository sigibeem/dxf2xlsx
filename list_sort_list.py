import tkinter, pathlib, tkinter.filedialog
list11 = ["fii-ko-ko", "jii", "hii", "fii-jiji-ji"]
list12 = []
keywd = "-"
list12 = [ i for i in list11 if keywd in i] 

print(list12)

fTyp = [("text file","*.txt")]
path12 = pathlib.Path("C:users\\田島\\Documents")

root = tkinter.Tk()
root.withdraw()
fd = tkinter.filedialog.asksaveasfilename(initialdir = path12, title = "Save as", filetypes = fTyp)

path =  pathlib.Path(fd.replace('/', '\\'))
with open(path, "w", encoding = "utf-8") as stxt:
    stxt.writelines(list12)