import pandas as pd

words = pd.read_csv('corncob_lowercase.txt', header=None)
words.columns = ["Word"]

words["First"] = words["Word"].str[0]
words["Length"] = words["Word"].str.len()

words.to_csv("Words.csv", index=True)