import tkinter as tk
import tkinter.font as tkfont
def redbut_click():
    select_item = area.get()
    lab_result.config(text=AREA_OPTIONS[select_item][0])
win = tk.Tk()
win.geometry('400x300')
win.title('分析程式主題')
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=15)
AREA_OPTIONS = ((' 屏東縣',0),(' 嘉義縣',1),( ' 台南市',2),(' 高雄市',3))
area = tk.IntVar()
area.set(3)
for item, value in AREA_OPTIONS:
    radbut = tk.Radiobutton(win, text=item, variable=area, value=value, command=redbut_click,font=default_font,fg='black' )
    radbut.pack()
lab_result = tk.Label(win,font=default_font,fg='black')
lab_result.pack(padx=20,pady=(5,10))
win.mainloop()

