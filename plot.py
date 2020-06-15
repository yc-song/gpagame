import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('db.csv', encoding='utf-8') #csv 불러옴
df.boxplot(column=["est"])
plt.show()