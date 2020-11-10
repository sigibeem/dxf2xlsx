# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("",".txt")]
iDir = os.path.abspath(os.path.dirname(__file__))
print(__file__)
#tkinter.messagebox.showinfo('プログラム','処理ファイルを選択してください！')
fd = tkinter.filedialog.askopenfilename(filetype = fTyp, initialdir = iDir)

# 処理ファイル名の出力
#tkinter.messagebox.showinfo('○×プログラム',file)

