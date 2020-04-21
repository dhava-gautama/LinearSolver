from numpy import array
from tabulate import tabulate as tbl

def sidel(A,B,max_iter,guess_x1,guess_x2,guess_x3):
    x1 = guess_x1 #Memasukan nilai tebakan x1 ke x2
    x2 = guess_x2 #Memasukan nilai tebakan x2 ke x2
    x3 = guess_x3 #Memasukan nilai tebakan x3 ke x3
    tabel = []
    meane = 1
    for i in range(max_iter):
        x1 = (B[0]-A[0][1]*x2-A[0][2]*x3)/A[0][0]
        x2 = (B[1]-A[1][0]*x1-A[1][2]*x3)/A[1][1]
        x3 = (B[2]-A[2][0]*x1-A[2][1]*x2)/A[2][2]
        tabel.append([i+1,x1,x2,x3])
        if len(tabel) >= 2:
            errx1 = (tabel[i][1]-tabel[i-1][1])/tabel[i][1]
            errx2 = (tabel[i][2]-tabel[i-1][2])/tabel[i][2]
            errx3 = (tabel[i][3]-tabel[i-1][3])/tabel[i][3]
            meane = (errx1+errx2+errx3)/3
        if meane < 0.01:
            break
    table = tbl(tabel, headers=['Iterasi ke-', 'x1', 'x2','x3'], tablefmt='orgtbl')
    print(table)

A = array([[5,-2,3],[-3,9,1],[2,-1,-7]])
B = array([-1,2,3])

sidel(A,B,10,0,0,0)
