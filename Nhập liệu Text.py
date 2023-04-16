#Tạo cửa sổ làm việc
from tkinter import *
win = Tk()
win.title('Phan Đình Hoàng')
win.geometry('300x150')
win.attributes('-topmost', True)

#tạo ra Label
name = Label(win, text = 'Họ và Tên:', font = ('Times New Roman',12))
name.place(x = 30,y = 30)

#Tạo ra Entry nhập liệu
entry = Entry(win,width = 20, font = ('Times New Roman', 12))
entry.place(x = 105, y = 30)
entry.focus()

#Tạo ra Button
def abc():
    name1 = Label(win, text = 'Bạn đã nhập ' + entry.get(), font = ('Times New Roman',12), bg = 'green', fg = 'black')
    name1.place(x = 105,y = 90)

but = Button(win, text = 'click vào đây', width = 10, height = 1, font = ('Times New Roman', 12), command = abc)
but.place(x = 105, y = 60)

win.mainloop()