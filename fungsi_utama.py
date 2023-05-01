#FUNGSI-FUNGSI SPESIFIKASI

#import library penting
import os
import random
import sys
from datetime import datetime
from fungsi_bantuan import *

#---------------------------------------------------------------------------------------------------------------------------------------
#F01. Login
def login(data_user, kondisi_user_pass):

    #Memasukkan matriks data_user ke dalam sebuah variabel untuk menyimpan matriks secara lokal
    arr = data_user

    #Melakukan pengecekan apakah pengguna sudah login atau belum
    if kondisi_user_pass[0] == "True":
        print("Login gagal!")
        print("Anda telah login dengan username",kondisi_user_pass[1],"silahkan lakukan \"logout\" sebelum melakukan login kembali.")

    #Apabila pengguna belum logim
    elif kondisi_user_pass[0] == "False":

        #input username dan password
        username = input("Username: ")
        password = input("Password: ")

        #mark untuk mengecek apakah password benar atau salah
        mark_password = ""
        for i in range(1,103):

            #Melakukan pengecekkan username 
            if username == arr[i][0]:

                #Melakukan pengecekan password
                if password == arr[i][1]:

                    print("Selamat datang,", arr[i][0])

                    #Menyimpan  data username dan password
                    kondisi_user_pass[1] = arr[i][0]
                    kondisi_user_pass[0] = "True"
                    kondisi_user_pass[4] = arr[i][2]
                    print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
                    break

                else: #Password Salah
                    print("Password salah!")
                    mark_password = "pass"
                    break


        #Apabila password entah bagaimana benar tapi username salah
        if kondisi_user_pass [0] == "False" and mark_password == "":
            print("Username tidak terdaftar!")

#-----------------------------------------------------------------------------------------------------------------------------------------
#F02. Logout
def logout(kondisi_user_pass) :

    #Apabila pengguna sudah login
    if kondisi_user_pass[0] == "True" :
        kondisi_user_pass[0] = "False" #Dalam keadaan login atau logout
        kondisi_user_pass[1] = ""   #Username dikosongkan
        kondisi_user_pass[2] = ""   #Password dikosongkan
        kondisi_user_pass[4] = ""   #Role dikosongkan

    #Apabila pengguna belum login
    elif kondisi_user_pass[0] == "False":
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")


#----------------------------------------------------------------------------------------------------------------------------------------
#F03. Summonjin
def summonjin(data_user, kondisi_user_pass):
    #Mengecek apakah Jin Sudah Lebih dari 100
    if kondisi_user_pass[3] == "False":
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")
        


        #Melakukan pemanggilan Jin
        terpanggil = False
        while not terpanggil :
            jenis_jin = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            if jenis_jin == "1" :
                jenis_jin = "Pengumpul"
                terpanggil = True
            elif jenis_jin == "2" :
                jenis_jin = "Pembangun"
                terpanggil = True
            else : #bukan 1 atau 2  
                print(f'Tidak ada jenis jin bernomor \"{jenis_jin}\"!')
        print(f'Memilih jin "{jenis_jin}".')


        #Input Username jin dan melakukan pengecekan apakah username sudaha da
        username_terpilih = False
        while not username_terpilih :
            username_jin = input("Masukkan username jin: ")
            username_terpilih = True
            for i in range(1,103):
                if username_jin == data_user[i][0]:
                    print(f'Username "{username_jin}" sudah diambil!')
                    username_terpilih = False
                    break
        
        #Input Password
        password_terpilih = False
        while not password_terpilih:
            password = input("Masukkan password jin: ")
            if len(password) < 5 or len(password) > 25:
                print("Password panjangnya harus 5-25 karakter!")
            else:
                password_terpilih = True
            
    
        #Mengecek array yang array yang masih None
        for i in range(103):
            if data_user [i][0] == None:
                data_user[i][0] = username_jin
                data_user[i][1] = password
                data_user[i][2] = jenis_jin
                break

        #Mengecek apakah semua array sudah terisi
        if data_user[102][0] != None:
            kondisi_user_pass[3] = "True"
        
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")
        print(f'Jin \"{username_jin}\" berhasil dipanggil!')

    else: #kondisi_user_pass[3] == "True"
        print("Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")

