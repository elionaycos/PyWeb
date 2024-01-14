from source.helper.module import *


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.header = bytes(
            "HTTP/1.0 200 OK\nContent-Type: text/html; charset=UTF-8\nConnection: close\r\n\n\r", "UTF-8")

    def create(self):
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.bind((self.ip, int(self.port)))
            self.sock.listen(10)
            self.accept()
        except Exception as error:
            print(f"Error ao Criar Servidor: {str(error)}")        

    def accept(self):
        print("Esperando Cliente!")
        self.cleint, self.addr = self.sock.accept()
        print(f"Cliente Conectado: {self.addr[0]}")

    def desconnect(self):
        self.cleint.close()
        self.accept()

    def recv(self):
        self.data = self.cleint.recvfrom(1024)  # 1kb
        print(self.data)

    def send(self, data):
        response = self.header+bytes(data, "UTF-8")
        self.cleint.sendall(response)
        self.desconnect()
