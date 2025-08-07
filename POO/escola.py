from abc import ABC, abstractmethod 
#from <modulo> import <nome>
#módulo: nome do módulo ou pacot que voce irá importar
#nome: nome da função, classe, varíavel ou submódulo que deseja importar
#import React from "react";

'''Classe abstrata: classe que não pode ser instanciada diretamente(não consigo criar) objeto diretamente nela. Definimos regras que devem ser
obdecidas'''
class Curso(ABC):
    def __init__ (self,nome):
        self.nome = nome
        self.alunos = []
        
    def inscrever_alunos(self,aluno, matricula):
        self.alunos.append((aluno, matricula))
        print(f"Aluno {aluno} com matrícula nº {matricula}, inscrito no curso de {self.nome}.")
        
    @abstractmethod
    def info_curso(self):
        pass
        
    def info_alunos(self):
        print(f"Alunos inscritos no curso {self.nome}: ")
        for aluno, matricula in self.alunos:
            print(f" - {aluno}, Matrícula {matricula}")

#Curso Específico        
class CursoMatematica(Curso):
    def info_curso(self):
        print(f"Curso de {self.nome}: Foco em álgebra e geometria")
        
#Curso específico
class CursoHistoria(Curso):
    def info_curso(self):
        print(f"Curso de {self.nome}: Foco em história mundial e cultura")
        
#testar
curso1 = CursoMatematica("Matematica")
curso2 = CursoHistoria("História")

curso1.inscrever_alunos("Breno", "RES098635")
curso1.inscrever_alunos("Rayssa", "RES0108666")
curso1.info_curso()
curso1.info_alunos()

curso2.inscrever_alunos("Ágatha", "RES100589")
curso2.info_curso()
curso2.info_alunos()



#Crie a função info_alunos()
curso1.info_alunos()
curso2.info_alunos()

#inserir matrícula dentro do __init__

