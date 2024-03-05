import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
columns = {*lst}
list = {}
for key in columns:
    list [key] = [*map(lambda w: 1 if w == key else 0, lst)]
data9 = pd.DataFrame(list)
data9.head()
