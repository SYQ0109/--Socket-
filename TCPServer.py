import tkinter
import socket
import threading
import time
from tkinter import *

HOST = ''
PORT = 8888
ADDRESS = (HOST, PORT)
BUFFER = 4096
ck = None
win = tkinter.Tk()
win.title('TCP SERVER')
win.geometry("400x300")
win.resizable(width=False, height=False)
users = {}


def run(ck, ca):
    user_name = ck.recv(1024)
    users[user_name.decode("utf-8")] = ck
    print_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n' + "" + user_name.decode("utf-8") + "Connected\n"
    text1.insert(tkinter.INSERT, print_str)
    for i in users:
        for j in users:
            users[i].send(j.encode("utf-8"))
    while True:
        r_data = ck.recv(BUFFER)
        data_str = r_data.decode("utf-8")
        text2.insert(tkinter.INSERT, '\n' + user_name.decode("utf-8") + ':' + data_str)

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(128)
    print_str = "SUCCESS!\n"
    text1.insert(tkinter.INSERT, print_str)
    while True:
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck, ca))
        t.start()


def start_sever():
    root.deiconify()
    win.withdraw()
    s = threading.Thread(target=start)
    s.start()


def _clear():
    entryIp.delete(0, END)

tkinter.Label(win, text = 'TCP SOCKET', font = ('Segoe UI Black', 25)).place(x=200, y=20, anchor = 'n')
labelIp = tkinter.Label(win, text='IP', font=('Impact', 18))
labelIp.place(x=100, y=100)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip, font=('Arial', 16), width=17)
entryIp.place(x=150, y=106)
labelPort = tkinter.Label(win, text='PORT', font=('Impact', 18))
labelPort.place(x=75, y=150)
e_port = tkinter.Variable()
entryPort = tkinter.Entry(win, textvariable=e_port, font=('Arial', 16), width=17)
entryPort.place(x=150, y=155)
button1 = tkinter.Button(win, text="Start", command=start_sever, font=('Impact', 14))
button1.place(x=150, y=200)
button2 = tkinter.Button(win, text="Clear", command=_clear, font=('Impact', 14))
button2.place(x=250, y=200)

root = tkinter.Tk()
root.withdraw()
root.title('TCP SERVER')
root.geometry("400x500")
root.resizable(width=False, height=False)
show_online = tkinter.Label(root, text='ONLINE', font=('Impact', 16))
show_online.place(x=0, y=10)
text1 = tkinter.Text(root, height=10, width=40, font=('Arial', 15))
text1.place(x=0, y=35)
show_mess = tkinter.Label(root, text='History', font=('Impact', 16))
show_mess.place(x=0, y=240)
text2 = tkinter.Text(root, height=10, width=40, font=('Arial', 15))
text2.place(x=0, y=270)

root.mainloop()

win.mainloop()