#F04. Hilangkan Jin
def hapusjin(data_user, data_candi):
    username_jin = input("Masukkan username jin : ")
    # cari jin dengan username jin yang sesuai
    mark = "False"
    for i in range(1,103):
        if data_user[i][0] == username_jin:
            # konfirmasi user untuk menghapus jin
            konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)? ")
            while konfirmasi != "y" and konfirmasi !="Y" and konfirmasi != "N" and konfirmasi != "n":
                konfirmasi = input(f"Apakah anda yakin ingin menghapus jin dengan username {username_jin} (Y/N)? ")

            if konfirmasi == "Y" or konfirmasi == "y":
                # hapus jin dari data
                data_user[i][0] = None
                data_user[i][1] = None
                data_user[i][2] = None
                # hapus juga candi yang dibuat oleh jin 
                for i in range (1,102):
                    if data_candi[i][1] == username_jin:
                        # hapus candi dari data
                        data_candi[i][0] = 0
                        data_candi[i][1] = 0
                        data_candi[i][2] = 0
                        data_candi[i][3] = 0
                        data_candi[i][4] = 0
                print("\nJin telah berhasil dihapus dari alam gaib.")  
                mark = "True"
                break
            elif konfirmasi =="N" or konfirmasi == "n": # konfirmasi == "N"
                print("\nJin batal dihapus dari alam gaib.") 
                mark = "True"
                break 

    if mark =="False": #Artinya jin tidak ada 
        print("\nTidak ada jin dengan username tersebut.")


#----------------------------------------------------------------------------------------------------------------------------------------
#F05. Ubah Tipe Jin
def ubahjin(data_user):
    #input username Jin dan pengecekan apakah username tersebut ada
    username_jin = input("Masukkan username jin : ")
    mark = "False"
    for i in range(1,104):
        if username_jin == data_user[i][0]:
            mark = "True"
            indeks = i

    #Jika ada maka akan dilakukan algoritma berikut untuk mengubah role jin
    if mark == "True":
        if data_user[indeks][2] == "Pengumpul":
            konfirmasi = input("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ")
            if konfirmasi == "Y":
                data_user[indeks][2] = "Pembangun"
                print("\nJin telah berhasil diubah.")
            else: # konfirmasi == "N"
                print("\nJin batal diubah.")
        elif data_user[indeks][2] == "Pembangun":
            konfirmasi = input("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ")
            if konfirmasi == "Y":
                data_user[indeks][2] = "Pengumpul"
                print("\nJin telah berhasil diubah.")
            else: # konfirmasi == "N"
                print("\nJin batal diubah.")
    else: # mark == "False"
        print("\nTidak ada jin dengan username tersebut.")

#---------------------------------------------------------------------------------------------------------------------------------------
# F06 - Jin Pembangun
# Input: matriks bahan, matriks matriks_candi, user yang sedang login
def bangun(data_bahan_bangunan, data_candi, kondisi_user_pass):
        
        #Me-random jumlah bahan
        pasir = random.randint(0,5)
        batu = random.randint(0,5)
        air = random.randint(0,5)

        #Pengecekan bahan bangunan yang dimiliki
        if pasir > data_bahan_bangunan[1][2] or batu > data_bahan_bangunan[2][2] or air > data_bahan_bangunan[3][2]:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else:

            #Jika cukup bahan bangunan akan dikurangi
            data_bahan_bangunan[1][2] -= pasir
            data_bahan_bangunan[2][2] -= batu
            data_bahan_bangunan[3][2] -= air
            print("Candi berhasil di bangun")

            #Mencari sisa candi yang harus dibangun
            indeks = 999999
            jumlah_candi = 0
            for i in range(1,101):
                if data_candi[i][1] == 0:
                    if i < indeks:
                        indeks = i
                if data_candi[i][1] != 0:
                    jumlah_candi += 1

            #Menyimpan data ke dalam matriks
            data_candi[indeks][0] = indeks-1
            data_candi[indeks][1] = kondisi_user_pass[1]
            data_candi[indeks][2] = pasir
            data_candi[indeks][3] = batu
            data_candi[indeks][4] = air
            print("Sisa candi yang perlu dibangun: {}".format(100-(jumlah_candi+1)))

