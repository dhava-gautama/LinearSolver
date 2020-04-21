# Find solution of linear problem using gauss eliminition
# Dhava Gautama
# https://github.com/dhava-stmkg/LinearSolver

#matrik = [1,2,3,-1,10],[2,5,4,8,8],[4,2,2,1,-2],[6,4,-1,-2,4]
matrik = [4,4,1,1,11],[2,1,2,-2,2],[1,-1,-1,2,0],[1,1,1,-1,2]

print(matrik)

# Operasi pertama : R1/R1(1,1)
operand_temp = matrik[0][0]
for i in range(0,5):
    temp = matrik[0][i]/operand_temp
    matrik[0][i] = temp
print(matrik)

# Operasi kedua : R2-R1*R2(2,1) , R3-R1*R3(3,1), R4-R1*R4(4,1)
for j in range(1,4): # Untuk R2 dan R3
    operand_temp = matrik[j][0] # matrik (j,0)
    for i in range(0,5):
        temp = matrik[0][i]*operand_temp
        matrik[j][i] =  matrik[j][i]-temp
print(matrik)

# Operasi ketiga : R2/R2(2,2)
operand_temp = matrik[1][1]
for i in range(0,5):
    temp = matrik[1][i]/operand_temp
    matrik[1][i] = temp
print(matrik)

# Operasi keempat : R1-R2*R1(1,2), R3-R2*R3(3,2), R4-R2*R4(4,2)
# R1-R2*R1(1,2)
operand_temp = matrik[0][1]
for i in range(0,5):
    temp = matrik[1][i] * operand_temp
    matrik[0][i] = matrik[0][i] - temp
# R3-R2*R3(3,2), R4-R2*R4(4,2)
for j in range(2,4): # Untuk R2 dan R3
    operand_temp = matrik[j][1] # matrik (j,0)
    for i in range(0,5):
        temp = matrik[1][i]*operand_temp
        matrik[j][i] =  matrik[j][i]-temp
print(matrik)


# Operasi kelima : R3/R3(3,3)
operand_temp = matrik[2][2]
for i in range(0,5):
    temp = matrik[2][i]/operand_temp
    matrik[2][i] = temp
print(matrik)

# Operasi keenam : R1-R3*R1(1,3), R2-R3*R2(2,3), R4-R3*R4(4,3)
for j in range(0,4):
    if j != 2:
        operand_temp = matrik[j][2]
        for i in range(0,5):
            temp = matrik[2][i]*operand_temp
            matrik[j][i] =  matrik[j][i]-temp
print(matrik)

# Operasi ketujuh : R4/R4(4,4)
operand_temp = matrik[3][3]
for i in range(0,5):
    temp = matrik[3][i]/operand_temp
    matrik[3][i] = temp
print(matrik)

# Operasi kedelapan : R1-R4*R1(1,4), R2-R4*R2(2,4), R3-R4*R3(3,4)
for j in range(0,4):
    if j != 3:
        operand_temp = matrik[j][3]
        for i in range(0,5):
            temp = matrik[3][i]*operand_temp
            matrik[j][i] =  matrik[j][i]-temp
print(matrik)

# Hasil
for i in range(0,4):
    print('x',i+1,'=',matrik[i][4])
