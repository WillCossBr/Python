# Orientação a objetos: Paradigma de Programação
# Classes e Objetos

class Veiculo:
    def movimentar(self):
        print("Sou um veículo e me desloco!")

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    print(30*'-')

    # Getter
    def get_fabr_modelo(self):
        print(f"Modelo: {self.__modelo}, Fabricante: {self.__fabricante}")

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    def get_num_registro(self):
        return self.__num_registro

#herança:
class Carro(Veiculo):
    #metodo __init__ será herdado
    def movimentar(self):
        print('Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f"Corro Muito!")

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.cat

    def movimentar(self):
        print('Eu voo alto!')

if __name__=='__main__':
    meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('490321-1')
    print(meu_veiculo.get_num_registro())

    print(30*'-')

    #objeto1
    meu_carro = Carro('Volkswagen', 'Polo')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    print(30*'-')

    #objeto2
    seu_carro = Carro('Audi', "A5 Sportback")
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    print(30*'-')

    #objeto3
    moto = Motocicleta("Harley-Davidson", 'Nightster Special')
    moto.movimentar()
    moto.get_fabr_modelo()

    print(30*'-')

    #objeto4
    meu_aviao = Aviao("Boing","747","Special")
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')

    print(30*'-')

    #Obs: colocar __ depois do ponto torna o
    #atributo privado.

    #Somente pelo metodo especial Getter eu consigo
    #acessar os atributos privados de uma classe.

    #Setter permite eu gravar um dado dentro da classe.

#----------------------------------------------------------------
