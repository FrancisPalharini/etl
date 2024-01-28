from processamento_dados import Dados


path_json= 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

#extract
dados_empresaA= Dados(path_json, 'json')
dados_empresaB= Dados(path_csv, 'csv')

#transform
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
dados_fusao = Dados.join(dados_empresaA,dados_empresaB)


#load

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(path_dados_combinados)