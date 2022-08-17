N = int(input())
print(N)

S100 = N // 100
N = N - S100 * 100 

S50 = N // 50
N = N - S50 * 50

S20 = N // 20
N = N - S20 * 20

S10 = N // 10
N = N - S10 * 10

S5 = N // 5
N = N - S5 * 5

S2 = N // 2
N = N - S2*2

S1 = N // 1
N = N - S1*1

print("{} nota(s) de R$ 100,00" .format(S100))
print("{} nota(s) de R$ 50,00" .format(S50))
print("{} nota(s) de R$ 20,00" .format(S20))
print("{} nota(s) de R$ 10,00" .format(S10))
print("{} nota(s) de R$ 5,00" .format(S5))
print("{} nota(s) de R$ 2,00" .format(S2))
print("{} nota(s) de R$ 1,00" .format(S1))