from tkinter import StringVar, Tk, filedialog, ttk
"""
root = Tk()
root.title("tkinter win")
root.mainloop()

"""
root = Tk()
root.withdraw()
Idir = "C:\\Users\\田島\\documents"
Type = [("","")]
root.filename =  filedialog.asksaveasfilename(initialdir = Idir,title = "Save as",filetypes =  Type)


"""
root = tkinter.Tk()
print(dir(tkinter.Tk()))
"""