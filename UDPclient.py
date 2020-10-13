import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("UDP SOCKET CLIENT")
win.geometry("1000x750")

ck = None#用于储存客户端的信息


def getInfo():
    while True:
        data = ck.recv(1024)#用于接受服务其发送的信息
        text.insert(tkinter.INSERT, data.decode("utf-8"))


def connectServer():
    global ck

    ipStr = eip.get()
    portStr = eport.get()
    userStr = var_username.get()
    pwStr = var_password.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipStr, int(portStr)))
    #2:bind()的参数是一个元组的形式
    loginStr = userStr + ":" + pwStr
    client.send(loginStr.encode("utf-8"))
    ck = client



def sendMail():
    #friend = efriend.get()
    sendStr = esend.get()
    #sendStr = friend + ":" + sendStr
    ck.send(sendStr.encode("utf-8"))
    userStr = var_username.get()
    printStr = "" + userStr + "> " +sendStr
    text.insert(tkinter.INSERT, printStr)


tkinter.Label(win, text = 'UDP SOCKET', font = ('Segoe UI Black', 25)).place(x=500, y=50, anchor = 'n')
tkinter.Label(win, text = 'UserName', font = ('MV Boli', 15)).place(x=50, y=130)
tkinter.Label(win, text = 'Password', font = ('MV Boli', 15)).place(x=50, y=180)
var_username = tkinter.StringVar()
entry_username = tkinter.Entry(win, textvariable = var_username, font =('MV Boli', 15))
entry_username.place(x=200, y=130)
var_password = tkinter.StringVar()
entry_password = tkinter.Entry(win, show = '*', textvariable = var_password, font =('MV Boli', 15))
entry_password.place(x=200, y=180)

tkinter.Label(win, text = "IP Address", font = ('MV Boli', 15)).place(x=500, y=130)
eip = tkinter.StringVar()
entryIp = tkinter.Entry(win, textvariable=eip, font =('MV Boli', 15)).place(x = 650, y=130)
tkinter.Label(win, text = "Port", font = ('MV Boli', 15)).place(x=500, y=180)
eport = tkinter.StringVar()
entryPort = tkinter.Entry(win, textvariable=eport, font =('MV Boli', 15)).place(x=650, y=180)
#euser = tkinter.Variable()
#entryUser = tkinter.Entry(win, textvariable=euser).grid(row=0, column=1)

#labelIp = tkinter.Label(win, text="ip").grid(row=1, column=0)
#eip = tkinter.Variable()
#entryIp = tkinter.Entry(win, textvariable=eip).grid(row=1, column=1)

#labelPort = tkinter.Label(win, text="port").grid(row=2, column=0)
#eport = tkinter.Variable()

#entryPort = tkinter.Entry(win, textvariable=eport).grid(row=2, column=1)

button = tkinter.Button(win, text="Login", font = ('Impact',20),command=connectServer).place(x=480, y=250)
text = tkinter.Text(win, height=20, width=120)
labeltext= tkinter.Label(win, text="Message", font = ('Impact',20)).place(x=100, y=300)
text.place(x=90, y=350)

esend = tkinter.Variable()
#labelesend = tkinter.Label(win, text="发送的消息").grid(row=5, column=0)
entrySend = tkinter.Entry(win, textvariable=esend, font=('Arial',20),width=50).place(x=90,y=620)

#efriend = tkinter.Variable()
#labelefriend= tkinter.Label(win, text="SendTo",font=('Impact',15)).place(x=90,y=620)
#entryFriend = tkinter.Entry(win, textvariable=efriend,font=('Arial',20)).place(x=150,y=620)

button2 = tkinter.Button(win, text="Send", font=('Impact',15),command=sendMail).place(x=850,y=620)
win.mainloop()