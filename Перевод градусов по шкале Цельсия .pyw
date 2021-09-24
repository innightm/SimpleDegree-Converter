# mytk1.py
# подключаем модуль, содержащий методы дл работы
# с графикой
import tkinter
# Создаём главное окно,
# в переменную window записываем ссылку на объект
window = tkinter.Tk()
window.title ('Перевод градусов')
window.geometry('300x330+300+180')
# Задаём обработчик событий для корневого окна
# Создаём объект-виджет класса Label в корневом окне window
# text - параметр для задания отображаемого текста
label = tkinter.Label (window, text = "Укажите значение в Фаренгейтах:")
# Отображает виджет с помощью менеджера pack
label.pack ()
frame = tkinter.Frame (window)
frame.pack()
var = tkinter.StringVar()
# Обновление содержимого переменной в момент ввода текста
#label = tkinter.Label (frame, textvariable=var)
#label.pack()
# Пробуем набрать текст в появившемся поле
#entry = tkinter.Entry (frame, textvariable=var)
#entry.pack()
# Контроллер: функция вызывается в момент нажатия на кнопку
def click():
    counter.set (counter.get()-32)
    counter.set (counter.get()*5/9)
counter = tkinter.IntVar()
counter.set(0)
#frame = tkinter.Frame(window)
#frame.pack()
# Создаём кнопку
button = tkinter.Button(frame, text = 'Перевести в Цельсии',
                        command=click)
button.pack()
entry = tkinter.Entry (frame, textvariable=counter)
entry.pack()
#label = tkinter.Label (frame, textvariable=counter)
#label.pack()
knopka_vihod = tkinter.Button (window, text = 'Выход', width = 10)
# Размещаем кнопки

knopka_vihod.pack ()
# Привязка к кнопке "Выход" функции Vihod
def Vihod (event):
    window.destroy()
knopka_vihod.bind ('<Button-1>', Vihod)

window.mainloop()

