import pandas as pd

df = pd.read_csv("data/avaliacoes.csv")
print(df.head())
print(len(df))
print(df["sentimento"].value_counts())

df["n_palavras"] = df["texto"].str.split().str.len()

print(df.groupby("sentimento")["n_palavras"].mean())

print(df[df["sentimento"] == "positivo"].head(3))
print(df[df["sentimento"] == "negativo"].head(3))

with open("resultados/exploracao.txt", "w", encoding="utf-8") as f:
    f.write("Número de linhas: " + str(len(df)) + "\n")
    f.write("Distribuição das classes:\n" + df["sentimento"].value_counts().to_string() + "\n")
    f.write("Tamanho médio dos textos (em palavras) por classe: \n" + df.groupby("sentimento")["n_palavras"].mean().round(2).to_string() + "\n")
    f.write("Exemplos Positivos:\n" + "\n".join(df[df["sentimento"] == "positivo"]["texto"].head(3)) + "\n")
    f.write("Exemplos Negativos:\n" + "\n".join(df[df["sentimento"] == "negativo"]["texto"].head(3)) + "\n")
    
    
    

