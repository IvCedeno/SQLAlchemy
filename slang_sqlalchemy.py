import sqlalchemy as db
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine("mysql+pymysql://root:@localhost/slang_sqlalchemy")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Palabra(Base):
    __tablename__ = 'slang'

    palabra = Column(String(255), primary_key=True, nullable=False)
    significado = Column(String(255), nullable=False)

    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

def agregarPalabra(palabra, significado):
    p = Palabra(palabra, significado)
    session.add(p)
    session.commit()
    print("Palabra agregada!\n")

def editarPalabra(palabraU, significado):
    p = session.query(Palabra).filter_by(palabra=palabraU).first()
    p.significado = significado
    session.commit()
    print("Palabra actualizada!\n")

def eliminarPalabra(palabraE):
    p = session.query(Palabra).filter_by(palabra=palabraE).first()
    session.delete(p)
    session.commit()
    print("Palabra eliminada!\n")
    
def listarPalabras():
    palabras = session.query(Palabra).all()
    for p in palabras:
        print("- " + p.palabra + ": " + p.significado)

def buscarPalabra(palabraB):
    p = session.query(Palabra).filter_by(palabra=palabraB).first()
    print("- " + p.palabra + ": " + p.significado + "\n")

Base.metadata.create_all(engine)

while True:
    print("Seleccione una opcion:")
    print("1. Agregar nueva palabra")
    print("2. Editar palabra existente")
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir")
    opcion = int(input())

    if opcion == 1:
        print("\nAgregar nueva palabra")
        palabra = input("Nueva palabra: ")
        significado = input("Significado: ")
        agregarPalabra(palabra, significado)
    elif opcion == 2:
        print("\nEditar palabra existente")
        palabra = input("Palabra: ")
        significado = input("Nuevo significado: ")
        editarPalabra(palabra, significado)
    elif opcion == 3:
        print("\nEliminar palabra existente")
        palabra = input("Palabra: ")
        eliminarPalabra(palabra)
    elif opcion == 4:
        print("\nListado de palabras")
        listarPalabras()
        print()
    elif opcion == 5:
        print("\nBuscar significado de palabra")
        palabra = input("Palabra: ")
        buscarPalabra(palabra)
    elif opcion == 6:
        print("\nHasta la proxima!!\n")
        break
    else:
        print("\nOpcion invalida! Intente nuevamente\n")