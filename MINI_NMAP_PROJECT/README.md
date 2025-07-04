# 🛰️ Python Network Tools – Mini Projects by Chitransh-AFK

This repo contains **three essential Python scripts** for learning real-world **network scanning**, **ping sweeping**, and **port discovery**. These tools are inspired by concepts behind **Nmap**, and offer a great start for ethical hacking or cybersecurity exploration.

---

## 📦 Project Summary

### ✅ 1. **LAN Device Discovery (Ping Sweep)**

> Find all active devices in your Wi-Fi network

**File:** `ping_sweep.py`

**How it works:**
- Automatically gets your local IP (e.g., `192.168.31.166`)
- Extracts the **network part** (e.g., `192.168.31`)
- Pings all IPs from `.1` to `.254`
- Uses `ThreadPoolExecutor` for **multithreaded** performance

**Key Functions Used:**
- `socket.gethostname()` & `socket.gethostbyname()` – get local IP
- `os.system("ping ...")` – to ping each IP
- `platform.system()` – to detect OS and switch ping flags (`-n` for Windows, `-c` for Linux)
- `ThreadPoolExecutor` – ping all IPs in parallel for speed

---

### ✅ 2. **Multithreaded Port Scanner**

> Scan ports 1–1024 of a target IP using 500 threads

**File:** `port_scanner_threaded.py`

**How it works:**
- Takes a target IP from user
- Scans TCP ports in the range 1–1024
- Uses `connect_ex()` to detect open ports
- Uses `socket.getservbyport()` to identify common services like HTTP, SSH, FTP
- Multithreaded using `threading.Thread` + `ThreadPoolExecutor` for speed

**Key Concepts:**
- `socket.connect_ex()` → returns `0` if port is open
- `settimeout(0.5)` → avoids waiting forever on unresponsive ports
- `join()` → ensures all threads finish before program ends

---

### ✅ 3. **Basic Port Scanner (Single-threaded)**

**File:** `port_scanner_basic.py`

> Simple loop-based scanner using sockets

**How it works:**
- Loops through each port from 1 to 1024
- Connects using `connect_ex()`
- Slower, but a great intro to socket usage

---

## 🌐 Networking Basics You Used

| Concept | Explanation |
|--------|-------------|
| **IP Address** | Unique identifier of a device in the network (e.g., `192.168.31.166`) |
| **Network Part** | First 3 parts of IP (e.g., `192.168.31`) – identifies the subnet |
| **Host Part** | Last part (e.g., `166`) – identifies the device |
| **Ping (ICMP)** | Used to check if a device is online (host alive or not) |
| **Port** | Logical endpoints for communication (e.g., 80 = HTTP, 22 = SSH) |
| **TCP** | Reliable protocol used for most scanning |
| **Threading** | Used to scan multiple ports or devices at the same time |
| **Timeouts** | Prevent scripts from hanging on slow targets |

---

## 📚 Python Modules Used

| Module | Purpose |
|--------|--------|
| `socket` | Network communication (IP/port scanning) |
| `os` | Run system commands (`ping`) |
| `platform` | Detect OS type for ping parameter |
| `threading` | Manually control threads |
| `concurrent.futures.ThreadPoolExecutor` | High-performance threading for parallel tasks |

---

## 🧠 Skills You’ve Practiced

- ✅ TCP port scanning using raw sockets  
- ✅ Cross-platform pinging  
- ✅ IP breakdown and subnet awareness  
- ✅ Multi-threading for speed  
- ✅ Real-world debugging of timeouts and unreachable hosts  

---

## 🛠️ Project Status

> 🚧 **This project is still in development.**

Coming Soon:
- 🕵️‍♂️ **Stealth scanning (SYN scans)**
- 🏷️ **Banner grabbing** to detect running services
- 🌍 **Geo IP lookup** for public IP identification

Stay tuned for more updates from **Chitransh_AFK**!
