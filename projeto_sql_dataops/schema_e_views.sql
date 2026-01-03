-- ==========================================================
-- PROJETO DATAOPS: SCHEMA, CARGA E VIEWS
-- Data: Dezembro/2025 ate 03//01/2026
-- Autor: Camis
-- ==========================================================

-- 1. (DDL)
CREATE TABLE tb_clientes_limpos (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    cidade VARCHAR(50),
    salario DECIMAL(10, 2)
);

CREATE TABLE tb_pedidos_normalizados (
    pedido_id VARCHAR(10) PRIMARY KEY,
    cliente_id INT,
    produto VARCHAR(50),
    valor DECIMAL(10, 2),
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES tb_clientes_limpos(cliente_id)
);

-- 2. (DML)
INSERT INTO tb_clientes_limpos (cliente_id, nome, idade, cidade, salario) VALUES
(1, 'Alice', 25, 'São Paulo', 4000.00),
(2, 'Bruno', 30, 'Rio de Janeiro', 5040.00),
(3, 'Camila', 30, 'Belo Horizonte', 5500.00),
(4, 'David', 45, 'São Paulo', 7000.00),
(5, 'Eduardo', 30, 'Recife', 5040.00),
(6, 'Fernanda', 22, 'Porto Alegre', 3500.00),
(7, 'Não Informado', 38, 'Curitiba', 6200.00);

INSERT INTO tb_pedidos_normalizados (pedido_id, cliente_id, produto, valor) VALUES
('P101', 1, 'Mouse', 50.00),
('P102', 1, 'Teclado', 150.00),
('P201', 2, 'Monitor', 800.00);

-- 3. (CAMADA GOLD)
CREATE OR REPLACE VIEW v_vendas_consolidadas AS
WITH total_pedidos_cte AS (
    SELECT 
        cliente_id, 
        SUM(valor) as total_gasto,
        COUNT(pedido_id) as qtd_pedidos,
        AVG(valor) as media_gasto
    FROM tb_pedidos_normalizados
    GROUP BY cliente_id
)
SELECT 
    c.nome as cliente_nome,
    c.cidade,
    t.total_gasto,
    t.qtd_pedidos,
    t.media_gasto
FROM tb_clientes_limpos c
LEFT JOIN total_pedidos_cte t ON c.cliente_id = t.cliente_id;