def cal():
    textvar.set('Hello world')
import tkinter as tk
win = tk.Tk()
win.geometry('400x300')
win.title('測試分析程式')
ptext = tk.Text(win)
textvar = tk.StringVar()
pButton1 = tk.Button(win,textvariable = textvar, command=cal,padx = 20,pady = 10)
textvar.set('點擊按鈕')
ptext.insert(tk.INSERT, '床前明月光\n')
ptext.insert(tk.INSERT, '儀式地上霜\n')
ptext.insert(tk.INSERT, '舉頭望明月\n')
ptext.insert(tk.INSERT, '低頭思故鄉\n')
pButton1.pack()
ptext.pack()
ptext.config(state = tk.NORMAL)
win.mainloop()