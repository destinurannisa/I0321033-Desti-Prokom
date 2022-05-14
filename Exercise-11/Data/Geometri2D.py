# Silakan perhatikan perintah pada file 11_Modul&Paket.ipynb sebelum membuka file ini
#Nama file : Geometry2D.py
import math

#luas persegi
def LuasPersegiPanjang (p,l):
    return p*l

#keliling persegi panjang
def KelilingPersegiPanjang (p,l):
    return 2*(p+l)

#luas bujur sangkar
def LuasBujurSangkar (s):
    return s*s

#keliling bujur sangkar
def KelilingBujurSangkar (s):
    return 4*s

#luas lingkaran
def LuasLingkaran (r):
    return math.pi*r*r

#keliling lingkaran
def KelilingLingkaran (r):
    return 2*math.pi*r

#luas segitiga
def LuasSegitiga (a,t):
    return (a*t)/2

#keliling segitiga
def KelilingSegitiga (a,b,c):
    return a+b+c
