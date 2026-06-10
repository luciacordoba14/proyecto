import pandas as pd
import seaborn as sns

datos = pd.read_csv("Datos/titanic.csv")

g = sns.countplot(x = "Sex", hue = "Survived", data = datos)
g.figure.savefig("plot.png")

