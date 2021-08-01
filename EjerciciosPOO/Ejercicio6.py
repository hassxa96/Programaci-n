"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda
"""

class Agenda():

    def __init__ (self):
        self.contactos= []


    def Menu(self):
        print("Bienvenido a la agenda: ")
        print("Pulsa 1 para añadir un contacto")
        print("Pulsa 2 para ver la lista de contactos")
        print("Pulsa 3 para buscar un contacto")
        print("Pulsa 4 para editar un contacto")
        print("Pulsa 5 para cerrar la agenda")
        x=int(input("Elija una opción: "))
        
        if x == 1:
            self.Añadir()
          
        elif x == 2:
            self.Lista()
         
        elif x == 3:
            self.Buscar()
            
        elif x== 4:
            self.Editar()
        elif x == 5:
            exit()
        self.Menu()

    def Añadir(self):
        a= input("Escriba el nombre: ")
        b= input("Escriba el teléfono: ")
        c= input("Escriba el email: ")
        self.contactos.append({'Nombre: ':a,'Telefono: ':b,'Email: ':c})

    def Lista(self):
        for i in range(len(self.contactos)):
            print(self.contactos[i]['Nombre: '])
    
    def Buscar(self):
        nombre=input("Introduzca el nombre del contacto: ")
        for i in range(len(self.contactos)):
            if nombre == self.contactos[i]['Nombre: ']:
                print(self.contactos[i])
                return i
    
    def Editar(self):
        contacto= self.Buscar()
        m=input("¿Quiere editar el nombre?: ")
        n=input("¿Quiere editar el número de teléfono?: ")
        r=input("¿Quiere editar el email?: ")
        if m == "Si":
            h=input("Introduzca el nuevo nombre: ")
            self.contactos[contacto]['Nombre: ']=h
        if n == "Si":
            j=input("Introduzca el nuevo teléfono: ")
            self.contactos[contacto]['Teléfono: ']=j
        if r == "Si":
            p=input("Introduzca el nuevo email: ")
            self.contactos[contacto]['Email: ']=p
    
    """
    def Editar(self):
	    print("---------------")
	    print("Editar contacto")
	    print("---------------")
	    data=self.Buscar()
	    condition=False
	    while condition==False:
		    print("Selecciona que quieres editar: ")
		    print("1. Nombre")
		    print("2. Teléfono")
		    print("3. E-mail")
		    print("4. Volver")
		    option=int(input("Introduzca la opción deseada: "))
		    if option==1:
			    nom=input("Introduzca el nuevo nombre: ")
			    self.contactos[data]['Nombre: ']=nom
		    elif option==2:
			    telf=input("Introduzca el nuevo teléfono: ")
			    self.contactos[data]['Teléfon: ']=telf
		    elif option==3:
			    email=input("Introduzca el nuevo email: ")
			    self.contactos[data]['Email: ']=email
		    elif option==4:
			    condition=True
    """
p1=Agenda()
p1.Menu()

