def lists(a,b):
    out=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                if a[i] not in out:
                    out.append(a[i])
    return out

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]

c= lists(a,b)
print (c)


