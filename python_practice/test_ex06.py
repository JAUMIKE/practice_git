import tkinter as tk
win = tk.Tk()
win.geometry('400x300')
win.title('分割測試')
text1 = tk.StringVar(value='GUI1')
ent1 = tk.Entry(win,textvariable=text1,width=15,justify=tk.CENTER)
ent1.grid(row=0,column=0,padx=5,pady=15)
text2 = tk.StringVar(value='GUI2')
ent2 = tk.Entry(win,textvariable=text2,width=15,justify=tk.CENTER)
ent2.grid(row=1,column=0,padx=5,pady=15,sticky=tk.N)
text3 = tk.StringVar(value='GUI3')
ent3 = tk.Entry(win,textvariable=text3,width=15,justify=tk.CENTER)
ent3.grid(row=2,column=0,padx=5,pady=15)
win.mainloop()
