import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carga de datos
df = pd.read_csv('train.csv')

# Exploración inicial de datos
print(df.head())
print(df.info())

# Análisis de datos faltantes
missing_values = df.isnull().sum()
print(missing_values)

# Visualización de datos faltantes
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Mapa de calor de datos faltantes')
plt.show()


