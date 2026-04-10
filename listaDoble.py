# Clase que representa un nodo de la lista doblemente enlazada
class Nodo:
    def __init__(self, dato):
        self.dato = dato          # Valor almacenado en el nodo
        self.siguiente = None     # Puntero al nodo siguiente (derecha)
        self.anterior = None      # Puntero al nodo anterior (izquierda)


# Clase que gestiona la lista doblemente enlazada
class ListaDobleEnlazada():
    def __init__(self):
        self.primero = None   # Referencia al primer nodo (cabeza)
        self.ultimo = None    # Referencia al último nodo (cola)
        self.size = 0         # Contador de nodos en la lista

    # Retorna True si la lista no tiene ningún nodo
    def vacia(self):
        return self.primero is None

    # Inserta un nuevo nodo al final de la lista
    def agregar_final(self, dato):
        nuevo = Nodo(dato)          # Crea el nodo con el dato recibido

        if self.vacia():
            # Si la lista está vacía, el nuevo nodo es cabeza y cola a la vez
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # Enlaza el último nodo actual con el nuevo nodo
            self.ultimo.siguiente = nuevo   # El último apunta →  al nuevo
            nuevo.anterior = self.ultimo    # El nuevo apunta ← al último
            self.ultimo = nuevo             # El nuevo pasa a ser el último
        
        self.size += 1   # Incrementa el tamaño de la lista

    # Recorre e imprime todos los nodos de izquierda a derecha
    def recorrer_adelante(self):
        actual = self.primero   # Comienza desde la cabeza de la lista

        while actual:                    # Continúa hasta llegar al final (None)
            print(actual.dato)           # Imprime el dato del nodo actual
            actual = actual.siguiente    # Avanza al siguiente nodo
        
        print()   # Línea en blanco al terminar el recorrido
    
    def recorrer_atras(self):
        actual = self.ultimo

        while actual:
            print(actual.dato)
            actual = actual.anterior

        print()

    def buscar(self,dato):
        actual = self.primero
        while actual:
            if actual.dato == dato:
                print("Encontrado")
                return 
            actual = actual.siguiente 
        print("No encontrado")



        
    def eliminar():
        pass


# ── Prueba ──────────────────────────────────────────────
lista = ListaDobleEnlazada()

lista.agregar_final("A")   # Lista: 10
lista.agregar_final("B")   # Lista: 10 ↔ 20
lista.agregar_final("C")   # Lista: 10 ↔ 20 ↔ 30

print("Recorrido Adelante")
lista.recorrer_adelante()  # Salida esperada: 10, 20, 30

print("Recorrido atras")
lista.recorrer_atras()

print("Buscar 20: ")
lista.buscar("A")

    