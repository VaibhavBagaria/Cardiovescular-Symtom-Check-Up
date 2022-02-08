from tkinter import *
from tkinter import messagebox as messagebox
from PIL import ImageTk,Image
root=Tk()
root.title("Cardiovascular Symtom Check")
root.geometry("600x600")
root.configure(bg='red')

img=ImageTk.PhotoImage(Image.open("heart.gif"))

title=Label(root,text="Use The check list to see if you have heart problems.")
title.place(relx=0.3, rely=0.05,anchor=CENTER)

image_L=Label(root,image=img,height=140,width=140,highlightthickness=5,borderwidth=2,relief=SOLID)
image_L.place(relx=0.7,rely=0.1,anchor=CENTER)

Q1_radio1=StringVar(value="0")
Q1label=Label(root,text="Are you having the experience of shortness of breah?")
Q1label.place(relx=0.3, rely=0.3,anchor=CENTER)
Q1_R1=Radiobutton(root,text="Yes",variable=Q1_radio1,value="yes")
Q1_R1.place(relx=0.7, rely=0.3,anchor=CENTER)
Q1_R2=Radiobutton(root,text="No",variable=Q1_radio1,value="no")
Q1_R2.place(relx=0.8, rely=0.3,anchor=CENTER)

Q2_radio1=StringVar(value="0")
Q2label=Label(root,text="Do you have chest pain?")
Q2label.place(relx=0.3, rely=0.4,anchor=CENTER)
Q2_R1=Radiobutton(root,text="Yes",variable=Q2_radio1,value="yes")
Q2_R1.place(relx=0.7, rely=0.4,anchor=CENTER)
Q2_R2=Radiobutton(root,text="No",variable=Q2_radio1,value="no")
Q2_R2.place(relx=0.8, rely=0.4,anchor=CENTER)

Q3_radio1=StringVar(value="0")
Q3label=Label(root,text="Are you having the experience of Nausea?")
Q3label.place(relx=0.3, rely=0.5,anchor=CENTER)
Q3_R1=Radiobutton(root,text="Yes",variable=Q3_radio1,value="yes")
Q3_R1.place(relx=0.7, rely=0.5,anchor=CENTER)
Q3_R2=Radiobutton(root,text="No",variable=Q3_radio1,value="no")
Q3_R2.place(relx=0.8, rely=0.5,anchor=CENTER)

Q4_radio1=StringVar(value="0")
Q4label=Label(root,text="Are you feeling tired pretty quickly?")
Q4label.place(relx=0.3, rely=0.6,anchor=CENTER)
Q4_R1=Radiobutton(root,text="Yes",variable=Q4_radio1,value="yes")
Q4_R1.place(relx=0.7, rely=0.6,anchor=CENTER)
Q4_R2=Radiobutton(root,text="No",variable=Q4_radio1,value="no")
Q4_R2.place(relx=0.8, rely=0.6,anchor=CENTER)

def check():
    score=0
    if Q1_radio1.get()=="yes" :
        score=score+10
        print(score)
        
    if Q2_radio1.get()=="yes" :
        score=score+10
        print(score)
        
    if Q3_radio1.get()=="yes" :
        score=score+10
        print(score)
        
    if Q4_radio1.get()=="yes" :
        score=score+10
        print(score)
        
    if score<=10:
        messagebox.showinfo("Report","You are safe.")
        
    elif score>10 and score<=20:
        messagebox.showinfo("Report","You are lucky to not die as you have mild health problems.")
        
    elif score>20 and score<=30:
        messagebox.showinfo("Report","Hope you had a good life now go to the docter or you'll die")
        
    else:
        messagebox.showinfo("Report","How are you reading this message?")
        
button_check=Button(root,text="Give reports",command=check)
button_check.place(relx=0.5, rely=0.75,anchor=CENTER)
root.mainloop()