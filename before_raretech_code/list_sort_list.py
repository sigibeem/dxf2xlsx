import tkinter, pathlib, tkinter.filedialog
list11 = [['1\tFS-MDO\n', '1\tTK-4215\n', '1\tPN-4000A/B\n', '1\tFS-RES-811\n', '1\t50-MIK/CHPO-U4(1)\n', '1\tJP-4210\n', '1\t100-G-P(2)\n', '1\t50-HY-U4(1)\n', '1\tSV-4140\n', '1\t40-CI(R)-P(1)(C5)\n', '1\t40-CI-P(1)(C5)\n', '1\t25-MIK-U4(1)\n', '1\t25-MIK-U4(1)\n', '1\t25-MIK-U4(1)\n', '1\t20-N(840)-P(1)\n', '1\t50/15-MIK/MDO/S(170)-\n', '1\t50/15-MIK/MDO/S(170)-U4(1)/P(6)(H120)(T1)\n',]
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