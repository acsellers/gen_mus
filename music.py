#!/usr/bin/env python

import random,sys
from struct import *

rate = 12000


def wl():
    return (rate/160.0)*(0.87055**(int(random.random()*10)))
    
if __name__ == '__main__':
    
    #number chosen by fair dice roll, guaranteed to be random
    random.seed(4)
    
    wla = wl()
    
    while True:
        wlb=wla
        wla=wl()
        
        if wla==wlb:
            wla *=2
            
        d=random.randint(5,15)*(rate/4)
        
        a=0
        b=0
        c=128
        ca=40/wla
        cb=20/wlb
        de=rate/10
        di=0
        for i in range(0,d):
            a+=1
            b+=1
            di+=1
            c+=ca
            c+=cb
            
            if (a>wla):
                
                a=0
                ca *= -1
                
            if (b>wlb):
                b=0
                cb *= -1
            
            if (di>de):
                di=0
                ca *= 0.9
                cb *= 0.9
            
            sys.stdout.write(pack('B',c))
            
            c=int(c)
            
            while c!=128:
                
                if c>128:
                    c-=1
                else:
                    c+=1
                
                sys.stdout.write(pack('B',c))
