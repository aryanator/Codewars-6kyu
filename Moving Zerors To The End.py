def move_zeros(array):
    a=[]
    s=0
    for i in array:
        if i==0:
            s=s+1
        else:
            a.append(i)
    for j in range(s):
        a.append(0)
    return a
