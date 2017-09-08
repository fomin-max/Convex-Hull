from tkinter import *

root = Tk()
root.geometry('600x600')

canv = Canvas(bg='gray')
canv.pack(fill=BOTH, expand=1)
t = []

def click(event):
    global prev_x, prev_y  # изменения в этих переменных будут сохранены и после окончания работы функции
    x = event.x
    y = event.y
    r = 50
    canv.create_oval([x + 5, y + 5], [x - 5, y - 5], activefill="green", activeoutline="yellow", outline="red",
                     fill="pink")
    if prev_x:  # если в переменной prev_x есть значение (не None)
        canv.create_line(x, y, prev_x, prev_y, width=3, fill="blue")
    # запомнить координаты этого щелчка как "предыдущие" для следующего
    prev_x = x
    prev_y = y
    t.append([x, y])
    print(t)


# до первого щелчка никаких "предыдущих" нет
prev_x = None
prev_y = None
# lbl = Label(root, width = 180)
# lbl.configure(text = "Hello")
# lbl.pack()
# ent = Entry(root)
# ent.pack()
# ent.bind('<Return>',caption)
canv.bind('<1>', click)

mainloop()
