import math
from math import sqrt
import itertools as it
import numpy as np
import pandas as pd

datos = [67228, 1129900996, 48149351, 1792290985, 281468426, 1880845088, 404110176, 1536436218, 1540144398, 1586499895,
         1146774113, 166785366, 695487027, 296972168, 459231948, 255122718, 1470162014, 66126916, 1146031713, 574170448,
         1438693565, 1604365382, 764303542, 1549937687, 826067299, 231316438, 789972396, 1322153818, 1425923617,
         1728214046, 1377145447, 104780363, 106970401, 407717068, 2027927946, 672026885, 1139356622, 55065655,
         2070495375, 990751637, 2122047868, 1997591747, 1912638278, 28826403, 1301534646, 624366980, 1130733618,
         1157125423, 195077129, 1601261781, 141689063, 1956200965, 2042466832, 213948129, 938579025, 1430285960,
         2031668849, 1268357843, 1367587179, 520243612, 1328459947, 38851370, 139946902, 592988449, 2032740263,
         2095743765, 138680261, 779389632, 1698781971, 633499732, 6073898, 1152272277, 232630893, 1407181111, 255528166,
         1842075609, 1640505311, 430218144, 98906759, 173555735, 668445519, 1076880376, 136302516, 1618818710,
         1015735127, 1112769486, 2029153126, 1936274322, 2142826863, 1190326251, 2003128752, 483800845, 867714373,
         114020234, 782659714, 824475323, 1392263217, 786070407, 165934105, 1420728929]

datosNormalizados = []

for i in range(len(datos)):
    datosNormalizados.append(datos[i] / max(datos))
# print(datosNormalizados)

# Prueba CHI 2
print("PRUEBA DE CHI CUADRADO")
confianza = 0.1
n = len(datos)
c = int(n ** (1 / 2))
gradosLibertad = c - 1
frecuenciaEsperada = n / c

clases = []
aux = 0
for i in range(c):
    clases.append(aux + 0.1)
    aux = round(clases[i], 2)
    round(clases[i], 0)
print("las clases son", clases)

fo = []
for i in range(c):
    fo.append(0)
for i in range(n):
    if datosNormalizados[i] <= clases[0]:
        fo[0] = fo[0] + 1
    for j in range(c):
        if clases[j - 1] <= datosNormalizados[i] <= clases[j]:
            fo[j] = fo[j] + 1
print('frecuencia observada', fo)
print("frecuencia esperada", frecuenciaEsperada)

chiCuadrado = 0
for i in range(c):
    chiCuadrado = chiCuadrado + ((frecuenciaEsperada - fo[i]) ** 2 / frecuenciaEsperada)
print('chiCuadrado obtenido:', chiCuadrado)
print('Con 9 grados de libertad y confianza de 0.1 el chiCritico es 14.68')
print('El chiCalculado es mayor que el chiCritico por lo tanto el generador no pasa la prueba')
print()

# Corridas
print("PRUEBAS DE CORRIDAS")
print("1) CRECIMIENTO")

corridas = ['+']
# si el dato siguiente es mayor + sino -
numeroCorridas = 0
positivos = 0
negativos = 0

for i in range(n - 1):
    if datosNormalizados[i + 1] > datosNormalizados[i]:
        corridas.append('+')
        positivos = positivos + 1
    else:
        corridas.append('-')
print(corridas)

for i in range(n - 1):
    if corridas[i] != corridas[i + 1]:
        numeroCorridas = numeroCorridas + 1
negativos = n - positivos
print('numero de corridas', numeroCorridas)
print('positivos', positivos)
print('negativos', negativos)

# Aplicamos las fórmulas para media, varianza y Z.
media = ((2 * positivos * negativos) / (positivos + negativos)) + 1
print('media', media)

varianza = sqrt((2 * positivos * negativos * ((2 * positivos * negativos) - positivos - negativos))
                / (((positivos + negativos) ** 2) * (positivos + negativos + 1)))
print('varianza', varianza)
z = abs((numeroCorridas - media) / sqrt(varianza))
print("Z=", z)

[infCrit, supCrit] = [-1.65 * varianza + media, 1.65 * varianza + media]

print('limite inferior = ', infCrit, ' -  limite superior = ', supCrit)

if supCrit >= numeroCorridas >= infCrit:
    print('El numero de corridas está entre los limites - Pasa La Prueba')
else:
    print('No Pasa La Prueba de crecimiento')
print()
print("2) POR ENCIMA Y DEBAJO DE LA MEDIA")
promedio = np.mean(datosNormalizados)
print('Promedio = ', promedio)
corridas = []
# si dato mayor que promedio + sino -
numeroCorridas = 0
positivos = 0
negativos = 0

