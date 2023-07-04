import socketserver
import crcmod


class Handler_TCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} sent:".format(self.client_address[0]))
        print(self.data)
        # Calculate the CRC of the received message
        crc16 = crcmod.mkCrcFun(0x11021, initCrc=0, xorOut=0xFFFF)
        crc = crc16(self.data)
        ak = "ACK"
        response = ak + str(crc)
        bytesToSend = str.encode(response)
        self.request.sendall(bytesToSend)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    tcp_server = socketserver.TCPServer((HOST, PORT), Handler_TCPServer)
    tcp_server.serve_forever()
