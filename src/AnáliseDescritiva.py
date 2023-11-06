import pandas as pd
import pyodbc

server = 'DELCOR' # Nome do servidor
database = 'DW' # Nome do banco de dados
username = 'VAB' # Nome de usuário
password = 'delcor101103'  # Senha

# 1. Conectar-se ao banco de dados SQL Server
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# 2. Carregar os dados das tabelas

query = '''
SELECT *
FROM DIMENSAO_CLASSIFICACAO
'''
data3 = pd.read_sql(query, conn)

# 3. Análise Descritiva

# Exemplo: calcular estatísticas descritivas para uma coluna específica
columns_to_calculate = ['ilesos','levemente_feridos','moderadamente_feridos','gravemente_feridos','mortos']

mean_column1 = data3[columns_to_calculate].mean()
median_column1 = data3[columns_to_calculate].median()
std_column1 = data3[columns_to_calculate].std()