import tkinter
import socket, threading

win = tkinter.Tk()  # 创建主窗口
win.title('UDP SOCKET SERVER')
win.geometry("600x400")
users = {}


def run(ck, ca):
    while True:
        userName = ck.recv(1024)
        dataStr = userName.decode("utf-8")
        infoList = dataStr.split(":")
        if infoList[0] == 'yiqisun' and infoList[1] == '12345678':
            #users[userName.decode("utf-8")] = ck  # 解码并储存用户的信息
            printStr = "" + infoList[0] + "已连接\n"  # 在连接显示框中显示是否连接成功
            text.insert(tkinter.INSERT, printStr)
            break

    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode("utf-8")
        printStr = "" + infoList[0] + ">" + dataStr
        text.insert(tkinter.INSERT, printStr)

def start():
    ipStr = eip.get()
    portStr = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, int(portStr)))
    server.listen(10)
    printStr = "Success！\n"
    text.insert(tkinter.INSERT, printStr)
    while True:
        ck, ca = server.accept()
        t = threading.Thread(target=run, args=(ck, ca))

        t.start()


def startSever():
    s = threading.Thread(target=start)
    s.start()

tkinter.Label(win, text = 'UDP SOCKET', font = ('Segoe UI Black', 20)).place(x=300, y=30, anchor = 'n')
tkinter.Label(win, text = "IP Address", font = ('MV Boli', 10)).place(x=50, y=80)
eip = tkinter.StringVar()
entryIp = tkinter.Entry(win, textvariable=eip, font =('MV Boli', 10)).place(x = 120, y=80)
tkinter.Label(win, text = "Port", font = ('MV Boli', 10)).place(x=320, y=80)
eport = tkinter.StringVar()
entryPort = tkinter.Entry(win, textvariable=eport, font =('MV Boli', 10)).place(x=360, y=80)

button = tkinter.Button(win, text="Start", font =('Impact', 13),command=startSever).place(x=300,y=120)
text = tkinter.Text(win, height=10, width=50)
labeltext = tkinter.Label(win, text='Message').place(x=50, y=180)
text.place(x=120, y=180)
win.mainloop()