import socket
import pickle
import time


ADDRESS = '127.0.0.1'
PORT = 5555

cli = socket.socket()
cli.connect((ADDRESS,PORT))

print("Connected with the server on IP : ", str(ADDRESS) + " PORT " + str(PORT) )

n=0

while(n==0):
    n+=1
    print("\n1. FOR ECHO MSG")
    print("2. FOR PALENDROME SERVICE")
    print("3. FOR LENGTH ")

    choice = int(input("Choice :  ") )

    if choice == 1:
        dataList = []
        msg = input("Enter your message  : ")

        flag = "echo"
        dataList.append(flag)
        dataList.append(msg)
        print("Sending data to the server.....")
        
        buff = pickle.dumps(dataList)
        cli.send(buff)
        
        print("Data has been successfully sent to the server...")
        time.sleep(1)
        messg = cli.recv(1024)
        decodeMsg = pickle.loads(messg)
        print(decodeMsg)
        print("\n \n")

        
    elif choice == 2:
        s = input("Enter your String : ")
        dataList = []
        flag = "palendrome"
        dataList.append(flag)
        dataList.append(s)

        buff = pickle.dumps(dataList)
        cli.send(buff)
        print("Data has been successfully sent to the server...Please wait for results")
        time.sleep(1)
        messg = cli.recv(1024)
        decodeMsg = pickle.loads(messg)
        print(decodeMsg)

    elif choice == 3:
        print("\nLength ......")
        uname = input("Enter the String : ")
        dataList = []
        flag = "length"
        dataList.append(flag)
        dataList.append(uname)
        buff = pickle.dumps(dataList)
        cli.send(buff)
        print("\nPlease wait.....")
        time.sleep(2)
        messg = cli.recv(1024)
        decodeMsg = pickle.loads(messg)
        print(decodeMsg)



    elif choice == 4:
        flag = "display"
        dataList = []
        dataList.append(flag)
        buff = pickle.dumps(dataList)
        cli.send(buff)
        print("Fetching users data from DATABASE......")
        time.sleep(2)
        user = cli.recv(1024)
        data = pickle.loads(user)

        for user in data:
            print("Name : " + user[1] + "\n" + "Pass : " + user[2] + "\n" + "Access R1 : " + user[3] + "\n" + "Access R2 : " + user[4] + "\n" + "Access R3 : " + user[5])
            print("\n")
