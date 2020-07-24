import tkinter as tk
import tkinter.font as tkfont
import tkinter.messagebox as tkmessagebox

def cal_bmi():
    msg.get()
win = tk.Tk()
win.geometry('600x460')
win.title('計算BMI數值')
default_font = tkfont.nametofont('TkDefaultFont')
default_font.configure(size=18)
height = tk.IntVar()
weight = tk.IntVar()
msg = tk.IntVar()
#標籤設定
input_height_label = tk.Label(win,text='請輸入身高(m)')
input_weight_label = tk.Label(win,text='請輸入體重(kg)')
#介面輸入資料來設定身高體重
height_entry = tk.Entry(win,textvariable=height)
weight_entry = tk.Entry(win,textvariable=weight)
#設定按鈕
button_cal = tk.Button(win,text='計算',command=cal_bmi)
input_height_label.pack()
height_entry.pack(padx=20,pady=10)
input_weight_label.pack()
weight_entry.pack(padx=20,pady=10)
button_cal.pack(padx=20,pady=10)
Labmsg1 = tk.Label(win,textvariable=height)
Labmsg2 = tk.Label(win,textvariable=height)
Labmsg1.pack()
Labmsg2.pack()
win.mainloop()

