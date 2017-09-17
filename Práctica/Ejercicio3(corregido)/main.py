from sensor import tomarMuestra
import time

arch = open("datos.txt",'w')
arch.write("")
arch.close()
while True:
    tomarMuestra()
    print "produje"
    time.sleep(3)
