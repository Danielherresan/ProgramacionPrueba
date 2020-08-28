a = int (input("Ingrese el primer número entero : "))
b = int (input("Ingrese el segundo número entero : "))
print (a,b)

if (a == b):
    print("Son numeros iguales")
elif (a>b):
    print("El numero A", a, "Es mayor que el numero", b)
else:
    print(f"el numero B {b} es mayor que A {a}")

#Dada una temperatura determinar si el paciente esta sano o no
# Temperatura menor a 36 grados hipotermia
# Temperatura en el intevalo a 36-37.5 normal
# Temperatura en el intevalo a 37.5-38 Alerta
# Temperatura mayor a 38- Fiebre
#Muestre el nombre del paciente y su estado

name = input("Ingrese el nombrel del paciente : ")
temperatura = float (input("Ingrese la temperatura del paciente :"))
if (temperatura < 36) :
    print(f"El paciente llamado {name} se encuentra en estado de hipotermia")
elif (temperatura>=36 and temperatura< 37.5) :
    print(f"El paciente llamado {name} se encuentra en estado favorable") 
elif (temperatura>=37.5 and temperatura< 38):
    print(f"El paciente llamado {name} se encuentra en estado de alerta") 
else: 
    print (f"El paciente llamado {name} se encuentra en estado de fiebre")
