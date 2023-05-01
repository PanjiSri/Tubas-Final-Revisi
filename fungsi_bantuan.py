#-----------------------------------------------------------------------------------------------------------------------------------------
#01. Fungsi untuk mengubah string ke dalam file berformat.csv
def write_to_csv(string_user, string_candi, string_bahan_bangunan):
        user = open("user.csv","w")
        user.write(string_user)
        user.close()
        candi = open("candi.csv","w")
        candi.write(string_candi)
        candi.close()
        bahan_bangunan = open("bahan_bangunan.csv","w")
        bahan_bangunan.write(string_bahan_bangunan)
        bahan_bangunan.close()

#----------------------------------------------------------------------------------------------------------------------------------------
#02-Fungsi Mengubah Matriks Menjadi String
def arr_to_string(file, user):
    if file == "user.csv":
        jumlah_kolom = 3
        banyak = 104
    elif file == "candi.csv":
        jumlah_kolom = 5
        banyak = 102
    elif file == "bahan_bangunan.csv":
        jumlah_kolom = 3
        banyak = 102
    string_user = ""

    for i in range(banyak):
        if user[i][1] != None and user[i][1] != 0:
            indeks = i
    long = indeks + 1   
    for i in range(long): ##len user diganti dengan fungsi untuk mencari panjang sendiri
        for j in range(jumlah_kolom):
            if j != (jumlah_kolom-1):
                string_user += "{};".format(user[i][j])
            elif j == (jumlah_kolom-1):
                string_user += "{}\n".format(user[i][j])
    return string_user

#---------------------------------------------------------------------------------------------------------------------------------------
#03-Fungsi ini digunakan untuk mengubah data-data di file csv menjadi matriks

#Penjelasan parameter:
#   file adalah file.csv yang ingin kita rubah
#   data, adalah data array

def csv_to_arr (file, data):
    with open (file) as f:
        i = 0
        for line in f:
            j = 0
            string_file = ""
            k = 0
            while (line[k]) != "\n":
                if line[k] == ";":
                    data[i][j] = string_file
                    string_file = ""
                    j += 1 
                    k += 1
                string_file += line[k]
                k += 1
            data[i][j] = string_file
            i += 1
    
    return data


#--------------------------------------------------------------------------------------------------------------------------------------
#04-Berikut adalah fungsi untuk mencari panjang dari array data_user, data_candi, dan data_bahan_bangunan
def panjang (arr):
    panjang = 0
    i = 0
    while arr[i][1] != None and arr[i][1]!=0:
        panjang += 1
        i += 1
    return panjang