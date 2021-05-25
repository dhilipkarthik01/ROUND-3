from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import os, shutil
import PIL.Image


class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Welcome to codechef")
        self.geometry('900x900')
        self.labelFrame = tk.LabelFrame(self,bg='#0ff0fc')
        #self.labelFrame.grid(column=0,row=1,padx= 20, pady= 20)
        fontStyle = tkFont.Font(family="Lucida Grande", size=12)
        self.btton()
        self.labelFrame.place(anchor="nw",x=50,y=50,width=800, height=550)
        self.configure(bg='black')
        self.label = tk.Label(self.labelFrame, text="",font=fontStyle,bg='#0ff0fc',fg='#fe01b1')
        self.label.grid(column =1,row = 2)
        pholder="\"Not all treasure is silver and gold, mate.\"\n   - Jack Sparrow"
        self.label.configure(text =pholder)

    def btton(self):
        self.button = tk.Button(self.labelFrame, text="Upload",height=2,width=10,command=self.fileDailog,bg="#21fc0d",fg='#033500')
        self.button.grid(column=1,row=1)
        self.button.grid(padx=375,pady=70)
    def fileDailog(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("png","*.png"),("jpeg","*.jpg")))
        #self.label = tk.Label(self.labelFrame, text="",bg='#0ff0fc',fg='#ff003f')
        #self.label.grid(column =1,row = 2)
        img = self.fileName
        image = PIL.Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())
        while (True):
                pixels = [value for value in imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3] +
                                        imgdata.__next__()[:3]]

                binstr = ''

                for i in pixels[:8]:
                    if (i % 2 == 0):
                        binstr += '0'
                    else:
                        binstr += '1'

                data += chr(int(binstr, 2))
                if (pixels[-1] % 2 != 0):
                        print(data)
                        self.label.configure(text = data)
                        #self.label.configure(text = x[0:10]+"\n"+x[10:20]+"\n"+x[20:30]+"\n"+x[30:40]+"\n"+x[40:50]+"\n")
                        break

if __name__ == '__main__':
    root = Root()
    root.mainloop()
