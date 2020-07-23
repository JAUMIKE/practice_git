def checkpw():
    pmsg.set('輸入密碼:'+ppw.get())
import tkinter as tk
win = tk.Tk()
win.geometry('400x300')
win.title('分析程式')
ppw = tk.StringVar()
pmsg = tk.StringVar()
pLabel = tk.Label(win,fg='blue',text='請輸入密碼:')
pLabel.pack()
pEntry = tk.Entry(win,textvariable=ppw,state='normal') 
pEntry.pack()
pButton = tk.Button(win,text='登入',command=checkpw)
pButton.pack()
pLabmsg = tk.Label(win,textvariable=pmsg)
pLabmsg.pack()
win.mainloop() 

