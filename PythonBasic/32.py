def lcm(x, y):
    list = []
    if x>y:
        lcm = x
    else:
        lcm = y

    while(True):
        if lcm%x==0 and lcm%y==0:
            return lcm
            break
        lcm+=1

print lcm(5, 125)