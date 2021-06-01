import socket
import pickle
import time


def main():

    ADDRESS = '127.0.0.1'
    PORT = 5555

    server = socket.socket()
    server.bind((ADDRESS,PORT))

    echoServerAddr = ('127.0.0.1', 5557)
    palendromeServerAddr = ('127.0.0.1', 5544)
    lengthServerAddr = ('127.0.0.1', 5559)



    server.listen(10)

    
    while (True):
        
        cli, addr = server.accept()
        print("Client accepted on address : ", addr)
    

        user = cli.recv(1024)
        data = pickle.loads(user)

        if data[0] == "echo":
            echo = socket.socket()
            echo.connect(echoServerAddr)
            data = pickle.dumps(data[1])
            echo.send(data)

            #recive Data Now
            data = echo.recv(1024)
            echo.close()

            #Now send it to the Client
            cli.send(data)
            cli.close()



        elif data[0] == "palendrome":
            pal = socket.socket()
            pal.connect(palendromeServerAddr)
            data = pickle.dumps(data[1])
            pal.send(data)
            time.sleep(1)

                #recive Data Now
            data = pal.recv(1024)
            pal.close()

                #Now send it to the Client
            cli.send(data)
            cli.close()
    
        elif data[0] == "length":
            len = socket.socket()
            len.connect(lengthServerAddr)
            data = pickle.dumps(data[1])
            len.send(data)

                #recive Data Now
            data = len.recv(1024)
            len.close()

            #Now send it to the Client
            cli.send(data)
            cli.close()
    
    
    

main()