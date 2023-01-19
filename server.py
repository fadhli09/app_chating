#app chating by
#M.Fadhli Ma'arif_21.83.0699
#Yoki Irawan_21.83.0665
#Dwi andika_21.83.0686
import socket
from threading import Thread
listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

def kirim_pesan(handlerSocket : socket.socket):
    while True:
        message = input()
        handlerSocket.send(message.encode())
        print("server : {}".format(message))

def terima_pesan(handlerSocket : socket.socket):
    while True:
        message = handlerSocket.recv(1024)
        print("client : {}".format(message.decode('utf-8')))

listenerSocket.bind((serverIP,serverPort)) 
listenerSocket.listen(0)
print("server menunggu koneksi dari client")
handler, addr = listenerSocket.accept()
print("sebuah client terkoneksi dengan alamat:{}".format(addr))

t1 = Thread(target=kirim_pesan,args=(handler,))
t2 = Thread(target=terima_pesan,args=(handler,))

t1.start()
t2.start()

t1.join()
t2.join()