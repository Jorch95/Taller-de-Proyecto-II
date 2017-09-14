# This Python file uses the following encoding: utf-8
import os, sys, string

def devolverValores():
    arch = open("datos.txt",'r')
    arreglo = ['E', 'E', 'E', 'E']
    print arreglo
    lines = arch.readlines()
    if len(lines) > devolverValores.pos:
        arreglo = lines[devolverValores.pos].strip().split('-')
        devolverValores.pos = devolverValores.pos + 1
    arch.close()
    return arreglo

devolverValores.pos = 0
