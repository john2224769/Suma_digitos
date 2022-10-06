# Hacer el diagrama de flujo y programa en python que lea un numero entero positivo de cualquier cantidad de cifras, que calcule la suma de sus digitos y que lo imprima 
# junto con el numero leido 



print("\n---------------------------------------------")
print("------ Suma de digitos de un numero ---------")
print("---------------------------------------------\n")

#input
n=int(input("\nIngrese un numero para sumar sus digitos: "))

#processing

sum=0
origin=n
digito=0
while n!=0:
    digito=n%10
    n=n//10
    sum=sum+digito
print("\nLa suma de los digitos del numero "+str(origin)+" es: "+str(sum))