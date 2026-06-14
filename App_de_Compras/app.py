import streamlit as st
import pandas as pd

st.title("Compras do Mês 🛒")
from db import create_table, add_product, delete_product, mark_as_bought, get_all_products

# Criar a tabela de produtos
create_table()

# Formulario para adicionar um novo produto
with st.form("add_product_form"):
    st.subheader("Adicionar Produto")
    nome = st.text_input("Nome do Produto")
    preco = st.number_input("Preço", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    submitted = st.form_submit_button("Adicionar")

    if submitted:
        add_product(nome, preco, quantidade)
        st.success(f"Produto '{nome}' adicionado com sucesso!")

# Exibir a lista de produtos
st.subheader("Lista de Produtos")
products = get_all_products()
if products:
    df = pd.DataFrame(products, columns=["Nome", "Preço", "Quantidade"])
    st.dataframe(df)
else:
    st.info("Nenhum produto adicionado ainda.")