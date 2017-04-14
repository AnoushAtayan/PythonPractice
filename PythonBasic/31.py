def gcd(i, j):
    gcd = 1
    if i%j ==0:
        gcd = j
    elif j%i==0:
        gcd=i
    else:
        for n in range(int(i/2), 0, -1):
            if i%n ==0 and j%n ==0:
                gcd = n
                break
    return gcd

print gcd(12, 81)

