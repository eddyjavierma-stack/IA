
# Mascara booleana
import numpy as np

matriz = np.array([[1,6,7],[7,3,7]])

# Aqui puedo poner e resultado en booleanos
mascara = matriz >5
# print(mascara)

# Aqui puedo poner el resultado en numeros 
mascara = matriz[matriz >5]
print(mascara)


matriz_1 = np. array([[7,8,4,6],[7,9,8,7]])
resultado = matriz_1[(matriz_1 >=7)&(matriz_1 <10)]
print(resultado)

# 
# Metodo np.where(), tiene 2 fucnicones
# Primera indices, devuele los indices de la coindicion dada


datos = np.array([2,4,5,7,5,8,7,9])
indices = np.where(datos >=5)
print(indices)

# Segundo cambio cmabia el valor de los numeros del arreglo a un valor que uno le indique 

valores = np.array([41,45,21,78,19,47,48])   # Aqui si desea crear 3 opciones se separan con coma y toso va dentro del ()
resultado = np.where(valores >=70, "Demasiada edad", np.where( valores >=45,"Mayor de edad", "Menor de la edad indicada"))
print(resultado)

# Valores Faltantes (NaN)
#Con los valors faltantes no se pueden hacer ejercicios y si lo resuleves te sale nan
datos_1 = np.array([1,2, np.nan, 5,7, np.nan])
promedio = np.mean(datos_1)
print(promedio)  # Aquie el resultado es nan

promedio_1= np.nanmean(datos_1)
print(promedio_1) # No toma en cuenta el nan

promedoi= np.isnan(datos_1)
print(promedoi)  # Aqui deveuelve la mascara booleana
print(promedoi.sum())  # Aqui devuelve la cantidad de np.nan existen en el arreglo.

limpio = datos_1[~np.isnan(datos_1)]
print(limpio) # Aqui elimina los valores np.nan y me muestra sin np.nan


rellenar = np.where(np.isnan(datos_1), 1,datos_1)
print(rellenar) # Aqui rellenamos con uno utilizando el metodo where y el metodo isnan