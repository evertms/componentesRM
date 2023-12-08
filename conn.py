import cx_Oracle

try:
    conn: object = cx_Oracle.connect(
        user = 'SYSTEM',
        password = 'zxczxc',
        dsn = 'localhost:1521/xe',
        encoding = 'UTF-8'
    )
    print(conn.version)

except Exception as ex: 
    print(ex)

curs = conn.cursor()

'''
Para las clases necesitaremos cada uno de los atributos de las personas, por lo cual decidimos hacer funciones
que obtengan cada uno de los atributos
'''

def get_mobos() -> list:
    curs.execute("select * from PRODUCTO where COD like 'MB%'")
    motherboards: list = curs.fetchall()
    return motherboards

def get_processors() -> list:
    curs.execute("select * from PRODUCTO where COD like 'PR%'")
    processors = curs.fetchall()
    return processors

def get_gpu() -> list:
    curs.execute("select * from PRODUCTO where COD like 'G%'")
    graficas = curs.fetchall()
    return graficas

def get_laptops() -> list:
    curs.execute("select * from PRODUCTO where COD like 'LAP%'")
    laptops: list = curs.fetchall()
    return laptops

# 
def get_persons() -> list:
    curs.execute("select * from PERSONA")
    persona: list = curs.fetchall()
    return persona

def get_clients() -> list:
    curs.execute("select * from CLIENTE")
    clients: list = curs.fetchall()
    return clients