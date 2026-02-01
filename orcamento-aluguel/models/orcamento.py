class Orcamento:
    def __init__(self, tipo, quartos, vagas, criancas):
        self.tipo = tipo
        self.quartos = quartos
        self.vagas = vagas
        self.criancas = criancas
        self.valor = 0

    def calcular(self):

        # =========================
        # VALOR BASE
        # =========================

        if self.tipo == "Apartamento":
            self.valor = 700

            # Quartos extras
            if self.quartos > 1:
                self.valor += (self.quartos - 1) * 150

            # Garagem
            if self.vagas > 0:
                self.valor += 300

            # Desconto
            if not self.criancas:
                self.valor *= 0.95

        elif self.tipo == "Casa":
            self.valor = 900

            # Quartos extras
            if self.quartos > 1:
                self.valor += (self.quartos - 1) * 180

            # Garagem
            if self.vagas > 0:
                self.valor += 300

        elif self.tipo == "Estudio":
            self.valor = 1200

            if self.vagas >= 2:
                self.valor += 250
                self.valor += (self.vagas - 2) * 60

        return round(self.valor, 2)