#----------------------------------------------------------------------------------------------------------------------------------------
#F07. Jin Pengumpul
def kumpul(data_bahan_bangunan):
    #Random jumlah bahan yang dapat dikumpulkan
    jumlah_batu = random.randint(0,5)
    jumlah_pasir = random.randint(0,5)
    jumlah_air = random.randint(0,5)

    #Menyimpan data ke dalam matriks data_bahan_bangunan
    data_bahan_bangunan[1][0] = "pasir"
    data_bahan_bangunan[1][1] = "material_partikel"
    data_bahan_bangunan[1][2] += jumlah_pasir
    data_bahan_bangunan[2][0] = "batu"
    data_bahan_bangunan[2][1] = "material_besar"
    data_bahan_bangunan[2][2] += jumlah_batu
    data_bahan_bangunan[3][0] = "air"
    data_bahan_bangunan[3][1] = "material_cair"
    data_bahan_bangunan[3][2] += jumlah_air

    print("Jin menemukan", jumlah_pasir,"pasir,",jumlah_batu, "batu, dan",  jumlah_air,"air")

#---------------------------------------------------------------------------------------------------------------------------------------
#F08. Batch Kumpul & Batch Bangun
def batchkumpul(data_user, data_bahan_bangunan):

#Batch Kumpul
    pasir = 0
    batu = 0
    air = 0
    jumlah_pengumpul = 0

    #Pengecekan Jumlah Pengumpul
    for i in range(1,103):
        if data_user[i][2] == "Pengumpul":
            jumlah_pengumpul += 1
    if jumlah_pengumpul == 0: #Tidak Punya Pengumpul
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else: #Punya Pengumpul
        print("Mengerahkan {} jin untuk mengumpulkan bahan.".format(jumlah_pengumpul))
        #Random Bahan yang dapat dikumpulkan untuk setiap Jin
        for i in range(jumlah_pengumpul):
            pasir += random.randint(0,5)
            batu += random.randint(0,5)
            air += random.randint(0,5)

        #Menyimpan data ke dalam matriks
        data_bahan_bangunan[1][2] += pasir
        data_bahan_bangunan[2][2] += batu
        data_bahan_bangunan[3][2] += air

        print("Jin menemukan total", pasir,"pasir",batu,"batu dan", air, "air.")

#Batch Bangun
def batchbangun(data_user, data_bahan_bangunan, data_candi):
    butuh_pasir = 0
    butuh_batu = 0
    butuh_air = 0

    total_pasir = 0
    total_batu = 0
    total_air = 0

    pasir = data_bahan_bangunan[1][2]
    batu = data_bahan_bangunan[2][2]
    air = data_bahan_bangunan[3][2]

    jumlah_pembangun = 0
    #Mengecek Jumlah Jin Pembangun
    for i in range(1, 103):
        if data_user[i][2] == "Pembangun":
            jumlah_pembangun += 1

    if jumlah_pembangun == 0: #Jin Pembangun 0
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        # k digunkanan untuks mencari indeks yang belum diisi id candi
        arr = [0 for i in range(jumlah_pembangun)]

        #Mencari indeks yang nilai nya sama dengan 0
        for i in range(101):
            if data_candi[i][1] == 0:
                k = i
                break
        
        indeks = 0
        mark = 1
        for i in range(k, 202): #dibagian ini mungkin bisa ditambahin selisih selisih 0 kedua dengan k sekarang untuk mengatasi penghapusan
            if i <= 100 and data_candi[i][1] == 0:
                if data_candi[i][1] == 0:
                    butuh_pasir = random.randint(0,5)
                    butuh_batu = random.randint(0,5)
                    butuh_air = random.randint(0,5)

                    #Loop agar jin pembangun bisa bergiliran dalam membangun
                    for j in range(103):     
                        if j > indeks and data_user[j][2] == "Pembangun":
                            indeks = j
                            break
                    arr[mark-1] = i
                
                #Penyimpanan pada matriks data candi
                data_candi [i][0] = i-1
                data_candi[i][1] = data_user[indeks][0]
                data_candi[i][2] = butuh_pasir
                data_candi[i][3] = butuh_batu
                data_candi[i][4] = butuh_air
                total_pasir += butuh_pasir
                total_batu += butuh_batu
                total_air += butuh_air
                mark += 1

            elif i > 100: #Jika candi yang dibangun sudah lebih dari 100 data tidak dimasukkan
                butuh_pasir = random.randint(0,5)
                butuh_batu = random.randint(0,5)
                butuh_air = random.randint(0,5)
                mark += 1
                total_pasir += butuh_pasir  
                total_batu += butuh_batu
                total_air += butuh_air
            
            #Memastikan kalau pembangunan hanya sejumlah jin pembangun
            if mark > jumlah_pembangun:
                break
        print("Mengerahkan",jumlah_pembangun,"jin untuk membangun candi dengan total bahan",total_pasir,"pasir,",total_batu,"batu, dan", total_air, "air.")
        #Mengecek Apakah Total Bahan cukup
        if total_pasir > pasir or total_batu > batu or total_air > air: #Bahan tidak cukup
            kurang_pasir = total_pasir - pasir
            kurang_batu = total_batu - batu
            kurang_air = total_air - air
            if kurang_pasir <= 0:
                kurang_pasir = 0
            if kurang_batu <= 0:
                kurang_batu = 0
            if kurang_air <= 0:
                kurang_air = 0
            print("Bangun gagal. Kurang",kurang_pasir,"pasir,",kurang_batu,"batu, dan", kurang_air, "air.")

            #matriks candi yang sudah diisi dikosongkan
            for i in range(jumlah_pembangun):
                if arr[i] > 0:
                    data_candi[arr[i]][0] = 0
                    data_candi[arr[i]][1] = 0
                    data_candi[arr[i]][2] = 0
                    data_candi[arr[i]][3] = 0
                    data_candi[arr[i]][4] = 0

        elif total_pasir <= pasir and total_batu <= batu and total_air <= air: #bahan cukup
            #data_bahan_bangunan dikurangi
            print("Jin berhasil membangun total {} candi".format(jumlah_pembangun))
            data_bahan_bangunan[1][2] -= total_pasir 
            data_bahan_bangunan[2][2] -= total_batu
            data_bahan_bangunan[3][2] -= total_air
