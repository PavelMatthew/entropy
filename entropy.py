# coding=windows-1251

from math import log2
from tkinter import *
import time


root = Tk()
root.resizable(False, False)
root.title("Энтропия")
root.geometry("777x777")


t0=Label(root,text="Из файла")
t0.pack()
entry = Entry(root)
entry.pack()

t1=Label(root,text="ТУТ БУДЕТ ЭНТРОПИЯ")
t1.pack()

t2=Label(root,text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")
t2.pack()

t01=Label(root,text="Ввести вручную текст")
t01.pack()
entry2 = Text(root)
entry2.pack()

t3=Label(root,text="ТУТ БУДЕТ ЭНТРОПИЯ")
t3.pack()

t4=Label(root,text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")
t4.pack()


def cnt_entropy1():

    t1.config(text="ТУТ БУДЕТ ЭНТРОПИЯ")
    t2.config(text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")

    start = time.time()
    try:

        filename=entry.get()

        with open(filename,encoding='utf-8') as file:    #открываем через менеджер контекста, filename определим позже

            text = file.read()  #считываем содержимое только для UTF-8 кодировки
            text1="".join([z for d in ' '.join(a for a in text.split()) for x in d for z in x if z.isalnum() or z ==' ']).replace("  ", " ")#убираем ненужные символы

            text1 = text1.lower()    #убираем верхний регистр
            words = text1.split()    #создаем в список, где каждый элемент — слово

        nonrep_words = list()
        for word in words:
                if word in nonrep_words:    #проверка, "есть ли данный элемент уже в списке?"
                 pass    #если есть, то ничего не делаем
                else:
                    nonrep_words.append(word)    #если нет, то добавляем
        H=0 #ЗНАЧЕНИЕ ЭНТРОПИИ


        for word in nonrep_words:
            p=words.count(word)/len(words)
            i=p*log2(p)
            print(word,p,i)
            H+=i
        H=(-1)*H
        t1.config(text="H="+str(H)+" Words="+str(len(words)))
        print(H)
        end = time.time()
        t2.config(text=str(end-start))


    except IOError:

        t1.config(text="Нет такого файла")

button = Button(root,text ="Вычислить энтропию ИЗ ФАЙЛА", command = cnt_entropy1)
button.pack()

def cnt_entropy2():

    t3.config(text="ТУТ БУДЕТ ЭНТРОПИЯ")
    t4.config(text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")

    start2 = time.time()


    enterText= entry2.get(1.0, "end-1c")  #считываем содержимое
    text1="".join([z for d in ' '.join(a for a in enterText.split()) for x in d for z in x if z.isalnum() or z ==' ']).replace("  ", " ")#убираем ненужные символы

    text1 = text1.lower()    #убираем верхний регистр
    words = text1.split()    #создаем в список, где каждый элемент — слово

    nonrep_words = list()
    for word in words:
        if word in nonrep_words:    #проверка, "есть ли данный элемент уже в списке?"
            pass    #если есть, то ничего не делаем
        else:
                    nonrep_words.append(word)    #если нет, то добавляем
    H1=0 #ЗНАЧЕНИЕ ЭНТРОПИИ


    for word in nonrep_words:
        p=words.count(word)/len(words)
        i=p*log2(p)
        print(word,p,i)
        H1+=i
        
    H1=(-1)*H1

    t3.config(text="H="+str(H1)+" Words="+str(len(words)))
    print(H1)
    end2 = time.time()
    t4.config(text=str(end2-start2))

button2 = Button(root,text ="Вычислить энтропию ВВОД ВРУЧНУЮ", command = cnt_entropy2)
button2.pack()





root.mainloop()