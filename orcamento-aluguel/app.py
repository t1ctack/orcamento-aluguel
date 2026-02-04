# Importações necessárias
from flask import Flask, render_template, request
from models.orcamento import Orcamento
import csv

# Inicializa o Flask
app = Flask(__name__)

# Rota principal do sistema
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None

    # Executa quando o formulário é enviado
    if request.method == "POST":
        try:
            # Dados enviados pelo formulário
            tipo = request.form["tipo"]
            quartos = int(request.form["quartos"])
            vagas = int(request.form["vagas"])

            # Checkbox retorna "on" quando marcado
            criancas = request.form.get("criancas") == "on"

            # =========================
            # VALIDAÇÕES
            # =========================

            # Quartos permitidos: 1 até 5
            if quartos < 1 or quartos > 5:
                resultado = "Erro: quantidade de quartos inválida (1 a 5)."
                return render_template("index.html", resultado=resultado)

            # Vagas permitidas: 0 até 10
            if vagas < 0 or vagas > 10:
                resultado = "Erro: quantidade de vagas inválida."
                return render_template("index.html", resultado=resultado)

            # =========================
            # CÁLCULO DO ORÇAMENTO
            # =========================

            orcamento = Orcamento(tipo, quartos, vagas, criancas)
            valor = orcamento.calcular()

            # =========================
            # GERAÇÃO DO CSV (12 meses)
            # =========================

            with open("orcamento.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Mês", "Valor do Aluguel (R$)"])

                for mes in range(1, 13):
                    writer.writerow([mes, f"{valor:.2f}"])

            # =========================
            # RESULTADO NA TELA
            # =========================

            valor_parcela_contrato = 2000 / 5

            resultado = (
                f"Aluguel mensal: R$ {valor:.2f} | "
                f"Contrato: R$ 2000 (5x de R$ {valor_parcela_contrato:.2f})"
            )

        except ValueError:
            resultado = "Erro: preencha os campos corretamente."

    # Renderiza a página
    return render_template("index.html", resultado=resultado)


# Executa o servidor
if __name__ == "__main__":
    app.run(debug=True)
