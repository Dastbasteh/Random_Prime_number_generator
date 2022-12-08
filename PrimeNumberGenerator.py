####################### Extended Euclidean algorithm(a,b) and multiplicative inverse of a mod b ############################################
#It takes a,b and returns gcd(a,b) and sa+tb=r, here a>=b
def Extended_Euclidean(a,b):
    a0=a
    b0=b
    t0=0
    t=1
    s0=1
    s=0
    q=a0//b0
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
        q=a0//b0
        r=a0-q*b0
    r=b0
    return [r,s,t]
 
##########################Inverse of a mod b ############################
def Multiplicative_inverse(a,b):
    return((Extended_Euclidean(a,b)[1])%b)

#################################### We define random n bit integers ########################

import random
def nBitRandom(n):
    return(random.randrange(2**(n-1)+1, 2**n-1))
    
#################################### Square and multiply algorithm computes x^y mod n ########################
    
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

#################################### Here we deteemine random integers without a small prime factors ########################
    
small_primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
def prime_candidate(bits):
    primefound=0
    while primefound==0:
        p=nBitRandom(bits)
        primefound=1
        for i in small_primes:
                if p%i==0:
                    primefound=0
                    break
    return p 
    
#################################### Here we use Miller Rabin algorithm which checks the primarity with error probability less thab 1/4 ########################
    
def Miller_Rabin(n):
    z="composite"    
    aa=n-1
    k=0
    while aa%2 == 0:
        aa >>= 1 
        k+=1
    assert (aa * 2**k ==n-1)
    a=random.randrange(1,n-1) 
    b=SAM(a,aa,n)
    if b%n==1:
        z="prime"
    else:
        for i in range(0,k):
            if b%n==(-1)%n:
                z="prime"
            else:
                b=SAM(b,2,n)
    return z            
                    

primes=[] 
for j in range(0,1):
    p=prime_candidate(2048)
    for i in range(1,20): #Here we run Miller_Rabin algorithm 20 times to reduce the error probability 
        if Miller_Rabin(p)=="composite":
            i=0
            while Miller_Rabin(p)=="composite":   
                p=prime_candidate(2048)        
    primes.append(p)
print(primes)    
    

        
