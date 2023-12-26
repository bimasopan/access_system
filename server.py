import socket
import subprocess
import os
import signal
import threading
import re

# Fungsi untuk menangani koneksi masuk
def threaded_client(connection):
    # Menerima data
    while True:
        data = connection.recv(2048)
        if data == "exit":
            break

        # Mengubah data menjadi perintah shell dan menjalankannya
        string = data.decode() # Tambahkan baris ini
        data = re.sub(' ', ' ', string) # Perbaikan di sini
        output = subprocess.check_output(data, shell=True)
        connection.send(output)
        # print('Received data: {}'.format(data))
        # print('Sent data: {}'.format(output.decode()))
        os.system(output.decode())

    connection.close()

def main():
    # Buat socket dan binding ke port 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(5) # Maksimal 5 koneksi

    print('Server is listening on port 5555')

    # Perulangan untuk menerima koneksi
    while True:
        client_socket, addr = server.accept()
        print('Got connection from', addr)
        # Mulai thread untuk menangani koneksi
        client_thread = threading.Thread(target=threaded_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()