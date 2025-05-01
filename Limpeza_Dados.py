import pandas as pd

def verificar_aprovacao(media):
        if media >= 7:
                return 'Sim'
        else:
                return 'Não'

dataset_despadronizado = pd.read_csv('datasets/Base_despadronizada.csv')

dataset_padronizado = dataset_despadronizado.copy()

# pra descobrir os valores que tem na coluna é so fazer dataset_despadronizado['sexo'].unique()
# atribuo à coluna 'sexo' a coluna sexo com os valores já ajustados pelo método replace(dicionário com substituições).
dataset_padronizado['sexo'] = dataset_padronizado['sexo'].replace({
    'M': 'Masculino',
    'Masculino': 'Masculino',
    'masc': 'Masculino',
    'F': 'Feminino',
    'Feminino': 'Feminino',
    'fem': 'Feminino'

})

dataset_padronizado['nota_matematica'] = dataset_padronizado['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
dataset_padronizado['nota_portugues'] = dataset_padronizado['nota_portugues'].astype(str).str.replace(',', '.').astype(float)
dataset_padronizado.to_csv('base_padronizada.csv', sep=';', decimal=',', index=False)


dataset_padronizado['media'] = (
    dataset_padronizado['nota_portugues'] +
    dataset_padronizado['nota_matematica'] +
    (dataset_padronizado['frequencia'] / 10)
) / 3

dataset_padronizado['aprovado'] = dataset_padronizado['media'].apply(verificar_aprovacao)
dataset_padronizado['aprovado'] = dataset_padronizado['media'].apply(verificar_aprovacao)

print(dataset_padronizado.head())