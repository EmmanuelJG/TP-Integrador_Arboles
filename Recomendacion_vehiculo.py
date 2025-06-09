
#Definicion de funciones

def recorrer_arbol(nodo):
    # Corrobora que no este en uno de los nodos hoja, para poder continuar
    if nodo[3] is not None:
        print(f"\nRecomendacion: {nodo[3]}")
        return

    # Toma la respusta de la primer pregunta (nodo raiz)
    respuesta = input(nodo[0] + " (si/no): ").strip().lower()
    
    # Dependiendo de la respuesta sigue por el nodo que corresponda
    if respuesta == "si":
        recorrer_arbol(nodo[1])
    elif respuesta == "no":
        recorrer_arbol(nodo[2])
    else:
        print("Respuesta incorrecta. Escriba 'si' o 'no', para poder continuar.")
        recorrer_arbol(nodo)

def main():
    # Arbol de decision creado a base de listas
    arbol = [
        "¿Querés un vehículo eléctrico?",

        # Si elije opcion SI, consulta si quiere un vehiculo ligero.
        [
            "¿Queres un vehículo ligero?",
            [None, None, None, "Te convendria una bicicleta eléctrica Volkswagen Cargo e-bike."],
            [None, None, None, "Te convendria un auto eléctrico Volkswagen ID.4."],
            None
        ],

        # Si elije opcion NO, consulta si quiere un vhiculo grande..
        [
            "¿Queres un vehiculo grande?",
            [None, None, None, "Te convendria una camioneta, tenemos disponible una Volkswagen Amarok."],
            
            # Si elije opcion NO, consulta si quiere un vehiculo no tan grande y familiar.
            [
                "¿Queres un vehiculo no tan grande y familiar?",
                [None, None, None, "Te convendria una camioneta para ciudad, tenemos disponible Volkswagen Suran."],
                [None, None, None, "Te convendria un auto para ciudad, tenemos disponible el Volkswagen Polo."],
                None
            ],
            None
        ],
        None
    ]

# Mensaje de inicio del programa siguiendo con el recorrido del arbol.
    print("Bienvenido al sistema de recomendacion de vehiculos Volkswagen, a continuacion debera contestar las siguientes preguntas:")
    recorrer_arbol(arbol)


#Codigo de ejecucion.

main()

print("Gracias por usar nuestro sistema de recomendacion.")