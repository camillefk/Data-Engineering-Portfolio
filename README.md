# Data-Engineering-Portfolio

Projetos de Data Engineering desenvolvidos no meu plano de estudos para me tornar uma Data Engineer

# ============================================

## Módulo SQL e Modelagem de Dados (Projeto DataOps)

Este módulo foca na estruturação, transformação e organização de dados relacionais utilizando **PostgreSQL**.

### O que foi desenvolvido:

- **Modelagem Relacional (DDL):** Criação de tabelas com definição estrita de tipos de dados e integridade referencial (Primary Keys e Foreign Keys).
- **Transformações Complexas:** Uso de **CTEs (Common Table Expressions)** para modularizar a lógica de agregação de métricas de vendas.
- **Camada de Abstração (Views):** Implementação de Views para simular a camada "Gold" de uma arquitetura Medallion, facilitando o consumo dos dados por ferramentas de BI.

### Arquitetura de Dados:

O projeto simula um fluxo onde dados limpos em Python são carregados e transformados para responder perguntas de negócio, como o gasto total por cliente e ticket médio.

> **Conceitos aplicados:** SQL Joins (Inner/Left), Funções de Agregação, CTEs, e Data Warehousing básico.
