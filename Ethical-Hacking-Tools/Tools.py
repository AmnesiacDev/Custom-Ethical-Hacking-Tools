import socket
import termcolor


class Tools:
    def __init__(self):
        self.open_ports = []

    def __scan_ip(self, ipaddress, port):
        port = int(port)
        for i in range(0,port):
            try:
                sk = socket.socket()
                sk.connect((ipaddress, i))
                self.open_ports.append(i)
                sk.close()
            except:
                pass

    def scan(self, *ipaddress, port=1000):
        for i in ipaddress:
            self.__scan_ip(i, port)

            tags = f"\nPort {10 * ''} Service"
            while len(self.open_ports) > 0:
                print(tags)
                tags = "\r"
                print(f"{self.open_ports.pop(0)} {10 * ''} null")