import socket
import my_elgamal
def server_program():
    # get the hostname
    host = "127.0.0.1"
    port = 2106  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    # receive data stream. it won't accept data packet greater than 1024 bytes
    while True:
        data = conn.recv(1024).decode()
        data = my_elgamal.decrypt(data)
        if not data:
            # if data is not received break
            break
        with open('received_file.txt', 'wb') as f:
            f.write(data.encode("utf-8"))
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()