#Daftar semua data yang urutannya yaitu: Nama tempat makan, daftar antrean driver, dan jarak tempat makan
semua_data = [
    ["Gudeg Yu Djum", 5, 10],
    ["Warmindo Sami Asih", 4, 8],
    ["McDonalds Kaliurang", 2, 6],
    ["Warung Penyetan Bu Wid", 6, 4],
    ["Bubur Ayam Bandung", 9, 2],
    ["Nasi Kulit Syuurga", 7, 9],
    ["RM Padang Sabana Murah", 1, 7],
    ["Ayam Geprek Bu Rum", 3, 5],
    ["Mie Gacoan Colombo", 10, 3],
    ["KFC Mirota", 8, 1],
]

#Membuat daftar baru dengan memecah beberapa bagian, termasuk hasil dari perhitungan antrean yang dijumlahkan dengan estimasi waktu ke resto
daftar_resto = []
waktu_antrean_driver = []
waktu_berdasar_jarak = []
waktu_total_pesanan = []

for i in range(len(semua_data)):
    for j in range(len(semua_data[i])):
        if j == 0:
            daftar_resto.append(semua_data[i][j])
        elif j == 1:
            #mengkonversi antrean ke menit, diasumsikan 1 antrian 5 menit maka dikali 10
            x = semua_data[i][j] * 5
            waktu_antrean_driver.append(x)
        elif j == 2:
            #mengkonversi jarak resto ke menit, diasumsikan 1 km ditempuh dalam 3 menit maka dikali 3
            y = semua_data[i][j] * 3
            waktu_berdasar_jarak.append(y)
for i in range(len(semua_data)):
    waktu_total_pesanan.append(waktu_antrean_driver[i]+waktu_berdasar_jarak[i])

data_baru = [[]]

for i in range(len(semua_data)-1):
    data_baru.append([])

for i in range(len(waktu_total_pesanan)):
    data_baru[i].append(waktu_total_pesanan[i])

for i in range(len(daftar_resto)):
    data_baru[i].append(daftar_resto[i])

def quick(data, idlow=0, idhigh=None):
    if idhigh == None:
        idhigh = len(data)-1
    
    if (idlow < idhigh):
        pivot = data[(idlow+idhigh)//2]

        i = idlow
        j = idhigh
        while (i<=j):
            while (data[i] < pivot):
                i+=1
            while (data[j] > pivot):
                j-=1
            
            if (i <= j):
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp
                i+=1
                j-=1
        
        quick(data, idlow, j)
        quick(data, i, idhigh)

data = data_baru
quick(data, idlow=0, idhigh=None)

#interface menampilkan data makanan
print("______________________________________________________________________________")
print("")
print("       DAFTAR MAKANAN BERDASARKAN WAKTU PENGIRIMAN DI SHOPEEFOOD/GOFOOD       ")
print("______________________________________________________________________________")
print("")
for i in range(len(data)):
    for j in range(len(data[i])):
        if j == 0:
            print("(",i+1,")")
            print("Waktu pengiriman: ", data[i][j], "menit")
        elif j == 1:
            print(data[i][j],)
            print("______________________________________________________________________________")
            print("")