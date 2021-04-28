from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Image")
# canvas = Canvas(root, width =700 ,height = 700)  
# canvas.pack()
img_names=["baby_yoda.webp","green.png","image-3.jpg","random.jpg"]
img_list=[]
for name in img_names:
    img=ImageTk.PhotoImage(Image.open("./images/"+name))
    img_list.append(img)

my_label=Label(image=img_list[0])
my_label.grid(row=0,columnspan=3)
status=Label(root,text="Current: 1/"+str(len(img_list)),relief=SUNKEN,anchor=E)


def forward(last_index):
    global my_label
    global left
    global right
    my_label.grid_forget()
    my_label=Label(image=img_list[last_index])
    my_label.grid(row=0,columnspan=3)
    right=Button(root,text=">>",command=lambda:forward(last_index+1))
    left=Button(root,text="<<",command=lambda:back(last_index-1))
    status=Label(root,text="Current: "+str(last_index+1)+"/"+str(len(img_list)),relief=SUNKEN,anchor=E)
    if (last_index== len(img_list)-1):
        right = Button(root,text=">>",state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    left.grid(row=1, column=0)
    right.grid(row=1, column=2)
    status.grid(row=2,sticky=W+E,columnspan=3)

def back(last_index):
    global my_label
    global left
    global right
    my_label.grid_forget()
    my_label=Label(image=img_list[last_index])
    my_label.grid(row=0,columnspan=3)
    right=Button(root,text=">>",command=lambda:forward(last_index+1))
    left=Button(root,text="<<",command=lambda:back(last_index-1))
    status=Label(root,text="Current: "+str(last_index+1)+"/"+str(len(img_list)),relief=SUNKEN,anchor=E)
    if (last_index== 0):
        left = Button(root,text="<<",state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    left.grid(row=1, column=0)
    right.grid(row=1, column=2)
    status.grid(row=2,sticky=W+E,columnspan=3)


left=Button(root,text="<<",command=back,state=DISABLED)
exit_button=Button(root,text="EXIT",command=root.quit)
right=Button(root,text=">>",command=lambda:forward(1))
exit_button.grid(row=1,column=1)
left.grid(row=1,column=0)
right.grid(row=1,column=2)
status.grid(row=2,sticky=W+E,columnspan=3)
root.mainloop()
