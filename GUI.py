from tkinter import *
import tkinter as tk
from model import *


master = Tk()
master.geometry('650x800')
bias = 0
epochs = 1
learning_rate = 0
mse = 0.1

def GUI():
    #creat_select_label(epochs,learning_rate)
    def select(xtext_box,ytext_box):
        e = Entry(master)
        e.place(x=xtext_box, y=ytext_box,width=200,height=30)
        e.focus_set()

    #_____if select bias______
    def print_selection():
        global bias
        if (var1.get() == 1):
            bias = 1
        elif (var1.get() == 0):
            bias = 0

    #_____select two class______
    def check_class():
        i = 0
        if (class_1.get() == 1): i = i + 1
        if (class_2.get() == 1): i = i + 1
        if (class_3.get() == 1): i = i + 1
        if (i >= 2):
            if (class_1.get() != 1): c_1.config(state='disabled')
            if (class_2.get() != 1): c_2.config(state='disabled')
            if (class_3.get() != 1): c_3.config(state='disabled')
        else:
            c_1.config(state='normal')
            c_2.config(state='normal')
            c_3.config(state='normal')


    # _____select two feature
    def check_feature():
        i = 0
        if (feature1.get() == 1): i = i + 1
        if (feature2.get() == 1): i = i + 1
        if (feature3.get() == 1): i = i + 1
        if (feature4.get() == 1): i = i + 1
        if (feature5.get() == 1): i = i + 1
        if (i >= 2):
            if (feature1.get() != 1): f1.config(state='disabled')
            if (feature2.get() != 1): f2.config(state='disabled')
            if (feature3.get() != 1): f3.config(state='disabled')
            if (feature4.get() != 1): f4.config(state='disabled')
            if (feature5.get() != 1): f5.config(state='disabled')
        else:
            f1.config(state='normal')
            f2.config(state='normal')
            f3.config(state='normal')
            f4.config(state='normal')
            f5.config(state='normal')

    def call_model():
        global learning_rate, epochs , mse
        learning_rate = float(learning_r.get())
        epochs        = int(epoch_l.get())
        mse           = float(mse_th.get())
        my_text, tn, fp, fn, tp,k1,k2 = input_user(check_class, check_feature, learning_rate, epochs, bias , mse)
        ############ result ################
        my_string_var.set(('Accuracy = ', my_text))
        m1.set(('TN = ', tn))
        m2.set(('FP = ', fp))
        m3.set(('FN = ', fn))
        m4.set(('TP = ', tp))



    # select class
    w = Label(master, text='Choose two classes', font="100")
    w.pack(anchor=tk.W, padx=10, pady=5)
    class_1 = IntVar()
    c_1 = Checkbutton(master, text="Adelie   ",variable=class_1,onvalue=1,offvalue=0,height=2,width=8,command=check_class)
    c_1.pack(anchor=tk.W)
    class_2 = IntVar()
    c_2 = Checkbutton(master, text="Gentoo   ",variable=class_2,onvalue=1,offvalue=0,height=2,width=9,command=check_class)
    c_2.pack(anchor=tk.W)
    class_3 = IntVar()
    c_3 = Checkbutton(master, text="Chinstrap",variable=class_3,onvalue=1,offvalue=0,height=2,width=10,command=check_class)
    c_3.pack(anchor=tk.W)
    check_class =[class_1 , class_2 , class_3]
    feat=check_class


    # select features
    w = Label(master, text='Choose two features', font="100")
    w.pack(anchor=tk.W, padx=10, pady=5)
    feature1= IntVar()
    f1 = Checkbutton(master, text="bill_length_mm    ",variable=feature1,onvalue=1,offvalue=0,height=2,width=15,command=check_feature)
    f1.pack(anchor=tk.W)
    feature2 = IntVar()
    f2 = Checkbutton(master, text="bill_depth_mm     ",variable=feature2,onvalue=1,offvalue=0,height=2,width=15,command=check_feature)
    f2.pack(anchor=tk.W)
    feature3 = IntVar()
    f3 = Checkbutton(master, text="flipper_length_mm ",variable=feature3,onvalue=1,offvalue=0,height=2,width=16,command=check_feature)
    f3.pack(anchor=tk.W)
    feature4 = IntVar()
    f4 = Checkbutton(master, text="gender            ",variable=feature4,onvalue=1,offvalue=0,height=2,width=12,command=check_feature)
    f4.pack(anchor=tk.W)
    feature5 = IntVar()
    f5 = Checkbutton(master, text="body_mass_g       ",variable=feature5,onvalue=1,offvalue=0,height=2,width=15,command=check_feature)
    f5.pack(anchor=tk.W)
    check_feature=[feature1 , feature2 , feature3 ,feature4,feature5]


    #----ladels learning rate-----
    l = tk.Label(master,text='Enter learning rate',font=100)
    l.pack(anchor=tk.W, padx=10, pady=8)
    learning_r = tk.StringVar()
    v = tk.Entry(master, textvariable=learning_r).place(x=240, y=400,width=200,height=30)


    #----ladels epochs-----
    l = tk.Label(master, text='Enter number of epochs',font=100)
    l.pack(anchor=tk.W, padx=10, pady=10)
    epoch_l = tk.StringVar()
    e = tk.Entry(master, textvariable=epoch_l).place(x=240, y=450,width=200,height=30)

    # ----ladels MSE-----
    l = tk.Label(master, text='Enter number of MSE ', font=100)
    l.pack(anchor=tk.W, padx=10, pady=10)
    mse_th = tk.StringVar()
    e = tk.Entry(master, textvariable=mse_th).place(x=240, y=500, width=200, height=30)


    #----ladels bias -----
    l = tk.Label(master, text='Do you want to add bias?',font=50)
    l.pack(anchor=tk.W, padx=10, pady=10)

    #____CheckBox_Bias____
    var1 = tk.IntVar()
    c1 = tk.Checkbutton(master, text='Bias',variable=var1, onvalue=1, offvalue=0,font=50 , command=print_selection).place(x=240,y=550)

    #_____Button submit______
    b = Button(master, text="Submit", width=22, height=1 ,font="20" , command= call_model )
    b.pack(anchor=tk.W, padx=10, pady=10)

    #_____________output_____________
    my_string_var = tk.StringVar()
    l = tk.Label(master, textvariable=my_string_var, font=40)
    l.pack(anchor=tk.W, padx=10, pady=10)

    m1 = tk.StringVar()
    m2 = StringVar()
    m3 = StringVar()
    m4 = StringVar()

    l = tk.Label(master, textvariable=m1, font=40)
    l.pack(anchor=tk.W, padx=10, pady=10)

    l = tk.Label(master, textvariable=m2, font=40).place(x=150, y=708)

    l = tk.Label(master, textvariable=m3, font=40)
    l.pack(anchor=tk.W, padx=10, pady=10)

    l = tk.Label(master, textvariable=m4, font=40).place(x=150, y=755)

    master.mainloop()







