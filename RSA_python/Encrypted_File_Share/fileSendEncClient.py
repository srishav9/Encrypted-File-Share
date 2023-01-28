import socket
import my_rsa
def client_program():
    host = "127.0.0.1"  # as both code is running on same pc
    port = 2106  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    with open('file_to_send.txt', 'rb') as f:
        message = f.read().decode()   
    message = my_rsa.rsa_enc(message).encode()
    client_socket.send(message)  # send message
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()