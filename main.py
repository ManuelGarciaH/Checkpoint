import pickle
from os import remove

ARCHIVO_PRINCIPAL = 'estudiantes.pckl'
ARCHIVO_TEMPORAL = 'temporal.pckl'

estudiantes = []

class Estudiante:
    def __init__(self, n, e, co, ca):
        self.nombre = n
        self.edad = e
        self.codigo = co
        self.carrera = ca

def menu()->None:
    opcion=0;
    while(opcion!=3):
        print("1-Para crear un nuevo estudiante")
        print("2-Ver estudiantes")
        print("3-Salir")
        opcion = int(input("-> "))
        if opcion==1:
            crearEstudiante()
        elif opcion==2:
            verEstudiantes()
        elif opcion==3:
            print("Cerrando programa")
        else:
            print("Opcion no valida")

def guardarEnTemporal(datos, elemento)->None:
    archivo_temporal = open(ARCHIVO_TEMPORAL, 'wb')
    datos.append(elemento)
    pickle.dump(datos, archivo_temporal)
    archivo_temporal.close()

def guardarEnPrincipal(nombre, edad, codigo, carrera)->None:
    estudiante = Estudiante(nombre, edad, codigo, carrera)
    estudiantes.append(estudiante)
    archivo = open(ARCHIVO_PRINCIPAL, 'wb')
    pickle.dump(estudiantes, archivo)
    archivo.close()
    remove(ARCHIVO_TEMPORAL)

def crearEstudiante()->None:
    datos = []

    nombre = input('Dame tu nombre-> ')
    guardarEnTemporal(datos, nombre)

    edad = int(input('Dame tu edad-> '))
    guardarEnTemporal(datos, edad)

    codigo = input('Dame tu codigo-> ')
    guardarEnTemporal(datos, codigo)

    carrera = input('Dame tu carrera-> ')

    guardarEnPrincipal(nombre, edad, codigo, carrera)
    

def verEstudiantes()->None:
    i=1;
    for e in estudiantes:
        print("FICHA DE ESTUDIANTE ", i)
        print("Nombre: ", e.nombre) 
        print("Edad: ", e.edad) 
        print("Codigo: ", e.codigo) 
        print("Carrera: ", e.carrera, "\n") 
        i=i+1

def cargarEstudiantes()->None:
    try:
        archivo = open(ARCHIVO_PRINCIPAL, 'rb')
        estudiante = pickle.load(archivo)
        for e in estudiante:
            estudiantes.append(e)
        archivo.close()
    except:
        pass
    cargarArchivoTemporal()

def cargarArchivoTemporal()->None:
    datosTemporales = []
    try:
        archivo_temporal = open(ARCHIVO_TEMPORAL, 'rb')
        datosTemporales = pickle.load(archivo_temporal)
        archivo_temporal.close()
        crearEstudianteDatosFaltantes(datosTemporales)
    except:
        pass
    menu()

def crearEstudianteDatosFaltantes(datosTemporales)->None:
    tamanioLista = len(datosTemporales)
    if tamanioLista>=1:
        nombre = datosTemporales[0]
        print("Nombre:", nombre)
        if(tamanioLista>=2):
            edad = datosTemporales[1]
            print("Edad:", edad)
            if(tamanioLista==3):
                codigo = datosTemporales[2]
                print("Codigo:", codigo)

    if tamanioLista==1:
        edad = int(input('Dame tu edad-> '))
        guardarEnTemporal(datosTemporales, edad)

        codigo = input('Dame tu codigo-> ')
        guardarEnTemporal(datosTemporales, codigo)

    elif tamanioLista==2:
        codigo = input('Dame tu codigo-> ')
        guardarEnTemporal(datosTemporales, codigo)

    carrera = input('Dame tu carrera-> ')

    guardarEnPrincipal(nombre, edad, codigo, carrera)

cargarEstudiantes()