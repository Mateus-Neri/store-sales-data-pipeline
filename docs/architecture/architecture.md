# Arquitetura do Projeto – Store Sales ETL

```mermaid
flowchart LR
    A[Fonte de Dados<br/>CSV / Dataset Bruto] --> B[Bronze Layer<br/>Extract]

    B --> C[Silver Layer<br/>Transform]

    C --> D1[Dimensões<br/>dim_customer]
    C --> D2[Dimensões<br/>dim_product]
    C --> D3[Dimensões<br/>dim_store]
    C --> D4[Dimensões<br/>dim_date]

    D1 --> F[Fact Table<br/>fact_sales]
    D2 --> F
    D3 --> F
    D4 --> F

    F --> P[Power BI<br/>Dashboard & KPIs]
