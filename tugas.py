# Inisialisasi list data penjualan
dataPenjualan = [
    [120, 150, 130, 170, 200, 190],
    [80, 100, 90, 110, 130, 120],
    [200, 210, 190, 180, 220, 210]
]

# Inisialisasi konstanta untuk ambang batas
"""
Menggunakan ambang batas 20% di atas rata-rata
"""
THRESHOLD = 0.2

# Inisialisasi list produk
produk = ['Produk A', 'Produk B', 'Produk C']

# Fungsi untuk mencari total penjualan dengan fungsi 'sum()'
def totalPenjualan(dataPenjualanProduk):
    return sum(dataPenjualanProduk)

# Fungsi untuk mencari bulan dengan penjualan tertinggi
""" 
Mencari bulan dengan penjualan tertinggi dengan cara mencari index dari 
nilai tertinggi lalu ditambah 1 karena index dimulai dari 0 
"""
def bulanPenjualanTertinggi(dataPenjualanProduk):   
    return dataPenjualanProduk.index(max(dataPenjualanProduk)) + 1  


# Fungsi untuk mencari bulan dengan penjualan terendah
""" 
Mencari bulan dengan penjualan terendah dengan cara mencari index dari 
nilai terendah lalu ditambah 1 karena index dimulai dari 0 
"""
def bulanPenjualanTerendah(dataPenjualanProduk):
    return dataPenjualanProduk.index(min(dataPenjualanProduk)) + 1 

# Fungsi untuk mencari lonjakan penjualan pada data penjualan produk
"""
Menentukan batas dengan mengalikan rata-rata dengan 1.2(120%) untuk mencari
nilai yang di atas 120% dari rata-rata. Mengiterasi data penjualan pada produk,
lalu jika ada yang di atas ambang batas maka dimasukkan ke dalam list lonjakan
karena bisa saja ada lebih dari 1 yang mengalami lonjakan.

Memanggil fungsi totalPenjualan untuk mencari total penjualan.
"""
def analisisLonjakan(dataPenjualanProduk):
    rata_rata = (totalPenjualan(dataPenjualanProduk) / len(dataPenjualanProduk))
    ambang_batas = rata_rata * (1 + THRESHOLD)
    count = 0
    lonjakan = {
        'rata_rata' : rata_rata,
        'ambang_batas' : ambang_batas,
        'list_lonjakan' : []
    }
    
    for i in dataPenjualanProduk:
        count += 1
        if i > ambang_batas:
            lonjakan['list_lonjakan'].append({
                "bulan" : count,
                "nilai" : i
            })
    return lonjakan
    
# Menampilkan hasil analisis data penjualan tiap produk
"""
Menampilkan analisis berupa :
1. Total Penjualan
2. Bulan dengan penjualan tertinggi
3. Bulan dengan penjualan terendah
4. Hasil analisis lonjakan
"""
for item in range(len(dataPenjualan)):
    dataLonjakan = analisisLonjakan(dataPenjualan[item])
    print(f"\n{produk[item]}")
    
    print(f"Total Penjualan                    : {totalPenjualan(dataPenjualan[item])}")
    print(f"Bulan dengan penjualan tertinggi   : Bulan ke-{bulanPenjualanTertinggi(dataPenjualan[item])}")
    print(f"Bulan dengan penjualan terendah    : Bulan ke-{bulanPenjualanTerendah(dataPenjualan[item])}")
    
    print(f"\nAnalisis Lonjakan :")
    
    print(f"Rata - rata   : {dataLonjakan['rata_rata']:.2f}")
    print(f"Ambang batas  : {dataLonjakan['ambang_batas']:.2f}")
    print("List Lonjakan :")
    if len(dataLonjakan['list_lonjakan']) > 0:
        for lonjakan in dataLonjakan['list_lonjakan']: 
            print(f"- Bulan {lonjakan['bulan']} dengan Nilai {lonjakan['nilai']}")
    else:
        print('Tidak ada lonjakan.')
    
