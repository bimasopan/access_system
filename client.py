import socket
import signal
import re
import os

def main():
    # Buat socket dan koneksi ke server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    # Mengirim data
    while True:
        user_cmd = input("Shell> ")
        if user_cmd == "exit":
            break

        string = user_cmd + "\n"
        user_cmd = re.sub(' ', ' ', string)
        client.send(user_cmd.encode())

        # Menerima data output dari server
        data = client.recv(2048)
        print('Received from server: {}'.format(data.decode()))

        # Mengambil output perintah shell
        os.system(user_cmd)

    client.close()

if __name__ == "__main__":
    main()