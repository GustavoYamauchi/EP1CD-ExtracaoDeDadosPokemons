import pandas as pd


bulbaCsv = pd.read_csv("file.csv", index_col="ndex")
seraCsv = pd.read_csv("file2.csv", index_col="ndex")

print(bulbaCsv)
print(seraCsv)


juncao = seraCsv.join(bulbaCsv)
juncao = juncao.sort_index(ascending=True)
juncao.to_csv("join.csv")