# Fungsi yang akan diuji
def hitung_total_belanja(jumlah_barang, harga_barang):
    total_belanja = jumlah_barang * harga_barang
    
    if jumlah_barang < 1 or jumlah_barang > 10:
        return "Jumlah barang tidak valid"
    elif harga_barang < 1000 or harga_barang > 100000:
        return "Harga barang tidak valid"
    elif total_belanja >= 500000:
        return "Maaf, total belanja anda melebihi batas maksimum"
    else:
        return total_belanja

# State Transition Testing
def test_hitung_total_belanja():
    # State 1: jumlah_barang valid (1-10) dan harga_barang valid (1000-100000)
    assert hitung_total_belanja(1, 1000) == 1000
    assert hitung_total_belanja(1, 50000) == 50000
    assert hitung_total_belanja(10, 1000) == 10000
    assert hitung_total_belanja(10, 5000) == 50000
    assert hitung_total_belanja(1, 200000) == "Harga barang tidak valid"
    assert hitung_total_belanja(1, 500) == "Harga barang tidak valid"

    # State 2: jumlah_barang tidak valid (<1 or >10) dan harga_barang valid (1000-100000)
    assert hitung_total_belanja(0, 1000) == "Jumlah barang tidak valid"
    assert hitung_total_belanja(11, 1000) == "Jumlah barang tidak valid"
    assert hitung_total_belanja(15, 50000) == "Jumlah barang tidak valid"

    # State 3: jumlah_barang valid (1-10) dan harga_barang tidak valid (<1000 or >100000)
    assert hitung_total_belanja(1, 500) == "Harga barang tidak valid"
    assert hitung_total_belanja(1, 200000) == "Harga barang tidak valid"
    assert hitung_total_belanja(10, 500) == "Harga barang tidak valid"
    assert hitung_total_belanja(10, 200000) == "Harga barang tidak valid"

    # State 4: jumlah_barang valid (1-10) dan harga_barang valid (1000-100000) dan total_belanja < 500000
    assert hitung_total_belanja(1, 49999) == 49999
    assert hitung_total_belanja(2, 24999) == 49998
    assert hitung_total_belanja(10, 49999) == 499990
    assert hitung_total_belanja(6, 100000) == "Maaf, total belanja anda melebihi batas maksimum"
    assert hitung_total_belanja(10, 50000) == "Maaf, total belanja anda melebihi batas maksimum"

