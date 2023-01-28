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

def mip(n,i):
    #finding multiplicative inverse of i in mod n.(Brute force algorithm)
    for j in range(1,n):
        if (i*j)%n==1:
            return j

####KEY GENERATION
p=397
q=401
phiN=(p-1)*(q-1)
e=343   
n=p*q
d=mip(phiN,e)   #private key

#Encryption
def rsa_enc(message):
    cipher=list()
    for el in message:
        k=exp(ord(el), e, n)
        cipher.append(k)
    c=""
    for el in cipher:
        c+=str(el)+" "
    return c

#Decryption    
def rsa_dec(enc_msg):
    enc_msg=enc_msg.split()
    plaint=""
    for el in enc_msg:
        x=exp(int(el),d,n)
        plaint+=chr(x)
    return plaint
