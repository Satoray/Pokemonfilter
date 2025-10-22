import pandas as pd

# Lê o arquivo Excel
arquivo_excel = "Pokemon.xlsx"
df = pd.read_excel(arquivo_excel)

# Nomes das colunas de tipo (ajuste se sua tabela tiver nomes diferentes)
coluna_tipo1 = "Type 1"
coluna_tipo2 = "Type 2"

# Filtra os Pokémons que tenham "Poison" em qualquer uma das duas colunas
df_poison = df[
    df[coluna_tipo1].str.contains("Poison", case=False, na=False) |
    df[coluna_tipo2].str.contains("Poison", case=False, na=False)
]

# Mostra o resultado
print(df_poison)

# Salva em um novo Excel
df_poison.to_excel("pokemon_poison.xlsx", index=False)
print("\n✅ Arquivo 'pokemon_poison.xlsx' gerado com sucesso!")
