#Santiago Rache
#Grupo: 213022_470
#Programa: Ingeniería de sistemas
#Código Fuente: Autoría Propia

#Validación:sólo acepta enteros >= mínimo (el 0 es válido)

def leer_entero(mensaje, minimo, mensaje_error):
    while True:
        dato = input (mensaje)
        if dato.isdecimal() and int(dato) >= minimo:
            return int(dato)
        print(mensaje_error)

#Datos iniciales, el usuario llena la matriz
#Formato por fila: [ID del cliente, Duración (segundos), Número de clics]
def pedir_sesiones():
    matriz=[]

    cantidad = leer_entero(
        "Número de sesiones (mínimo 5): ",
        5,
        "Error: debe digitar un número entero de 5 o más, "
        "sin letras, espacios ni signos negativos. Intente de nuevo."
    )
    for i in range (cantidad):
        print(f"\nSesión {i+1}")
        id_cliente = leer_entero(
            "ID del cliente: ",
            0,
            "Error: el ID debe ser un número entero (0 o mayor), "
            "sin letras, espacios ni signos negativos."
        )
        duración = leer_entero(
            "Duración (segundos): ",
            0,
            "Error: la duración debe ser un número entero (0 o mayor), "
            "sin letras, espacios y signos negativos."
        )
        clics = leer_entero(
            "Número de clics: ",
            0,
            "Error: los clics deben ser un número entero (0 o mayor), "
            "sin letras, espacios o signos negativos."
        )
        matriz.append([id_cliente, duración, clics])
    return matriz

#Módulo: clasificación de compromiso de una sesión
def clasificar_compromiso(duración, clics):
    if duración > 180 and clics > 8:
        return "Alto"
    elif duración < 60 and clics <3:
        return "Bajo"
    else:
        return "Medio"

#Salida: Informe con ID y clasificación final
def generar_informe(matriz):
    print("\nINFORME DE COMPROMISO DE SESIONES")
    print("-"*35)
    for fila in matriz:
        id_cliente = fila[0]
        clasificacion = clasificar_compromiso(fila[1], fila[2])
        print(f"Cliente {id_cliente}: {clasificacion}")

#Programa principal
def main():
    sesiones = pedir_sesiones()
    generar_informe(sesiones)

main()