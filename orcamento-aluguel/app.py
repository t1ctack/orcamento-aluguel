# Importações necessárias para o funcionamento do sistema
from flask import Flask, render_template, request
from models.orcamento import Orcamento
import csv

# Criação da aplicação Flask
app = Flask(__name__)

# Rota principal do site
@app.route("/", methods=["GET", "POST"])
def index():

    # Variável que armazena o resultado do cálculo
    resultado = None

    # Verifica se o formulário foi enviado
    if request.method == "POST":

        # Coleta os dados vindos do formulário HTML
        tipo = request.form["tipo"]
        quartos = int(request.form["quartos"])
        vagas = int(request.form["vagas"])

        # Checkbox retorna "on" se marcado
        criancas = request.form.get("criancas") == "on"

        # Cria um objeto da classe Orcamento
        orcamento = Orcamento(tipo, quartos, vagas, criancas)

        # Chama o método de cálculo
        valor = orcamento.calcular()

        # Gera o arquivo CSV com as 12 parcelas
        with open("orcamento.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Mês", "Valor do Aluguel (R$)"])

            for mes in range(1, 13):
                writer.writerow([mes, f"{valor:.2f}"])

        # Armazena o valor final para exibir no site
        resultado = valor

    # Renderiza o HTML e envia o resultado
    return render_template("index.html", resultado=resultado)

# Executa a aplicação
if __name__ == "__main__":
    app.run(debug=True)
