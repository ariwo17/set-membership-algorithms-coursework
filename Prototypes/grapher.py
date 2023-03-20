import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
pd_insert_time = pd.DataFrame.from_dict(test.insert_time)
pd_search_time = pd.DataFrame.from_dict(test.mean_search_time)

pd_insert_time

pd_insert_time_averaged = pd_insert_time.groupby(np.arange(len(pd_insert_time))//200).median()

algo = 'BST'
upper_ylim = 0.001
insert_graph = sns.lineplot(data=pd_insert_time_averaged)
insert_graph.set(title=f'Time Taken to Insert as Inserted words Increase ({algo})', xlabel='Number of Elements Already Inputed', ylabel='Time Taken to Insert 1 Extra Element')
plt.show()

pd_search_time

search_graph = sns.lineplot(data=pd_search_time)
search_graph.set(title='Search', xlabel='Number of Words to search from', ylabel='Time taken')
plt.show()