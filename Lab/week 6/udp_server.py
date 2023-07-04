import socket
import datetime
import crcmod

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

crc16 = crcmod.mkCrcFun(0x11021, initCrc=0, xorOut=0xFFFF)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
try:
    while True:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        crc = crc16(message)
        now = datetime.datetime.now()
        dateStr = now.strftime("%Y-%m-%d %H:%M:%S")
        response = "{} CRC: 0x{:04X}".format(dateStr, crc)
        bytesToSend = str.encode(response)
        UDPServerSocket.sendto(bytesToSend, address)

except KeyboardInterrupt:
    print("UDP server stopped by user")
    UDPServerSocket.close()
