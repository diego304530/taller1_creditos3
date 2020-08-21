pais = input("ingrese su pais ")
Continente = input("ingrese continente ")

tipo_pais= str(type(pais))
tipo_continente = str(type(Continente))

print(tipo_pais[8:11])
print(f"El pais es {pais} con tipo de dato {tipo_pais[8:11]}")
print (f"El continente es {Continente} con tipo de dato  {tipo_continente[8:11]} ")