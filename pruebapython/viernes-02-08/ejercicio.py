nota =  input('Ingrese sus notas: ')

nota = [float(nota) for nota in nota.split()] #(split) divide el string en una lista donde cada elemento es una nota

promedio = sum(nota) / len(nota)

print("Su promedio es: ", promedio)