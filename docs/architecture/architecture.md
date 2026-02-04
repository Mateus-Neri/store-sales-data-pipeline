# Arquitetura do Projeto – Store Sales ETL

```mermaid
flowchart LR
    A[Fonte de Dados - CSV / Dataset Bruto] --> B[Bronze Layer - Extract]
    B --> C[Silver Layer - Transform]

    C --> D1[dim_customer]
    C --> D2[dim_product]
    C --> D3[dim_payment]
    C --> D4[dim_time]

    D1 --> F[fact_sales]
    D2 --> F
    D3 --> F
    D4 --> F

    F --> P[Power BI - Dashboard e KPIs]
