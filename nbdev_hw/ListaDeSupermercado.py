# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/ListaDeSupermercado.ipynb.

# %% auto 0
__all__ = ['ListaDeSupermercado']

# %% ../nbs/ListaDeSupermercado.ipynb 3
class ListaDeSupermercado:
    def __init__(self):
        """Constructor de la clase ListaDeSupermercado."""
        self.articulos = []

    def agregar_articulo(self,
                        articulo: Articulo): #  El artículo a agregar.
        """
        Agrega un artículo a la lista.
        """
        self.articulos.append(articulo)

    def imprimir_todos_los_articulos(self):
        """Imprime todos los artículos en la lista."""
        for articulo in self.articulos:
            print(f"Nombre: {articulo.nombre}, Cantidad: {articulo.cantidad}")

    def imprimir_articulos_no_agregados(self):
        """Imprime los artículos que no han sido marcados como agregados."""
        for articulo in self.articulos:
            if not articulo.agregado:
                print(f"Nombre: {articulo.nombre}, Cantidad: {articulo.cantidad}")

