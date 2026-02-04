# 📘 Data Dictionary — Camada Gold

Este documento descreve as tabelas analíticas da camada **Gold**, modeladas em formato **Star Schema**, utilizadas para análises e visualizações no Power BI.

---

## 🧱 Tabela Fato

### fact_sales

Tabela central que armazena os eventos de venda.

| Coluna                | Tipo     | Descrição |
|----------------------|----------|----------|
| sale_id              | int (PK) | Identificador único da venda |
| customer_id          | int (FK) | Chave para a dimensão de clientes |
| product_id           | int (FK) | Chave para a dimensão de produtos |
| time_id              | int (FK) | Chave para a dimensão de tempo |
| payment_id           | int (FK) | Chave para a dimensão de pagamento |
| amount               | decimal  | Valor total da venda |
| item_rating          | decimal  | Avaliação do produto pelo cliente |
| discount_applied_pct | decimal  | Percentual de desconto aplicado |

---

## 📐 Tabelas Dimensão

### dim_customer

Informações descritivas dos clientes.

| Coluna              | Tipo    | Descrição |
|---------------------|---------|----------|
| customer_id         | int (PK)| Identificador do cliente |
| age                 | int     | Idade do cliente |
| gender              | varchar | Gênero do cliente |
| previous_purchases  | int     | Número de compras anteriores |

---

### dim_product

Informações dos produtos vendidos.

| Coluna         | Tipo    | Descrição |
|---------------|---------|----------|
| product_id    | int (PK)| Identificador do produto |
| item_purchased| varchar | Nome do item comprado |
| category      | varchar | Categoria do produto |

---

### dim_time

Dimensão de tempo simplificada baseada em estação do ano.

| Coluna   | Tipo    | Descrição |
|----------|---------|----------|
| time_id  | int (PK)| Identificador do tempo |
| season   | varchar | Estação do ano |

---

### dim_payment

Forma de pagamento utilizada na venda.

| Coluna         | Tipo    | Descrição |
|----------------|---------|----------|
| payment_id     | int (PK)| Identificador do pagamento |
| payment_method | varchar | Método de pagamento |