for i in range(n):
    if datosNormalizados[i] > promedio:
        corridas.append('+')
        positivos = positivos + 1
    else:
        corridas.append('-')
print(corridas)

for i in range(n - 1):
    if corridas[i] != corridas[i + 1]:
        numeroCorridas = numeroCorridas + 1
negativos = n - positivos
print('numero de corridas', numeroCorridas)
print('positivos', positivos)
print('negativos', negativos)

# Aplicamos las fórmulas para media, varianza y Z.
media = ((2 * positivos * negativos) / (positivos + negativos)) + 1
print('media', media)

varianza = sqrt((2 * positivos * negativos * ((2 * positivos * negativos) - positivos - negativos))
                / (((positivos + negativos) ** 2) * (positivos + negativos + 1)))
print('varianza', varianza)
z = abs((numeroCorridas - media) / sqrt(varianza))
print("Z=", z)

[infCrit, supCrit] = [-1.65 * varianza + media, 1.65 * varianza + media]

print('limite inferior = ', infCrit, ' -  limite superior = ', supCrit)

if supCrit >= numeroCorridas >= infCrit:
    print('El numero de corridas está entre los limites - Pasa La Prueba de corridas por encima y debajo de la media')
else:
    print('No Pasa La Prueba')

# Serie

print()
print("PRUEBA DE SERIES")
print("2 DIMENSIONES\n")

k = 2
grupos = int(n / k)
total_clases = math.ceil(sqrt(grupos))
dimension = math.ceil(total_clases ** (1 / 3))
print('Grupos', grupos)
print('Total de clases', total_clases)
print('Dimension', dimension)
grupos_total = np.zeros((grupos, k))
total_final_clases = dimension ** k
print('Clases por dimension', total_final_clases)
fe = grupos / total_final_clases
print('Frecuencia esperada', fe)

aux = 0
for i in range(0, grupos * 2, 2):
    grupos_total[aux] = datosNormalizados[i], datosNormalizados[i + 1]
    aux += 1

# print("Datos por grupos de 2 dimensiones: \n", grupos_total)

a = list(it.product([1, 2, 3, 4], repeat=2))

# print('codificacion para las clases \n', a)


auxDatos = np.zeros((grupos, k))

for i in range(grupos):
    for j in range(k):
        if grupos_total[i][j] <= 0.25:
            auxDatos[i][j] = 1
        else:
            if 0.25 <= grupos_total[i][j] <= 0.50:
                auxDatos[i][j] = 2
            else:
                if 0.50 <= grupos_total[i][j] <= 0.75:
                    auxDatos[i][j] = 3
                else:
                    auxDatos[i][j] = 4

# print('Datos codificados dependiendo las clases (Dimension 2) \n', auxDatos)
fo = []
for i in range(16):
    fo.append(0)

for i in range(grupos):
    for j in range(16):
        if np.array_equal(auxDatos[i], a[j]):
            fo[j] = fo[j] + 1
print('Frecuencias absolutas observadas\n', fo)
print()

df = pd.DataFrame({"Clases": a, "FrecObs": fo})
pd.set_option("max_rows", None)
df.head()
print(df)

chiCuadrado = 0
for i in range(total_final_clases):
    chiCuadrado = chiCuadrado + ((fe - fo[i]) ** 2 / fe)
print()
print('chiCuadrado obtenido:', chiCuadrado)
# 8 clases, 7 grados de libertad con confianza de 0.1
chiTabla = 12.02
print('chiCuadrado tabla (7 grados de libertad con confianza de 0.1) :', chiTabla)
print(chiCuadrado, '>', chiTabla)
print()
print('RESULTADO: \nComo el valor calculado es MAYOR que el valor critico, NO PASA LA PRUEBA!\n')

print("3 DIMENSIONES\n")

k = 3
grupos = int(n / k)
total_clases = math.ceil(sqrt(grupos))
dimension = math.ceil(total_clases ** (1 / 3))
print('Grupos', grupos)
print('Total de clases', total_clases)
print('Dimension', dimension)
grupos_total = np.zeros((grupos, k))
total_final_clases = dimension ** k
print('Clases por dimension', total_final_clases)
fe = grupos / total_final_clases
print('Frecuencia esperada', fe)

aux = 0
for i in range(0, grupos * 3, 3):
    grupos_total[aux] = datosNormalizados[i], datosNormalizados[i + 1], datosNormalizados[i + 2]
    aux += 1

# print("Datos por grupos de 3 dimensiones: \n", grupos_total)

a = list(it.product([1, 2, 3], repeat=3))

