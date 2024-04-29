import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

categories = sorted(data['whoAmI'].unique())
one_hot = pd.DataFrame(0, columns=categories, index=data.index)
one_hot = one_hot.add((data['whoAmI'] == categories[:, None]).astype(int))
one_hot.columns = [f"{col}_onehot" for col in one_hot.columns]

data_one_hot = pd.concat([data, one_hot], axis=1)

data_one_hot.head()