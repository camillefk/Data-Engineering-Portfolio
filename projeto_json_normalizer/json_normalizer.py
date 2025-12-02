import pandas as pd
import json

JSON_INPUT_PATH = 'dados_aninhados.json'

def normalize_json_data(input_path):
#Nessa função eu quero ler o json, aplicar o shredding e gerar dataframes normalizados.
    print(f"Iniciando a normalização do arquivo: {input_path}")

#Leitura do arquivo JSON
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
        #Aqui vou carregar o conteudo do json para uma lista/dicionário
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Arquivo não encontrado em: {input_path}")
        return
    except json.JSONDecodeError:
        print(f"ERRO: Não foi possível decodificar o arquivo JSON: {input_path}")
        return

    print(f"JSON lido. Total de registros principais (clientes): {len(data)}")

#Shredding e normalização
#1. Normalização dos dados principais (cliente)
#A atividade pediu para eu achatar o "detalhes_contato"
    df_clientes = pd.json_normalize(
        data=data,
        meta=['cliente_id', 'nome', 'status_assinatura'],
        record_path=None,
        sep='_'
    )

    print("\n---Tabela 1: Clientes (Normalizada) ---")
    print(f"Colunas: {list(df_clientes.columns)}")
    print(df_clientes[['cliente_id', 'detalhes_contato_email']].head())


#2. Shredding dos dados aninhados (pedidos)
    df_pedidos = pd.json_normalize(
        data=data,
        record_path='pedidos', #vou expandir a lista presente em 'pedidos'
        meta=['cliente_id'] #vou repetir a chave 'cliente_id'
    )
    
    print("\n--- Tabela 2: Pedidos (Shredding e Normalizada) ---")
    print(f"Colunas: {list(df_pedidos.columns)}")
    print(df_pedidos.head())


#3. Salvandos as tabelas planas (CSV) 
#Para a tabela Clientes
    CLIENTES_OUTPUT_PATH = 'clientes_normalizados.csv'
    df_clientes.to_csv(CLIENTES_OUTPUT_PATH, index=False)
    print(f"\nSUCESSO! Tabela de Clientes salva em: {CLIENTES_OUTPUT_PATH}")

#Para a tabela Pedidos
    PEDIDOS_OUTPUT_PATH = 'pedidos_normalizados.csv'
    df_pedidos.to_csv(PEDIDOS_OUTPUT_PATH, index=False)
    print(f"SUCESSO! Tabela de Pedidos salva em: {PEDIDOS_OUTPUT_PATH}")


if __name__ == "__main__":
    normalize_json_data(JSON_INPUT_PATH)