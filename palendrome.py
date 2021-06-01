import socket
import pickle 


ADDRESS = '127.0.0.1'
PORT = 5544

server = socket.socket()
server.bind((ADDRESS,PORT))


def isPalindrome(s):
	return s == s[::-1]


while(True):
    print("Listening......")
    server.listen(10)

    cli, addr = server.accept()
    print("Client connected : " + str(addr))

    data = cli.recv(1024)
    data = pickle.loads(data)

    msg = "0"

    if isPalindrome(data):
        msg = "Yes it is Palendrome"
    else:
        msg = "No it is not palendrome"

    data = pickle.dumps(msg)
    cli.send(data)
    cli.close()

