import socket

def main():
    # Inisialisasi socket klien
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Koneksi ke server
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    
    try:
        # Meminta pengguna untuk memasukkan pesan
        pesan = input("Masukkan pesan untuk dikirim ke server: ")
        
        # Kirim pesan ke server
        client_socket.sendall(pesan.encode())
        
        # Terima balasan dari server
        balasan = client_socket.recv(1024).decode()
        
        # Tampilkan balasan
        print("Balasan dari server:", balasan)
    
    finally:
        # Tutup koneksi
        client_socket.close()

if __name__ == "__main__":
    main()
    
# Penjelasan
# Client diminta untuk memasukkan sebuah pesan. Dalam contoh ini, pengguna memasukkan "Ini adalah sebuah pesan dari client." 
# Lalu client mengirimkan pesan tersebut ke server.
# Server menghitung jumlah karakter dalam pesan tersebut (30 karakter) dan mengirim balasan kembali ke client.
# Client menerima balasan dari server, yaitu "30", dan menampilkannya ke pengguna.