# Importa as bibliotecas necessárias
from flask import Flask, render_template, request
from models.orcamento import Orcamento
import csv

# Cria a aplicação Flask
app = Flask(__name__)

# Rota principal do sistema
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    # Verifica se o formulário foi enviado
    if request.method == "POST":
        try:
            # Coleta os dados do formulário
            tipo = request.form["tipo"]
            quartos = int(request.form["quartos"])
            vagas = int(request.form["vagas"])

            # Checkbox retorna "on" quando marcado
            criancas = request.form.get("criancas") == "on"

            # =========================
            # VALIDAÇÕES LÓGICAS
            # =========================

            # Quartos só podem ser 1 ou 2
            if quartos < 1 or quartos > 2:
                resultado = "Erro: quantidade de quartos inválida."
                return render_template("index.html", resultado=resultado)

            # Vagas não podem ser negativas nem absurdas
            if vagas < 0 or vagas > 10:
                resultado = "Erro: quantidade de vagas inválida."
                return render_template("index.html", resultado=resultado)

            # =========================
            # PROCESSAMENTO
            # =========================

            # Cria o objeto de orçamento (POO)
            orcamento = Orcamento(tipo, quartos, vagas, criancas)

            # Calcula o valor do aluguel
            valor = orcamento.calcular()

            # =========================
            # GERAÇÃO DO CSV
            # =========================

            with open("orcamento.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Mês", "Valor do Aluguel (R$)"])

                for mes in range(1, 13):
                    writer.writerow([mes, f"{valor:.2f}"])

            # Define o resultado final
            resultado = f"Aluguel mensal: R$ {valor:.2f}"

        except ValueError:
            # Erro caso algo que não seja número seja enviado
            resultado = "Erro: preencha os campos corretamente."

    # Renderiza a página HTML
    return render_template("index.html", resultado=resultado)


# Executa a aplicação
if __name__ == "__main__":
    app.run(debug=True)
