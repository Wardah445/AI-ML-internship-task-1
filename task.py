import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IRIS.csv")
print(df.head())
print(df.info()) 
print(df.describe())

sns.pairplot(df, hue="species", markers=["o", "s", "D"])
plt.suptitle("Scatter Plot Matrix of Iris Features", y=1.02)
plt.show()
df.hist(figsize=(10, 8), bins=15, edgecolor='black')
plt.suptitle("Histograms of Iris Features", y=1.02)
plt.show()
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, orient="h")
plt.title("Box Plots of Iris Features")
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x="Species", y="SepalLength", data=df)
plt.title("Sepal Length by Species")
plt.show()