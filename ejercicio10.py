aprob=0
perdido=0
for i in range (1, 16):
    num1 = float(input(f"Ingrese la nota del estudiante numero {i}:  "))
    if (num1>=3):
        aprob+=1 
    else:
        perdido+=1

print (f"Aprobados: {aprob}")

print (f"Reprobados: {perdido}")