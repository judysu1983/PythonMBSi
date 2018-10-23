# install seaborn using this command:
# pip install --user git+https://github.com/mwaskom/seaborn.git#egg=seaborn

import seaborn as sns
import numpy as np
import pandas as pd

counts = {};

filepath = 'input.txt'  
with open(filepath) as fp:  
	line = fp.readline()
	cnt = 1
	while line:	
		line = line.strip()
		tokens = line.split("\\") 
		#print(len(tokens))
		language = tokens[2]
		count = tokens[4]
		#print("language = " + language + ", count = " + count)
		counts[language] = counts.get(language, 0) + int(count)
		#print(counts[language])
		line = fp.readline()
		cnt += 1

sns.set(style="darkgrid")
barChartData = pd.DataFrame(counts.items(), columns=['language', 'count'])
print(barChartData)
ax = sns.barplot(x="language", y="count", data=barChartData)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.tick_params(axis='x', labelsize=5)
ax.figure.savefig("output.png", dpi=300)
