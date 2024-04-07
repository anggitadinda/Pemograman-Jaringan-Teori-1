import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

pesan_ke_server = input("Masukkan pesan untuk dikirim ke server: ")

client_socket.send(pesan_ke_server.encode())

balasan_dari_server = client_socket.recv(1024).decode()

print("Balasan dari server:", balasan_dari_server)

client_socket.close()

# Penjelasan
# Client.py
# -	Import Library: Mengimpor modul socket untuk menggunakan fungsi-fungsi socket dalam Python.
# -	Inisialisasi Socket client: Membuat socket client menggunakan socket.socket() dengan parameter socket.AF_INET untuk menentukan domain alamat (IPv4) dan socket.SOCK_STREAM untuk menentukan jenis socket (TCP).
# -	Koneksi ke Server: client melakukan koneksi ke server dengan menggunakan metode connect() dengan alamat localhost dan port 12345.
# -	Mengirim Pesan ke Server: client meminta pengguna untuk memasukkan pesan yang akan dikirim ke server, kemudian pesan tersebut dikirim menggunakan metode send(). Pesan tersebut diencode menjadi byte sebelum dikirim.
# -	Terima Balasan dari Server: client menerima balasan dari server menggunakan metode recv() dengan buffer size 1024. Balasan tersebut kemudian di-decode dari byte menjadi string.
# -	Tampilkan Balasan: Balasan dari server, yaitu jumlah karakter pesan, ditampilkan ke pengguna.
# -	Tutup Koneksi: Setelah menerima balasan, koneksi dengan server ditutup menggunakan metode close().