#-----------------------------------------------------------------------------------------------------------------------------------
#F09-Laporan Jin
def laporanjin(data_candi, data_user, data_bahan):

    #inisialisasi array
    arr_data_jin = [None for i in range(102)]
    kemunculan_jin = [(-1) for i in range(102)]
    arr_maks = ["" for i in range(102)]
    arr_min = ["" for i in range(102)]

    #menyimpan semua data jin pembangun
    mark = "False"
    indeks = 0
    for i in range (1,102):
        if data_candi[i][1] != 0:
             arr_data_jin[indeks] = data_candi[i][1]
             indeks += 1
             mark = "True"

    if mark == "True":
        #mencari jumlah kemunculan setiap jin pembangun
        jumlah = 0
        for i in range(102):
            if arr_data_jin[i] != None:
                for j in range(102):
                    if arr_data_jin[i] == data_candi[j][1]:
                        jumlah += 1

                kemunculan_jin[i] = jumlah
                jumlah = 0
        
        
        
        #mencari jumlah terbanyak dan terkecil kemunculan jin pembangun
        maks = 0
        mini = 99999999999999
        for i in range(102):
            if kemunculan_jin[i] > maks:
                maks = kemunculan_jin[i]
            if kemunculan_jin[i] <= mini and kemunculan_jin[i] != -1:
                mini = kemunculan_jin[i]

        #pencarian jin dengan nilai minimum atau maksimum
        indeks = 0
        indeks_min = 0
        for i in range(102):
            if kemunculan_jin[i] == maks:
                arr_maks[indeks] = arr_data_jin[i]
                indeks += 1
            if kemunculan_jin[i] == mini:
                arr_min[indeks_min] = arr_data_jin[i]
                indeks_min += 1
        
        #pengurutan berdasarkan leksikografis
        jin_terajin = arr_maks[0]
        jin_termalas = arr_min[0]
        for i in range(102):
            if arr_maks[i] != "":
                if arr_maks[i].lower() >= jin_terajin.lower():
                    jin_terajin = arr_maks[i]
            if arr_min[i] != "":
                if arr_min[i].lower() >= jin_termalas.lower():
                    jin_termalas = arr_min[i]

    elif mark == "False":
        jin_terajin = "-"
        jin_termalas = "-"        

    #program untuk mencari totaljin
    total_jin = 0
    jin_pembangun = 0
    jin_pengumpul = 0
    for i in range(3, 104):
        if data_user[i][0] != None:
            total_jin += 1
        if data_user[i][2] == "Pengumpul":
            jin_pengumpul += 1
        if data_user[i][2] == "Pembangun":
            jin_pembangun += 1
    
    #Program mencari total bahan bangunan
    Jumlah_pasir = data_bahan [1][2]
    jumlah_batu = data_bahan [2][2]
    jumlah_air = data_bahan[3][2]

    print("Total Jin:",total_jin)
    print("Total Jin Pengumpul:",jin_pengumpul)
    print("Total Jin Pembangun:",jin_pembangun)
    print("Jin Terajin:", jin_terajin)
    print("Jin Termalas:", jin_termalas)
    print("Jumlah Pasir:",Jumlah_pasir,"unit")
    print("Jumlah Air:", jumlah_air,"unit")
    print("Jumlah Batu:", jumlah_batu,"unit")
