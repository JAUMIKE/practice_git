import tkinter as tk
win = tk.Tk()
win.geometry('300x200')
win.title('測試畫面')
pLabel1 = tk.Label(win,text = '計算過程', fg='green',bg='silver',font = ('新細明體',12),padx=20,pady=10)
pLabel1.pack()
win.mainloop()