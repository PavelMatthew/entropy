# coding=windows-1251

from math import log2
from tkinter import *
import time
import pyperclip
from tkinter import ttk
import tkinter.messagebox as mb


root = Tk()
root.resizable(False, False)
root.title("Энтропия")
root.geometry("777x777")


t0=Label(root,text="Из файла")
t0.pack()
entry = Entry(root)
entry.pack()


t01=Label(root,text="Ввести вручную текст")
t01.pack()
entry2 = Text(root)
entry2.pack()




def cnt_entropy_from_str(str_for_entropy):



    start = time.time()

    text1="".join([z for d in ' '.join(a for a in str_for_entropy.split()) for x in d for z in x if z.isalnum() or z ==' ']).replace("  ", " ")#убираем ненужные символы

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

    num_words=len(words)
    end = time.time()
    time_of_method=end-start

    return (H,num_words,time_of_method)

def cnt_entropy_file():


    try:

        filename=entry.get()



        with open(filename,encoding="utf-8") as file:    #открываем через менеджер контекста

                text = file.read()  #считываем содержимое только для UTF-8 кодировки
                H,num_words,time_of_method=cnt_entropy_from_str(text)
                global Hf
                Hf=H
                global Wf
                Wf=num_words
                global Tf
                Tf=time_of_method
                t1.config(text="H="+str(H)+" Words="+str(num_words))
                print(str(H))

                t2.config(text=str(time_of_method))
    except IOError:
            
            mb.showwarning(title="Ошибка", message="Нет такого файла")
      

    except UnicodeDecodeError:

            mb.showwarning(title="Ошибка", message="Поменяйте кодировку на UTF-8")
        


button1 = Button(root,text ="Вычислить энтропию ИЗ ФАЙЛА", command = cnt_entropy_file)
button1.pack()

t1=Label(root,text="ТУТ БУДЕТ ЭНТРОПИЯ ИЗ ФАЙЛА")
t1.pack()

t2=Label(root,text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")
t2.pack()

def cnt_entropy_enter():


    enterText= entry2.get(1.0, "end-1c")  #считываем содержимое
    H,num_words,time_of_method=cnt_entropy_from_str(enterText)
    global He
    He=H
    global We
    We=num_words
    global Te
    Te=time_of_method
    t3.config(text="H="+str(H)+" Words="+str(num_words))
    print(str(H))

    t4.config(text=str(time_of_method))

button2 = Button(root,text ="Вычислить энтропию ВВОД ВРУЧНУЮ", command = cnt_entropy_enter)
button2.pack()

t3=Label(root,text="ТУТ БУДЕТ ЭНТРОПИЯ ВВОДА")
t3.pack()

t4=Label(root,text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")
t4.pack()

def cnt_entropy_buffer():



    enterText=pyperclip.paste()  #считываем содержимое буфера
    H,num_words,time_of_method=cnt_entropy_from_str(enterText)
    global Hb
    Hb=H
    global Wb
    Wb=num_words
    global Tb
    Tb=time_of_method
    t5.config(text="H="+str(H)+" Words="+str(num_words))
    print(str(H))

    t6.config(text=str(time_of_method))
  

button3 = Button(root,text ="Вычислить энтропию ИЗ БУФЕРА", command = cnt_entropy_buffer)
button3.pack()

t5=Label(root,text="ТУТ БУДЕТ ЭНТРОПИЯ БУФЕРА")
t5.pack()

t6=Label(root,text="ТУТ БУДЕТ ВРЕМЯ ВЫПОЛНЕНИЯ")
t6.pack()

def write_to_file_result(from_what,entropy,words_num,time):



    your_string=str(from_what) + " H="+str(entropy)+" Words="+str(words_num)+" Time_of_process="+str(time)

    with open('results.txt','a') as f:
        
        f.write(your_string + '\n')



enabled1 = IntVar()
enabled_checkbutton= ttk.Checkbutton(text="Запись из ФАЙЛА", variable=enabled1,onvalue=1, offvalue=0)
enabled_checkbutton.pack()

enabled2 = IntVar()
enabled_checkbutton= ttk.Checkbutton(text="Запись из окна ВВОДА", variable=enabled2,onvalue=1, offvalue=0)
enabled_checkbutton.pack()

enabled3 = IntVar()
enabled_checkbutton= ttk.Checkbutton(text="Запись из БУФЕРА", variable=enabled3,onvalue=1, offvalue=0)
enabled_checkbutton.pack()

def check_for_writing():

    
    if enabled1.get()==1:
        write_to_file_result("From_File",Hf,Wf,Tf)
    if enabled2.get()==1:
        write_to_file_result("From_Enter",He,We,Te)
    if enabled3.get()==1:
        write_to_file_result("From_Buffer",Hb,Wb,Tb)

button4 = Button(root,text ="Записать", command = check_for_writing)
button4.pack()


root.mainloop()