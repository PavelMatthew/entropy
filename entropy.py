# coding=windows-1251

from math import log2
from tkinter import *
import time


root = Tk()
root.resizable(False, False)
root.title("��������")
root.geometry("777x777")


t0=Label(root,text="�� �����")
t0.pack()
entry = Entry(root)
entry.pack()

t1=Label(root,text="��� ����� ��������")
t1.pack()

t2=Label(root,text="��� ����� ����� ����������")
t2.pack()

t01=Label(root,text="������ ������� �����")
t01.pack()
entry2 = Text(root)
entry2.pack()

t3=Label(root,text="��� ����� ��������")
t3.pack()

t4=Label(root,text="��� ����� ����� ����������")
t4.pack()


def cnt_entropy1():

    t1.config(text="��� ����� ��������")
    t2.config(text="��� ����� ����� ����������")

    start = time.time()
    try:

        filename=entry.get()

        with open(filename,encoding='utf-8') as file:    #��������� ����� �������� ���������, filename ��������� �����

            text = file.read()  #��������� ���������� ������ ��� UTF-8 ���������
            text1="".join([z for d in ' '.join(a for a in text.split()) for x in d for z in x if z.isalnum() or z ==' ']).replace("  ", " ")#������� �������� �������

            text1 = text1.lower()    #������� ������� �������
            words = text1.split()    #������� � ������, ��� ������ ������� � �����

        nonrep_words = list()
        for word in words:
                if word in nonrep_words:    #��������, "���� �� ������ ������� ��� � ������?"
                 pass    #���� ����, �� ������ �� ������
                else:
                    nonrep_words.append(word)    #���� ���, �� ���������
        H=0 #�������� ��������


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

        t1.config(text="��� ������ �����")

button = Button(root,text ="��������� �������� �� �����", command = cnt_entropy1)
button.pack()

def cnt_entropy2():

    t3.config(text="��� ����� ��������")
    t4.config(text="��� ����� ����� ����������")

    start2 = time.time()


    enterText= entry2.get(1.0, "end-1c")  #��������� ����������
    text1="".join([z for d in ' '.join(a for a in enterText.split()) for x in d for z in x if z.isalnum() or z ==' ']).replace("  ", " ")#������� �������� �������

    text1 = text1.lower()    #������� ������� �������
    words = text1.split()    #������� � ������, ��� ������ ������� � �����

    nonrep_words = list()
    for word in words:
        if word in nonrep_words:    #��������, "���� �� ������ ������� ��� � ������?"
            pass    #���� ����, �� ������ �� ������
        else:
                    nonrep_words.append(word)    #���� ���, �� ���������
    H1=0 #�������� ��������


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

button2 = Button(root,text ="��������� �������� ���� �������", command = cnt_entropy2)
button2.pack()





root.mainloop()