from socketReceive import rec
import websocketTran as wt
from temperature import shabi
from socketTransfer import socketTransfer
import noisefigure as nf

def main():
    while True:
        re = rec()
        if re[0]:
            wt.asyncio.run(wt.hello(re[0]))
            #nfValue = nf.main()
            print('0')
            #if nfValue:
            #    print('1')
            #    wt.asyncio.run(wt.hello("left"))
main()