import socket

class NetworkTools:

    def port_scan(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        s.close()
        return "Open" if result == 0 else "Closed"
