from abc import ABC,abstractmethod
from datetime import datetime,date
import os

class Persona(ABC):
    def __init__(self,nom,edad,sex,email,direcc):
        self.nombre = nom
        self.edad = edad
        self.sexo = sex
        self.correo = email
        self.direccion = direcc
    
    @abstractmethod
    def mostrarpersona(self):
        pass

class pantalla():
    def limpiar():
        os.system("cls")
    pass

class Login():
    def __init__(self,opc,nom,ide) -> None:
        self.opcion = opc
        self.nombre = nom
        self.id = ide
    
    def usuario(self):
        if self.opcion == 1:
            print('** Iniciar Sesion **')
            user = str(input("Ingrese el nombre: "))
            clave = int(input("Ingrese su ID: "))
            if user == self.nombre and clave == self.id:
                pantalla.limpiar()
                x=sistema()
                x.menu()
        else:
            print('** Iniciar Sesion **')
            user = str(input("Ingrese el nombre: "))
            clave = int(input("Ingrese su ID: "))
            if user == self.nombre and clave == self.id:
                pantalla.limpiar()
                y=sistema()
                y.menu()

class sistema():
    def __init__(self):
        self.contactos = []

    def menu(self):
        opciones = ['1. Añadir Paciente.',
                    '2. Lista de Paciente.',
                    '3. Mostrar Receta',
                    '4. Mostrar Horario',
                    '5. Editar Paciente',
                    '6. Salir','_____________________________']

        print("\n",'** MENU DE OPCIONES **')
        for i in range(len(opciones)):
            print(opciones[i])

        op = int(input('Ingrese una opcion: '))
        pantalla.limpiar()
        if op == 1:
            self.anadir()
        elif op == 2:
            self.lista()
        elif op == 3:
            self.MostrarReceta()
        elif op == 4:
            self.Horario()
        elif op == 5:
            self.editar()
        elif op == 6:
            self.cerrar()
        self.menu()

    def anadir(self):
        nom = str(input('-> Ingrese el nombre: '))
        edad = str(input('-> Ingrese la edad: '))
        sex = str(input('-> Ingrese el sexo (M/F): '))
        eml = str(input('-> Ingrese el Email: '))
        cdad = str(input('-> Ingrese la Ciudad: '))
        Ide = str(input('-> Ingrese el ID: '))
        pantalla.limpiar()
        self.contactos.append({'Nombre': nom.upper(), 'Edad': edad, 'Sexo': sex, 'Email': eml, 'Ciudad': cdad, 'Id': Ide})

    def lista(self):
        if len(self.contactos) == 0:
            print('-> No se han encontrado Pacientes.','\n')
        else:
            for i in range(len(self.contactos)):
                print(' _____________________________', '\n',
                      'Nombre: ', self.contactos[i]['Nombre'],
                      '\n', 'Edad: ', self.contactos[i]['Edad'],
                      '\n', 'Sexo: ', self.contactos[i]['Sexo'],
                      '\n', 'Email: ', self.contactos[i]['Email'],
                      '\n', 'Ciudad: ', self.contactos[i]['Ciudad'],
                      '\n', 'Id: ', self.contactos[i]['Id']
                      , '\n', '------------------------------','\n')


    def MostrarReceta(self):
        if len(self.contactos) == 0:
            print('-> No se han encontrado Pacientes.','\n')
        else:
            pantalla.limpiar()
            nom = str(input('->Ingrese el contacto que desea buscar: '))
            for i in range(len(self.contactos)):
                if nom.upper() == self.contactos[i]['Nombre']:
                    print(' _____________________________', '\n',
                        'Nombre: ', self.contactos[i]['Nombre']
                        , '\n', '------------------------------')
                    empresa = Empresa()
                    v1=self.contactos[i]['Nombre']
                    v2=self.contactos[i]['Edad']
                    v3=self.contactos[i]['Sexo']
                    v4=self.contactos[i]['Email']
                    v5=self.contactos[i]['Ciudad']
                    v6=self.contactos[i]['Id']
                    art1 = Medicamento("Paracetamol",3,100)
                    art2 = Medicamento("Apronax",1,200)
                    paciente = Paciente(v1,v2,v3,v4,v5,v6)
                    receta = Receta(paciente)
                    receta.agregarDetalle(art1,3)
                    receta.agregarDetalle(art2,2)
                    receta.mostrarReceta(empresa.nombre,empresa.ruc)

                else:
                    pantalla.limpiar()
                    print('-> El Paciente no se encuentra agregado')

    def Horario(self):
        dia = date.today()
        print("Hoy: ",dia,"\n")
        dias = ["Lunes: 08:00 am - 04:30 pm","Martes: 08:00 am - 04:30 pm","Miercoles: 08:00 am - 04:30 pm","Jueves: 08:00 am - 04:30 pm",
        "Viernes: 08:00 am - 04:30 pm"]
        for i in dias:
            print(i)

    def editar(self):
        if len(self.contactos) == 0:
            print('-> No se han encontrado Pacientes.','\n')
        else:
            nom = str(input('Ingrese el contacto que desea editar: '))
            for i in range(len(self.contactos)):
                if nom.upper() == self.contactos[i]['Nombre']:
                    nnom = str(input('-> Ingrese el nuevo nombre: '))
                    self.contactos[i]['Nombre'] = nnom.upper()
                    self.contactos[i]['Edad'] = str(input('-> Ingrese la nueva Edad: '))
                    self.contactos[i]['Sexo'] = str(input('-> Ingrese el Sexo (M/F): '))
                    self.contactos[i]['Email'] = str(input('-> Ingrese el nuevo email: '))
                    self.contactos[i]['Ciudad'] = str(input('-> Ingrese la nueva Ciudad: '))
                    self.contactos[i]['Id'] = str(input('-> Ingrese la nueva Id: '))
                    pantalla.limpiar()
                else:
                    print('-> El Paciente no se encuentra agregado','\n')

    def cerrar(self):
        print('---FIN DEL PROGRAMA---','\n')
        exit()

