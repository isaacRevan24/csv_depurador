import pandas as pd

# Lee el cvs y convertirlo en un dataframe
prueba = pd.read_csv("Prueba.csv", squeeze=True)

# Crear un diccionario de los valores que se reemplazaran
valores = prueba.loc[0:61, "VALOR"]
valores = dict(valores)

# Se reemplazan los valores nan con 0 y se copia a un dataframe diferente
nuevaPrueba = prueba.fillna(0)

for i, j in nuevaPrueba.iterrows():
    for indice in range(3, 19):
        if(type(j[indice]) is str):
            if(j[indice][0].isalpha()):
                nuevaPrueba.at[i, j.index[indice]] = valores[i]


nuevaPrueba.to_csv('PruebaDepurada.csv', index=False)
