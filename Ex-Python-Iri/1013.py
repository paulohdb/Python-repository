value = input().split()

J, L, K = value

MaiorAB = (int(J) + int(L) + abs(int(J) - int(L))) / 2
SecondAB = (int(MaiorAB) + int(K) + abs(int(MaiorAB) - int(K))) / 2

print("%d eh o maior" %SecondAB)