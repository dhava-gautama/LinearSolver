# Find solution of linear problem using Gauss-Seidel iterative method
# Dhava Gautama
# https://github.com/dhava-stmkg/LinearSolver

from numpy import array
from tabulate import tabulate as tbl

'''
Algoritma program linear solver menggunakan metode Gauss-Seidel
1. Definisikan fungsi dalam bentuk matriks
2. Hitung nilai x1, x2, dan x3 secara berurutan
3. Menghitung nilai error dari x1, x2 dan x3
4. Program berhenti ketika nilai error memenuhi kriteria atau telah mencapai iterasi maksimum
'''

def sidel(A,max_iter,guess_x1,guess_x2,guess_x3):
    x1 = guess_x1 #Memasukan nilai tebakan x1 ke x2
    x2 = guess_x2 #Memasukan nilai tebakan x2 ke x2
    x3 = guess_x3 #Memasukan nilai tebakan x3 ke x3
    tabel = [] #Membuat tabel kosong
    for i in range(max_iter): #Di ulang sampai iterasi maksimum
        x1 = (A[0][-1]-A[0][1]*x2-A[0][2]*x3)/A[0][0] #Rumus x1
        x2 = (A[1][-1]-A[1][0]*x1-A[1][2]*x3)/A[1][1] #Rumus x2
        x3 = (A[2][-1]-A[2][0]*x1-A[2][1]*x2)/A[2][2] #Rumus x3
        tabel.append([i+1,x1,x2,x3]) #Memasukan nilai indeks,x1,x2,x3 kedalam array tabel
        if len(tabel) >= 2: #Jika data di array tabel lebih dari 2
            errx1 = abs((tabel[i][1]-tabel[i-1][1])/tabel[i][1]) #hitung error x1
            errx2 = abs((tabel[i][2]-tabel[i-1][2])/tabel[i][2]) #hitung error x2
            errx3 = abs((tabel[i][3]-tabel[i-1][3])/tabel[i][3]) #hitung error x3
            if (errx1 < 0.01 and errx2 < 0.01 and errx3 < 0.01): #jika nilai error x1, x2, x3 memenuhi kriteria
                print("Solusi ditemukan pada iterasi ke", i + 1) #print keterangan
                break #hentikan iterasi
    table = tbl(tabel, headers=['Iterasi ke-', 'x1', 'x2','x3'], tablefmt='orgtbl') #membuat tabel dari data di array tabel
    print("Gauss–Seidel method") #print keterangan
    print(table) #print tabel

no1 = array([[25,5,1,106.8],[64,8,1,177.2],[144,12,1,279.2]])
no2 = array([[5,-2,3,-1],[-3,9,1,2],[2,-1,-7,3]])
no3 = array([[2,-1,-7,3],[-3,9,1,2],[5,-2,3,-1]])

sidel(no2,10,0,0,0)
