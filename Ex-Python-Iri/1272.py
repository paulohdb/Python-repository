
n = int(input())


for i in range(n):

    words = input()

    lst = words.split()

    taman = len(lst)

    ocult = ""

    for j in range(taman):

        palavra = lst[j]

        ocult = ocult + palavra[0]

    print(ocult)