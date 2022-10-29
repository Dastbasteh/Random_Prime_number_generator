#Extended Euclidean algorithm(a,b) and multiplicative inverse of a mod b
#It takes a,b and returns gcd(a,b) and sa+tb=r, here a>=b
def Extended_Euclidean(a,b):
    import math
    a0=a
    b0=b
    t0=0
    t=1
    s0=1
    s=0
    q=math.floor(a0/b0)
    r=a0-q*b
    while r>0:
        temp=t0-q*t
        t0=t
        t=temp
        temp=s0-q*s
        s0=s
        s=temp
        a0=b0
        b0=r
        q=math.floor(a0/b0)
        r=a0-q*b0
    r=b0
    return r,s,t
    
print(Extended_Euclidean(97,21))  
#Inverse of a mod b
def Multiplicative_inverse(a,b):
    return((Extended_Euclidean(a,b)[1])%b)
print(Multiplicative_inverse(97,21))  

import random
def nBitRandom(n):
    return(random.randrange(2**(n-1)+1, 2**n-1))
print (nBitRandom(1024))

def SAM(x,y,n):
    def binary(n):
      return bin(n).replace("0b", "")
    y=binary(y)
    z=1
    for char in y:
        if char=="1":
            z=((z**2)*x)%n
        else:
            z=(z**2)% n
    return(z)
    
def Miller_Rabin(n):
            z="composite"    
            aa=n-1
            k=0
            while aa%2==0:
                aa=aa/2
                k+=1
            m=(n-1)/(2**k)
            a=random.randrange(1,n-1) 
            b=SAM(int(a),int(m),n)
            if b%n==1:
                z="prime"
            else:
                for i in range(0,k):
                    if b%n==(-1)%n:
                        z="prime"
                    else:
                        b=(b**2)%n
            return z            
                    
print(Miller_Rabin(nBitRandom(1024)))                
a=nBitRandom(64)                
while Miller_Rabin(a)=="composite":   
    a=nBitRandom(64)
print(a)    
    

        