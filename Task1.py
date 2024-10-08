import pandas as pd
import matplotlib.pyplot as plt

#Loading dataset
df = pd.read_csv('C:\\Users\\DELL\\Desktop\\Dataset\\Population.csv')
print(df.head())

# Plotting with Matplotlib a Bar Chart for Categorical Data
categorical_column = 'gender'
category_counts = df[categorical_column].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar')
plt.title(f'Distribution of {categorical_column}')
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# Plotting with Matplotlib a Histogram for Continuous Data
continuous_column = 'age'

plt.figure(figsize=(10, 6))
plt.hist(df[continuous_column].dropna(), bins=30, edgecolor='black')
plt.title(f'Distribution of {continuous_column}')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
