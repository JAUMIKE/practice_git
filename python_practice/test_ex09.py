import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

def combox_select(event):
    select_area = event.widget.get()
    lab_result.config(text=select_area)
win = tk.Tk() 
win.geometry('400x300')
win.title('分析程式主題')
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS = (('屏東縣',0),('台南市',1),('高雄市',2),('台東縣',3))
area = tk.StringVar()
combox = ttk.Combobox(win,value=AREA_OPTIONS,textvariable=area,font=default_font)
combox.bind('<<ComboboxSelected>>',combox_select)
combox.current(2)
combox.pack(padx=20,pady=10)
lab_result = tk.Label(win,font=default_font,fg='blue',width=18)
lab_result.pack(padx=10,pady=(5,10))
win.mainloop()