
from datetime import date

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: str):
        """_Uma classe que representa uma pessoa!_

        Args:
            nome (str): _Nome da pessoa._
            idade (int): _Idade da pessoa._
            sexo (str): _Sexo da pessoa._
        """

        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        """_Método para representação de classe!_

        Returns:
            str: _Retorna uma string contendo informações completas sobre a classe!_
        """
        return f"Class: {__class__.__name__}  - Atributes: {', '.join([f'{key}: {value}' for key,value in self.__dict__.items()])}"
    

class Usuario(Pessoa):
    def __init__(self, username: str, passwword: int, email: str, **kwargs):
        super().__init__(**kwargs)
        self.username = username
        self.passwword = passwword
        self.email = email
    
    @classmethod
    def gera_user_por_idade(cls, username: str, passwword: int, email: str, ano_nascimento: int, **kwargs) -> object:
        ano_atual = date.today().year
        idade_do_usuario = ano_atual - ano_nascimento 
        return cls(username, passwword, email, idade = idade_do_usuario, **kwargs)

    @staticmethod
    def verifica_maioridade(idade: int) -> str:
        return f'{"É maior" if idade >=18 else "É menor"} de idade!' 


    def __str__(self) -> str:
        return f"Class: {__class__.__name__}  - Atributes: {', '.join([f'{key}: {value}' for key,value in self.__dict__.items()])}"
    

if __name__ == '__main__':
    eu = Usuario.gera_user_por_idade('felrfdev', 123, 'comunidadehawks@gmail.com', 1988, nome='Felipe', sexo='Masculino')
    print(eu)
    print(Usuario.verifica_maioridade(eu.idade))