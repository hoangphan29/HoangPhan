#Tạo cửa sổ làm việc
from tkinter import *
import decimal #Thư viện Decimal tính toán chính xác hơn

win = Tk()
win.title('Phan Đình Hoàng')
win.geometry('300x200')
win.attributes('-topmost', True)

#tạo ra Label1
name1 = Label(win, text = 'Số thứ nhất:', font = ('Times New Roman',12))
name1.place(x = 30,y = 30)

#tạo ra Label2
name2 = Label(win, text = 'Số thứ hai: ', font = ('Times New Roman',12))
name2.place(x = 30,y = 60)

#Tạo ra Entry nhập liệu1
entry1 = Entry(win,width = 20, font = ('Times New Roman', 12))
entry1.place(x = 105, y = 30)
entry1.focus()

#Tạo ra Entry nhập liệu2
entry2 = Entry(win,width = 20, font = ('Times New Roman', 12))
entry2.place(x = 105, y = 60)

#Tạo ra Button
def abc():
    name1 = Label(win, text = 'Kết quả tính là: ' + str(decimal.Decimal(entry1.get()) + decimal.Decimal(entry2.get())), font = ('Times New Roman',12), bg = 'green', fg = 'black')
    name1.place(x = 105,y = 120)

but = Button(win, text = 'Cộng 2 số', width = 10, height = 1, font = ('Times New Roman', 12), command = abc)
but.place(x = 105, y = 90)

win.mainloop()