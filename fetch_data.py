import pandas as pd
print(pd.__version__)

df = pd.read_csv('dataset/testset.txt', sep="\t", header=None)
df.columns = ["tweetId", "tweetText", "userId", "imageId(s)", "username", "timestamp", "label"]

print(df.head(5))