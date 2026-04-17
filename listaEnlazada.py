# ============================================================
# NODO: La unidad fundamental de cualquier lista enlazada.
# Cada nodo guarda UN dato y UNA referencia al siguiente nodo.
# Sin referencia al siguiente = último nodo (apunta a None).
# ============================================================
class Nodo:
    def __init__(self, dato):
        self.dato = dato          # El valor que almacena el nodo (cualquier tipo)
        self.siguiente = None     # Puntero al siguiente nodo. None = no hay siguiente


# ============================================================
# LISTA: Es el "contenedor". No guarda datos directamente,
# solo mantiene dos punteros clave:
#   - primero: puerta de entrada a la lista
#   - ultimo:  acceso rápido al final (evita recorrer toda la lista)
# ============================================================
class ListaSimplememteEnlazada:
    def __init__(self):
        self.primero = None   # Referencia al primer Nodo (o None si la lista está vacía)
        self.ultimo = None    # Referencia al último Nodo (optimiza agregar al final)

    # --------------------------------------------------------
    # vacia(): Verifica si la lista no tiene elementos.
    # Si primero == None, no existe ningún nodo → lista vacía.
    # --------------------------------------------------------
    def vacia(self):
        return self.primero == None

    # --------------------------------------------------------
    # agregar_ultimo(): Inserta un nuevo nodo al FINAL.
    # Caso especial: si la lista está vacía, primero Y ultimo
    # apuntan al mismo nodo (es el único nodo existente).
    # Caso normal: el nodo actual "ultimo" conecta su puntero
    # .siguiente al nuevo nodo, y "ultimo" se actualiza.
    # --------------------------------------------------------
    def agregar_ultimo(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)   # El único nodo es primero y último
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)  # Encadena y actualiza el puntero ultimo

    # --------------------------------------------------------
    # recorrido(): Visita cada nodo desde el inicio hasta el fin.
    # Patrón clave: aux = self.primero → avanzar con aux = aux.siguiente
    # El ciclo termina cuando aux llega a None (no hay más nodos).
    # --------------------------------------------------------
    def recorrido(self):
        aux = self.primero          # aux es un puntero temporal que "camina" la lista
        while aux != None:
            print(aux.dato)         # Procesa el dato del nodo actual
            aux = aux.siguiente     # Mueve el puntero al siguiente nodo

    # --------------------------------------------------------
    # eliminar_ultimo(): Elimina el último nodo.
    # Recorre la lista hasta encontrar el PENÚLTIMO nodo
    # (aquel cuyo .siguiente == self.ultimo).
    # Luego corta el enlace y actualiza self.ultimo.
    # IMPORTANTE: No maneja el caso de lista vacía o de 1 elemento
    # (bug potencial a tener en cuenta).
    # --------------------------------------------------------
    def eliminar_ultimo(self):
        aux = self.primero
        while aux.siguiente != self.ultimo:   # Busca el penúltimo nodo
            aux = aux.siguiente
        aux.siguiente = None   # Rompe el enlace con el último nodo
        self.ultimo = aux      # El penúltimo se convierte en el nuevo último

    # --------------------------------------------------------
    # agregar_inicio(): Inserta un nuevo nodo al PRINCIPIO.
    # El nuevo nodo apunta a quien era "primero" antes,
    # y self.primero se actualiza al nuevo nodo.
    # --------------------------------------------------------
    def agregar_inicio(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero   # El nuevo nodo apunta al antiguo primero
            self.primero = aux             # La lista ahora inicia en el nuevo nodo

    # --------------------------------------------------------
    # eliminar_inicio(): Elimina el primer nodo.
    # Solo redirige self.primero al segundo nodo.
    # El primer nodo queda sin referencias → Python lo recolecta.
    # IMPORTANTE: No maneja lista vacía (AttributeError si está vacía).
    # --------------------------------------------------------
    def eliminar_inicio(self):
        self.primero = self.primero.siguiente   # Salta el primer nodo


# ============================================================
# BLOQUE PRINCIPAL con manejo de errores.
# try/except captura cualquier excepción del programa
# (ej: ingresar letras en lugar de números, lista vacía, etc.)
# ============================================================
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaSimplememteEnlazada()
        while opcion != 7:
            print("--- Lista Simplemente Enlazada ---\n 1. Agregar último\n 2. Eliminar último\n 3. ¿Está vacía la lista?\n 4. Agregar Inicio\n 5. Eliminar Inicio\n 6. Mostrar\n 7. Salir")
            opcion = int(input("Ingrese su opción "))
            if opcion == 1:
                dato = input("Ingresa un número ")
                lista.agregar_ultimo(dato)
            elif opcion == 2:
                lista.eliminar_ultimo()
            elif opcion == 3:
                print("SI" if lista.vacia() else "NO")
            elif opcion == 4:
                dato = input("Ingresa un número ")
                lista.agregar_inicio(dato)
            elif opcion == 5:
                lista.eliminar_inicio()
            elif opcion == 6:
                lista.recorrido()
            elif opcion == 7:
                print("Adiós")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)