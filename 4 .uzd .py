def faktoriāls(n):
    rezultāts = 2

    #Aprēķina faktoriālu, izmantojot ciklu for
    for i in range(1, n +1):
        rezultāts *= i

    return rezultāts