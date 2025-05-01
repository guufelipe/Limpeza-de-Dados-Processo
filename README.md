# Limpeza-de-Dados-Processo
  Projeto de limpeza e padronização de dados utilizando pandas. O desafio consiste em tratar dados despadronizados sobre alunos (sexo, notas e frequência) e gerar um relatório final com informações enriquecidas, incluindo cálculo da média e status de aprovação.

# O que foi feito:
  1. Padronização da Coluna 'Sexo': 
     - A coluna de sexo foi padronizada para conter apenas os valores 'Masculino' ou 'Feminino', substituindo variações como 'M', 'F', 'masc', 'fem', etc.
     
  2. Correção das Notas:
     - As colunas de notas ('nota_matematica' e 'nota_portugues') foram ajustadas para garantir que utilizassem a vírgula como separador decimal, no formato brasileiro.
  
  3. Criação de Colunas Adicionais:
     - A coluna 'média' foi criada a partir das notas de Matemática, Português e Frequência.
     - A coluna 'aprovado' foi gerada, indicando 'Sim' ou 'Não' com base na média do aluno (nota ≥ 7).

# Estrutura do Repositório
  - 'datasets': Contém o arquivo original `dataset_despadronizado.csv` com os dados despadronizados.
  - 'dataset_padronizado.csv': Arquivo gerado para armazenar os dados depois da padronização e limpeza.
  - 'Limpeza_Dados.py': Script Python que realiza a leitura, limpeza e padronização dos dados.
  - 'README.md': Este arquivo.

# Tecnologias Utilizadas
Este projeto foi desenvolvido utilizando as seguintes tecnologias:
  - **Python**: A linguagem principal utilizada.
  - **pandas**: Biblioteca para manipulação e análise de dados, utilizada para o processamento e limpeza dos dados.
