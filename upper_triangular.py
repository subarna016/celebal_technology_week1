#upper triangular
rows = int(input("Enter the number of rows: "))
i = rows
while i>=1:
    j=rows
    while j>i:
        print(' ', end=' ')
        j = j-1
    k = 1
    while k<=i:
        print('*', end=' ')
        k = k+1
    print()
    i = i - 1