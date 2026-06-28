import pandas as pd
import matplotlib.pyplot as plt

# Leitura da planilha
dados = pd.read_excel("pesquisa_problemas_urbanos.xlsx")

# Renomeando as colunas
dados.columns = [
    "Bairro",
    "FaixaEtaria",
    "Problema",
    "Gravidade",
    "Tempo",
    "Prioridade"
]

dados["Problema"] = (
    dados["Problema"]
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace("\xa0", " ", regex=True)
)

# Convertendo a gravidade para número
dados["Gravidade"] = pd.to_numeric(dados["Gravidade"])

# Informações da base
print("\nPrimeiras linhas da base:\n")
print(dados.head())

print("\nQuantidade de respostas:", len(dados))

# Problemas mais citados
dados_explodido = dados.copy()

dados_explodido["Problema"] = (
    dados_explodido["Problema"]
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace("\xa0", " ", regex=True)
    .str.split(";")
)

dados_explodido = dados_explodido.explode("Problema")

dados_explodido["Problema"] = dados_explodido["Problema"].str.strip()

problemas = dados_explodido["Problema"].value_counts()

print("\nProblemas mais citados:\n")
print(problemas)

plt.figure(figsize=(8,5))
problemas.plot(kind="bar")
plt.title("Problemas Urbanos Mais Citados")
plt.xlabel("Problema")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Participantes por bairro
bairros = dados["Bairro"].value_counts()

print("\nParticipantes por bairro:\n")
print(bairros)

plt.figure(figsize=(8,5))
bairros.plot(kind="bar")
plt.title("Participantes por Bairro")
plt.xlabel("Bairro")
plt.ylabel("Quantidade")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Gravidade média
dados_explodido = dados.copy()

dados_explodido["Problema"] = (
    dados_explodido["Problema"]
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace("\xa0", " ", regex=True)
    .str.split(";")
)

dados_explodido = dados_explodido.explode("Problema")

dados_explodido["Problema"] = dados_explodido["Problema"].str.strip()

gravidade = (
    dados_explodido
    .groupby("Problema")["Gravidade"]
    .mean()
    .sort_values(ascending=False)
)

print("\nGravidade média:\n")
print(gravidade.round(2))

plt.figure(figsize=(8,5))
gravidade.plot(kind="bar")
plt.title("Gravidade Média dos Problemas")
plt.xlabel("Problema")
plt.ylabel("Gravidade média (1 a 5)")
plt.xticks(rotation=45, ha='right')
plt.ylim(0,5)
plt.tight_layout()
plt.show()

# Prioridade do problema
prioridade = dados["Prioridade"].value_counts()

print("\nProblema deve ser tratado com prioridade?\n")
print(prioridade)

plt.figure(figsize=(6,6))
prioridade.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Os moradores consideram esse problema prioritário?")
plt.ylabel("")
plt.tight_layout()
plt.show()