import socket 
import threading

Host='127.0.0.1'
port=12345

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((Host,port))

#function to revice data from server
def receive():
    while True:
        try:
            message=client.recv(1024).decode('utf-8')
            if message=='USERNAME':
                username=input("Enter Your USERNAME: ")
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("Connection to server lost.")
            client.close()
            break
#function to send mssg to server
def send():
    while True:
        try:
            message=input('MESSAGE: ')
            client.send(message.encode('utf-8'))
        except:
            print("Error Sending Message")
            client.close()
            break

#starts both reciving and outgoing threads
receive_thread=threading.Thread(target=receive)
receive_thread.start()

send_thread=threading.Thread(target=send)
send_thread.start()