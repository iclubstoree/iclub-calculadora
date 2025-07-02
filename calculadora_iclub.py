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

# Configurações da página
st.set_page_config(page_title="Calculadora de Parcelas iClub", layout="centered")
st.markdown("<h1 style='text-align: center; color: #e60000;'>Calculadora de Parcelamento - iClub</h1>", unsafe_allow_html=True)

# Entradas do usuário
valor_total = st.number_input("Valor total do produto (sem entrada)", min_value=0.0, format="%.2f", step=10.0)
valor_entrada = st.number_input("Valor da entrada (opcional)", min_value=0.0, format="%.2f", step=10.0)

# Lógica de cálculo e exibição
if valor_total > 0:
    restante = max(valor_total - valor_entrada, 0)
    st.markdown("### Simulação de Parcelas")

    for parcelas, taxa in taxas.items():
        valor_com_taxa = restante * (1 + taxa / 100)
        parcela = valor_com_taxa / parcelas

        valor_formatado = f"R$ {valor_com_taxa:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        parcela_formatada = f"R$ {parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        entrada_formatada = f"R$ {valor_entrada:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        if valor_entrada > 0:
            texto_copia = f"{entrada_formatada} + {parcelas}x de {parcela_formatada}"
        else:
            texto_copia = f"{parcelas}x de {parcela_formatada}"

        texto_html = f"""
        <div style='padding: 8px; background-color: #f9f9f9; border: 1px solid #ddd; border-radius: 6px; margin-bottom: 6px;'>
            <span style='font-weight: bold'>{texto_copia} - Total: {valor_formatado}</span>
            <br>
            <input type='text' value='{texto_copia}' id='input_{parcelas}' readonly style='position:absolute; left:-9999px;'>
            <button onclick="navigator.clipboard.writeText(document.getElementById('input_{parcelas}').value)">Copiar</button>
        </div>
        """
        st.markdown(texto_html, unsafe_allow_html=True)
