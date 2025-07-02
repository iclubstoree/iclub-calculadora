from flask import Flask, render_template, request
app = Flask(__name__)

taxas = {
    0: 1.55,
    1: 4.50, 2: 5.00, 3: 5.50, 4: 5.80, 5: 6.20,
    6: 6.80, 7: 7.20, 8: 7.80, 9: 8.40, 10: 8.95,
    11: 9.49, 12: 9.99, 13: 12.34, 14: 12.74,
    15: 13.14, 16: 13.54, 17: 13.94, 18: 14.34,
    19: 14.74, 20: 15.14, 21: 15.54
}

@app.route('/', methods=['GET', 'POST'])
def index():
    parcelas_resultado = []
    if request.method == 'POST':
        try:
            valor_total = float(request.form['valor_total'].replace(',', '.'))
            entrada = request.form['valor_entrada']
            valor_entrada = float(entrada.replace(',', '.')) if entrada else 0.0
        except:
            valor_total = 0.0
            valor_entrada = 0.0

        restante = max(valor_total - valor_entrada, 0)

        for i in range(0, 22):
            taxa = taxas.get(i, 0) / 100
            valor_com_taxa = restante * (1 + taxa)
            valor_total_final = valor_com_taxa + valor_entrada
            parcela = valor_com_taxa if i == 0 else valor_com_taxa / i

            texto = ""
            if valor_entrada > 0:
                if i == 0:
                    texto = f"R$ {valor_entrada:,.2f} + R$ {parcela:,.2f}"
                else:
                    texto = f"R$ {valor_entrada:,.2f} + {i}x R$ {parcela:,.2f}"
            else:
                if i == 0:
                    texto = f"R$ {parcela:,.2f}"
                else:
                    texto = f"{i}x R$ {parcela:,.2f}"

            parcelas_resultado.append({
                'id': i,
                'qtd': 'Débito' if i == 0 else f'{i}x',
                'texto': texto.replace(",", "X").replace(".", ",").replace("X", "."),
                'total': f'R$ {valor_total_final:,.2f}'.replace(",", "X").replace(".", ",").replace("X", ".")
            })

    return render_template('index.html', parcelas=parcelas_resultado)

if __name__ == '__main__':
    app.run(debug=True)
