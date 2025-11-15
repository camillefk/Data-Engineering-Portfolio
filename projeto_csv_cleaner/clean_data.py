import pandas as pd
import os

#Definição do caminho do arquivo
CSV_INPUT_PATH = 'dados_sujos.csv'
CSV_OUTPUT_PATH = 'dados_limpos.csv'

def clean_and_save_data(input_path, output_path):
    print(f"Iniciando a limpeza do arquivo: {input_path}")

    #Leitura do arquivo
    try:
        #Lendo o CSV para um DataFrame do Pandas
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado no caminho: {input_path}")
        return
    
    print("\n--- Informações Iniciais do DataFrame (Antes da Limpeza) ---")
    df.info() #Mostra o tipo de dados e a contagem de não-nulos
    print("\nContagem de Nulos por Coluna:")
    print(df.isnull().sum())
    print("\nPrimeiras 5 linhas:")
    print(df.head())

    #Próximo passo é a lógica de limpeza
    df_limpo = df.copy() #Criei uma cópia para trabalhar de forma segura

    #Código de limpeza aqui
    #1. Tratamento da coluna 'Nome' (Categórica)
    print("-> 1. Tratando 'Nome' (Categórica): Preenchendo com 'Não Informado'...")
    df_limpo['Nome'].fillna('Não Informado', inplace=True)

    #2. Tratamento das colunas numéricas ('Idade', Salário')
    print("-> 2. Tratando 'Idade' e 'Salário' (Numéricas): Preenchendo com a Média... ")

    #Calcula a média (mean) das colunas
    media_idade = df_limpo['Idade'].mean()
    media_salario = df_limpo['Salario'].mean()

    #Aplica a imputação pela média
    df_limpo['Idade'].fillna(media_idade, inplace=True)
    df_limpo['Salario'].fillna(media_salario, inplace=True)

    #LEMBRAR: É uma boa prátia lembrar de arredondar a idade para um número inteiro. Salário pode ser mantido como float
    df_limpo['Idade'] = df_limpo['Idade'].round(0).astype(int)

    print("\nVerificação de Nulos APÓS a Limpeza:")
    print(df_limpo.isnull().sum())


    #Salvar o arquivo limpo
    #print("\n--- Informações Finais do DataFrame (Após a Limpeza) ---")

    print(f"\nSalvando arquivo limpo em: {output_path}")
    #O argumento index=False é crucil para não criar uma coluna de índice desnecessária no novo CSV
    df_limpo.to_csv(output_path, index=False)
    print(f"SUCESSO! O arquivo {output_path} foi criado.")

    print("\n--- Informções Finais do DataFrame ---")
    df_limpo.info()
    print("\nPrimeiras 5 linhas do arquivo limpo:")
    print(df_limpo.head())


    #código para salvar

    #Execução do script
if __name__ == "__main__":
    clean_and_save_data(CSV_INPUT_PATH, CSV_OUTPUT_PATH)