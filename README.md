# Store Sales ETL Project

Pipeline de dados **end-to-end** utilizando a arquitetura **Medallion (Bronze, Silver e Gold)** para processamento de dados de vendas, com **Databricks + PySpark** e visualização no **Power BI**.

Este projeto foi desenvolvido com foco em **engenharia de dados**, modelagem dimensional e geração de insights analíticos.

---

## 📌 Visão Geral do Projeto

O objetivo do projeto é transformar dados brutos de vendas em **tabelas analíticas (fatos e dimensões)** prontas para consumo em ferramentas de BI, permitindo análises como:

- Receita total  
- Ticket médio  
- Vendas por categoria  
- Vendas por gênero  
- Avaliação média dos produtos  

---

## 🏗️ Arquitetura de Dados (Medallion)

O pipeline segue a arquitetura Medallion:

### 🥉 Bronze
- Extração dos dados brutos  
- Nenhuma transformação de negócio  
- Dados no formato original  

### 🥈 Silver
- Limpeza dos dados  
- Padronização de colunas  
- Tratamento de valores nulos  
- Preparação para modelagem dimensional  

### 🥇 Gold
- Criação das **dimensões**  
- Criação da **tabela fato**  
- Dados prontos para análise e BI  

---

## 📊 Modelo Dimensional

### Dimensões
- `dim_customer`
- `dim_product`
- `dim_time`
- `dim_payment`

### Fato
- `fact_sales`

O modelo segue o padrão **Star Schema**, facilitando consultas analíticas e melhor performance no Power BI.

---

## 📁 Estrutura do Repositório

```text
store-sales-data-pipeline/
│
├── README.md
│
├── docs/
│   ├── architecture/
│   └── data_dictionary/
│
├── etl/
│   ├── bronze/
│   │   └── extract_store_sales.py
│   ├── silver/
│   │   └── transform_store_sales.py
│   └── gold/
│       ├── dimensions/
│       │   ├── dim_customer.py
│       │   ├── dim_product.py
│       │   ├── dim_time.py
│       │   └── dim_payment.py
│       └── facts/
│           └── fact_sales.py
│
├── powerbi/
│   └── store_sales_dashboard.pbix
│
└── assets/ 
    ├── dashboard_preview.png
    └── store_sales_analytics_schema.png
```text

# 📈 Dashboard Power BI

O dashboard final foi desenvolvido no **Power BI** e contém:

## KPIs
- **Total de Clientes**
- **Receita Total**
- **Ticket Médio**

## Gráficos
- **Vendas por Categoria**
- **Vendas por Gênero**
- **Avaliação Média dos Produtos**

## Filtros
- **Estação do ano (Season)**

📷 **Prévia do dashboard** disponível na pasta `/assets`.

---

## 🛠️ Tecnologias Utilizadas
- Databricks  
- Apache Spark (PySpark)    
- Power BI  
- Git & GitHub  

---

## 🚀 Como Executar o Projeto
1. Execute o pipeline de extração na camada **Bronze**
2. Rode as transformações da camada **Silver**
3. Gere as tabelas analíticas na camada **Gold**
4. Conecte o **Power BI** ao Databricks (Databricks Connector)
5. Utilize as tabelas do schema **Gold** para análise

---

## 🎯 Objetivo Educacional
Este projeto foi desenvolvido com fins de **estudo e portfólio**, simulando um pipeline de dados utilizado em ambientes corporativos reais.

---

## 👤 Autor
**Mateus Neri**  
Estudante de Análise e Desenvolvimento de Sistemas  
Foco em Dados e Analytics
