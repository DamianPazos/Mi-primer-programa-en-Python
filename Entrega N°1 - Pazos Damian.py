# Consigna: Crear un programa para calcular la nota final del estudiante en base a dos exámenes, los exámenes cuentan con un porcentaje distinto de la nota final
# nota_1  cuenta como el 40% de la nota final
# nota_2 cuenta como el 60% de la nota final

# Se ingresa el valor de la primer nota
nota_1 = float(input("Ingrese la nota del examen N°1 \n")) 
# Se ingresa el valor de la segunda nota
nota_2 = float(input("Ingrese la nota del examen N°2 \n")) 
# Se realiza el calculo de la nota final
nota_final = nota_1*0.4 + nota_2*0.6 
# Se devuelve por pantalla la nota final
print("La nota final es" ,nota_final)  
# Pausa del programa
input("Ingrese la tecla enter para salir") 