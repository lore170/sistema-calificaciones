# Sistema de calificaciones 
calificaciones = [85, 67, 92, 74, 58] 

print("SISTEMA DE CALIFICACIONES") 
print("-" * 30) 

# Mostrar el vector inicial 
print("\nCalificaciones iniciales:") 
for indice in range(len(calificaciones)): 
    print(f"Estudiante {indice + 1}: {calificaciones[indice]}") 

# Acceder a un elemento mediante su índice 
print("\nCalificación almacenada en el índice 2:") 
print(calificaciones[2]) 

# Calcular el promedio 
suma = 0 
for nota in calificaciones: 
    suma += nota 
promedio = suma / len(calificaciones) 

# Buscar la calificación más alta y la más baja 
calificacion_mayor = max(calificaciones) 
calificacion_menor = min(calificaciones) 

# Contar estudiantes aprobados y reprobados 
aprobados = 0 
reprobados = 0 
for nota in calificaciones: 
    if nota >= 70: 
        aprobados += 1 
    else: 
        reprobados += 1 

# Presentar los resultados 
print(f"\nPromedio: {promedio:.2f}") 
print(f"Calificación más alta: {calificacion_mayor}") 
print(f"Calificación más baja: {calificacion_menor}") 
print(f"Estudiantes aprobados: {aprobados}") 
print(f"Estudiantes reprobados: {reprobados}") 

# Modificar una calificación 
print("\nModificación de una calificación:") 
print(f"Valor anterior del índice 1: {calificaciones[1]}") 
calificaciones[1] = 79 
print(f"Nuevo valor del índice 1: {calificaciones[1]}") 

# Mostrar el vector actualizado 
print("\nCalificaciones actualizadas:") 
for indice in range(len(calificaciones)): 
    estado = "Aprobado" if calificaciones[indice] >= 70 else "Reprobado" 
    print(f"Estudiante {indice + 1}: {calificaciones[indice]} - {estado}") 

# Calcular nuevamente el promedio 
nuevo_promedio = sum(calificaciones) / len(calificaciones) 
print(f"\nNuevo promedio: {nuevo_promedio:.2f}")