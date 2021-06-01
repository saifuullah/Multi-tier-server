import socket
import pickle 


ADDRESS = '127.0.0.1'
PORT = 5557

server = socket.socket()
server.bind((ADDRESS,PORT))


while(True):
    print("Listening......")
    server.listen(10)

    cli, addr = server.accept()
    print("Client connected : " + str(addr))

    data = cli.recv(1024)
    
    cli.send(data)
    cli.close()

