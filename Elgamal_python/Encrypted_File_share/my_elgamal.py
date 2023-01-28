def mip(n,i):
    #finding multiplicative inverse of i in mod n.(Brute force algorithm)
    for j in range(1,n):
        if (i*j)%n==1:
            return j

def decimalToBinary(num):
    b=list()
    while num >= 1:
        b.append(num % 2)    
        num = num // 2
    return b

def exp(a, x, n):
    #implementing square and multiply algorithm to find large exponentiations
    bin = decimalToBinary(x)
    y=1
    for i in range(len(bin)):
        if bin[i]==1:
            y=(a*y)%n
        if i<len(bin)-1:
            a=(a*a)%n
    return y
#d is private key(random)
#prime,e1,e2 are public key set
prime,e1,d,r=193,2,3,4
e2=exp(e1,d,prime)

def encrypt(message):
    #encryption
    ct1=exp(e1,r,prime)
    ct2=(exp(e2,r,prime)*message)%prime
    return (ct1,ct2)

def decrypt(ct):
    #decryption
    ct1=list()
    ct2=list()
    i=0
    ct=ct.split()
    n=len(ct)/2
    for el in ct:
        if i<n:
            ct1.append(int(el))
        else:
            ct2.append(int(el))
        i+=1
    plain=''
    for i in range(len(ct1)):
        temp=exp(ct1[i],prime-1-d,prime)
        pt=(ct2[i]*temp)%prime
        plain+=chr(pt)
    return plain

def process(message):
    c1=list()
    c2=list()
    for ch in message:
        asc=ord(ch)
        a,b=encrypt(asc)
        c1.append(a)
        c2.append(b)
    st=''
    for i in range(len(c1)):
        st+=str(c1[i])+ " "
    for i in range(len(c2)):
        if i<len(c1)-1:
            st+=str(c2[i])+ " "
        else:
            st+=str(c2[i])
    return st