class Doctor(Persona):
    def __init__(self,nomb,edad,sex,email,direcc,IdMed,espec):
        super().__init__(nomb,edad,sex,email,direcc)
        self.__IdMed = IdMed
        self.especialidad = espec
    
    @property
    def IdMed(self):
        return self.__IdMed
    
    def name(self):
        nm = self.nombre
        return nm
    def Ide(self):
        ide = self.IdMed
        return ide

    def mostrarpersona(self):
        print(f"Nombre:{self.nombre} Edad:{self.edad} Sexo:{self.sexo} Email:{self.correo}\n"
        f"Ciudad:{self.direccion} ID:{self.IdMed} Especialidad:{self.especialidad}")


class Enfermera(Persona):
    def __init__(self,nomb,edad,sex,email,direcc,IdEnf):
        super().__init__(nomb,edad,sex,email,direcc)
        self.__IdEnf = IdEnf

    @property
    def IdEnf(self):
        return self.__IdEnf
    
    def mostrarpersona(self):
        print(f"Nombre:{self.nombre} Edad:{self.edad} Sexo:{self.sexo} Email:{self.correo}"
         f" Ciudad:{self.direccion} ID:{self.IdEnf}")

    def name(self):
        nm = self.nombre
        return nm
    def Ide(self):
        ide = self.IdEnf
        return ide

class Paciente(Persona):
    def __init__(self,nomb,edad,sex,email,direcc,IdPaciente):
        super().__init__(nomb,edad,sex,email,direcc)
        self.__IdPaciente = IdPaciente

    @property
    def IdPaciente(self):
        return self.__IdPaciente
    
    def mostrarpersona(self):
        print(f"Nombre:{self.nombre} Edad:{self.edad} Sexo:{self.sexo} Email:{self.correo}" 
        f" Ciudad:{self.direccion} ID:{self.IdPaciente}")

class Medicamento:
    _secuencia=0
    def __init__(self,des,pre,sto):
        Medicamento._secuencia += 1
        self.__codigo = Medicamento._secuencia
        self.descripcion = des
        self.precio = pre
        self.stock = sto
    
    @property
    def codigo(self):
        return self.__codigo
        
    def mostrarMedicamento(self):
        print(self.codigo,self.descripcion)

