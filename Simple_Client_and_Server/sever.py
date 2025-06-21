import socket#importing the socket module

#making the server socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("127.0.0.1",12345))#bind the server to listen the client on 127.0.0.1 ip and 12345 port 
server.listen(1)
print("Server is waiting for a connection...")

client_socket,client_address=server.accept()

print(f"Connected by {client_address}")

data=client_socket.recv(1024).decode()

print(f"client says: {data}")

client_socket.send("hello from sever!".encode())
print("Closing the Connection....")

client_socket.close()
server.close()
