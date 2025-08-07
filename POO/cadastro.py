class Usuario:
    def __init__(self, nome, email):
        self.__email = email
        self.__nome = nome
    
    def get_nome(self): #permite acessar atributo
        return self.__nome
    
    def set_nome(self, nome): #permite modificar atributo
        if nome.strip(): #remove espaço no inicio e no fim
            self.__nome = nome
            
    def get_email(self):
        return self.__email 
            
    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email=email
        else:
            print("Email Inválido")
            
usuario = Usuario("Carlos", "carlos@gmail.com") 
print(usuario.get_nome())
print(usuario.get_email())




#alteradores
usuario.set_nome("Brenao do grau")
usuario.set_email("brenaodograu006007008@picamole.com")
print(usuario.get_nome())
print(usuario.get_email()) 
#usuario.set_nome("Carlos André")
#print(usuario.get_nome())


#set_nome altera
#get_nome get você recebe

#usuario.set_email("emailinvalido")
#print(usuario.get_email())