class Empresa:
    def __init__(self,nombre='Heart Hospital',ruc='0010957102545',telefono='0999798674',direccion='Guayaquil',dias='Lunes a viernes',hora='24h'):
        self.nombre = nombre
        self.ruc = ruc
        self.telefono = telefono
        self.direccion = direccion
        self.dias = dias
        self.hora = hora


class Citas(Empresa):
    _cita=0
    def __init__(self,fecha,nombre,cedula,telefono,direccion):
        Citas._cita = Citas._cita + 1
        self.cita = "N"+str(Citas._cita)
        self.fecha = fecha
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.direccion = direccion
    
    def mostrarCitas(self,empNombre,empRuc):
        print("|Empresa: {:17}      Ruc:{}".format(empNombre,empRuc))    
        print("|Cita Medica:{}                  Fecha:{}".format(self.cita,self.fecha))
        print("|Nombre: {}              Direccion del paciente: {}".format(self.nombre,self.direccion))
        print("|Cedula: {}              telefono: {}".format(self.cedula,self.telefono))

class detalleDiagnostico:
    _linea=0
    def __init__(self,medicamento,cantidad):
        detalleDiagnostico._linea += 1
        self.linea = detalleDiagnostico._linea
        self.medicamento = medicamento
        self.precio = medicamento.precio
        self.cantidad = cantidad
class Receta:
    _factura=0
    _iva=0.12
    def __init__(self,paciente):
        Receta._factura = Receta._factura + 1
        self.factura = "F"+str(Receta._factura)
        self.fecha = date.today()
        self.paciente = paciente
        self.subtotal = 0
        self.iva = 0 
        self.total = 0
        self.detalleDiagnostico = []
    
    def agregarDetalle(self,medicamento,cantidad):
        detalle = detalleDiagnostico(medicamento,cantidad)
        self.subtotal += round(detalle.precio*detalle.cantidad,2)
        self.iva = round(self.subtotal*Receta._iva,2)
        self.total = round(self.subtotal+self.iva,2)
        self.detalleDiagnostico.append(detalle)    
    
    def mostrarReceta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc:{}".format(empNombre,empRuc))    
        print("Receta#:{:13}  Fecha:{}".format(self.factura,self.fecha))
        self.paciente.mostrarpersona()
        print("Linea medicamento     Precio Cantidad Subtotal")
        for det in self.detalleDiagnostico:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea,det.medicamento.descripcion,det.precio,det.cantidad,det.precio*det.cantidad))  
        print("*"*23,"Subtotal=> ",self.subtotal)
        print("*"*26,"Iva=> ",self.iva)
        print("*"*23,"Total=> ",self.total)
        

#inicio
if __name__ == '__main__':  
    doct = Doctor("Miguel",32,"M","Miguel-32@gmail.com","Milagro",58579,"Neurocirujano") # <- El nombre y el id son para iniciar sesión
    enfe = Enfermera("Maria",27,"F","Maria_L@gmail.com","Guayaquil",26438) # <- El nombre y el id son para iniciar sesión
    pantalla.limpiar()
    print("--DOCTOR--")
    doct.mostrarpersona()
    d = doct.name()
    di = doct.Ide()
    print("\n","--ENFERMERA--")
    enfe.mostrarpersona()
    e = enfe.name()
    ei = enfe.Ide()
    
    #iniciar sesion
    print("\n","Ingrese que tipo de usuario es: \n 1.- Doctor\n 2.- Enfermera") 
    op = int(input("Ingrese la opcion: "))

    while True:
        while op > 0 and op < 3:
            pantalla.limpiar()
            if op == 1:
                opc = Login(1,d,di)
                opc.usuario()
                exit()
            elif op == 2:
                opc = Login(2,e,ei)
                opc.usuario()
                exit()
        pantalla.limpiar()
        print("\n","Ingrese que tipo de usuario es: \n 1.- Doctor\n 2.- Enfermera")
        print("Seleccione: 1 o 2")
        op = int(input("Ingrese la opcion: "))
    
