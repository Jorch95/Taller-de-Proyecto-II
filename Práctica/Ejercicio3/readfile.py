# This Python file uses the following encoding: utf-8
import os, sys, string  
def devolverValores():
    arreglo = [] #datos que se devuelven.
    arch = open("datos.txt",'r')
    for linea in arch.readlines():
        arreglo = linea.split("-")
    return arreglo
