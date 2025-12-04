import pandas as pd
import json

class JSONDataProcessor:
    #Classe para carregar, fazer shredding e normalizar os dados JSON aninhados
    def __init__(self, input_path, output_clientes, output_pedidos):
        #init é para definir os atributos do objeto
        self.input_path = input_path
        self.output_clientes = output_clientes
        self.output_pedidos = output_pedidos
        self.data = None

    def _load_data(self):
        #método para carregar o json e tratar erros de I/O (INPUT/OUTPUT)
        try:
            with open(self.input_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f) 

            #Aqui nesse if -not self.data- ta falando basicamente "se self.data estiver vazio..."
            #No isinstance verifica se uma váriavel é de um certo tipo, como por exemplo, ta verificando se o self.data é do tipo list.
            if not self.data or not isinstance(self.data, list):
                print("AVISO: O arquivo JSON está vazio ou não é uma lista.")
                return False
            
            return True
        
        except FileNotFoundError:
            print(f"ERRO: Arquivo não encontrado: {self.input_path}")
            return False
        except json.JSONDecodeError as e:
            print(f"ERRO: JSON inválido. Detalhe: {e}")
            return False
        except Exception as e:
            print(f"ERRO inesperado ao carregar JSON: {e}")
            return False
        
    def process_data(self):
        #método principal para normalizar, gerenciar e salvar pipeline
        #chamar método de carregamento
        if not self._load_data():
            print("Processamento cancelado devido a erro na carga de dados.")
            return
        
        print(f"Iniciando normalização de {len(self.data)} registros.")

        try:
            # 1. Normalização dos Clientes (Dicionário Simples)
            df_clientes = pd.json_normalize(
                data=self.data, 
                meta=['cliente_id', 'nome', 'status_assinatura'], 
                record_path=None, 
                sep='_'
            )

            # 2. Shredding dos Pedidos (Lista Aninhada)
            df_pedidos = pd.json_normalize(
                data=self.data,
                record_path='pedidos',
                meta=['cliente_id']
            )
            
            #3. SALVANDO
            df_clientes.to_csv(self.output_clientes, index=False)
            print(f"SUCESSO! Clientes salvos em: {self.output_clientes}")
            
            df_pedidos.to_csv(self.output_pedidos, index=False)
            print(f"SUCESSO! Pedidos salvos em: {self.output_pedidos}")
            
        except KeyError as e:
            print(f"ERRO DE ESTRUTURA: Chave {e} não encontrada. Verifique o JSON.")
        except Exception as e:
            print(f"ERRO inesperado durante o processamento Pandas: {e}")
            
        finally:
            print("\n--- FIM DO PROCESSO ---")


# 2. EXECUÇÃO DO SCRIPT
if __name__ == "__main__":
    
    # Definindo os caminhos
    JSON_INPUT_PATH = 'dados_aninhados.json'
    CLIENTES_OUTPUT_PATH = 'clientes_normalizados_poo.csv'
    PEDIDOS_OUTPUT_PATH = 'pedidos_normalizados_poo.csv'
    
    # Instanciando a classe (criando o OBJETO processador)
    processor = JSONDataProcessor(JSON_INPUT_PATH, CLIENTES_OUTPUT_PATH, PEDIDOS_OUTPUT_PATH)
    
    # Executando o método principal
    processor.process_data()