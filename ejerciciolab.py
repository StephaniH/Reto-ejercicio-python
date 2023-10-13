#Declaracion de variables
numero = 1
primos = []

#solicitar número
n = int(input("Ingresar un valor grande: "))

#Realizacion de operaciones
while numero <= n:
	count = 1
	x = 0
	
	while count <= numero:
		if numero % count == 0:
			x += 1

		count += 1

	if x == 2:
		primos.append(numero)

	numero += 1

#Impresion de los resultados
print("Los números primos del 1 al {} son:\n{}".format(n, primos))

#Guardado de los resultados en archivo de texto
f = open('results.txt', 'a')
f.write("Los números primos del 1 al {} son:\n{}\n\n".format(n, primos))
f.close()