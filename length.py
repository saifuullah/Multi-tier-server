import socket
import pickle 


ADDRESS = '127.0.0.1'
PORT = 5559

server = socket.socket()
server.bind((ADDRESS,PORT))


while(True):
    print("Listening......")
    server.listen(10)

    cli, addr = server.accept()
    print("Client connected : " + str(addr))

    data = cli.recv(1024)
    data = pickle.loads(data)

    leng = 0
    for i in range(len(data)):
        leng += 1
    
    data = pickle.dumps(leng)
    cli.send(data)
    cli.close()

