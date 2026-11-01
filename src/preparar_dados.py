# Preparação dos dados dos vinhos
# Como rodar (na pasta principal do projeto): python src/preparar_dados.py

import pandas as pd

# 1. Ler a base original
df = pd.read_csv('data/WineQT.csv')
print('Base original:', df.shape[0], 'linhas e', df.shape[1], 'colunas')

# 2. Remover a coluna Id (serve só para identificar a linha)
df_vinhos = df.drop('Id', axis=1)

# 3. Verificar valores nulos
print('Valores nulos:', df_vinhos.isnull().sum().sum())

# 4. Remover registros duplicados, mantendo a primeira ocorrência
print('Registros duplicados:', df_vinhos.duplicated().sum())
df_vinhos = df_vinhos.drop_duplicates().reset_index(drop=True)

# 5. Criar a variável alvo: 1 = alta qualidade (nota >= 7), 0 = baixa/média
df_vinhos['alta_qualidade'] = (df_vinhos['quality'] >= 7).astype(int)

print('Base tratada:', df_vinhos.shape[0], 'linhas')
print('Vinhos de alta qualidade:', df_vinhos['alta_qualidade'].sum())
print('Vinhos de baixa/média qualidade:', (df_vinhos['alta_qualidade'] == 0).sum())

# 6. Salvar a base tratada
df_vinhos.to_csv('data/vinhos_tratados.csv', index=False)
print('Arquivo salvo em data/vinhos_tratados.csv')
