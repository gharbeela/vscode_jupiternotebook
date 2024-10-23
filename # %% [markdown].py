# %% [markdown]
# # jupyter notebook in vs code
# this is much better to run here than in real notebook

# %%
print("this is my first code in vs code as jupyter notebook")

# %%
name="my name is gharbeela"
name

# %%
import numpy as np 
g=np.array([3,4,5,6,7,8])
g

# %%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

phool=pd.read_csv("iris.csv")


# %%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

phool=pd.read_csv("iris.csv")
sns.histplot(data=phool,x="PetalLengthCm",y="SepalLengthCm",hue="Species",palette="dark")
plt.title("lenght comparison among sepal and petal")


plt.show

# %%
import seaborn as sns
sns.set_theme(style="whitegrid", palette="dark")

tips = sns.load_dataset("tips")


flierprops = {
    'marker': '^',       # Change to square ('s'), triangle ('^'), etc.
    'color': 'blue',     # Color of the outlier markers
    'alpha': 1         # Transparency of the outlier markers
}




# Draw a nested boxplot to show bills by day and time
sns.boxplot(x="day", y="total_bill",
            hue="smoker", palette=["#ede139", "#72ed39"]
            ,data=tips,flierprops=flierprops)
sns.despine(offset=10, trim=True)
plt.show

# %% [markdown]
# 

# %%



