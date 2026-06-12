import sqlite3

# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('App_de_Compras.db')
    return conn

# Criação da tabela de produtos
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            comprado BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()
    
# Função para adicionar um produto
def add_product(nome, preco, quantidade):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, preco, quantidade) 
        VALUES (?, ?, ?)
    ''', (nome, preco, quantidade))
    conn.commit()
    conn.close()
    
# Função para deletar um produto
def delete_product(product_nome):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE nome = ?', (product_nome,))
    conn.commit()
    conn.close()
    
# Função para marcar um produto como comprado
def mark_as_bought(product_nome):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE produtos SET comprado = 1 WHERE nome = ?', (product_nome,))
    conn.commit()
    conn.close()
    
# Função para obter todos os produtos
def get_all_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    products = cursor.fetchall()
    conn.close()
    return products