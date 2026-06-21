# Lista donde se almacenarán las tareas
tareas = []


# Función para agregar una tarea
def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")

    tarea = {
        "nombre": nombre,
        "completada": False
    }

    tareas.append(tarea)

    print("✅ Tarea agregada correctamente.")


# Función para mostrar todas las tareas
def mostrar_tareas():

    if len(tareas) == 0:
        print("⚠️ No hay tareas registradas.")
        return

    print("\n===== LISTA DE TAREAS =====")

    for i, tarea in enumerate(tareas):

        estado = "Completada ✓" if tarea["completada"] else "Pendiente"

        print(f"{i + 1}. {tarea['nombre']} - {estado}")


# Función para marcar una tarea como completada
def completar_tarea():

    if len(tareas) == 0:
        print("⚠️ No hay tareas registradas.")
        return

    mostrar_tareas()

    try:
        numero = int(input("Ingrese el número de la tarea completada: "))

        if 1 <= numero <= len(tareas):
            tareas[numero - 1]["completada"] = True
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ Número de tarea inválido.")

    except ValueError:
        print("❌ Debe ingresar un número.")


# Función para eliminar una tarea
def eliminar_tarea():

    if len(tareas) == 0:
        print("⚠️ No hay tareas registradas.")
        return

    mostrar_tareas()

    try:
        numero = int(input("Ingrese el número de la tarea que desea eliminar: "))

        if 1 <= numero <= len(tareas):

            tarea_eliminada = tareas.pop(numero - 1)

            print(f"🗑️ Tarea '{tarea_eliminada['nombre']}' eliminada correctamente.")

        else:
            print("❌ Número de tarea inválido.")

    except ValueError:
        print("❌ Debe ingresar un número.")


# Función para buscar tareas
def buscar_tarea():

    if len(tareas) == 0:
        print("⚠️ No hay tareas registradas.")
        return

    nombre_buscar = input("Ingrese el nombre de la tarea a buscar: ")

    encontrada = False

    print("\n===== RESULTADOS =====")

    for tarea in tareas:

        if nombre_buscar.lower() in tarea["nombre"].lower():

            estado = "Completada ✓" if tarea["completada"] else "Pendiente"

            print(f"- {tarea['nombre']} ({estado})")

            encontrada = True

    if not encontrada:
        print("❌ No se encontraron tareas con ese nombre.")


# Menú principal
while True:

    print("\n===================================")
    print(" SISTEMA DE GESTIÓN DE TAREAS")
    print("===================================")

    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Completar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()

    elif opcion == "2":
        mostrar_tareas()

    elif opcion == "3":
        completar_tarea()

    elif opcion == "4":
        eliminar_tarea()

    elif opcion == "5":
        buscar_tarea()

    elif opcion == "6":
        print("👋 Gracias por utilizar el sistema.")
        break

    else:
        print("❌ Opción no válida. Intente nuevamente.")