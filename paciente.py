from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.__cpf=cpf

    def setCpf(self, cpf):
        self.__cpf=cpf

    def getCpf(self):
        return self.__cpf
    
    def mostrar(self):
        return f"Nome do paciente: {self.getNome()}\n Idade: {self.getIdade()}\n CPF: {self.getCpf()}"