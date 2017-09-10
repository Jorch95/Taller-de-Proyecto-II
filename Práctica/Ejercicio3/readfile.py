# This Python file uses the following encoding: utf-8
import os, sys, string  
arch = open("datos.txt",'r')
for linea in arch.readlines():
    print linea.split("-")

