T = int(input())
chaA, chaB, chaC, chaD, chaE = input().split()

chaA = int(chaA)
chaB = int(chaB)
chaC = int(chaC)
chaD = int(chaD)
chaE = int(chaE)

rit = 0

if chaA == T:
    rit = rit + 1

if chaB == T:
    rit = rit + 1

if chaC == T:
    rit = rit + 1

if chaD == T:
    rit = rit + 1

if chaE == T:
    rit = rit + 1

print(rit)