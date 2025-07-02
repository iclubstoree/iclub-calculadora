# calculadora_iclub.py
import streamlit as st

# Tabela de taxas por parcela
taxas = {
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
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>Simulador de Parcelamento</div>", unsafe_allow_html=True)

st.markdown("<div class='input-box'>", unsafe_allow_html=True)
valor_total = st.number_input("Digite o valor total da compra:", min_value=0.0, format="%.2f")
valor_entrada = st.number_input("Digite o valor da entrada (opcional):", min_value=0.0, format="%.2f")
st.markdown("</div>", unsafe_allow_html=True)

if valor_total > 0:
    restante = max(valor_total - valor_entrada, 0)
    st.markdown("<div class='subtitle'>Opções de Pagamento</div>", unsafe_allow_html=True)

    for parcelas, taxa in taxas.items():
        valor_com_taxa = restante * (1 + taxa / 100)
        parcela = valor_com_taxa / parcelas

        valor_formatado = f"R$ {valor_com_taxa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        parcela_formatada = f"R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        entrada_formatada = f"R$ {valor_entrada:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        if valor_entrada > 0:
            texto_copia = f"{entrada_formatada} + {parcelas}x {parcela_formatada}"
        else:
            texto_copia = f
