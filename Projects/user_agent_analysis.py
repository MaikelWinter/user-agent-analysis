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