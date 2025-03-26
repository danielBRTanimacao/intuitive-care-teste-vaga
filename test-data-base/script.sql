CREATE TABLE operators (
    cnpj VARCHAR(20) PRIMARY KEY,
    operator_name VARCHAR(255),
    status VARCHAR(50),
    updated_date DATE
);

CREATE TABLE financial_statements (
    id SERIAL PRIMARY KEY,
    operator_cnpj VARCHAR(20) REFERENCES operators(cnpj),
    reference_date DATE,
    category VARCHAR(255),
    expense NUMERIC(15,2)
);

COPY operators(cnpj, operator_name, status, updated_date)
FROM '/path/to/csv/Relatorio_cadop.csv'
DELIMITER ','
CSV HEADER
ENCODING 'UTF8';

COPY financial_statements(operator_cnpj, reference_date, category, expense)
FROM '/path/to/csv/financial_statements_2023.csv'
DELIMITER ','
CSV HEADER
ENCODING 'UTF8';

SELECT o.operator_name,
       SUM(fs.expense) AS total_expense
FROM financial_statements fs
JOIN operators o ON fs.operator_cnpj = o.cnpj
WHERE fs.category = 'EVENTS/ KNOWN OR REPORTED CLAIMS FOR MEDICAL HOSPITAL ASSISTANCE'
  AND fs.reference_date >= (CURRENT_DATE - INTERVAL '3 months')
GROUP BY o.operator_name
ORDER BY total_expense DESC
LIMIT 10;

SELECT o.operator_name,
       SUM(fs.expense) AS total_expense
FROM financial_statements fs
JOIN operators o ON fs.operator_cnpj = o.cnpj
WHERE fs.category = 'EVENTS/ KNOWN OR REPORTED CLAIMS FOR MEDICAL HOSPITAL ASSISTANCE'
  AND fs.reference_date >= (CURRENT_DATE - INTERVAL '1 year')
GROUP BY o.operator_name
ORDER BY total_expense DESC
LIMIT 10;
