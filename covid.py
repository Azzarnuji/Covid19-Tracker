from os import system
import sys
from sys import platform
import requests
from flask import Flask,render_template,request
import json
import urllib.request
class Covid:
    '''Nama Mahasiswa'''
    jumlah_cvd = 0
    def __init__(self, nomor):
        URL = 'https://data.covid19.go.id/public/api/prov.json'
        response = urllib.request.urlopen(URL)
        data = json.loads(response.read())
        nomer = nomor
        data2 = data['list_data'][nomer]
        self.hari = data['last_date']
        self.nama_daerah = data2['key']
        self.doc_count = data2['doc_count']
        self.jumlah_kasus = data2['jumlah_kasus']
        self.jumlah_sembuh = data2['jumlah_sembuh']
        self.jumlah_meninggal = data2['jumlah_meninggal']
        self.jumlah_dirawat = data2['jumlah_dirawat']
        data3 = data2['penambahan']
        self.pen_positif = data3['positif']
        self.pen_sembuh = data3['sembuh']
        self.pen_meninggal = data3['meninggal']
        Covid.jumlah_cvd += 1
    def tampilkan_daftar(self):
        print("Jumlah Mahasiswa".Mahasiswa.jumlah_mhs)
    def tampilkan_profil(self):
        print("Last Date: ",self.hari)
        print ("Daerah:",self.nama_daerah)
        print ("Doc Count:",self.doc_count)
        print ("Jumlah Kasus:",self.jumlah_kasus)
        print ("Jumlah Sembuh:",self.jumlah_sembuh)
        print ("Jumlah Meninggal:",self.jumlah_meninggal)
        print ("Jumlah Dirawat:",self.jumlah_dirawat)
        print("Penambahan Positif: ",self.pen_positif)
        print("Penambahan Sembuh: ", self.pen_sembuh)
        print("Penambahan Meninggal: ",self.pen_meninggal)

def check_os():
    if platform == "linux" or platform == "linux2":
        system('clear')
    elif platform == "win32":
        system('cls')
    else:
        print('Os Not Compatible')
def main():
    URL = 'https://data.covid19.go.id/public/api/prov.json'
    response = urllib.request.urlopen(URL)
    data = json.loads(response.read())
    i = 0
    while i <= 33:
        data1 = data['list_data'][i]
        print (i,"Data Positif: ",data1['key'])
        i += 1
    tanya = int(input("Masukkan Nomor: "))
    check_os()
    # Membuat objek pertama dari kelas Karyawan
    covid1 = Covid(tanya)
    covid1.tampilkan_profil()
#print("Total karyawan :", Mahasiswa.jumlah_mhs)

if __name__ == '__main__':
    try:
        tanya = input("Mulai Program??y/n: ")
        if tanya == "y" or tanya == "Y":
            check_os()
            main()
        elif tanya == "n" or tanya == "N":
            print("Goodbye :)")
            sys.exit("Exiting")
        else:
            print("Input Salah")
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt\n"
                "Exiting")
        sys.exit()

