import socket #importing the module

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
UDP_IP='0.0.0.0' #listen on all interfacees
UDP_PORT=12345 #Any port above 1024

server.bind((UDP_IP,UDP_PORT))#binding socket to address
print(f"UDP server listening on {UDP_PORT}....")

while True:
    data,addr=server.recvfrom(1024)#Recv the byte and store the data and ip and port of the client
    print(f"Recived message from {addr}: {data.decode()}")