#------------------------------------------------------------------------------------------------------------------------------------
#F10-LaporanCandi
def laporancandi(data_candi):
    
    #Mencari total candi, pasir, batu, dan air
    total_candi = 0
    total_pasir = 0
    total_batu = 0
    total_air = 0
    for i in range(1,102):
        if data_candi[i][1] != 0:
              total_candi += 1
        total_pasir += data_candi[i][2]
        total_batu += data_candi[i][3]
        total_air += data_candi[i][4]
    
    if total_candi == 0: #jika tidak ada candi
         mahal = "-"
         murah = "-"
         idmaks = "-"
         idmin = "-"

    else: #jika ada candi

        #Prosedur untuk menghitung hara bahan bangunan
        def harga_candi(variabel,i):
            pasir = variabel[i][2]
            batu = variabel[i][3]
            air = variabel[i][4]
            nilai = 10000 * pasir + 15000 * batu + 7500 * air
            return nilai
        
        mahal = -9999999999999999999999999
        murah = 99999999999999999999999999

        #Mencari candi termahal dan termurah dan ID nya
        for i in range(1,102):
              if data_candi[i][1] != 0:
                if harga_candi(data_candi,i) > mahal:
                    mahal = harga_candi(data_candi,i)
                    idmaks = data_candi[i][0]
                if harga_candi(data_candi,i) < murah:
                    murah = harga_candi(data_candi,i)
                    idmin = data_candi[i][0]
            
    print("Total Candi:", total_candi)
    print("Total Pasir yang digunakan:",total_pasir)
    print("Total Batu yang digunakan:", total_batu)
    print("Total Air yang digunakan:", total_air)
    if idmaks == "-":
        print("ID Candi Termahal:",idmaks)
        print("ID Candi Termahal:",idmin)
    else:
        print("ID Candi Termurah:",idmin,"(Rp {})".format(murah))
        print("ID Candi Termahal:",idmaks,"(Rp {})".format(mahal))
#------------------------------------------------------------------------------------------------------------------------------------
#F11-hancurkancandi
def hancurkancandi(matriks_candi):
    id_candi = int(input("Masukkan ID candi: "))

    #Mengecek keberadaan candi
    mark = "False"
    for i in range(1,101):
        if matriks_candi[i][0] == id_candi and matriks_candi[i][1] != 0:
            indeks = i
            mark = "True"
            break
            
    #jika candi tidak ada
    if mark == "False":
        print("Tidak ada candi dengan ID tersebut.")
    else: #Jika ada
        choice = ""
        while choice != "N" and choice != "Y" and choice!="y" and choice!="n":
            choice = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")

        #Penghapusan data candi 
        if choice == "Y" or choice =="y":
            matriks_candi[indeks][0] = 0
            matriks_candi[indeks][1] = 0
            matriks_candi[indeks][2] = 0
            matriks_candi[indeks][3] = 0
            matriks_candi[indeks][4] = 0 
            print("Candi telah berhasil dihancurkan.")
 
        else:
            print("Candi batal dihancurkan.")


#-------------------------------------------------------------------------------------------------------------------------------------
#F12-AyamBerkokok
def ayamberkokok(data_candi):
    def banyak(data_candi):
        banyak_candi = 0
        for i in range(1, 102):
            if data_candi[i][1] != 0:
                banyak_candi += 1
        
        return banyak_candi
    
    if banyak(data_candi) >= 100:
        print("Kukuruyuk.. Kukuruyuk..")
        print(f"Jumlah Candi:  {banyak(data_candi)}")
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else:
        print("Kukuruyuk.. Kukuruyuk..")
        print(f"Jumlah Candi:  {banyak(data_candi)}")
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    # Keluar program
    import sys
    sys.exit()     


