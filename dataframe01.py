"""
Pandas dataframe code
"""
import pandas as pd

# Creating DataFrame
# specify values for each column

df = pd.DataFrame(
    {"a": [4, 5, 6],
     "b": [7, 8, 9],
     "c": [10, 11, 12]
     },
    index=[1, 2, 3]

)

df.head()

print(df.shape)

