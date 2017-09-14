from flask import Flask
from flask import request
from flask import render_template
from web import index
from sensor import tomarMuestra
import time
import threading
lock = threading.Lock()


def threadproductor():
    arch = open("datos.txt",'w')
    arch.write("")
    arch.close()
    while True:
        lock.acquire()
        tomarMuestra()
        lock.release()
        print "produje"
        time.sleep(1)


def threadconsumidor():
    while True:
        time.sleep(3)
        lock.acquire()
        index()
        lock.release()
        print "consumi"

#ThreadPrincipal
print "dddddd"
prod = threading.Thread(target=threadproductor)
prod.start()
print "0999999999"
cons = threading.Thread(target=threadconsumidor)
print "ddddddaaa"
cons.start()
print "xxx"
