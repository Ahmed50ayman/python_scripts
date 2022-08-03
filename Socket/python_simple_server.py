# server
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=("127.0.0.1",1234)
sock.bind(address)
sock.listen(2)
while True:
    try : 
        connection , ip_address = sock.accept()
        print("We have a new client in {:<16}".format(ip_address[0]))
        connection.sendall("Hello,clinet".encode("utf-8"))
        print(connection.recv(1024).decode("utf-8"))
        while True:
            d=input().encode("utf-8")
            if d == "exit":
                break
            else:
                print("you hava a massage : \n")
                connection.sendall(d)
                print(connection.recv(1204).decode("utf-8"))
    finally:
        connection.close()