# print('codificacion para las clases \n', a)


auxDatos = np.zeros((grupos, k))

for i in range(grupos):
    for j in range(k):
        if grupos_total[i][j] <= 0.33:
            auxDatos[i][j] = 1
        else:
            if 0.33 <= grupos_total[i][j] <= 0.66:
                auxDatos[i][j] = 2
            else:
                auxDatos[i][j] = 3

# print('Datos codificados dependiendo las clases (Dimension 3) \n', auxDatos)
fo = []
for i in range(len(a)):
    fo.append(0)

for i in range(grupos):
    for j in range(len(a)):
        if np.array_equal(auxDatos[i], a[j]):
            fo[j] = fo[j] + 1
print('Frecuencias absolutas observadas\n', fo)
print()

df = pd.DataFrame({"Clases": a, "FrecObs": fo})
pd.set_option("max_rows", None)
df.head()
print(df)

chiCuadrado = 0
for i in range(total_final_clases):
    chiCuadrado = chiCuadrado + ((fe - fo[i]) ** 2 / fe)
print()
print('chiCuadrado obtenido:', chiCuadrado)
# 6 clases, 5 grados de libertad con confianza de 0.1
chiTabla = 9.24
print('chiCuadrado tabla (7 grados de libertad con confianza de 0.1) :', chiTabla)
print(chiCuadrado, '>', chiTabla)
print()
print('RESULTADO: \nComo el valor calculado es MAYOR que el valor critico, NO PASA LA PRUEBA!')
print()
# Poquer

def truncate(num, ka):
    integer = int(num * (10 ** ka)) / (10 ** ka)
    return float(integer)

print("PRUEBA DE POQUER")
print("3 decimales")

datosParaPoker = []

# CONVERTIMOS LOS NUMEROS A STRINGS Y CORTAMOS LA CADENA DESDE LA SEGUNDA POSICION HASTA LA
# QUINTA PARA OBTENER LOS PRIMEROS 3 DECIMALES

for i in range(len(datosNormalizados)):
    aux = (str(datosNormalizados[i]))
    datosParaPoker.append(aux[2:5])

for i in range(len(datosNormalizados)):
    if len(datosParaPoker[i]) == 1:
        datosParaPoker[i] = '000'

cartasIguales = 0
cartasDistintas = 0
dosIgualesUnaDistinta = 0

for i in range(len(datosParaPoker)):
    aux = datosParaPoker[i]
    if aux[0] == aux[1] and aux[0] == aux[2]:
        cartasIguales = cartasIguales + 1
    else:
        if aux[0] != aux[1] and aux[0] != aux[2] and aux[1] != aux[2]:
            cartasDistintas = cartasDistintas + 1
        else:
            dosIgualesUnaDistinta = dosIgualesUnaDistinta + 1

print('Frecuencia de cartas Iguales = ', cartasIguales, '-- Frecuencia Esperada = ', 0.01*len(datosNormalizados))
print('Frecuencia de cartas Distintas = ', cartasDistintas, '-- Frecencia Esperada = ', 0.72*len(datosNormalizados))
print('Frecuencia de dos iguales y una distinta = ', dosIgualesUnaDistinta, '-- Frecuencia Esperada = ', 0.24 *
      len(datosNormalizados))
foPoker = [cartasIguales, cartasDistintas, dosIgualesUnaDistinta]
print(foPoker)

fePoker = [0.01*len(datosNormalizados), 0.72*len(datosNormalizados), 0.24 * len(datosNormalizados)]


chiCuadrado = 0
for i in range(2):
    chiCuadrado = chiCuadrado + ((fePoker[i]-foPoker[i])**2/fePoker[i])
print()
print('chiCuadrado obtenido:', chiCuadrado)
# 3 clases, 2 grados de libertad con confianza de 0.1
chiTabla = 4.61
print('chiCuadrado tabla (2 grados de libertad con confianza de 0.1) :', chiTabla)
print(chiCuadrado, '<', chiTabla)
print()
print('RESULTADO: \nComo el valor calculado es menor que el valor critico, pasa la prueba! \n')


print("CONCLUSIONES")
print("Respecto a este generador, utilizando una alta confianza como la es del 10% solo pasó 2 pruebas de todas las que"
      " le hicimos.\n"
      "Las pruebas que pasó son las de corridas por encima y debajo de la media la cual no es una buena prueba y no nos"
      "dice mucho, la otra prueba que pasó fue la de poquer que nos indica si 3 numeros decimales siguen algun patron, "
      "nada más\n"
      "por lo tanto concluimos que este generador no es bueno en cuanto a independencia de los datos.")
