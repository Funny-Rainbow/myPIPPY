import socket
from time import sleep
from time import time
#np.set_printoptions(threshold=sys.maxsize)
speedNow = 'No QR detected'
i = 0
threshold = 0.1
def socketTransfer(speedNow):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0.01)
    addrT = ("192.168.43.135", 8888)#pad IP
    data = speedNow
    data = str(speedNow)
    #print('data',data)
    s.sendto(data.encode(), addrT)
    print('Sending message: ', data.encode())
    s.close()

if __name__ == '__main__':
    socketTransfer(3)