from tkinter import *
from tkinter import filedialog
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as message_box
import urllib.request
import json
 

"""
Окно для открытия файла
Возвращает имя файла, который должен быть открыт
"""
def open(): 
    try:
        url = tkSimpleDialog.askstring("", "Enter a url:")
        data = urllib.request.urlopen(url)
    except:
        message_box.showerror(title="Error", message="Wrong url")
    else:
        data = data.read().decode('utf-8')
        text_box.delete('1.0', 'end')           # Удаление старого напечатанного
        text_box.insert('1.0', data)            # Вставка нового текста файла


"""
Проверка json файла на ошибки
"""
def is_JSON(data):
    try:
        json.loads(data)    # Попытка переобразования строки в формате JSON в объект Python. Если нельзя - выдаёт ошибку
    except ValueError as e:
        return False
    return True


"""
Проверка синтаксиса json файла
"""
def check():
    if is_JSON(text_box.get(1.0, END)):
        message_box.showinfo(title="Syntax checker", message="All good")
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax")


"""
Сохранение файла
"""
def save():
    if is_JSON(text_box.get(1.0, END)):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".json", filetypes=[("json files", '*.json')])
        file_save = str(text_box.get(1.0, END))
        file.write(file_save)
    else:
        message_box.showerror(title="Syntax checker", message="Invalid syntax")


window = Tk()
window.title("Редактор JSON")
window.geometry('700x700')

text_box = Text(wrap=WORD)                             # Создание техтового блока
text_box.pack(side='left', fill='both', expand=True)   # Размещаем и убираем отступы, размещаем посередине

# Добавление панели меню
menu = Menu(window)  
new_item = Menu(menu)  

menu.add_cascade(label='File', menu=new_item)
new_item.add_command(label='Open URL', command=open)
new_item.add_command(label='Check', command=check)
new_item.add_command(label='Save', command=save)

window.config(menu=menu) 
scroll = Scrollbar(window)                          # Создание полосы прокрутки
scroll.pack(side=LEFT, fill=Y)
text_box.config(yscrollcommand=scroll.set)
window.mainloop()