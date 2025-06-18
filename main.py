import random
from tkinter import *
from tkinter import messagebox as mb


def passgen(passlength, symbol_sets=[]):
    '''
    функция генерирует пароль указанной длины,
    как хаотичную смесь символов
    '''
    password, i, sym_set_num = '', 0, 0
    random.shuffle(symbol_sets)  # перемешиваем хаотично элементы списка с множествами символов
    while i < passlength:
        sym_set_actual = symbol_sets[sym_set_num]
        password += sym_set_actual[random.randint(0,
                                                  len(sym_set_actual) - 1)]  # случайно выбираем символ из текущего множества и приписываем к паролю справа
        i += 1
        sym_set_num = (sym_set_num + 1) % (len(symbol_sets))
    return password


def writePassgen():
    outputField['state'] = "normal"
    outputField.delete(0, END)
    chekbox_list = [enabled1.get(), enabled2.get(), enabled3.get(), enabled4.get()]
    while '' in chekbox_list:
        chekbox_list.remove('')
    if not chekbox_list:
        mb.showerror(title="Внимание!", message="Ни один набор символов не выбран.")
        return
    outputField.insert(INSERT, passgen(int(inputField.get()), chekbox_list))
    outputField['state'] = "disabled"
    window.clipboard_clear()  # Очистить буфер обмена
    window.clipboard_append(outputField.get())  # Занести сгенеренный пароль в буфер обмена
    label4.config(text="Пароль скопирован в буфер обмена.")


window = Tk()
window.geometry('300x250')
window.title("Генератор паролей")

label1 = Label(window, text="Длина пароля:", font="Arial 11 bold")
label1.place(x=5, y=10)

inputField = Spinbox(window, from_=1, to=20, width=5)
inputField.place(x=130, y=15)

label2 = Label(window, text="Наборы символов:", font="Arial 11 bold")
label2.place(x=5, y=50)

label4 = Label(window, text="", font="Arial 9 normal italic")
label4.place(x=5, y=210)

enabled1 = StringVar()
enabled2 = StringVar()
enabled3 = StringVar()
enabled4 = StringVar()
inputChk1 = Checkbutton(window, text='Цифры', onvalue='0123456789', offvalue='', variable=enabled1)
inputChk1.place(x=20, y=70)
inputChk1.select()
inputChk2 = Checkbutton(window, text='Латиница, нижний регист', onvalue='abcdefghijklmnopqrstuvwxyz', offvalue='',
                        variable=enabled2)
inputChk2.place(x=20, y=90)
inputChk2.select()
inputChk3 = Checkbutton(window, text='Латиница, верхний регист', onvalue='ABCDEFGHIJKLMNOPQRSTUVWXYZ', offvalue='',
                        variable=enabled3)
inputChk3.place(x=20, y=110)
inputChk3.select()
inputChk4 = Checkbutton(window, text='Спецсимволы', onvalue='!@#$%&?', offvalue='', variable=enabled4)
inputChk4.place(x=20, y=130)

label3 = Label(window, text="Новый пароль:", font="Arial 11 bold")
label3.place(x=5, y=160)

outputField = Entry(window, width=30)
outputField.place(x=5, y=180)

btn1 = Button(window, text="Сгенерировать", command=writePassgen, font="Arial 9 bold")
btn1.place(x=200, y=180)

window.mainloop()
