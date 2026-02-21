class Tarea:
    def __init__(self, nombre, apellido, correo, descripcion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.descripcion = descripcion

    def mostrar_info(self):
        print("\n📋 Tarea Asignada")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Correo: {self.correo}")
        print(f"Tarea: {self.descripcion}")


#Creamos una lista vacía
lista_tareas = []

#Preguntamos cuántas tareas quiere ingresar
cantidad = int(input("¿Cuántas tareas desea registrar? "))

for i in range(cantidad):
    print(f"\n--- Registro {i+1} ---")
    
    nombre = input("Ingrese el Nombre: ")
    apellido = input("Ingrese el Apellido: ")
    correo = input("Ingrese el correo: ")
    descripcion = input("Ingrese la tarea: ")

    nueva_tarea = Tarea(nombre, apellido, correo, descripcion)
    
    # Guardamos la tarea en la lista
    lista_tareas.append(nueva_tarea)


# Mostramos todas las tareas registradas
print("\n========= LISTADO DE TAREAS =========")

for tarea in lista_tareas:
    tarea.mostrar_info()