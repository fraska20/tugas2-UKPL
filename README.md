
# Equivalence Partitioning

Untuk fungsi kategori_pengguna, dapat dikelompokkan input usia ke dalam beberapa kelompok ekivalen seperti berikut:



 - Usia tidak valid: usia < 0 atau usia > 100
 - Anak-anak: 0 <= usia < 12
 - Remaja: 12 <= usia < 18
 - Dewasa: 18 <= usia < 60
 - Lansia: usia >= 60
 
 ### Pengujian dengan Equivalence Class Partitioning

Dalam pengujian menggunakan metode ECP, setidaknya satu pengujian harus dilakukan pada setiap kelompok ekivalen. Dalam kasus ini, terdapat 5 kelompok ekivalen, sehingga perlu dilakukan setidaknya 5 pengujian.

- Kelompok ekivalen 1 (usia tidak valid):
    - Input: -5, 200
    - Output yang diharapkan: "Usia tidak valid"
- Kelompok ekivalen 2 (anak-anak):
    - Input: 5, 11
    - Output yang diharapkan: "Anak-anak"
- Kelompok ekivalen 3 (remaja):
    - Input: 12, 17
    - Output yang diharapkan: "Remaja"
- Kelompok ekivalen 4 (dewasa):
    - Input: 18, 59
    - Output yang diharapkan: "Dewasa"
- Kelompok ekivalen 5 (lansia):
    - Input: 60, 100
    - Output yang diharapkan: "Lansia"


## Screenshots
![App Screenshot](https://i.postimg.cc/VNP3sZyK/ecp.png)

# State Transition Testing

Dalam kasus fungsi hitung_total_belanja, terdapat empat state yang mungkin terjadi pada sistem:

- State 1: jumlah_barang valid (1-10) dan harga_barang valid (1000-100000)
- State 2: jumlah_barang tidak valid (<1 or >10) dan harga_barang valid (1000-100000)
- State 3: jumlah_barang valid (1-10) dan harga_barang tidak valid (<1000 or >100000)
- State 4: jumlah_barang valid (1-10) dan harga_barang valid (1000-100000) dan total_belanja < 500000

Untuk menguji setiap transisi antar state, dilakukan pengujian dengan memberikan nilai input yang tepat sehingga sistem berada pada state yang sesuai dengan transisi yang diuji. Kemudian dilakukan verifikasi output yang dihasilkan oleh sistem sesuai dengan ekspektasi yang telah ditetapkan.


## Screenshots
![App Screenshot](https://i.postimg.cc/mD4x2X9b/stt.png)