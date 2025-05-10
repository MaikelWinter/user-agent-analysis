import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\31620\AppData\Roaming\JetBrains\PyCharm2024.3\scratches\example.txt"
open(path).readline()

records = [json.loads(line) for line in open(path)]

frame = pd.DataFrame(records)

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'

tz_counts = clean_tz.value_counts()
print(tz_counts)

subset = tz_counts[:10]
sns.barplot(y=subset.index, x=subset.values)

plt.show()

print('sjoboobo')
print(frame['a'].iloc[0])
print(frame['a'][0])

results = pd.Series([x.split()[0] for x in frame['a'].dropna()])
print(results.value_counts()[:8])

cframe = frame[frame['a'].notnull()].copy()
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

print(cframe['os'][:5])

by_tz_os = cframe.groupby(['tz', 'os'])
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

indexer = agg_counts.sum(1).argsort()
print(indexer[:10])

count_subset = agg_counts.take(indexer[-10:])
print(count_subset)

count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
print(count_subset[:10])

sns.barplot(x='total', y='tz', hue='os', data=count_subset)
plt.show()

g = count_subset.groupby('tz')
results2 = count_subset.total / g.total.transform('sum')

print(results2)