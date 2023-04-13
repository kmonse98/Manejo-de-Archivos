import sys
# Comprobación de seguridad, ejecutar solo si se escriben 2 argumentos realmente
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("ERROR: Introdujo uno (1) o más de dos (2) argumentos ")
    print("EJEMPLO: python ejemplo1.py 'Texto' 5")
    
print("Nota: El argumento 0 es el nombre del archivo:",sys.argv[0])


    