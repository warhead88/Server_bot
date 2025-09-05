import socket, time, paramiko

def wait_for_boot(ip, port=22, timeout=300, delay_after_ssh=0):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection((ip, port), timeout=5) as sock:
                sock.settimeout(5)
                banner = sock.recv(1024).decode(errors="ignore").strip()
                if banner.startswith("SSH-2.0"):
                    time.sleep(delay_after_ssh)
                    return True
        except Exception:
            time.sleep(5)
    return False
