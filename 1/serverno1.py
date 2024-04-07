import socket

def hitung_jumlah_karakter(pesan):
    return str(len(pesan))

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)

print("Server berjalan. Menunggu koneksi...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Terhubung dengan", client_address)

    pesan_dari_klien = client_socket.recv(1024).decode()

    if pesan_dari_klien:
        print("Pesan dari klien:", pesan_dari_klien)
        
        jumlah_karakter = hitung_jumlah_karakter(pesan_dari_klien)

        client_socket.send(jumlah_karakter.encode())
        print("Jumlah karakter pesan:", jumlah_karakter)

    client_socket.close()
    
#  Penjelasan
#  Server.py
# -	Import Library: Mengimpor modul socket untuk menggunakan fungsi-fungsi socket dalam Python.
# -	Fungsi hitung_jumlah_karakter: Fungsi ini menerima sebuah string dan mengembalikan jumlah karakternya dalam bentuk string.
# -	Inisialisasi Socket Server: Membuat socket server menggunakan socket.socket() dengan parameter socket.AF_INET untuk menentukan domain alamat (IPv4) dan socket.SOCK_STREAM untuk menentukan jenis socket (TCP).
# -	Bind Socket: Mengikat (bind) socket ke alamat localhost dan port 12345 menggunakan metode bind().
# -	Listen for Connections: Memulai mendengarkan (listen) koneksi masuk dengan metode listen(). Parameter 5 menentukan jumlah maksimum koneksi yang diterima oleh server.
# -	Loop untuk Menerima Koneksi: Server memasuki loop tak terbatas untuk terus menerima koneksi masuk dari client.
# -	Terima Koneksi: Ketika ada koneksi masuk, server menerima koneksi dan mendapatkan objek socket baru untuk berinteraksi dengan client. Fungsi accept() akan mengembalikan objek socket client dan alamat client.
# -	Terima Pesan dari client: Server menerima pesan dari client menggunakan metode recv() dengan buffer size 1024. Pesan tersebut kemudian di-decode dari byte menjadi string.
# -	Proses Pesan: Jika pesan diterima dari client, server akan menghitung jumlah karakter pesan menggunakan fungsi hitung_jumlah_karakter.
# -	Kirim Balasan: Server mengirim balasan berupa jumlah karakter pesan kembali ke client menggunakan metode send(). Sebelumnya, jumlah karakter dikonversi menjadi string dan diencode ke dalam byte.
# -	Tutup Koneksi: Setelah mengirim balasan, koneksi dengan client ditutup menggunakan metode close().