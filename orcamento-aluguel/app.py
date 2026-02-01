from flask import Flask, render_template, request
from models.orcamento import Orcamento
import csv

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    if request.method == "POST":
        try:
            # Dados do formulário
            tipo = request.form["tipo"]
            quartos = int(request.form["quartos"])
            vagas = int(request.form["vagas"])
            criancas = request.form.get("criancas") == "on"

            # =========================
            # VALIDAÇÕES
            # =========================

            # Quartos: mínimo 1, máximo 5
            if quartos < 1 or quartos > 5:
                resultado = "Erro: quantidade de quartos inválida (1 a 5)."
                return render_template("index.html", resultado=resultado)

            # Vagas: mínimo 0, máximo 10
            if vagas < 0 or vagas > 10:
                resultado = "Erro: quantidade de vagas inválida."
                return render_template("index.html", resultado=resultado)

            # =========================
            # CÁLCULO
            # =========================

            orcamento = Orcamento(tipo, quartos, vagas, criancas)
            valor = orcamento.calcular()

            # =========================
            # CSV
            # =========================

            with open("orcamento.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Mês", "Valor do Aluguel (R$)"])
                for mes in range(1, 13):
                    writer.writerow([mes, f"{valor:.2f}"])

            resultado = f"Aluguel mensal: R$ {valor:.2f}"

        except ValueError:
            resultado = "Erro: preencha todos os campos corretamente."

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
