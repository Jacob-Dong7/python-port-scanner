import socket
class PortScan:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = int(port)
        return
    
    def scan(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
        s.settimeout(2)
        result = s.connect_ex((self.ip, self.port))
        if result == 0:
            print("Port is open")
        else:
            print("Port is closed")
        s.close()
        return