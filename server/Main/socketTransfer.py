import socket
from time import sleep
from time import time
#np.set_printoptions(threshold=sys.maxsize)
i = 0
def socketTransfer(speedNow):
    data = speedNow
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    addrT = ("192.168.43.135", 8888)#pad IP
    s.sendto(data.encode(), addrT)
    s.close()