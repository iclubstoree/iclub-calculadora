# calculadora_iclub.py
import streamlit as st

# Tabela de taxas por parcela
taxas = {
    0: 1.55,
    1: 4.50, 2: 5.00, 3: 5.50, 4: 5.80, 5: 6.20,
    6: 6.80, 7: 7.20, 8: 7.80, 9: 8.40, 10: 8.95,
    11: 9.49, 12: 9.99, 13: 12.34, 14: 12.74,
    15: 13.14, 16: 13.54, 17: 13.94, 18: 14.34,
    19: 14.74, 20: 15.14, 21: 15.54
}

st.set_page_config(page_title="Calculadora de Parcelamento", layout="centered")

# Estilo customizado com CSS
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 28px;
        color: #000;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .subtitle {
        font-size: 20px;
        margin-top: 30px;
        color: #000;
    }
    .input-box {
        background-color: #fff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .header-row {
        display: flex;
        font-weight: bold;
        padding: 8px 0;
        border-bottom: 1px solid #ccc;
    }
    .row {
        display: flex;
        align-items: center;
        padding: 8px 0;
        border-bottom: 1px solid #eee;
    }
    .col {
        flex: 1;
        padding: 0 10px;
        position: relative;
    }
    .copy-input {
        width: 100%;
        font-size: 14px;
        padding: 4px;
    }
    .copy-btn {
        position: absolute;
        right: 10px;
        top: 50%;
        transform: translateY(-50%);
        background-color: #2e7d32;
        color: #fff;
        border: none;
        padding: 4px 8px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 12px;
    }
    .copy-btn:active { background-color: #1b5e20; }</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Simulador de Taxas</div>", unsafe_allow_html=True)

st.markdown("<div class='input-box'>", unsafe_allow_html=True)
valor_total = st.number_input("Digite o valor da compra:", min_value=0.0, format="%.2f", value=None, placeholder="R$ 0,00")
valor_entrada = st.number_input("Digite o valor da entrada (opcional):", min_value=0.0, format="%.2f", value=None, placeholder="R$ 0,00")
if valor_entrada is None:
    valor_entrada = 0.0
st.markdown("</div>", unsafe_allow_html=True)

if valor_total is not None:
    restante = max(valor_total - (valor_entrada or 0), 0)
    st.markdown("<div class='subtitle'>Opções de Pagamento</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='header-row'>
        <div class='col'>Quantidade</div>
        <div class='col'>Valor da Parcela</div>
        <div class='col'>Total</div>
    </div>
    """, unsafe_allow_html=True)

    for parcelas, taxa in sorted(taxas.items()):
        valor_com_taxa = restante * (1 + taxa / 100)
        valor_total_final = valor_com_taxa + (valor_entrada or 0)
        parcela = valor_com_taxa if parcelas == 0 else valor_com_taxa / parcelas

        valor_formatado = f"R$ {valor_total_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        parcela_formatada = f"R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        entrada_formatada = f"R$ {(valor_entrada or 0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        if valor_entrada > 0:
            if parcelas == 0:
                texto_copia = f"{entrada_formatada} + {parcela_formatada}"
            else:
                texto_copia = f"{entrada_formatada} + {parcelas}x {parcela_formatada}"
        else:
            if parcelas == 0:
                texto_copia = f"{parcela_formatada}"
            else:
                texto_copia = f"{parcelas}x {parcela_formatada}"

        linha_html = f'''
        <div class='row'>
            <div class='col'>{'Débito' if parcelas == 0 else f'{parcelas}x'}</div>
            <div class='col'>
                <input class='copy-input' type='text' value='{texto_copia}' id='input_{parcelas}' readonly>
                <button class='copy-btn' onclick=\"navigator.clipboard.writeText(document.getElementById('input_{parcelas}').value); this.innerText='Copiado'; setTimeout(() => this.innerText='Copiar', 1500);\">Copiar</button>
            </div>
            <div class='col'>{valor_formatado}</div>
        </div>
        '''

        st.markdown(linha_html, unsafe_allow_html=True)
