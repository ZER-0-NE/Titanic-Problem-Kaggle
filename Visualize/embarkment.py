import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df=pd.read_csv("../datasets/train.csv")
data_test=pd.read_csv("../datasets/test.csv")


df["Died"]=1-df["Survived"]

# Extracting the TITLE from the Name
df.groupby('Embarked')[['Survived','Died']].agg('sum').plot(kind='bar',figsize=(15,8))
plt.title("Distribution with respect to Embarkment")
plt.xlabel("Groups")
plt.ylabel("Count")
plt.show()
