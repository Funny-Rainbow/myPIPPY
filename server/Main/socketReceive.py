import socket
from time import sleep

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(0.01)
s.bind(("192.168.43.126", 8003)) #raspi ip and port
print("UDP bound on port...")


def rec():
    while True:
        try:
            data, addrR = s.recvfrom(128)
            datastr=data.decode(encoding='UTF-8')
            hello = datastr.split(' ')
            return hello[0], int(hello[1])
        except:
            return False,False





if __name__ == '__main__':
    i=1
    while True:
        re = rec()
        if re != rec():
            continue