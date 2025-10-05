dataPenjualan = [
    [120, 150, 130, 170, 200, 190],
    [80, 100, 90, 110, 130, 120],
    [200, 210, 190, 180, 220, 210]
]

produk = ['Produk A', 'Produk B', 'Produk C']

def totalPenjualan(dataPenjualanProduk):
    return sum(dataPenjualanProduk)

def bulanDenganPenjualanTertinggi(dataPenjualanProduk):   
    return dataPenjualanProduk.index(max(dataPenjualanProduk)) + 1  

def bulanDenganPenjualanTerendah(dataPenjualanProduk):
    return dataPenjualanProduk.index(min(dataPenjualanProduk)) + 1 

def lonjakanPenjualan(dataPenjualanProduk):
    lonjakan = []
    treshold = (totalPenjualan(dataPenjualanProduk) / len(dataPenjualanProduk)) * 1.15
    count = 0
    for i in dataPenjualanProduk:
        count += 1
        if i > treshold:
            lonjakan.append(count)
            
    return lonjakan
    
for item in range(len(dataPenjualan)):
    lonjakan = ""
    for i in lonjakanPenjualan(dataPenjualan[item]): lonjakan+= f"Bulan ke-{i}" if len(lonjakan) == 0 else f", Bulan ke-{i}"
    print(produk[item])
    print(f"Total Penjualan                    : {totalPenjualan(dataPenjualan[item])}")
    print(f"Bulan dengan penjualan tertinggi   : Bulan ke-{bulanDenganPenjualanTertinggi(dataPenjualan[item])}")
    print(f"Bulan dengan penjualan terendah    : Bulan ke-{bulanDenganPenjualanTerendah(dataPenjualan[item])}")
    print(f"Lonjakan Penjualan                 : {lonjakan if len(lonjakan) > 0 else '-'} \n")
    