#--------------------------------------------------------------------------------------------------------------------------------------
#F13-Fungsi Load
def load(nama_folder, data_user, data_candi, data_bahan_bangunan):

    Folder = "save\\{}".format(nama_folder)

    #Mengecek apakah nama_folder ada
    if not os.path.exists(Folder):
        print("Folder \"{}\" tidak ditemukan".format(nama_folder))
        sys.exit(1)

    print("Loading...")

    #Melakukan load data kedalam matriks
    file_path1 = os.path.join(Folder, "user.csv")
    data_user = csv_to_arr(file_path1, data_user)
    file_path2 = os.path.join(Folder, "candi.csv")
    data_candi = csv_to_arr(file_path2, data_candi)
    file_path3 = os.path.join(Folder, "bahan_bangunan.csv")
    data_bahan_bangunan = csv_to_arr(file_path3, data_bahan_bangunan)

    print("Selamat datang di program \"Manajerial Candi\"")
    print("Silahkan masukkan username Anda")





#-----------------------------------------------------------------------------------------------------------------------------------------
#F14-Fungsi Save
def save(user, candi, bahan_bangunan):

    #mendapatkan folder parent
    parent = os.getcwd()

    #menambahkan folder save
    save_folder = os.path.join(parent, 'save')

    #input nama folder baru
    input_file = input("Masukkan nama folder: ")

    #path dari folder yang ditambahkan oleh pengguna
    file_path = os.path.join(save_folder, input_file)

    #Mengubah array menjadi string
    string_user = arr_to_string("user.csv",user)
    string_candi = arr_to_string("candi.csv",candi)
    string_bahan_bangunan = arr_to_string("bahan_bangunan.csv",bahan_bangunan)

    print("Saving...")

    #Mengecek apakah folder save sudah ada
    if not (os.path.exists(save_folder)):
        print("Membuat folder save...")

    #Mengecek apakah folder yang diinputkan sudah ada
    if os.path.exists(file_path): #sudah ada
        
        #Mengubah lokasi current directory
        os.chdir(file_path)

                #menulis string ke dalam format.csv
        write_to_csv(string_user, string_candi, string_bahan_bangunan)
        print("Berhasil menyimpan data di folder save/{}".format(input_file))

    else: #belum ada
        #Membuat path yang diinginkan
        os.makedirs(file_path)

        #Mengubah lokasi current directory
        os.chdir(file_path)
        write_to_csv(string_user, string_candi, string_bahan_bangunan)
        print("Membuat folder save/{}".format(input_file))
        print("Berhasil menyimpan data di folder save/{}".format(input_file))

    #kembali ke directory awal
    os.chdir(parent)


#----------------------------------------------------------------------------------------------------------------------------------------
#F15-Help
def help(role):
    if role[4] == "": #belum login
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")

    elif role[4] == "bandung_bondowoso": #Bandung Bondowoso
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin dan candi yang dibuat jin ikut terhapus apabila jin sudah dihapus")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin, yaitu berupa Jin Pengumpul dan Jin Pembangun")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh pasukan jin dengan tipe pengumpul untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengerahkan seluruh pasukan jin dengan tipe pembangun untuk membangun candi")
        print("7. laporanjin")
        print("   Untuk mengetahui kinerja dari para jin")
        print("8. laporancandi")
        print("   Untuk mengetahui progress pembangunan candi")
        print("9. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        print("10. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")

    elif role[4] == "roro_jonggrang": #Roro Jonggrang
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk memeriksa jumlah candi yang berhasil dibangun, mengetahui pemenangnya, dan mengakhiri permainan yang kemudian program akan otomatis keluar")
        print("4. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        print("5. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        
    elif role[4] == "Pengumpul": #Jin Pengumpul
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan resource candi")
        print("3. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
       
    elif role[4] == "Pembangun": #Jin Pembangun
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. save")
        print("   Untuk menyimpan data yang berada di program sesuai dengan struktur data eksternal")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")

#------------------------------------------------------------------------------------------------------------------------------------
#F16. Exit
import sys
def exit(data_user, data_candi, data_bahan_bangunan):
    while True: 
        penyimpanan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if penyimpanan == "y" or penyimpanan == "Y":
            save(data_user, data_candi, data_bahan_bangunan)
            sys.exit()

        elif penyimpanan == "n" or penyimpanan == "N":
            sys.exit()