# client

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address=("127.0.0.1",1234)
sock.connect(ip_address)
try:
    s=sock.sendall("Hello,server".encode("utf-8"))
    print(sock.recv(1024).decode("utf-8"))
    while True:
        data=sock.recv(1024).decode("utf-8")
        if data == "exit":
            break
        else:
            print("you have a massage : \n")
            print("{}".format(data))
            sock.sendall(input().encode("utf-8"))
finally:
    sock.close()


