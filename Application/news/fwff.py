import pandas as pd

csv_file = './data/daily_top10_articles.csv'
df = pd.read_csv(csv_file)

print("CSV file columns:", df.columns)