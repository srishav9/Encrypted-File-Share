# import required module
from cryptography.fernet import Fernet
from tqdm import tqdm

def gen_key():
    # key generation
    key = Fernet.generate_key()
    # string the key in a file
    with open('fernet_filekey.key', 'wb') as filekey:
        filekey.write(key)
    print("Key generated successfully")

def get_key():
    # opening the key file
    with open('fernet_filekey.key', 'rb') as filekey:
        key = filekey.read()
    return key

def encrypt(data, output):
    key = get_key()
    # using the key
    fernet = Fernet(key)
    # opening the original file to encrypt
    with open(data, 'rb') as file:
        original = file.read()
    # encrypting the file
    encrypted = fernet.encrypt(original)
    # opening the file in write mode and 
    # writing the encrypted data
    with open(output, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(data, output):
    key = get_key()
    # using the key
    fernet = Fernet(key)
    # opening the encrypted file
    with open(data, 'rb') as enc_file:
        encrypted = enc_file.read()
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    # opening the file in write mode and
    # writing the decrypted data
    with open(output, 'wb') as dec_file:
        dec_file.write(decrypted)

gen_key()

for i in tqdm(range(100)):
    opname = "cipher"+str(i)
    encrypt("test.mp4", f"{opname}.mp4")

for i in tqdm(range(100)):
    opname = "test"+str(i)
    inname = "cipher"+str(i)
    decrypt(f"{inname}.mp4", f"{opname}.mp4")

