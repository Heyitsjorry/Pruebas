import csv

def obtener_fichero_calificaciones():
    lista = []
    archivo_csv = r'C:\Users\jorry\Downloads\calificaciones.csv' #especificar ruta del archivo
    with open (archivo_csv,newline="") as archivo: #abrir archivo
        lector_csv = csv.reader(archivo,delimiter=";") #crear un lector con delimitador especifico ";"(devuelve un valor que necesita ser iterado)
        pos = 0 
        for linea in lector_csv:
            if pos != 0:
                for i in range(2, len(linea)):
                    if linea[i] == '':
                        linea[i] = '0.0'  # Usar punto decimal para valores numéricos
    
                Apellidos = linea[0]
                Nombre = linea[1]
                Asistencia = float(linea[2].replace('%', ''))
                Parcial1 = float(linea[3].replace(',', '.'))
                Parcial2 = float(linea[4].replace(',', '.'))
                Ordinario1 = float(linea[5].replace(',', '.'))
                Ordinario2 = float(linea[6].replace(',', '.'))
                Practicas = float(linea[7].replace(',', '.'))
                OrdinarioPracticas = float(linea[8].replace(',', '.'))
                
                lista.append({
                    'Apellidos': Apellidos,
                    'Nombre': Nombre,
                    'Asistencia': Asistencia,
                    'Parcial1': Parcial1,
                    'Parcial2': Parcial2,
                    'Ordinario1': Ordinario1,
                    'Ordinario2': Ordinario2,
                    'Practicas': Practicas,
                    'OrdinarioPracticas': OrdinarioPracticas
                })
            else:
                    pos = 1
    
    # Ordenar la lista de diccionarios por apellidos en orden alfabético
    lista.sort(key=lambda x: x['Apellidos'])

    return lista

def calcular_nota_final(lista_alumnos):
    for alumno in lista_alumnos:
        parcial1 = alumno['Ordinario1'] if alumno['Parcial1'] < 4 else alumno['Parcial1']
        parcial2 = alumno['Ordinario2'] if alumno['Parcial2'] < 4 else alumno['Parcial2']
        practicas = alumno['OrdinarioPracticas'] if alumno['Practicas'] < 4 else alumno['Practicas']
        
        nota_final = (parcial1 * 0.30) + (parcial2 * 0.30) + (practicas * 0.40)
        alumno['NotaFinal'] = nota_final

    return lista_alumnos

def clasificar_alumnos(lista_alumnos):
    aprobados = []
    suspensos = []

    for alumno in lista_alumnos:
        asistencia_ok = alumno['Asistencia'] >= 75.0
        parciales_ok = alumno['Parcial1'] >= 4 and alumno['Parcial2'] >= 4
        practicas_ok = alumno['Practicas'] >= 4
        nota_final_ok = alumno['NotaFinal'] >= 5.0

        if asistencia_ok and parciales_ok and practicas_ok and nota_final_ok:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)

    return aprobados, suspensos

# Especificar la ruta del archivo CSV
archivo_csv = r'C:\Users\jorry\Downloads\calificaciones.csv'

# 1. Obtener la lista de calificaciones ordenada por apellidos
lista_alumnos = obtener_fichero_calificaciones()

# 2. Calcular la nota final de cada alumno
lista_alumnos = calcular_nota_final(lista_alumnos)

# 3. Clasificar a los alumnos en aprobados y suspensos
aprobados, suspensos = clasificar_alumnos(lista_alumnos)

# Imprimir los resultados
print("Alumnos Aprobados:")
for alumno in aprobados:
    print(alumno)

print("\nAlumnos Suspensos:")
for alumno in suspensos:
    print(alumno)
