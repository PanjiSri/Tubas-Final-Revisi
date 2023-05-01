#Program Manajerial Candi
#Program ini adalah prorgram semacam dimana pengguna bisa bermain dengan berbagai macam role dan melakukan command sesuai role yang berseuaian


#PENTING!: diharapkan untuk membaca panduan.md sebelum menjalankan Program Manajerial Candi


#Anggota Kelompok
#Kerlyn Deslia Andeskar : 19622005
#Jonathan Wiguna : 19622014
#Muhammad Rafi Dhiyaulhaq : 19622158	
#Panji Sri Kuncara Wisma : 19622140

#KAMUS UTAMA
#data_user : array [0..103] of array [0..2] of string
#data_bahan_bangunan : array [0..101] of array [0..2] of 0
#data_candi : array [0..101] of 	array [0..4] of 0


#ALGORITMA UTAMA
#import library penting
import os
import random
import sys
from datetime import datetime
from fungsi_bantuan import *
from fungsi_utama import *
import argparse


#I
#Matriks untuk menyimpan data user.csv
data_user = [[None for j in range(3)] for i in range(104)]

#Matriks untuk menyimpan data candi.csv
data_candi = [[0 for j in range(5)] for i in range(102)]

#Matriks untuk menyimpan data bahan_bangunan.csv
data_bahan_bangunan = [[0 for j in range(3)] for i in range(102)]

#Array untuk menyimpan beberapa kondisi
#["False jika belum login", "username", "password", "False jika candi belum 100", "Role"]
kondisi_user_pass = ["False","","","False",""]


#Implementasi Argparse Untuk Me-Load Program
parser = argparse.ArgumentParser(   )
parser.add_argument("nama_folder", nargs="?")
args = parser.parse_args()

if not args.nama_folder:
    print("\nTidak ada nama folder diberikan!")
    print("\nUsage: python main.py <nama_folder>")
    sys.exit(1)

#F13-Load
load(args.nama_folder,data_user, data_candi, data_bahan_bangunan)


#Pemanggilan Fungsi Berdasarkan Command yang ada
command = input(">>>")
mark = False
while(mark == False):

    #F01-Login
    if command == "login":
        login(data_user, kondisi_user_pass)
    
    #F02-Logout
    elif command == "logout":
        logout(kondisi_user_pass)
    
    #F03-Summon Jin
    elif command == "summonjin":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            summonjin(data_user, kondisi_user_pass)
        else : 
            print("Summon jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")

    #FO4-Hilangkan Jin
    elif command == "hapusjin":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            hapusjin(data_user, data_candi)
        else : 
            print("Hapus jin hanya dapat dilakukan oleh akun Bandung Bondowoso.")

    #F05-Ubah Tipe Jin
    elif command == "ubahjin":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            ubahjin(data_user)
        else :
            print("Ubah jin hanya dapat dilakukan oleh akun Bandung Bondowoso.") 

    #F06-Jin Pembangun
    elif command == "bangun":
        if kondisi_user_pass[4] == "Pembangun" :
            bangun(data_bahan_bangunan, data_candi, kondisi_user_pass)
        else :
            print("Bangun hanya dapat dilakukan oleh akun dengan role jin pembangun.") 

    #F07-Jin Pengumpul
    elif command == "kumpul":
        if kondisi_user_pass[4] == "Pengumpul" :
            kumpul(data_bahan_bangunan)
        else : 
            print("Kumpul hanya dapat dilakukan oleh akun dengan role jin pengumpul.")

    #F08-Batch Kumpul
    elif command == "batchkumpul":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            batchkumpul(data_user, data_bahan_bangunan)
        else :
            print("Batch kumpul hanya dapat dilakukan oleh akun Bandung Bondowoso.") 
    
    #F08-Batch Bangun
    elif command == "batchbangun":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            batchbangun(data_user, data_bahan_bangunan, data_candi)
        else : 
            print("Batch bangun hanya dapat dilakukan oleh akun Bandung Bondowoso.")

    #F09-Ambil Laporan Jin
    elif command == "laporanjin":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            laporanjin(data_candi, data_user, data_bahan_bangunan)
        else :
            print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.") 
    
    #F10-Ambil Laporan Candi
    elif command == "laporancandi":
        if kondisi_user_pass[4] == "bandung_bondowoso" :
            laporancandi(data_candi)
        else :
            print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.") 

    #F11-Hancurkan Candi
    elif command == "hancurkancandi":
        if kondisi_user_pass[4] == "roro_jonggrang" :
            hancurkancandi(data_candi)
        else : 
            print("Ayam berkokok hanya dapat dilakukan oleh akun Roro Jonggrang.")
    
    #F12-Ayam Berkokok
    elif command == "ayamberkokok":
        if kondisi_user_pass[4] == "roro_jonggrang" :
            ayamberkokok(data_candi)
        else : 
            print("Ayam berkokok hanya dapat dilakukan oleh akun Roro Jonggrang.")

    #F14-Save
    elif command == "save":
        save(data_user, data_candi, data_bahan_bangunan)
    

    #F15-Help
    elif command == "help":
        help(kondisi_user_pass)
    
    #F16-Exit
    elif command == "exit":
        exit(data_user, data_candi, data_bahan_bangunan)

    #Command tidak terdefinisi di Spesifikasi
    else : 
        print("Perintah tidak dikenal")

    command = input(">>>")



