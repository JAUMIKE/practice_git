import tkinter as tk
import tkinter.messagebox as tkmessagebox
import tkinter.font as tkfont

def cal():
    tkmessagebox.showinfo(title='計算',message='計算方塊')
def view():
    num_y = int(input('請輸入數字y:'))
    num_x = int(input('請輸入數字x:'))
    tkmessagebox.showinfo(title='檢視',message='檢視計算結果為%d'%(num_x+num_y))
def about():
    tkmessagebox.showinfo(title='關於我們',message='程式設計者:自己')
def exit():
    if(tkmessagebox.askquestion(title='告知',message='是否關閉?')== 'yes'):
        win.destroy()
def hello():
    tkmessagebox.showinfo(title='訊息告知',message='Hello World!!')
def main():
    global win  
    win = tk.Tk()
    win.geometry('400x300')
    win.title('試題與測驗分析程式')
    default_font = tkfont.nametofont('TkDefaultFont')
    default_font.config(size=15)
    menubar = tk.Menu(win) 
    win.config(menu=menubar)
    menu_file = tk.Menu(menubar,tearoff=0)
    menu_cal = tk.Menu(menubar,tearoff=0)
    menu_help = tk.Menu(menubar,tearoff=0)
    menu_another = tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label='檔案',menu=menu_file)
    menubar.add_cascade(label='計算',menu=menu_cal)
    menubar.add_cascade(label='Help',menu=menu_help)
    menubar.add_cascade(label='其他',menu=menu_another)
    menu_file.add_command(label='結束',command=exit)
    menu_cal.add_command(label='計算',command=cal)
    menu_cal.add_command(label='檢視',command=view)
    menu_help.add_command(label='關於',command=about)
    menu_another.add_command(label='打招呼',command=hello)
    win.mainloop()
main()    
