import socket 
import time
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input("Enter the Server IP Adderres: ")
client.connect((ip,12345))

print("Connect established .....")
time.sleep(1)
print("Reciving Data...")


filename=client.recv(1024).decode()
print(f"File Name is : {filename}")
time.sleep(5)
client.send(b"ok")
print("Transfering file ......")

with open("received_" + filename, "wb") as f:

    while True:
        chunk = client.recv(1024)

        if not chunk:
            break

        f.write(chunk)

print(f"Received total: {len("received_" + filename)} bytes")


print(f'File is stored as photo2.jpeg')


client.close()
