import socket

target=input("Enter the target IP Address: ")#target ip address
start_port=1
end_port=1024

print(f"🔍 Scanning for {target} from {start_port} to {end_port}")

#scan loop 
for port in range(start_port,end_port+1):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    result=s.connect_ex((target,port)) # if 0=open
    if result == 0:
        print(f"Port {port} is OPEN")
    
    s.close()
print("Done!")
