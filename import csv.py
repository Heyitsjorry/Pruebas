import csv

archivo_csv = r"C:\Users\jorry\Downloads\datos.csv"
datos_diccionario=[]

with open (archivo_csv,newline="") as archivo:
    lector_csv= csv.DictReader(archivo,delimiter= ";")

    for fila in lector_csv:
        datos_diccionario.append(dict(fila))
        
for fila in datos_diccionario:
    print(fila)