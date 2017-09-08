from tkinter import *

root = Tk()
root.geometry('800x800')
root.title('Создание выпуклой оболочки')

canv = Canvas(bg='#00E39F')
canv.pack(fill=BOTH, expand=1)
canv.pack()

t = []
myconst = 0

def rotate(A, B, C):  # скалярное произведение
    return (B[0] - A[0]) * (C[1] - B[1]) - (B[1] - A[1]) * (C[0] - B[0])


def jarvismarch(A):  # алгоритм Джарвиса
    n = len(A)
    minPoint = A[0][0]
    k = 0
    P = A
    for i in range(1, n):
        if A[i][0] < minPoint:
            minPoint = A[i][0]
            k = i
    leftPoint = A[k]
    P.remove(P[k])
    H = [leftPoint]
    P.append(leftPoint)
    while True:
        right = 0
        for i in range(1, len(P)):
            if rotate(H[-1], P[right], P[i]) < 0:
                right = i
        if P[right] == H[0]:
            break
        else:
            H.append(A[right])
            P.remove(P[right])
    return H

def click(event):
    global myconst, t
    if myconst > 0:
        t = []
        myconst = 0
        canv.delete("all")
    x = event.x
    y = event.y
    canv.create_oval([x + 5, y + 5], [x - 5, y - 5], activefill="green", activeoutline="yellow", outline="red",
                     fill="pink")
    t.append([x, y])

def myfunc(event):
    global t
    global myconst
    try:
        w = jarvismarch(t)
        for i in range(len(w)):
            canv.create_oval([w[i][0] + 5, w[i][1] + 5], [w[i][0] - 5, w[i][1] - 5], activefill="red", activeoutline="yellow", outline="red",
                             fill="yellow")

        canv.create_line(w[0:len(w)], fill='blue')
        canv.create_line(w[len(w)-1], w[0], fill='blue')
        myconst += 1
        t = []
    except:
        canv.delete("all")

w = Label(canv, text="Приветствую тебя в моей программе!\n Расставляй точки мышкой, для построения\n оболочки нажми Enter на клавиатуре :)", font=("Helvetica", 26), fg="orange", bg='#00E39F')

w.pack()
root.bind('<1>', click)
root.bind('<Return>', myfunc)


mainloop()
