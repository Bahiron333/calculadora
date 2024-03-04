def sep_num(lista):
    num_par=[]
    num_impar=[]
    n=[]
    for n in lista:
        if n%2==0:
            num_par.append(n)
        else:
            num_impar.append(n)
    return num_par,num_impar

p,s = sep_num([1,2,6,7,9])


print(f"numero par: {p}")
print(f"numero impar: {s}")
