#!/usr/bin/env python
import numpy as np
def esCuasiOrden(R) :
	n = np.size(R,0)
	for i in range(0, n) :
		for j in range(0, n) :
			# Primero, revisar si es refleja
			if i==j and R[i,i] == 0:
				return False
			# Si la casilla es 1, revisar la columna de j 
			# para ver con quien se relaciona
			elif R[i,j] == 1 :
				for k in range(0, n) :
					if R[j,k]==1 and R[i,k] ==0:
						print(i," se relaciona con ",j, " y ", j," se relaciona con",k, " pero ",i," no se relaciona con ",k)
						return False 
	return True

def mayorEquivalencia(R) :
	n = np.size(R,0)
	ansR = np.zeros((n,n), dtype=np.int)
	for i in range(0, n):
		for j in range(0, n):
			if R[i,j] == 1 and R[j,i] == 1 :
				ansR[i,j] = 1
	return ansR

n = input("Ingrese el numero de elementos del conjunto: ")
print("Ingrese los indices de los pares de elementos \
 que pertenecen a la relacion. Ingrese un 0 para terminar")
R = np.zeros((n,n), dtype=np.int) #Crea array de tamano nxn llena de 0s
while(True):
	i = input("Primer índice: ")
	if i == 0:
		break
	j = input("Segundo índice: ")
	R[i-1,j-1] = 1
if esCuasiOrden(R):
	print("R es es cuasi-orden")
	print("La matriz representante de la mayor relación de equivalencia en R es")
	maxR = mayorEquivalencia(R)
	print(np.transpose(maxR)) # Transpone la matriz para que se vea
					# de la manera estandar
else:
	print("R no es cuasi-orden")



