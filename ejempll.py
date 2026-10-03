import numpy as np

# Matriz de 2 filas y 3 columnas (shape: 2, 3)
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Vector de 3 elementos (shape: 3,)
vector = np.array([10, 20, 30])

# --- AQUÍ OCURRE EL BROADCASTING ---
resultado = matriz + vector
print(resultado)