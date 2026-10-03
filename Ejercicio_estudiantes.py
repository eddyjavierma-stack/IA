# Analisis numérico de Datos de Estudiantes
# Objetivo: Normalizar las features utilizando su propio
#           mínimo y máximo para llevar sus valores al rango [0, 1].


from re import X

import numpy as np

# Creare una lista de estudientes con todos sus valores

nombre_estudiante = np.array(['Eddy', 'Evelyn', 'Brianna', 'Conciencia', 'Amarillo', 'Negrita', 'Chucky', 'Mishu'])
edad = np.array([37, 30, 29, 22, 25, 19, 24, 35])
horas_estudio = np.array([5, 8, 3, 10, 4, 6, 2, 9])
asistencia = np.array([90, 95, 75, 98, 85, 88, 70, 97])  # La verdadera forma estan en columnas estan que parecen horizontales
tareas_entregadas = np.array([8, 10, 6, 10, 7, 8, 5, 10])
nota_examen = np.array([7.5, 8.5, 6.0, 9.0, 7.0, 7.5, 5.5, 9.2])
nota_final = np.array([8.0, 9.0, 6.5, 9.5, 7.2, 8.0, 6.0, 9.6])

X = np.stack([ edad, horas_estudio, asistencia, tareas_entregadas, nota_examen], axis=1)
print(X)
print(X.shape)
print(X.ndim)

y = nota_final

print(y[0])
print(y.shape)
print(y.ndim)

print(x[4,2])  # Esto pide el primero la fila te da la posicion y el segundo la 



promedio = np.mean(y)  # Saca el promedio general de las notas
print (promedio)
nota_minima = np.min(y)
nota_maxima = np.max(y)
nota_mediana = np.median(y)

varianza_notas = np.var(y)  # Para sacar la varianza 
desviacion_estandar = np.std(y)

q1 = np.percentile(y, 25)  # Es para medir el 25% de los valores bajos del 50%
q3 = np.percentile(y, 75)  # Es para medir el 25% de los valores altos del 50%
iqr = q3-q1    # Es para medir la variacion entre elementos

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 -1.5 * iqr
outliers_inferiores = np.where(y <= limite_inferior)  # Es para medir los valores atípicos bajos
outliers_superiores = np.where(y > limite_superior)    # Es para medir los valores atípicos altos

correlacion = np.corrcoef(horas_estudio, y)  # Es la correlacion entre horas de estudio y las notas (Correlacion positiva)
covarianza = np.cov(horas_estudio, y)   # Es para medir la covarianza, la relacion entre la varibale horas_estiudio y la variable y.

# Vamos a calcular el min-max de horas de estudio
minimo_horas = np.min(horas_estudio)
maximo_horas = np.max(horas_estudio)
horas_nomalizadas= (horas_estudio - minimo_horas)/ (maximo_horas - minimo_horas)

meida_horas = np.mean(horas_estudio)
desviacion_horas = np.std(horas_estudio)
horas_estandarizadas = (horas_estudio - meida_horas)/ desviacion_horas

valores_maximos = np.min(horas_nomalizadas)
valores_minimos = np.max(horas_nomalizadas) 

# Sacar los valores maximos y minimos de asistencia
minimo_asistencia = np.min(asistencia)
maximo_asitencia = np.max(asistencia)
asistencia_normalizada = (asistencia - minimo_asistencia)/ (maximo_asitencia - minimo_asistencia)

min_global =np.min(X, axis=0)
max_global =np.max(X,axis=0)

x_min_max_global = (X - min_global)/(max_global- min_global)
print(x_min_max_global)

min_x = np.min(x_min_max_global, axis=0)
max_x = np.max(x_min_max_global, axis=0)

print(min_x)
print(max_x)

# Para visualizar la tabla completa
for nombre, datos in zip(nombre_estudiante, X):
    print(f"Estudiante: {nombre} -> Datos: {datos}")
