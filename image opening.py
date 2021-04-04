from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
root=Tk()
root.title('open image')
def open():
    root_filetype=filedialog.askopenfilename(initialdir='/image-opening-file/images',title='select a file',filetypes=(('png files','*.png'),('all files','*.*')))
    global myimage
    mylabel=Label(root,text=root_filetype).pack()
    myimage=ImageTk.PhotoImage(Image.open(root_filetype))
    myimagelabel=Label(root,image=myimage).pack()
mybutton=Button(root,text='open file',command=open).pack()
mainloop()