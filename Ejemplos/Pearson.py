def avg(l):
    suma = 0
    for i in l:
        suma += i

    if len(l) == 0:
        return 0
    return suma/len(l)

def desv(m, i1, i2):
    desviaciones = []
    for u in m:
        if u[i1] and u[i2]:
            desviaciones.append(u[i2] - u[i1])

    return desviaciones

def pred(m, user, item):
    desvs = []
    for i in range(len(m[0])):
        if i != item:
            desvs.append([i,desv(m, i, item)])

    sum1 = 0
    total = 0
    for d in desvs:
        temp = (m[user][d[0]] + avg(d[1]))*len(d[1])
        sum1 += temp
        total += len(d[1])

    return sum1/total

m = [[5,3,4], # each col is a movie, each row is user
     [None,2,4],
     [4,2,None],

     [1,2,3],[1,1,2],[3,3,3],[1,5,3],[5,5,4],[4,5,3],[3,2,1]]


print(pred(m, 2, 2))
print(pred(m, 1, 0))