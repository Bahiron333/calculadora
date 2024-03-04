def par_impar(num):
    if num%2 == 0:
        return "par"
    else:
        return "impar"
        
num = int(input("Ingrese un numero: "))

resultado = par_impar(num)
print(f"Resultado: {resultado}")