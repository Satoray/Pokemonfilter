import pandas as pd

# Caminho do arquivo CSV de entrada
arquivo_csv = "Retail_Transaction_Dataset.csv"

# Caminho do arquivo XLSX de saída
arquivo_excel = "Dataset.xlsx"

# Lê o CSV (ajuste o separador se necessário)
df = pd.read_csv(arquivo_csv, sep=",")  # sep=";" se for separado por ponto e vírgula

# Salva no formato Excel (.xlsx)
df.to_excel(arquivo_excel, index=False)

print("✅ Conversão concluída! Arquivo salvo como:", arquivo_excel)
