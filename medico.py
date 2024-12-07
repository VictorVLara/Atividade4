from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, idade, crm):
        super().__init__(nome, idade)
        self.__crm=crm

    def setCrm(self, crm):
        self.__crm=crm

    def getCrm(self):
        return self.__crm

    def mostrar(self):
        return f"Nome do médico: {self.getNome()} \nIdade: {self.getIdade()} \nCRM: {self.getCrm()}"