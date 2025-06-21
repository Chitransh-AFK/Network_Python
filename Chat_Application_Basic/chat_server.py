import socket 
import threading

host='127.0.0.1'
port=12345

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()#ready to accept the clients without qeueing them

clients=[] #Stores the client data
usernames=[]#stores the username of the client

#sends the message to the client connected except who sent it 
def broadcast(messg,sender):
    for client in clients:
        if client!=sender:
            try:
                client.send(messg)
#handles the error if any client disconnects of shutdown the program forcibly it will free up the server storage and remove it from clients list
            except:
                client.close()
                clients.remove(client)
                break
#recover the data from the client and handles a single client
def handle_client(client):
    while True:
        try:
            messg=client.recv(1024)
            
            index=clients.index(client)
            username=usernames[index]#clients[2] ↔ usernames[2]
            formatted=f"\n🟢{username}:{messg.decode('utf-8')}".encode('utf-8')

            broadcast(formatted,client)
        except:
            usernames.remove(username)
            clients.remove(client)
            broadcast(f"\n🔴 {username} left the chat.".encode('utf-8'), client)
            client.close()
            break
#makes a new thread for every client it connects with 
def recieve_connection():
    print('Server is ready to recieve the connection....')
    while True:
        client,addr=server.accept()

        client.send("USERNAME".encode('utf-8'))
        username=client.recv(1024).decode('utf-8')
        usernames.append(username)

        print(f"Connected with {addr}")
        clients.append(client)
        #starting a new thread for a client
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()

#Starting the server loop
recieve_connection()



