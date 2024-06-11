# import required module
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os, time

# Get current directory
CURR_DIR = os.path.dirname(__file__)

def gen_key():
    # key generation 128 bit
    key = get_random_bytes(16)
    # storing the key in a file
    with open('aes_key.key', 'wb') as filekey:
        filekey.write(key)
    # for backup key
    with open('backup_aes_key.key', 'wb') as filekey:
        filekey.write(key)
    print("Key generated successfully")

def get_key():
    # opening the key file
    with open('aes_key.key', 'rb') as filekey:
        key = filekey.read()
    return key

def get_data_nonce_tag(data):
    # opening the encrypted file
    with open("enc_main_"+data, 'rb') as enc_file:
        e = enc_file.read()
    # opening the nonce file
    with open('enc_nonce_'+data, 'rb') as nonce:
        n = nonce.read()
    # opening the tag file
    with open('enc_tag_'+data, 'rb') as tag:
        t = tag.read()
    return (e,n,t)

def encrypt(data):
    output_main = "enc_main_"+data
    output_tag = "enc_tag_"+data
    output_nonce = "enc_nonce_"+data
    key = get_key()
    # using the key
    with open(data, 'rb') as file:
        original = file.read()
    # encrypting the file
    cipher = AES.new(key, AES.MODE_EAX)
    cipherbyte, tag = cipher.encrypt_and_digest(original)
    nonce = cipher.nonce
    # opening the file in write mode and 
    # writing the encrypted data
    with open(output_main, 'wb') as encrypted_file:
        encrypted_file.write(cipherbyte)
    with open(output_nonce, 'wb') as encrypted_file:
        encrypted_file.write(nonce)
    with open(output_tag, 'wb') as encrypted_file:
        encrypted_file.write(tag)

def decrypt(data):
    output = "dec_"+data
    key = get_key()
    encrypted, nonce, tag = get_data_nonce_tag(data)
    # decrypting the file
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    plaindata = cipher.decrypt_and_verify(encrypted, tag)
    # opening the file in write mode and
    # writing the decrypted data
    with open(output, 'wb') as dec_file:
        dec_file.write(plaindata)

# generate key needs to be done only once
gen_key()
        
# get the files in current directory
# files = ['testplain0.mp4', 'testplain1.mp4', 'testplain2.mp4']#, 'testplain3.mp4', 'testplain4.mp4', 'testplain5.mp4', 'testplain6.mp4']
files = list()
for file in os.listdir(CURR_DIR):
    if os.path.isfile(file) and 'mp4' in file:
      files.append(file)
# iterate over files and encrypt one by one
for file in files:
    start_time = time.time()
    encrypt(file)
    end_time = time.time()
    time_taken =  end_time - start_time
    print(f"{file} took {round(time_taken, 3)} seconds to encrypt.")
    # Decrypting
    start_time = time.time()
    decrypt(file)
    end_time = time.time()
    time_taken =  end_time - start_time
    print(f"{file} took {round(time_taken, 3)} seconds to decrypt.")

