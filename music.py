#!/usr/bin/env python

import random,sys
from struct import *

rate = 6000

def wl():
    return (rate/160.0)*(0.87055**(int(random.random()*10)))
if __name__ == '__main__':
    
    #number chosen by fair dice roll, guaranteed to be random
    random.seed(4)
    
    wla = wl()
    
    playing = True
    
    while playing:
        wlb=wla
        wla=wl()
        
        if wla==wlb:
            wla = wla * 2
            
        d=int(random.random()*10+5)*rate/4
        
        a=0.0
        b=0.0
        c=128.0
        ca=40/wla
        cb=20/wlb
        de=rate/40
        di=0
        
        for i in range(0,d):
            a+=1.0
            b+=1.0
            di+=1
            c=(c + ca + cb)

            if (a>wla):
                a=0.0
                ca=-ca
                
            if (b>wlb):
                b=0.0
                cb=-cb
            
            if (di>de):
                di=0
                ca = ca * 0.9
                cb = cb * 0.9


            
            sys.stdout.write(pack('B',int(c)))
        
        c=int(c)
        while c!=128:
            
            if c>128:
                c-=1
            else:
                c+=1
            
            sys.stdout.write(pack('B',c))

