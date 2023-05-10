# Fungsi yang akan diuji
def kategori_pengguna(usia):
    if usia < 0 or usia > 100:
        return "Usia tidak valid"
    elif usia < 12:
        return "Anak-anak"
    elif usia < 18:
        return "Remaja"
    elif usia < 60:
        return "Dewasa"
    else:
        return "Lansia"

# Pengujian dengan Equivalence Class Partitioning
def test_kategori_pengguna():
    # Kategori Usia Anak-anak
    assert kategori_pengguna(5) == "Anak-anak"
    assert kategori_pengguna(11) == "Anak-anak"

    # Kategori Usia Remaja
    assert kategori_pengguna(12) == "Remaja"
    assert kategori_pengguna(17) == "Remaja"

    # Kategori Usia Dewasa
    assert kategori_pengguna(18) == "Dewasa"
    assert kategori_pengguna(59) == "Dewasa"

    # Kategori Usia Lansia
    assert kategori_pengguna(60) == "Lansia"
    assert kategori_pengguna(100) == "Lansia"

    # Kategori Usia Tidak Valid
    assert kategori_pengguna(-5) == "Usia tidak valid"
    assert kategori_pengguna(200) == "Usia tidak valid"
