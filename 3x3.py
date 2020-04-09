# Find solution of linear problem using gauss eliminition
# Dhava Gautama
# https://github.com/dhava-stmkg/Gauss_LinearSolver

matrik = [25,5,1,106.8],[64,8,1,177.2],[144,12,1,279.2]

print(matrik)

# Operasi pertama : R1/R1(1,1)
operand_temp = matrik[0][0]
for i in range(0,4):
    temp = matrik[0][i]/operand_temp
    matrik[0][i] = temp
print(matrik)

# Operasi kedua : R2-R1*R2(2,1) , R3-R1*R3(3,1)
for j in range(1,3): # Untuk R2 dan R3
    operand_temp = matrik[j][0] # matrik (j,0)
    for i in range(0,4):
        temp = matrik[0][i]*operand_temp
        matrik[j][i] =  matrik[j][i]-temp
print(matrik)

# Operasi ketiga : R2/R2(2,2)
operand_temp = matrik[1][1]
for i in range(0,4):
    temp = matrik[1][i]/operand_temp
    matrik[1][i] = temp
print(matrik)

# Operasi keempat : R1-R2*R1(1,2), R3-R2*R3(3,2)
# R1-R2*R1(1,2)
operand_temp = matrik[0][1]
for i in range(0,4):
    temp = matrik[1][i] * operand_temp
    matrik[0][i] = matrik[0][i] - temp
# R3-R2*R3(3,2)
operand_temp = matrik[2][1]
for i in range(0, 4):
    temp = matrik[1][i] * operand_temp
    matrik[2][i] = matrik[2][i] - temp

print(matrik)

# Operasi kelima : R3/R3(3,3)
operand_temp = matrik[2][2]
for i in range(0,4):
    temp = matrik[2][i]/operand_temp
    matrik[2][i] = temp
print(matrik)

# Operasi keenam : R1-R3*R1(1,3), R2-R3*R2(2,3)
for j in range(0,2):
    operand_temp = matrik[j][2]
    for i in range(0,4):
        temp = matrik[2][i]*operand_temp
        matrik[j][i] =  matrik[j][i]-temp
print(matrik)

# Hasil
for i in range(0,3):
    print('x',i+1,'=',matrik[i][3])
