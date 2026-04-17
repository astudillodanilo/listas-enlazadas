# ============================================================
# LISTA CIRCULAR: El último nodo NO apunta a None.
# Apunta de vuelta al PRIMERO, cerrando el ciclo.
# Solo necesitamos un puntero: self.ultimo
# (desde ultimo podemos llegar al primero con ultimo.siguiente)
#
# TRUCO CLAVE: self.ultimo.siguiente == self.primero SIEMPRE
# ============================================================
class ListaCircular:
    def __init__(self):
        self.ultimo = None    # Solo necesitamos 1 puntero en la circular

    def vacia(self):
        return self.ultimo is None

    # --------------------------------------------------------
    # agregar_ultimo(): Insertar al final del ciclo.
    # Caso vacío: el único nodo apunta a sí mismo (¡ciclo de 1!).
    # Caso normal: el nuevo nodo entra entre el último y el primero,
    # manteniendo el ciclo cerrado.
    # --------------------------------------------------------
    def agregar_ultimo(self, dato):
        nuevo = NodoDoble(dato) if False else Nodo(dato)  # usamos Nodo simple aquí
        if self.vacia():
            self.ultimo = nuevo
            self.ultimo.siguiente = self.ultimo    # ← apunta a sí mismo, ciclo cerrado
        else:
            nuevo.siguiente = self.ultimo.siguiente    # Nuevo → primero (antiguo)
            self.ultimo.siguiente = nuevo              # Antiguo último → nuevo
            self.ultimo = nuevo                        # Nuevo es ahora el último

    # --------------------------------------------------------
    # agregar_inicio(): Inserta antes del primero.
    # El "primero" siempre es self.ultimo.siguiente.
    # Solo hay que insertar antes de él y NO mover self.ultimo.
    # --------------------------------------------------------
    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.vacia():
            self.ultimo = nuevo
            self.ultimo.siguiente = self.ultimo
        else:
            nuevo.siguiente = self.ultimo.siguiente    # Nuevo → primero actual
            self.ultimo.siguiente = nuevo              # Último → nuevo (que es el nuevo primero)

    # --------------------------------------------------------
    # eliminar_inicio(): Elimina self.ultimo.siguiente (el primero).
    # El último ahora apunta al segundo nodo (nuevo primero).
    # --------------------------------------------------------
    def eliminar_inicio(self):
        if self.vacia():
            print("Lista vacía")
            return
        if self.ultimo.siguiente == self.ultimo:    # Solo 1 nodo
            self.ultimo = None
        else:
            self.ultimo.siguiente = self.ultimo.siguiente.siguiente  # Saltamos el primero

    # --------------------------------------------------------
    # eliminar_ultimo(): Eliminar el último es O(n) porque
    # debemos encontrar el PENÚLTIMO para que apunte al primero.
    # El penúltimo es el nodo cuyo .siguiente == self.ultimo.
    # --------------------------------------------------------
    def eliminar_ultimo(self):
        if self.vacia():
            print("Lista vacía")
            return
        if self.ultimo.siguiente == self.ultimo:    # Solo 1 nodo
            self.ultimo = None
        else:
            aux = self.ultimo.siguiente             # Empieza en el primero
            while aux.siguiente != self.ultimo:     # Busca el penúltimo
                aux = aux.siguiente
            aux.siguiente = self.ultimo.siguiente   # Penúltimo → primero (saltando último)
            self.ultimo = aux                       # Penúltimo se convierte en el nuevo último

    # --------------------------------------------------------
    # recorrido(): CUIDADO — no hay None que detenga el ciclo.
    # La condición de parada es: cuando aux vuelva al primero
    # (self.ultimo.siguiente), el ciclo debe terminar.
    # --------------------------------------------------------
    def recorrido(self):
        if self.vacia():
            print("Lista vacía")
            return
        primero = self.ultimo.siguiente    # Referencia al primer nodo
        aux = primero
        while True:
            print(aux.dato)
            aux = aux.siguiente
            if aux == primero:             # Parar cuando regresamos al inicio
                break


# Reutilizamos la clase Nodo de la lista simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


try:
    if __name__ == "__main__":
        lista = ListaCircular()
        opcion = 0
        while opcion != 6:
            print("\n--- Lista Circular ---")
            print(" 1. Agregar último\n 2. Agregar inicio\n 3. Eliminar último")
            print(" 4. Eliminar inicio\n 5. Mostrar\n 6. Salir")
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
                print("Adiós")
except Exception as e:
    print(e)