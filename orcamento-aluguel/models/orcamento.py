# Classe responsável por representar o orçamento do imóvel
# Aqui aplicamos Programação Orientada a Objetos (POO)

class Orcamento:
    def __init__(self, tipo, quartos, vagas, criancas):
        # Tipo do imóvel (Apartamento, Casa ou Estudio)
        self.tipo = tipo

        # Quantidade de quartos escolhidos
        self.quartos = quartos

        # Quantidade de vagas de garagem / estacionamento
        self.vagas = vagas

        # Indica se o cliente possui crianças (True ou False)
        self.criancas = criancas

        # Valor final do aluguel (inicialmente zero)
        self.valor = 0

    # Método responsável por calcular o valor do aluguel
    def calcular(self):

        # Verifica se o imóvel é um Apartamento
        if self.tipo == "Apartamento":
            self.valor = 700  # valor base do apartamento

            # Acréscimo para apartamento com 2 quartos
            if self.quartos == 2:
                self.valor += 200

            # Desconto de 5% caso não tenha crianças
            if not self.criancas:
                self.valor *= 0.95

        # Verifica se o imóvel é uma Casa
        elif self.tipo == "Casa":
            self.valor = 900  # valor base da casa

            # Acréscimo para casa com 2 quartos
            if self.quartos == 2:
                self.valor += 250

        # Verifica se o imóvel é um Estúdio
        elif self.tipo == "Estudio":
            self.valor = 1200  # valor base do estúdio

            # Duas vagas têm valor fixo
            if self.vagas >= 2:
                self.valor += 250

                # Vagas extras custam R$ 60 cada
                self.valor += (self.vagas - 2) * 60

        # Garagem para casa e apartamento
        if self.tipo in ["Apartamento", "Casa"] and self.vagas > 0:
            self.valor += 300

        # Retorna o valor final arredondado
        return round(self.valor, 2)
