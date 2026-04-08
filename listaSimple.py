# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato            # Guarda el valor del nodo
        self.siguiente = None       # Apunta al siguiente nodo (inicialmente vacío)


# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabecera = None        # Primer nodo de la lista (inicialmente vacío)
    
    def agregar_nodo(self, nuevo_dato):
        # Crea un nuevo nodo con el dato recibido
        nuevo_nodo = Nodo(nuevo_dato)
        
        # El nuevo nodo apunta al nodo actual de la cabecera
        nuevo_nodo.siguiente = self.cabecera
        
        # La cabecera ahora será el nuevo nodo
        self.cabecera = nuevo_nodo
    
    def insertar_al_final(self, dato):
        # Crea un nuevo nodo con el dato
        nuevo = Nodo(dato)
        
        # Si la lista está vacía, el nuevo nodo será la cabecera
        if self.cabecera is None:
            self.cabecera = nuevo
            return
        
        # Recorre la lista hasta llegar al último nodo
        actual = self.cabecera
        while actual.siguiente:
            actual = actual.siguiente
        
        # El último nodo apunta al nuevo nodo
        actual.siguiente = nuevo
    
    
    def imprimirLista(self):
        # Comienza desde la cabecera
        temp = self.cabecera
        
        # Recorre la lista hasta el final
        while temp:
            print(temp.dato, end=' ')  # Imprime el dato del nodo
            temp = temp.siguiente      # Avanza al siguiente nodo
        
        print()  #Espacio al final dato

listaEnlazada=ListaEnlazada()
listaEnlazada.agregar_nodo("Tony")
listaEnlazada.agregar_nodo("Luna")
listaEnlazada.agregar_nodo("Trosky")
listaEnlazada.agregar_nodo("lucas")
listaEnlazada.imprimirLista()

listaEnlazada.insertar_al_final("pinina")
listaEnlazada.imprimirLista()