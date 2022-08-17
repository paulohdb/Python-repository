Value1 = input().split()
Value2 = input().split()

x1, y1 = Value1
x2, y2 = Value2

distance = ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5

print("{:.4f}" .format(distance))