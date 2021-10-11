from tkinter import *
import requests
tkwindow = Tk()
tkwindow.geometry("400x150")
tkwindow.title("Simple bonk checker")
e = Entry(tkwindow, width=50)
e.pack()
f = Entry(tkwindow, width=50)
f.pack()
def check():
    url = "https://bonk2.io/scripts/login_legacy.php"
    data = {"username":e.get() ,"password":f.get()}
    checker = requests.post(url,data=data)
    if "success" in checker.text:
        successlabel = Label(tkwindow, text="Valid").pack()
    elif "fail" in checker.text:
        faillabel = Label(tkwindow, text="Fail").pack()
myButtton = Button(tkwindow, text="check", command=check).pack()
tkwindow.mainloop()