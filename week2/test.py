import numpy as np

xp = [3, 4]
yp = [24.08, 28.96]
result = np.interp(input("Ingrese el valor a interpolar:\n"), xp, yp)
print(result)
