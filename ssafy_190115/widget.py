from tkinter import *
import webbrowser

def browser():
    webbrowser.open("http://www.daum.net")

root = Tk()

root.title("Hello")
root.geometry("640x400+550+250")

# Label(어떤 tkinter 윈도우/프로그램에 넣을지, text="넣고싶은 텍스트")
lbl1 = Label(root, text="Hello", fg="red", bg="yellow")
lbl1.pack()

lbl2 = Label(root, text="My widget")
lbl2.pack()
 
txt = Entry(root)
txt.pack()
 
btn = Button(root, text="OK", command = browser)
btn.pack()

root.mainloop()