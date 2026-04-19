
---

# 📁 2. monitor.py (PASTE THIS)

```python
import socket
import sys

def check_host(target):
    print(f"\n[+] Checking target: {target}")

    try:
        host = socket.gethostbyname(target)
        print("[✓] Host is reachable")
        return host
    except:
        print("[!] Host not reachable")
        return None


def scan_ports(target):
    print("\n[+] Scanning ports...")

    ports = [21, 22, 23, 80, 443, 3306]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[!] Open port detected: {port}")

        s.close()

    print("[✓] Scan completed")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python monitor.py <target>")
        sys.exit()

    target = sys.argv[1]

    print("🛡️ Network Security Monitor Started")

    ip = check_host(target)

    if ip:
        scan_ports(ip)
