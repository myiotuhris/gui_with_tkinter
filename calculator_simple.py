from tkinter import *
root=Tk()
root.title("Basic Calculator")
#root.iconbitmap('./icon_c.ico')
e=Entry(root,width=20,borderwidth=5)
e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
# global f_num
# global operation

def num_click(num):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(num))

def clear_click():
    e.delete(0,END)

def myadd():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    global operation
    operation="+"
    e.delete(0,END)

def mysub():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    global operation
    operation="-"
    e.delete(0,END)

def mymul():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    global operation
    operation="*"
    e.delete(0,END)

def mydiv():
    first_num=e.get()
    global f_num
    f_num=int(first_num)
    global operation
    operation="/"
    e.delete(0,END)

def equal():
    second_num=e.get()
    e.delete(0,END)
    if(operation=="+"): e.insert(0,int(second_num)+f_num)
    if(operation=="-"): e.insert(0,f_num-int(second_num))
    if(operation=="*"): e.insert(0,int(second_num)*f_num)
    if(operation=="/"): e.insert(0,f_num/int(second_num))


button_1=Button(root,text="1",padx=30,command=lambda:num_click("1"))
button_2=Button(root,text="2",padx=30,command=lambda:num_click("2"))
button_3=Button(root,text="3",padx=30,command=lambda:num_click("3"))
button_4=Button(root,text="4",padx=30,command=lambda:num_click("4"))
button_5=Button(root,text="5",padx=30,command=lambda:num_click("5"))
button_6=Button(root,text="6",padx=30,command=lambda:num_click("6"))
button_7=Button(root,text="7",padx=30,command=lambda:num_click("7"))
button_8=Button(root,text="8",padx=30,command=lambda:num_click("8"))
button_9=Button(root,text="9",padx=30,command=lambda:num_click("9"))
button_0=Button(root,text="0",padx=30,command=lambda:num_click("0"))
button_add=Button(root,text="+",padx=25,command=myadd)
button_sub=Button(root,text="-",padx=32,command=mysub)
button_mul=Button(root,text="*",padx=31,command=mymul)
button_div=Button(root,text="/",padx=32,command=mydiv)
button_clear=Button(root,text="C",pady=90,command=clear_click)
button_eq=Button(root,text="=",padx=60,command=equal)

button_7.grid(row=1,column=0,columnspan=1)
button_8.grid(row=1,column=1,columnspan=1)
button_9.grid(row=1,column=2,columnspan=1)

button_4.grid(row=2,column=0,columnspan=1)
button_5.grid(row=2,column=1,columnspan=1)
button_6.grid(row=2,column=2,columnspan=1)

button_1.grid(row=3,column=0,columnspan=1)
button_2.grid(row=3,column=1,columnspan=1)
button_3.grid(row=3,column=2,columnspan=1)

button_0.grid(row=4,column=0,columnspan=1)
button_add.grid(row=1,column=3,columnspan=1)
button_sub.grid(row=2,column=3,columnspan=1)
button_mul.grid(row=3,column=3,columnspan=1)
button_div.grid(row=4,column=3,columnspan=1)
button_eq.grid(row=4,column=1,columnspan=2)
button_clear.grid(row=1,rowspan=4,column=4)

root.mainloop()
