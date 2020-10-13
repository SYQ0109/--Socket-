import tkinter
from tkinter import *
import threading
import socket
import time

HOST = '10.89.72.7'
PORT = 8888
ADDRESS = (HOST, PORT)
BUFFER = 4096
ck = None
users = {}

def get_info():
    while True:
        data = ck.recv(BUFFER)
        print(data.decode('utf-8'))
        if data == '退出':
            ck.close()
            break
        else:
            if ':' in data.decode('utf-8'):
                print(data.decode('utf-8'))
                text.insert(tkinter.INSERT, data.decode("utf-8"))  # 显示在信息框上

def connect_server():
    global ck
    user_str = e_user.get()
    #print(user_str)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socked所准守ipv4或ipv6，和相关协议的
    #print("success\n")
    #print(ADDRESS)
    client.connect((HOST, PORT))
    #print('yeah\n')
    client.send(user_str.encode("utf-8"))
    ck = client
    t = threading.Thread(target=get_info)
    t.start()


def send_mail():
    send_str = entrySend.get(0.0, 2.0)
    text.insert(INSERT, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n' + '我:' + send_str)
    entrySend.delete('0.0', END)
    send_str = send_str
    ck.send(send_str.encode("utf-8"))


def cancel():
    entrySend.delete('0.0', END)

def exit_system():
    sys.exit(1)


def login_sever():
    connect_server()
    root.deiconify()
    win1.withdraw()

win1 = tkinter.Tk()
win1.title('TCP CLIENT')
win1.geometry('400x300')
win1.resizable(width=False, height=False)
tkinter.Label(win1, text = 'TCP SOCKET', font = ('Segoe UI Black', 25)).place(x=200, y=20, anchor = 'n')
e_user = tkinter.Variable()
labelUse = tkinter.Label(win1, text='UserName', font=('Impact', 16)).place(x=50, y=80)
entryUser = tkinter.Entry(win1, font=('Arial', 16), width=17, textvariable=e_user).place(x=160, y=80)
input_password = tkinter.Label(win1, text='Password', font=('Impact', 16)).place(x=50, y=150)
input_password_entry = tkinter.Entry(win1, show='*', font=('Arial', 16), width=17).place(x=160, y=150)
button = tkinter.Button(win1, text='Login', font=('Impact', 14), command=login_sever).place(x=150, y=200)
no_login = tkinter.Button(win1, text='Quit', font=('Impact', 14), command=exit_system).place(x=280, y=200)

root = tkinter.Tk()
root.withdraw()

root.title("聊天窗口")
root.geometry('600x400')
root.resizable(width=False, height=False)
text = tkinter.Text(root, height=20, width=59, font=("Arial", 15))
text.place(x=0, y=55)
label_text = tkinter.Label(root, text="History", font=('Impact', 14)).place(x=0, y=30)
e_send = tkinter.Variable()
label_send = tkinter.Label(root, text="Send Message", font=('Impact', 14)).place(x=0, y=230)
entrySend = tkinter.Text(root, height=5, width=51, font=('Arial', 15))
entrySend.place(x=0, y=270)
button2 = tkinter.Button(root, text="Send", width=10, command=send_mail).place(x=350, y=350)
button3 = tkinter.Button(root, text="Clear", width=10, command=cancel).place(x=450, y=350)

root.mainloop()

win1.mainloop()
