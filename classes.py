from conn import *

class Cliente:
    def __init__(self, id: str, direccion: str, CI: int):
        self.__id = id
        self.direccion = direccion
        self.__CI = CI

    def __repr__(self) -> str:
        return f"{self.__id}, {self.direccion}, {self.__CI}"

class Producto:
    def __init__(self, cod: str, 
                descripcion: str,
                precio: int,
                stock: int,
                id_unidad_medida: int, 
                cod_prod_compatibl: str = "") -> None:
        self.__cod = cod
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock 
        self.cod_prod_compatibl = cod_prod_compatibl
        self.id_unidad_medida = id_unidad_medida

    def __repr__(self):
        return f"{self.__cod}\n{self.descripcion}\n{self.cod_prod_compatibl}\n{self.id_unidad_medida}"
    
    def get_prod_name(self):
        return self.descripcion
    
    def get_price(self):
        return self.precio

class Motherboard(Producto):
    def __init__(self, cod: str, 
                descripcion: str,
                precio: int,
                stock: int,
                id_unidad_medida: int, 
                cod_prod_compatibl: str = "") -> None:
        super().__init__(cod, descripcion, precio, stock, id_unidad_medida, cod_prod_compatibl)

class Processor(Producto):
    def __init__(self, cod: str, 
                descripcion: str,
                precio: int,
                stock: int,
                id_unidad_medida: int, 
                cod_prod_compatibl: str = "") -> None:
        super().__init__(cod, descripcion, precio, stock, id_unidad_medida, cod_prod_compatibl)

class GraphCard(Producto):
    def __init__(self, cod: str, 
                descripcion: str,
                precio: int,
                stock: int,
                id_unidad_medida: int, 
                cod_prod_compatibl: str = "") -> None:
        super().__init__(cod, descripcion, precio, stock, id_unidad_medida, cod_prod_compatibl)

class Laptop(Producto):
    def __init__(self, cod: str, 
                descripcion: str,
                precio: int,
                stock: int,
                id_unidad_medida: int, 
                cod_prod_compatibl: str = "") -> None:
        super().__init__(cod, descripcion, precio, stock, id_unidad_medida, cod_prod_compatibl)        
                
# Poblar lista con objetos de la clase Cliente
resultclients: list = get_clients()
clientes: list = []
for row in resultclients:
    c = Cliente(row[0], row[1], row[3])
    clientes.append(c)    

# Poblar lista con objetos de la clase Motherboard
resultmobo: list = get_mobos()
mobos: list = []
for row in resultmobo:
    m = Motherboard(row[0], row[1], row[2], row[3], row[5], row[4])
    mobos.append(m)

# Poblar lista con objetos de la clase Processor
resultproc: list = get_processors()
processors: list = []
for row in resultproc:
    p = Processor(row[0], row[1], row[2], row[3], row[5], row[4])
    processors.append(p)

# Poblar lista con objetos de la clase Laptop
resultgpu: list = get_gpu()
graphcards: list = []
for row in resultgpu:
    gc = GraphCard(row[0], row[1], row[2], row[3], row[5], row[4])
    graphcards.append(gc)

# Poblar lista con objetos de la clase Laptop
resultlaptop: list = get_laptops()
t = get_laptops()
laptops: list = []
for row in resultlaptop:
    l = Laptop(row[0], row[1], row[2], row[3], row[5], row[4])
    laptops.append(l)

conn.close()
print("Conexión terminada")