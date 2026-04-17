# ============================================================
# NODO DOBLE: A diferencia del nodo simple, este tiene DOS
# punteros: uno al siguiente y otro al anterior.
# Esto permite navegar la lista en AMBAS direcciones.
# ============================================================
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None    # Puntero al nodo PREVIO (nuevo respecto a la simple)
        self.siguiente = None   # Puntero al nodo SIGUIENTE


class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero is None

    # --------------------------------------------------------
    # agregar_ultimo(): Igual que en la simple, pero además
    # el nuevo nodo debe apuntar hacia atrás con .anterior
    # al nodo que era último antes de él.
    # --------------------------------------------------------
    def agregar_ultimo(self, dato):
        nuevo = NodoDoble(dato)
        if self.vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.anterior = self.ultimo      # El nuevo apunta HACIA ATRÁS al último actual
            self.ultimo.siguiente = nuevo     # El último actual apunta HACIA ADELANTE al nuevo
            self.ultimo = nuevo               # Actualiza el puntero ultimo

    # --------------------------------------------------------
    # agregar_inicio(): Inserta al principio.
    # El nuevo nodo debe apuntar hacia adelante al antiguo primero,
    # y el antiguo primero debe apuntar hacia atrás al nuevo.
    # --------------------------------------------------------
    def agregar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.vacia():
            self.primero = self.ultimo = nuevo
        else:
            nuevo.siguiente = self.primero        # Nuevo → antiguo primero
            self.primero.anterior = nuevo         # Antiguo primero ← nuevo
            self.primero = nuevo                  # La lista ahora empieza en nuevo

    # --------------------------------------------------------
    # eliminar_ultimo(): GRAN VENTAJA sobre la lista simple.
    # En la simple necesitábamos recorrer toda la lista O(n).
    # Aquí el último ya conoce a su anterior → O(1).
    # Solo redirigimos self.ultimo al nodo anterior.
    # --------------------------------------------------------
    def eliminar_ultimo(self):
        if self.vacia():
            print("Lista vacía")
            return
        if self.primero == self.ultimo:       # Solo hay un elemento
            self.primero = self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior    # Retrocede el puntero ultimo
            self.ultimo.siguiente = None          # Corta el enlace hacia el nodo eliminado

    # --------------------------------------------------------
    # eliminar_inicio(): Elimina el primer nodo.
    # El nuevo primero debe borrar su puntero .anterior (= None)
    # para no mantener una referencia al nodo eliminado.
    # --------------------------------------------------------
    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
            return
        if self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente   # Avanza primero
            self.primero.anterior = None            # Limpia el puntero hacia atrás

    # --------------------------------------------------------
    # recorrido_inverso(): EXCLUSIVO de listas dobles.
    # Recorre de atrás hacia adelante usando .anterior.
    # Imposible en una lista simplemente enlazada.
    # --------------------------------------------------------
    def recorrido_inverso(self):
        aux = self.ultimo
        while aux is not None:
            print(aux.dato)
            aux = aux.anterior    # Navega en reversa usando el puntero anterior

    def recorrido(self):
        aux = self.primero
        while aux is not None:
            print(aux.dato)
            aux = aux.siguiente


# ---- Menú de prueba ----
try:
    if __name__ == "__main__":
        lista = ListaDoblementeEnlazada()
        opcion = 0
        while opcion != 8:
            print("\n--- Lista Doblemente Enlazada ---")
            print(" 1. Agregar último\n 2. Agregar inicio\n 3. Eliminar último")
            print(" 4. Eliminar inicio\n 5. Recorrido normal\n 6. Recorrido inverso")
            print(" 7. ¿Vacía?\n 8. Salir")
            opcion = int(input("Opción: "))
            if opcion == 1:
                lista.agregar_ultimo(input("Dato: "))
            elif opcion == 2:
                lista.agregar_inicio(input("Dato: "))
            elif opcion == 3:
                lista.eliminar_ultimo()
            elif opcion == 4:
                lista.eliminar_inicio()
            elif opcion == 5:
                lista.recorrido()
            elif opcion == 6:
                lista.recorrido_inverso()
            elif opcion == 7:
                print("Sí" if lista.vacia() else "No")
            elif opcion == 8:
                print("Adiós")
except Exception as e:
    print(e)